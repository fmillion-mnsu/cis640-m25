# CIS 640 - Advanced Database Systems

## Capstone Group Project

This project serves as your primary project for the CIS 640 course. The purpose of this project is to:

* give you experience working with multiple database systems
* give you experience working with database programming - both in-database and externally via APIs
* enhance your skills in evaluating a real-world business or organizational scenario and designing and implementing a data model to support that scenario
* develop skills in producing reports based on data analysis

This project will serve as a majority of your grade for the course.

## Project Description

For this project, **you will design and implement a full data model for a business scenario of your group's choosing.**

A few examples of scenarios you can build:

* An e-commerce system
* A financial management system (e.g. a bank, investment firm, etc.)
* A social media network's data system

Your project will consist of all of the following:

* A written report containing a description of your project, including data flow diagrams, ERDs, data dictionaries, etc. as applicable and appropriate. This is sometimes known as a Requirements Analysis document.   
  * Part of this requirements analysis process is to determine the *most appropriate* database for a given type of data. For example, while you could store customer orders in a time-series database, time-series databases are not the optimal choice for that type of data, since the types of queries that time-series databases excel at - specifically aggregating data based on timestamps - would not be as useful for tasks such as reviewing individual orders.
* Implementation of the data model using **at least three (3) different types of database server**, one of which must be a traditional relational database (e.g. Microsoft SQL Server). 
* Specify **six (6) business questions** that you can answer with your data model:
  * At least **two (2)** cases *must* involve *accessing and aggregating data from at least two different servers*.
  * At least **two (2)** cases *must* involve advanced SQL programmability - e.g. stored procedures, functions or views.
  * Each of your three servers must be involved in at least **one (1)** query - that is, you cannot design a data model and a set of scenarios where none of the scenarios access one of your databases.
* An **analytics dashboard**, using PowerBI or an equivalent tool or framework, that must utilize data from at least **two (2)** of your three databases.
  * Your dashboard must offer some form of interactivity - for example, if one of your items is "sales by month" with the view showing sales by day within a given month, the user should be able to select a month to view.
  * Your dashboard should be business focused - that is, don't simply display raw data, but answer practical **business questions** based on your scenario. You may use one or more of your business question scenarios as a data source!
* A **presentation** (approximately 10-15 minutes) covering your project, your data model, your business questions, and your dashboard. Where possible and appropriate you should provide visual demonstrations of your solution - either live or with a video. (I *strongly* recommend you record a video even if you plan to demo live - this serves as a backup should a technical issue arise during your presentation!)
* Documentation of your **weekly sprints** (see below)

While you should be focusing on building a realistic data model within the domain you choose, your **data model** must include the following:

* A minimum of **five (5) distinct entities**. An *entity* in this case is defined as a single logical set of data. Examples of entities are "customer", "product", and "order".
* At least one aspect of the database that involves **temporal (time-based) data**. 
  * Note that you do not necessarily need to use a time-series database to store time-based data. Only use a time-series database if the types of queries you will be doing on the data would be optimized by a time-series database.
* You must have at least one **one-to-many** and one **many-to-many** relationship among your data elements.
  * Note that this does not need to be within a single database server! For example, if a product belongs to one manufacturer, and you store manufacturer data in a relational database but product data in a document NoSQL database, that still counts as a one-to-many relationship and can be illustrated as such.

You will need **sample data** for your project. You have a few options:

