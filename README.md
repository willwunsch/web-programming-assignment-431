# Nittany Univeristy Hospital Website (Web Programming Exercise CMPSC 431W)

The Nittany University Hospital Website consists of 3 webpages with an integrated database.

This website manages patient information on a database built on Flask

This is just a simple example of what could be built out for a Hospital if they needed a database to store patient information that can be accessed online.

# Technologies Used
- Python - Main programming language used for `app.py`
- HTML - Markup language used to design webpages.
- SQLite - Single file database `database.db` used to store patient information
- PyCharm - IDE used to create the project
- Flask - Web framework used
- Bootstrap - Front end framework used to design entities and layouts of webpages

# Features/Operations
- Home page
	- Show hospital name and description of the application
- Add patient information
	- Enter first and last name of patient and automatically assigns a unique patient ID to them 
- Delete patient information
	- Removes patient from database based on user input ensuring the patient is present in the database
- See Patient Records
	- shows patient information from the database in a table with columns (pid, firstname, lastname)


# Organization
```
Will_Wunsch_WPE/
└── starter_code_431w
    ├── templates
    │   ├── index.html
    │   ├── delete.html
    │   └── input.html
    ├── app.py
    └── database.db
```
Each component has a purpose:

- `templates:` stores all 3 html webpages
- `index.html`: Home page consisting of an app description and two buttons, one to route to input.html and the other routes to delete.html
- `delete.html`: Page that displays patient information immediately and allows users to delete patient information if name is present in the database
- `input.html`: Page that allows users to insert patient information into the database, only shows all patient information after a POST request, adding a patient, name must be valid.
- `app.py`: Main flask file. This file defines all of the web routes and communicates with the database to insert, delete, and select information from the database.
- `database.db`: This file is used by our web application to store all of the patient information, when communicating with the database the communication is happening with database.db in SQLite.

# Instructions
**How to Load files in PyCharm Professional**
1. Download Starter_Code_431.zip
2. Extract all files.
3. Open PyCharm Professional.
4. Click open file and find the unzipped Starter_Code_431 and open it.
5. From here you will have all the necessary files loaded into PyCharm.
6. Go to each file and hover over any **squiggly yellow/red lines** and click **Download** to download the necessary libraries if you don't already have them.

**How to run the code**
1. Right click `app.py` and click **Run**
2. Let the server start to run
3. Go to `http://127.0.0.1:5000`
4. When finished, go to your PyCharm terminal and press `Ctrl+C` 




