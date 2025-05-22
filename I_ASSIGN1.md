# Individual Assignment 1

In this assignment you will explore data in a MongoDB database and develop some queries to answer questions about the data.

## Requirements

For this assignment you will devise **four** (4) questions you can ask about the data in the database. You can read the [documentation about the sample datasets](https://www.mongodb.com/docs/atlas/sample-data/#available-sample-datasets) on MongoDB's website. The documentation will explain the structure of the documents in each dataset.

This is an open-ended assignment. You can use the existing datasets loaded into your MongoDB servers, or you can choose to locate and load your own dataset. MongoDB Compass allows you to upload JSON data to your database - you are free to create new databases and collections to store your own data. 

> Use common sense - a "dataset" should consist of a reasonable number of records. A "dataset" consisting of only five records is definitely too small. On the other hand you need not go overboard - you don't need to locate and import a dataset of a million records. If you're unsure, aim for datasets with between 100 and 10,000 records.

Your questions should be **high-level questions** (think "business questions") that you will then write queries to solve.

1. Ensure you have access to MongoDB per the instructions on D2L - this information is not hosted here since it contains your access credentials.

2. **Explore** the datasets in your database. 

3. Once you have an understanding of what data is available, decide on six (6) **questions** you can ask about the data. 

    > Note that you do **not** need to use only a single database for your questions. You could, for example, come up with two questions for the AirBnB dataset, five for the Supply store dataset and one for the Planets dataset.

4. **Design your queries** using MongoDB Compass's aggregation editor.

5. For each query:

    * Describe the question you are answering in a couple of sentences.
    * Paste the query (or queries) that you ran to answer the question.
  
        > Please change the font of any code you paste into a document to a fixed-width font, such as Courier New or Lucida Console. This makes your code much easier to read. It is OK if you write the whole document in a fixed-width font as well for simplicity.

    * Provide either the answer to your question if it is a simple scalar or minimal object, or provide a sampling of some of the data that answers your question.

6. If you used any custom datasets in your project, either include those in your submission, or provide a link to access the dataset.

Your questions can be narrow in scope and in general should be answerable with one query, although using a second query is OK if you document how the queries interact. However, the aggregation framework actually does make complex nested queries possible!

Here are a couple of examples of the kinds of questions you should come up with - this will give you an idea of the scope to aim for:

* How many (just a count) AirBnB properties are within 50 miles of the Mall of America in Bloomington?
* What is the oldest movie listed in the movie database?
* At what location (its call letters) was the highest temperature forecast reported?

## Submission

Your submission should consist of:

* The document you prepared based on the above specifications
* If applicable, any datasets you used in your project.

This submission is due on May 30th, 2025 at 11:59 PM.
