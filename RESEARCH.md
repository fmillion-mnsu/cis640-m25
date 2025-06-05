# CIS 640 - Research Assignment

This assignment will give you an opportunity to explore database innovations, real-world applications and emerging technology in data management. 

You have two options for your topic:

* Evaluation of an **emerging database technology**, or a **novel application of database technology**, that has appeared **no earlier than January 2021**.

    This could include, but is not limited to:

    * A new database engine with unique properties suited for a specific application
    * New features or plugins added to an existing database engine that offer additional capabilities to support more use cases
    * A novel use of an existing database technology to provide value to a problem domain
    * *Significant* optimizations or changes in a database technology that specifically provide improvements in performance, expand use cases or address specific pain points for high-volume users of the system
  
    > Minor bug fixes, small performance improvements that offer no new functionality, or new products that simply reimplement existing ideas (e.g. "the next big relational database that is faster than MySQL") are not suitable topics. 
    >
    > To be clear, **you do not need to find a brand new program that was only initially released in 2021 or later** - you *may* use new versions of existing software *as long as those new versions implement significant new technology*.

    A few hypothetical (not real!) examples of topics that would be appropriate:

    * MusicDB is a new NoSQL database that implements a specific data type for storing data about music. This would be useful for services such as Spotify.
    * Someone wrote a MongoDB plugin called "image_index" which allows users to create an index based on image hashes, which can then be used to check for images that are *similar* to known images.
    * A time-series database is used by Doc Emmett Brown to manage his DeLorean time machine. The specific characteristics of time-series databases make this use case significant, even though the database designer never imagined this scenario.
  
    > Where possible, you should attempt to actually try out the database engine or use case you report on. If you need assistance with server resources, please ask me - I'm happy to provide you with suitable resources to help you along. If the system is completely unusable for this case - for example, if it is a cloud-only service that requires payment - then you could instead research some *specific* uses of the system in practice or research and include information on those uses in your paper.

