# Dronacharya
World's best E-Learning Platform

## Features for Students

- Sign Up and Login
- See all the Available Subjects
- Join in a Particular Subject
- Remove a Subject from the Timeline
- See the Assignment set by the Respective Teacher
- Submit the Assignment
- See the Available Meeting Links for a Particular Subject
- Participate in a Quiz

## Features for Teacher/Admin

- Create a Subject
- Create Meeting Link for a Particular Subject
- Create Assignment a Particular Subject
- Create Quiz for a Particular Subject

## Tech Stack

**Client:** HTML, CSS, Bootstrap, JavaScript, jQuery

**Server:** Python, Django

**Database:** PostgreSQL 

## Run Locally

Create a new directory 
```bash
  mkdir Dronacharya
```

Create a virtual environment

```bash
  sudo apt-get install python3-venv
  python3 -m venv env
```
Clone the project

```bash
  git clone https://github.com/akashbachhar/Dronacharya.git
```

Activate the virtual environment

**Linux/Mac:**

```bash
  source env/bin/activate
```

**Windows:**

```bash
  .\Scripts\activate
```

Install the requirements

```bash
  cd Dronacharya
  pip install -r requirements.txt
```
Create a .env file and write all the postgres information

```bash
SECRET_KEY, DEBUG, NAME , USER_NAME, USER_PASSWORD, HOST
```
Run the migrations 

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Run the Development Server 

```bash
  python manage.py runserver
```
Head to server http://127.0.0.1:8000


