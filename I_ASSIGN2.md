# Individual Assignment 2 - Python in SQL Server

In this assignment you will explore the use of Python within SQL Server using Machine Learning Services to solve data analysis problems that are better suited to Python than pure SQL.

## Requirements

For this assignment you will create at least **two** (2) Python-based solutions that demonstrate Python's strengths for data processing and analysis within SQL Server. You will use the AdventureWorks and/or WideWorldImporters sample databases that are already loaded on your cloud SQL Server instance.

Your solutions should showcase Python's capabilities in areas where it excels beyond what SQL can easily accomplish. Think of tasks involving statistical analysis, text processing, complex data transformations, time-series analysis, or mathematical modeling. More details on this below.

## Steps

1. **Connect to your SQL Server instance** using the credentials provided on D2L.

2. **Explore** the AdventureWorks and WideWorldImporters databases to understand what data is available.

    * [More information on AdventureWorks](https://github.com/microsoft/sql-server-samples/blob/master/samples/databases/adventure-works/README.md)
    * [More information on WideWorldImporters](https://www.microsoft.com/en-us/sql-server/blog/2016/06/09/wideworldimporters-the-new-sql-server-sample-database/)

3. **Design at least two Python-based solutions** that meet these criteria:

    * Each solution must combine data from **at least 2 tables**
    * Each solution must return tabular results that can be used in subsequent SQL queries. More on this later.
    * Your solutions must address **at least 3** of these 5 categories:
        - **Statistical Analysis** - correlations, distributions, outlier detection, descriptive statistics
        - **Text Processing** - pattern extraction, string manipulation beyond basic SQL functions
        - **Time-based Analysis** - trend analysis, seasonality detection, rolling calculations
        - **Data Transformation** - complex reshaping, pivoting, aggregation that would be cumbersome in pure SQL
        - **Mathematical Modeling** - regression analysis, clustering, predictive calculations

        > You can satisfy two - or even perhaps three - of these criteria with a single query or problem domain. 
        >
        > For example, a Python-based query that performs statistical analysis on data while also using time-based analysis (e.g. average per day) would satisfy two of the domain areas.
        >
        > You can write a minimum of two queries, but in that case at least one of your queries must satisfy two areas, and the second must satisfy a *different* area - in other words, all of your queries collectively must involve at least three of these domains.

4. **Implement your solutions** using Python in SQL Server. Make sure to first write and test your Python code, and then **create a method** so that those results can be accessed by other SQL statements.

    > You are not tied to one specific strategy! There are a few methods you can use, including *but not limited to*:
    >
    > * Wrapping your code in a table-valued function
    > * Using `sp_execute_external_script` in a stored procedure
    > * Creating an ETL script that *copies the resulting data from your script into a new table* (also you will want to generally first `TRUNCATE` your target table to remove all existing records!)
    >
    > Other ideas may also be possible - take time to explore!

5. **Demonstrate SQL integration** by writing at least one SQL query that uses the results from at least one of your Python scripts. This query should be a normal `SELECT` query, which may utilize `JOIN`s or other SQL functions, but the source data for this particular query must be the result of one of your Python queries - in whichever way you decide to make the tabular data available.

## What Makes a Good Solution?

Your Python code should leverage Python's strengths rather than simply replicating basic SQL operations. For example:

**Good examples:**
* Calculating rolling correlations between sales metrics across different product categories
* Performing sentiment analysis on product descriptions
* Creating customer segments using clustering algorithms
* Analyzing seasonal trends with statistical modeling
* Complex data reshaping that would require multiple sequential ETL operations in SQL

**Poor examples (avoid these):**
* Simple `GROUP BY` operations that are easily done in SQL
* Basic filtering with WHERE clauses
* Simple aggregate functions impemented in Python, such as `COUNT`, `SUM` or `AVERAGE`.

> Use common sense - if you can easily accomplish the same task with a single SQL statement, you should choose a different approach that better showcases Python's capabilities.

## Submission

Your submission should consist of:

* A single SQL script file (.sql) containing all your Python-in-SQL code with clear comments
* Sample output demonstrating that your solutions work correctly
* File naming: `LastName_FirstName_PythonSQL.sql`

This assignment is individual work. Each student must work independently and submit their own original solution.

This submission is due on **June 20th, 2025** at 11:59 PM.

## Grading Rubric

This project will be graded as follows:

|-|-|
| Item | Percentage |
|-|-|
| Technical execution - Code works, results are accurate | 60% |
| Scope fulfillment - Queries address at least three of the problem domains; at least two Python queries are written | 30% |
| Code quality, submission formatting | 10% |

This assignment is worth **125 points**.

## Resources

* Course GitHub repository: <https://github.com/fmillion-mnsu/cis640-m25/>
* [SQL Server Machine Learning Services Documentation](https://learn.microsoft.com/en-us/sql/machine-learning/sql-server-machine-learning-services?view=sql-server-ver16)
* [Python Package Information](https://learn.microsoft.com/en-us/sql/machine-learning/package-management/python-package-information?view=sql-server-ver17)

MSSQL includes the following Python libraries: 

* [pandas](https://pandas.pydata.org/docs/)
* [numpy](https://numpy.org/doc/)
* [scikit-learn](https://scikit-learn.org/stable/user_guide.html)
* [matplotlib](https://matplotlib.org/stable/index.html)
* [revoscalepy](https://learn.microsoft.com/en-us/sql/machine-learning/python/ref-py-revoscalepy?view=sql-server-ver17)

## Examples

Here are some example scenarios to help you brainstorm:

* Analyze purchasing patterns to identify customer segments based on buying behavior
* Calculate rolling averages and correlations for sales data across time periods
* Perform text analysis on product names or descriptions to find patterns
* Detect outliers in sales or inventory data using statistical methods
* Create time-series forecasts for seasonal trends

### Code Example

Here's a simple code example that demonstrates the syntax (please note that you may **NOT** use this example):

```sql
-- Note: This simple example replicates the GROUP BY SQL function.
-- This is not a permitted use case for your assignment, but is given here as reference.

-- Execute Python script...
EXEC sp_execute_external_script
    @language = N'Python',
    @script = N'
import pandas as pd

# Pandas groupby
result = InputDataSet.groupby("ProductCategory").size().reset_index(name="Count")

# set new DataFrame to result
OutputDataSet = result
    ',
    @input_data_1 = N'SELECT ProductCategory FROM Production.Product';
```

For more details please refer to [Using Python in Microsoft SQL Server](mssql/PYTHON-IN-MSSQL.md) in this repository.