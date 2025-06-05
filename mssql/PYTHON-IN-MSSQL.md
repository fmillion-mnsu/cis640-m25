# Python in Microsoft SQL Server

Microsoft SQL Server Machine Learning Services is a powerful tool that allows you to **directly run Python code within Microsoft SQL Server**. This lets you process data "where it lives" - Python code can access, manipulate, transform and process the data without the data ever needing to leave the server.

This offers many advantages:

* No latency - data does not need to traverse a network to get to Python
* Security - raw data doesn't leave SQL Server
* Tabular data - Python code can generate tabular data that SQL Server can treat as if it were a view or table - i.e. it can be used in standard SQL queries
* No credentials - your Python script does not need to know your login credentials, thus again enhancing security

## Setting up Python

Your class provided SQL Servers already have Python machine learning services! However, Microsoft provides steps for [Windows](https://learn.microsoft.com/en-us/sql/machine-learning/install/sql-machine-learning-services-windows-install?view=sql-server-ver15) and [Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup-machine-learning?view=sql-server-ver15) if you want to learn how to set it up yourself. 

You need to first **enable SQL Server Machine Learning Services** in order to use Python. Run the following command in SQL:

```
exec sp_configure @configname = 'external scripts enabled', @configvalue = 1;
RECONFIGURE WITH OVERRIDE;
```

If that succeeds, you're good to go!

## A "Hello World" Example

This is the simplest Python query you can run:

```
EXEC sp_execute_external_script
    @language = N'Python',
    @script = N'
        # Your Python code here
        OutputDataSet = InputDataSet
    ',
    @input_data_1 = N'SELECT columns FROM table'
    WITH RESULT SETS ((<column_definitions>));
```

Let's go over this script...

* The `EXEC` command is used to run stored procedures. SQL Server implements access to external tools like Python via a system-level stored procedure.
* The stored procedure expects two parameters:
  * `@language`: The language to use. For us, it's `Python`. The `R` language is also supported on some setups.
  * `@script`: The literal text of your Python script. This can be inserted directly as seen here, or it could even come as the result of a database query!
* The `@input_data_1` parameter contains the string representation of an SQL query. The results of this query will be available to the Python script.
* The `<column_definitions>` MUST be replaced with the actual list of columns your script returns, including the data types. This looks exactly like the columns in a `CREATE TABLE` statement.
  * There is no way to *fully automate* this process - to create a "generic" copy-input-to-output script. However, you can use SQL Server's ability to generate `CREATE` scripts to quickly discover the exact types of each field of your input table.

As you may have noticed the `InputDataSet` variable contains the entire result from the input data, and the script expects you to set `OutputDataSet` if you want to return tabular data.

Therefore, this script simply returns the result of the input - the SQL query that you used as the source.

## Let's try some transformation

We need a database at least one table to actually try doing some ETL. Create a new database in SQL Server and call it `PythonDemo`, and then run the following script against it:

```
USE [PythonDemo]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Users](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[firstName] [varchar](64) NOT NULL,
	[lastName] [varchar](64) NOT NULL,
	[dateOfBirth] [date] NOT NULL,
CONSTRAINT [PK_Users] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

SET IDENTITY_INSERT [dbo].[Users] ON 
GO

INSERT [dbo].[Users] ([id], [firstName], [lastName], [dateOfBirth]) VALUES (1, N'Harry', N'Potter', CAST(N'1980-07-31' AS Date))
INSERT [dbo].[Users] ([id], [firstName], [lastName], [dateOfBirth]) VALUES (2, N'Hermione', N'Granger', CAST(N'1979-09-19' AS Date))
INSERT [dbo].[Users] ([id], [firstName], [lastName], [dateOfBirth]) VALUES (3, N'Ron', N'Weasley', CAST(N'1980-03-01' AS Date))
INSERT [dbo].[Users] ([id], [firstName], [lastName], [dateOfBirth]) VALUES (4, N'Draco', N'Malfoy', CAST(N'1980-06-05' AS Date))
INSERT [dbo].[Users] ([id], [firstName], [lastName], [dateOfBirth]) VALUES (5, N'Ginny', N'Weasley', CAST(N'1981-08-11' AS Date))
INSERT [dbo].[Users] ([id], [firstName], [lastName], [dateOfBirth]) VALUES (6, N'Severus', N'Snape', CAST(N'1960-01-09' AS Date))
INSERT [dbo].[Users] ([id], [firstName], [lastName], [dateOfBirth]) VALUES (7, N'Minerva', N'McGonogall', CAST(N'1935-10-04' AS Date))
INSERT [dbo].[Users] ([id], [firstName], [lastName], [dateOfBirth]) VALUES (8, N'Tom', N'Riddle', CAST(N'1926-12-31' AS Date))
GO

SET IDENTITY_INSERT [dbo].[Users] OFF
GO
```

Now that we have a bit of data, let's try running a script:

```
EXEC sp_execute_external_script
    @language = N'Python',
    @script = N'
import pandas as pd
from datetime import datetime

def calculate_age(birth_date):
    """Calculates a person''s age given a birthdate"""
    today = datetime.now().date()

    # This lets us accept both strings in Y-m-d format as well as datetime objects.
    if isinstance(birth_date, str):
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    elif hasattr(birth_date, "date"):
        birth_date = birth_date.date()
    
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

# Generate a dataframe that will contain the results
result_df = pd.DataFrame()
result_df["id"] = InputDataSet["id"]
result_df["fullName"] = InputDataSet["lastName"] + ", " + InputDataSet["firstName"] 
result_df["age"] = InputDataSet["dateOfBirth"].apply(calculate_age)

# Set the output to the dataframe - the values will be computed before returning
OutputDataSet = result_df
',
    @input_data_1 = N'SELECT id, firstName, lastName, dateOfBirth FROM Users',
    @input_data_1_name = N'InputDataSet',
    @output_data_1_name = N'OutputDataSet'
WITH RESULT SETS ((
    id INT,
    fullName NVARCHAR(255),
    age INT
));
```

If you run this script, you should see a table appear with the results!

Let's say that we want to actually write these values to a new table. First, we need to create a table for the results that matches the schema:

And then:

```
INSERT INTO UserAge (id, fullName, age)
EXEC sp_execute_external_script
    @language = N'Python',
    @script = N'
import pandas as pd
from datetime import datetime

def calculate_age(birth_date):
    """Calculates a person''s age given a birthdate"""
    today = datetime.now().date()

    # This lets us accept both strings in Y-m-d format as well as datetime objects.
    if isinstance(birth_date, str):
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    elif hasattr(birth_date, "date"):
        birth_date = birth_date.date()
    
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

# Generate a dataframe that will contain the results
result_df = pd.DataFrame()
result_df["id"] = InputDataSet["id"]
result_df["fullName"] = InputDataSet["lastName"] + ", " + InputDataSet["firstName"] 
result_df["age"] = InputDataSet["dateOfBirth"].apply(calculate_age)

# Set the output to the dataframe - the values will be computed before returning
OutputDataSet = result_df
',
    @input_data_1 = N'SELECT id, firstName, lastName, dateOfBirth FROM Users',
    @input_data_1_name = N'InputDataSet',
    @output_data_1_name = N'OutputDataSet'
WITH RESULT SETS ((
    id INT,
    fullName NVARCHAR(255),
    age INT
));
```

We can even create a stored procedure that will run this script and update the ages every time we run it:

```
CREATE PROCEDURE sp_updateUserAges
AS
BEGIN

    TRUNCATE TABLE UserAge;

    INSERT INTO UserAge (id, fullName, age)
    EXEC sp_execute_external_script
        @language = N'Python',
        @script = N'
import pandas as pd
from datetime import datetime

def calculate_age(birth_date):
    """Calculates a person''s age given a birthdate"""
    today = datetime.now().date()

    # This lets us accept both strings in Y-m-d format as well as datetime objects.
    if isinstance(birth_date, str):
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    elif hasattr(birth_date, "date"):
        birth_date = birth_date.date()
    
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

# Generate a dataframe that will contain the results
result_df = pd.DataFrame()
result_df["id"] = InputDataSet["id"]
result_df["fullName"] = InputDataSet["lastName"] + ", " + InputDataSet["firstName"] 
result_df["age"] = InputDataSet["dateOfBirth"].apply(calculate_age)

# Set the output to the dataframe - the values will be computed before returning
OutputDataSet = result_df
',
    @input_data_1 = N'SELECT id, firstName, lastName, dateOfBirth FROM Users',
    @input_data_1_name = N'InputDataSet',
    @output_data_1_name = N'OutputDataSet'
WITH RESULT SETS ((
    id INT,
    fullName NVARCHAR(255),
    age INT
));
END
```

## A much more advanced example

The [AdventureWorks](https://banbao991.github.io/resources/DB/AdventureWorks.pdf) database is a sample database that contains a large amount of demo data that is useful for experimenting with SQL Server.

Let's consider the following scenario:

> &ldquo;The AdventureWorks marketing team wants to segment customers based on purchasing behavior to create targeted campaigns. Use Python's clustering algorithms to identify customer segments based on order history, total spend, and product preferences.&rdquo; 

First, we will create a view to simplify extracting customer metrics from the database and providing them to Python. This allows us to **filter and process some of the data in SQL**, which is more optimal for performance than letting Python do all the heavy lifting:

```
CREATE VIEW CustomerMetrics AS
SELECT 
    c.CustomerID,
    COUNT(DISTINCT soh.SalesOrderID) as OrderCount,
    SUM(sod.LineTotal) as TotalSpend,
    DATEDIFF(day, MAX(soh.OrderDate), GETDATE()) as DaysSinceLastOrder,
    COUNT(DISTINCT p.ProductSubcategoryID) as ProductVariety
FROM Sales.Customer c
JOIN Sales.SalesOrderHeader soh ON c.CustomerID = soh.CustomerID
JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
JOIN Production.Product p ON sod.ProductID = p.ProductID
WHERE soh.OrderDate >= DATEADD(year, -2, GETDATE())
GROUP BY c.CustomerID;
```

Now, let's try a script that will utilize K-means clustering in Python to generate a result set:

```
EXEC sp_execute_external_script
    @language = N'Python',
    @script = N'
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

# Standardize features
scaler = StandardScaler()
features = ["OrderCount", "TotalSpend", "DaysSinceLastOrder", "ProductVariety"]
X_scaled = scaler.fit_transform(InputDataSet[features])

# Perform K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
InputDataSet["Segment"] = kmeans.fit_predict(X_scaled)

# Calculate segment characteristics
segment_profiles = InputDataSet.groupby("Segment")[features].mean().round(2)

# Prepare output
OutputDataSet = InputDataSet[["CustomerID", "Segment"]]
print("Segment Profiles:")
print(segment_profiles)
    ',
    @input_data_1 = N'SELECT * FROM CustomerMetrics'
    WITH RESULT SETS ((CustomerID int, Segment int));
```