* Generate data yourself - there are many "faker" libraries available to generate e.g. fake customers complete with addresses and phone numbers, fake product data, etc.
* Find a public, open dataset. Resources such as [Kaggle](https://www.kaggle.com/) are a good place to start.
  * If you use an open dataset, you should avoid using the data "as-is". You should instead use either a script or an automation task of some kind to perform an **ETL** (extract, transform, load) operation on your sample dataset, in order to mold its data into your data model. In other words, **don't build your data model around the dataset**; instead, use ETL techniques to conform the dataset to your model.

> Note that while you will likely be working with small datasets as a proof of concept, you should be taking care to consider the performance and scalability of your application with larger volumes of data. For example, a slow query might not "feel" slow if performed on only 1,000 records, but that same query might take long enough to cause timeouts when presented with 1,000,000 rows. Consider realistic live scenarios for your system and ensure that you have demonstrated how you have attempted to approach these concerns. (For example, creating appropriate indexes to speed up query processing would be a good idea.) If your approach would fall outside the scope of the project (e.g. configuring automated scale-up/scale-out) then you do not have to implement it, but you should document and explain how the strategy in question will help to maintain performance of the application when under a realistic load.
 
### Specifics: Data processing application

Your Python (or other language) application serves as a data integration harness - this means that it *demonstrates* how the databases work together to solve business problems and provide insight. There are no strict requirements for user interface - you may write one script overall with options, or one script per business question.

Your scripts should implement the following characteristics:

* Configurability - provide a mechanism for users to provide alternative database login information. You can use defaults, but allow overrides where applicable. (Example: in Python, you can use the [argparse module](https://docs.python.org/3/library/argparse.html) and provide configuration on the command line.)
* Basic error handling - catch obvious exceptions such as requested data not found, server not reachable, error from the server, etc.
* A command line interface is all that is required for this portion of the assignment, but you are free to expand beyond that if you desire.

Note that this application is *separate* from the dashboard you will build using PowerBI or a similar analytics tool. While you can use some of the same business scenarios and questions in your dashboard, consider creating the dashboard to be a distinct, separate step in the project.

## Logistics

For this project, **you will be working in a group of 3 students.** Groups will be assigned by me. 

Of particular importance is that I will be providing you access to cloud servers appropriate for your data project. To facilitate this process, **your group must submit a brief draft of your project idea, including which servers you require, by May 27th before the start of class.** Once I have approved your project idea, I will provision and provide you with access credentials for the servers you have selected.

This initial submission **does not need to include specific data models**. You only need to provide me with:

* the overall project idea (example: "an E-commerce store selling computer parts")
* the database servers you need (example: "MySQL, MongoDB and InfluxDB")
* if you need any data preloaded - I can help you with sample datasets if you are struggling

### Available servers

I can provide you access to all of the following servers:

* Traditional SQL: MySQL/MariaDB, PostgreSQL, Microsoft SQL Server, Oracle Database
* NoSQL Document: MongoDB, Elasticsearch
* Time-series database: InfluxDB
* Graph database: Neo4J
* Caching database: Redis, Memcached

Other databases can be made available but may take longer to configure and deploy. 

### Agile methodology 

We will use a simplified and slightly modified version of the **Agile software development strategy**. If you are not familiar with Agile development, [the Agile Software Development Manifesto](https://agilemanifesto.org/) is a good place to start. 

Given the short length of this course, you will engage in **four (4) weekly sprints**, with the first starting the second week of the course (the week of May 26th). 

You must adopt some strategy for implementing and managing the Agile strategy. I strongly recommend [Trello](https://trello.com/), which offers a free tier. You can use Trello to create cards for task assignment, as a simple knowledge base, and more. 

For each **sprint**, you will:

* Start with a Retrospective of the previous sprint - meet with your group members and review what you achieved during the past week. **As part of this retrospective, document which tasks each individual group member engaged with**. (This is part of how your individual grade is calculated!)
  * You may alternatively end the previous sprint with the retrospective, if that makes more sense to you. A retrospective is basically wrapping up the previous sprint - you can think of it as "the end of this sprint" or "the start of the next sprint" - either is correct.
* Have a **sprint planning meeting** - discuss and assign your tasks among your group members.

At least **twice per week**, you will have a **stand-up meeting**. The purpose of a stand-up meeting is to *very briefly* update your team members on your own personal progress in the project. Each team member should respond to the following three questions:

* What did I work on before (i.e. since the last standup)?
* What will I work on now?
* What (if anything) do I need help with / do I have any "blockers"

Stand-up meetings are intended to be extremely brief - even in larger teams, 15 minutes is a typical upper limit on time. For small teams of 3 students, stand-up meetings will probably take 5 minutes at most. 

Document your stand-up meetings - it would be OK if you simply use Zoom transcription or AI summarization to make this easy.

The documentation you provide related to the Agile methodology for your project must include details on individual team member contributions and details on your sprint planning and retrospective meetings. 

### Weekly task outline

To help you keep this larger project organized and to keep you on track, I suggest the following structure for each week of the project. You are of course free to adjust this as appropriate for your group's project or your group's existing skillset.

* Week 1:
  * Core data model design - actually discuss and decide on what data will be stored where, the relationships among the data, and standards for e.g. field naming
  * Implement the data model in live database servers
  * Locate and insert a test dataset using ETL techniques, or generate a test dataset using fake data
* Week 2:
  * Implement your six business questions as code - either SQL programmability or external code as appropriate
  * Write stored procedures, functions, views, etc. as required
  * If applicable, link servers (e.g. Microsoft SQL -> MongoDB) as part of your data design
  * Create appropriate indexes where applicable to ensure performance
* Week 3:
  * Write the Python (or other language) external application that can execute your six scenarios
    * Scenarios should be flexible - e.g. don't make a scenario "sales by product in June 2024", but instead "sales by product over week/month/year/etc." and provide a way for the parameters of the query to be provided
  * Begin implementing analytics dashboard
* Week 4:
  * Finish implementing anaytics dashboard
  * Test and validate project stack
  * Work on final presentation

## Schedule

There are a few important deadlines for this project:

|-|-|
| Component | Due Date |
|-|-|
| Project proposal - including which database servers you'd like to use | *May 27, 2025*, by the start of class |
| Presentation of project to class | *June 17th, 2025*, during class |
| Final deliverables package | *June 20th, 2025*, at 11:59 PM |

## Deliverables

Your final submission for this project will include:

* Your documentation, including:
  * the data model you designed, including the entities and their relationships
  * the three database servers you chose, which data is stored in which server, and the *justification* for why you chose to store data in a given server
* Any code you wrote - including, but not limited to SQL stored procedures, Python code, etc.
* Screenshots of your dasboard, including the flexibility of the user to manipulate the data
* Your final presentation materials (e.g. a PowerPoint presentation)

## Grading Rubric

This project will be graded as follows:

|-|-|
| Item | Percentage |
|-|-|
| Project proposal | 10% |
| Documentation of data model and project scope | 15% |
| Implementation of data model into database servers | 15% |
| Design and implementation of data harness application (e.g. Python command line app) | 15% |
| Design and implementation of analytics dashboard (e.g. PowerBI) | 15% |
| Documentation of Agile process and individual team contributions | 15% |
| Final project presentation | 15% |

Your final grade may be adjusted based on your individual contributions to your project. If you are not contributing fairly, you may lose points individually on various aspects of the project while the rest of the group will not. As just one example, if you were to "skip" presenting with your group, you would receive no credit for the final project presentation but your other group members would receive credit.

## Submission

You should prepare a Zip file of all of your final deliverables and submit it onto D2L **before June 20th, 2025 at 11:59 PM**.

Late submission policy applies to the group as a whole - **if the submission is late, the entire group grade will be lowered per the late work policy in the syllabus.** Don't take chances!

## Support

If you have any questions, concerns, or are uncertain about anything with respect to this project, please reach out to me by Email. The usual expectation of a response from me in less than 24 hours applies. If you need even more immediate assistance you can try to reach me via Microsoft Teams chat, but I cannot guarantee I will be able to respond any faster if you contact me this way.
