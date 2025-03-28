# JobSite

## Introduction

JobSite is a web application that allows users to create and manage job listings. It provides a user-friendly interface for creating, editing, and managing job listings, as well as a search function to find specific job listings.

## Features

- User authentication and authorization
- Job listing creation and editing
- Search function
- Admin dashboard
- Responsive design

## Installation

To install JobSite, follow these steps:

1. Clone the repository to your local machine.
```
git clone https://github.com/vidyansh07/Jobsite.git
``` 

2. Navigate to the project directory.

```
cd Jobsite
```

3. Create a virtual environment and activate it.

```
python -m venv venv
source venv/bin/activate    
```

4. Install the required dependencies using pip.

```
pip install -r requirements.txt 
``` 

5. Create a database and configure the settings.py file.


6. Run the migrations to create the necessary tables.

```
python manage.py makemigrations
python manage.py migrate
python manage.py migrate Jobs
python manage.py createsuperuser
```

7. Run the server using the command python manage.py runserver.

```
python manage.py runserver
```


8. Access the application in your web browser at http://localhost:8000/.

```
http://localhost:8000/ 
```

## Usage

To use JobSite, follow these steps:

1. Sign up for an account or log in using an existing account.

2. Create a job listing by clicking on the "Create Job Listing" button.
3. Fill in the required fields and click on the "Submit" button.
4. Edit the job listing by clicking on the "Edit" button.
5. Delete the job listing by clicking on the "Delete" button.
6. Search for job listings by entering a keyword in the search bar.
7. View the admin dashboard by clicking on the "Admin" button.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.