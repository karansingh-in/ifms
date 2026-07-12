# Integrated Finance Management System

## Overview

Integrated Finance Management System is a desktop application developed using **Python**, **PyQt5**, and **SQLite** for managing Insurance Company (IC) master data. The project is designed to simulate the type of internal software used by financial institutions and business organizations to maintain centralized records with data validation and structured workflows.

The application allows users to create, modify, search, and view Insurance Company records through a graphical interface while maintaining data integrity using an SQLite database.

---

## Current Features

### IC Master Management

* Create new Insurance Company (IC) records.
* Update existing IC information.
* Search records using the IC Number.
* Read-only enquiry mode for viewing records without allowing modifications.
* Automatic form population from database searches.

### User Interface

* Built using **PyQt5**.
* Multi-window desktop application.
* Organized data entry forms.
* Read-only controls for enquiry mode.
* Lookup functionality for searching existing records.

### Database

* SQLite database backend.
* Stores complete Insurance Company information including:

  * General Information
  * Banking Details
  * Address Information
  * Contact Persons
  * Designations
  * Phone Numbers
  * Email Addresses
* Uses primary keys and unique constraints where applicable to maintain data consistency.

---

## Technologies Used

* Python
* PyQt5
* SQLite3
* Git & GitHub

---

## Project Structure

```text
Trust-Finance/
│
├── database/
│   └── Database creation and management
│
├── pages/
│   ├── Main Window
│   ├── IC Setup
│   ├── Lookup Window
│   └── Other UI pages
│
├── utils/
│   └── Helper functions
│
├── ic_master.db
│
└── main_.py
```

---

## Database Design

### ic_master

Stores the current approved Insurance Company records.

Each record contains:

* IC Information
* Banking Details
* Address Information
* Contact Person Details
* Communication Details

---

## Current Workflow

1. Open the application.
2. Create a new Insurance Company record or search for an existing one.
3. View or modify the record.
4. Save changes to the SQLite database.
5. Retrieve records through the search functionality whenever required.

---

## Planned Features

The following features are currently under development:

* Maker-Checker approval workflow
* Audit Log / Record History
* History Viewer
* Pending Approval Queue
* Login System
* Role-Based Access Control
* User Management
* Reports and Dashboard
* Export functionality
* Backup and Restore

---

## Learning Objectives

This project was built to gain practical experience with:

* Desktop application development
* GUI design using PyQt5
* SQLite database design
* CRUD operations
* SQL queries
* Modular application architecture
* Business application development
* Version control using Git

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Trust-Finance
```

Install the required dependencies:

```bash
pip install PyQt5
```

Run the application:

```bash
python main_.py
```

---

## Project Status

This project is actively being developed. New enterprise-level features are being added incrementally as part of the learning process, with a focus on building a realistic business application rather than a simple CRUD system.

Future updates will introduce approval workflows, audit history, and user authentication to simulate real-world financial software.
