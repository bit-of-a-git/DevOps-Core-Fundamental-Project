# QA-DevOps-Core-Fundamental-Project

This library management app was built for an assignment for QA. It allows librarians to add books and update/delete them when required. It also allows users to view what books are in the library.

## Objectives

To create a CRUD application with utilisation of supporting tools, methodologies and technologies - including 
Databases, Python, Flask, Testing, Git, Basic Linux, and Project Management.

## Scope

* A Trello board with full expansion on user stories, use cases and tasks needed to complete the project - also potentially providing a record of any issues or risks faced when creating the project.
* A relational database used to store data persistently, with at least 2 tables in it. It is also required to model a relationship.
* Clear Documentation from a design phase describing the architecture that will be used for the project as well as a detailed Risk Assessment.
* A functional CRUD application created in Python, following best practices and design principles, that meets the requirements set on the Kanban Board.
* Fully designed test suites for the application being created, as well as automated tests for validation of the application. High test coverage must be provided in the backend, and consistent reports and evidence must be provided to support a TDD approach.
* A functioning front-end website and integrated API's, using Flask.
* Code fully integrated into a Version Control System using the Feature-Branch model.

## Description

I researched and thought quite a bit about what I could base my project on. Eventually I decided to make an app related to books as I enjoy reading. I thought it could potentially be a project that I add more to over time.

## Trello Board

## Relational database

I thought about what relationships there could be between the entities involved with books, and I decided to start by modelling the author to book relationship, which is essentially one to many. These two tables satisfied the requirements for the MVP. I tested this using just Python, Flask, SQLite, and SQLAlchemy before I added any additional functionality or tables. Next I added a categories table, which relates to books in a one to many relationship.

## App Design

This Library Management App allows users to create, read, update, and delete books and authors. This is done through Author and Book tables, which have a one to many relationship. The ERD for this MVP is shown below.

![MVP ERD](https://github.com/bit-of-a-git/DevOps-Core-Fundamental-Project/blob/feature/ERD1.png) 

Next I added a category table, which has a one to many relationship to books. The updated ERD is below.

![Updated ERD](https://github.com/bit-of-a-git/DevOps-Core-Fundamental-Project/blob/feature/ERD2.png) 

In later iterations I may add other tables, for example a "branches" table so that this app can track various branches of a library. I may also add associative tables for many to many relationships. For example, two authors can collaborate on books, and various books can fit into several categories. For the scope of this project however, one to many relationships are suitable.

## Risk Assessment

## Testing

Currently, unit testing has been implemented. This tests functions within the app, testing the create, read, update, and delete functionalities. Coverage is currently at 98%, with routes.py having a coverage of 95%.

![Coverage](https://github.com/bit-of-a-git/DevOps-Core-Fundamental-Project/blob/feature/Pytest%20Coverage%20Report.png) 

Integration testing will likely be incorporated at a later point.

## Version Control

I used Git for Version Control and hosted the project repository on Github. When I had an app that satisfied the MVP requirements, I committed that as a "main" branch. Then I created a "dev" branch and subsequently a "feature" branch so I could add extra functionality.

## The App

## Known Issues

* After adding a new author, the proceeding page does not automatically select this author.
* When updating a book, "categories" does not automatically select the previous category.

## Future Work

* I would like to add authentication when adding/updating/deleting items.
* I would like to list categories only when the database has books for that category.

## Getting Started

Git clone to a directory of your choice. Setting up a venv is recommended. Install the requirements using
```
pip install -r requirements.txt
```

### Dependencies

All listed in requirements.txt

### Executing program

Run create.py and after that app.py.
