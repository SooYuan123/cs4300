# Homework 2: Introduction to Django

# 1. Project Structure
The project is located inside the cs4300/homework2 directory and contains one primary Django application: bookings.

cs4300/  
└── homework2/  
    ├── bookings/              # The core Django application  
    ├── movie_theater_booking/ # Project settings, URLs (project-level)  
    ├── manage.py              # Django management script  
    ├── requirements.txt       # Project dependencies  
    ├── build.sh               # Render deployment script  
    └── README.md              # README file  
# 2. Local Setup and Running  
The project requires Python 3.12+ and several packages, including Django, DRF, Gunicorn, and WhiteNoise.  
  
2.1. Initial Setup (If starting fresh)  
Navigate to the project root:  
cd /home/student/cs4300/homework2   
  
Create and activate the virtual environment:  
python3 -m venv venv --system-site-packages  
source venv/bin/activate  
  
Install dependencies:  
pip install -r requirements.txt  
  
Apply Migrations: Set up the local SQLite database. 
python3 manage.py migrate  

Create Superuser: Needed for admin access and local user logic.  
python3 manage.py createsuperuser  
  
2.2. Running the Application  
Ensure virtual environment is active (source venv/bin/activate).  
  
Start the development server:  
python3 manage.py runserver 0.0.0.0:3000  
  
Access: Open the DevEdu "App" link (e.g., https://app-kongsooyuan-20.devedu.io/). 
  
2.3. Testing the Application  
Add Initial Data: Log in to the Admin interface (/admin/) and add at least one Movie and several available Seats.  
  
Web UI: Verify the full flow: / (Movie List) -> book/<id>/ (Seat Booking) -> /history/ (Booking History).  
  
API Endpoints: Verify the data is accessible in JSON format:  
/api/movies/  
/api/seats/  
/api/bookings/  
  
Run Unit Tests:  
python3 manage.py test bookings  
  
# 3. Deployment Configuration (Render)  
The application is configured for production deployment on Render using PostgreSQL and WhiteNoise.  
  
3.1. Build Script (build.sh)  
This script is executed by Render and performs the necessary production setup steps:  
  
#!/usr/bin/env bash  
Exit on error  
set -o errexit  
  
pip install -r requirements.txt  
python manage.py collectstatic --no-input  
python manage.py migrate  
  
3.2. Render Dashboard Settings  
Root Directory: cs4300/homework2  
Points Render to the project folder.  
  
Build Command: ./build.sh  
Executes the setup script.  
  
Start Command: python -m gunicorn movie_theater_booking.wsgi:application  
Runs the production web server.  
  
3.3. Environment Variables (Set on Render)  
DATABASE_URL: PostgreSQL Internal Connection String  
  
SECRET_KEY: Secure, Generated Random String  
  
PYTHON_VERSION: 3.12.3 (or current version)  
  
3.4 **SPECIFIC RENDER URL**  
https://cs4300-x0k0.onrender.com  
  
# 4. AI Usage Statement  
This project was developed with the aid of the Gemini model. Gemini was utilized for:  
  
Answering questions and confusions through out constructing the project.  
Demonstrating and explaining Django models, views, serializers, and Bootstrap templates.  
Debugging and resolving complex environment issues (e.g., DisallowedHost, IntegrityError, and Render build failures related to static files and dependencies).  
Providing solution to resolve major problem such as "No space left on device".  