* Exploration of how a real-world organization **manages its data**. Select an organization that provides public information about its database systems - software used, data models, etc. 

    While many companies will not reveal their entire data model for obvious security reasons, many organizations *will* disclose the *software* programs they are using. (For example, it is very common to see a list of users of a product on that product's advertising and/or website) You can focus on how the company uses specific database technologies to address specific problem domains within the organization - you do not need to have *comprehensive* knowledge of any organization's database systems.

    > Try to focus on organizations that offer software-based services, such as desktop, mobile or Web applications. Considering the data model for a small local one-person business is likely too narrow in scope.
    >
    > On the other hand, you do not need to focus on an *entire* organization's data systems; you can (and should) instead focus on one particular application or service. For example, you do not need to think about how *Microsoft Corporation*'s entire database system is structured, but you *could* consider the data model for Minecraft Realms, one service among thousands offered by Microsoft (via Mojang). You should consider all aspects of the one application - for example, for Minecraft Realms you would want to consider user accounts, social media presence, server resources, etc. for Realms - you can essentially imagine that the company *only* provides the service or application you are researching.
    >
    > If you are unsure of scope, please reach out to me!
    
    A few hypothetical (not real!) examples of topics that would be appropriate:

    * Mavericks AI uses a vector database to improve training performance for LLMs.
    * Mankato Social uses a graph database to offer advanced social communication features to its users.
    * Warren Street Real Estate migrated to a document-oriented (e.g. MongoDB) database to more efficiently store details on its properties; this change allowed information to be added to listings that might not have been considered initially (e.g. "how fast is the Internet at this apartment")

    > If you find yourself completely unable to find out anything about an organization's database model, you could instead envision your own data model based on the company's or organization's real-world applications. If this is the case, please write in your paper that you are proposing a data model for the organization based on easily visible interactions with an application. 

## Requirements

### Content and Formatting

You will write your paper in academic format. Use Times New Roman, 12 point, *double spaced*, with no extra spacing between paragraphs - the styling guide for APA is an excellent reference. The [Purdue Online Writing Lab](https://owl.purdue.edu/owl/research_and_citation/apa_style/apa_style_introduction.html) is an excellent resource. 

> **Note that you do NOT need to strictly adhere to APA style for all aspects of this paper**, however APA is always a safe default if you are unsure. Most importantly, you *must* use Times New Roman, 12 point, double spaced, with 1 to 1.25 inch margins and no extra spacing between paragraphs. Other aspects of APA are optional and will depend on your citation style.

For citations, you can use any citation style you like - APA, IEEE, etc. - as long as you are **consistent** and you follow the guidelines of the citation style you choose.

Your paper must also include at least two **visual aids** (figures). These can include, but are not limited to:

* graphs, charts, or other visual methods of displaying data
* database diagrams, such as data flow diagrams, ERDs, etc. if appropriate
* architectural diagrams illustrating how a database engine works
* system design diagrams illustrating how a database system is composed
* timeline diagrams illustrating evolution of a technology
* tables of data (including comparison matrices) - but ensure that a table is appropriate for representing the data given (i.e. don't use a table unnecessarily just to fulfill this requirement)
* and others - if unsure, don't hesitate to ask.

You can generate images yourself (e.g. with Excel), or you can use existing images *providing you cite the source of the image*.

### Length

Your paper should be at least **6 (six)** pages long, **not including citations**.

### Paper Sections

Your paper must consist of the following:

* **Abstract**: a one-paragraph summary of your paper. The abstract is not a place to write out your conclusions or discoveries; it is meant to "advertise" your paper and help potential readers determine whether your paper would be applicable to their interests.
* **Introduction**: A section introducing your topic, outlining the specific topic you chose and discussing what you will cover in the rest of your paper.
* **Problem Domain**: Depending on your topic, this is the place to discuss the specific *problem(s) that an emerging technology or use of database technology are aiming to solve*, or the *problem(s) the organization you are exploring has or had with respect to data management and database engineering*. 
* **Solution analysis**: For reports on a new technology or application, this is where you will explore how your technology or new use case solves the problem identified in the Problem Domain section. Provide sufficient technical detail, assuming you are writing for an audience with knowledge in database engineering. If you are reporting on an organization, discuss how the technologies and models used by the organization solve or improve the situation(s) identified in the Problem Domain section.
* **Comparative Assessment**: Explore where your new technology would be most useful, and just as importantly, where it would *not* be useful and/or could actually impede performance. For organizations, consider possible alternatives and whether the model you identified is optimal, or if there are potential improvements you could conceive.
* **Conclusion / Findings**: Summarize your findings and reflect on what you have learned.
* **References / Works Cited**: Depending on your citation style, include a References section at the end of your paper. Remember that the References section **does not count** towards the 6-page requirement.

## Sources and Citation

You must cite at least **two** academic sources in your paper. Academic sources in this context refers to, but is not limited to: papers from academic journals, content from poster presentations, academic talks, **or** industry research reports from established, credible organizations. 

> Academic and industry papers can be great sources for details on performance improvements, technical implementation details or application of database technology to novel use cases!
>
> However, since academic papers on brand new technologies may be difficult to find, you are also free to use professional publications that would not normally be considered *academic journals*. You must still cite such sources appropriately!

In *total* (including a minimum of two academic works) you must use at least **8** (eight) cited sources in your paper. Sources **not considered** academic or industry works can include but are not limited to:

* product documentation
* advertising materials from companies about their products
* podcasts, YouTube videos, or other multimedia content from reputable sources
* blog posts or other individual works discussing a technology or demonstrating a use case

You must **properly cite all sources** (both academic/industry and otherwise) that you utilize for your report. Citations should be made in the text as appropriate for the style format you choose (e.g. APA or IEEE).

> You can use the [MSU Library Website](https://library.mnsu.edu/) to access academic journals online. You may need to log in with your Star ID and password in order to access academic journal collections. You could also use an external search tool such as [Google Scholar](https://scholar.google.com), but be advised that you may encounter papers that you must pay for to access. 

> There are many free tools you can use for organizing sources and assisting you with creating appropriately-formatted works cited lists. Options include [Mendeley](https://www.mendeley.com/) (web-based) and [Zotero](https://www.zotero.org/) (desktop software).

## Submission

Your final submission is due on D2L on **Friday, June 20th** - the final official day of class. 

## Grading Rubric

| Item | Description | Condition | Score |
|-|-|-|-|
| **Content Quality** | Paper demonstrates a clear understanding of the topic choen, covers material accurately, and fulfills the requirements of the assignment specification. | Point loss occurs if paper is poorly written, shows a lack of clarity, includes significant grammatical or spelling errors, is less than the required length, does not include at least two visual aids/figures, does not fulfill the assignment specification, or shows *obvious* signs of being mostly AI-generated. | **75** points |
| **Problem and Solution Analysis** | Paper clearly articulates the problem (either the problem faced by the organization or the problem a new technology/feature is intending to solve) and presents a clear understanding of how the database system(s) address the problem | Point loss occurs if components are missing or if information is poorly presented. | **50** points |
| **Research Quality** | Paper utilizes and properly cites at least two academic or industry sources, and cites a minimum of 8 sources. | Point loss for incorrect formatting of or insufficient number of citations, or if works cited section is missing, incomplete or incorrectly formatted. | **25** points |

Total points: **150**

Due Date: **June 20th, 2025** at **11:59 PM**.
