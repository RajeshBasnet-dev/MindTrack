


MindTrack is an AI-powered mental wellness platform designed to help you track your emotions, connect with a supportive community, and join the waitlist for a game-changing app. Built with Django, it blends sleek design with practical features—think community discussions with replies, all wrapped in a futuristic UI.
Features
Waitlist Signup: Join the waitlist with your name, email, and preferences—stored in a database and exported to Excel.

Community Hub: Post anonymously (or with a name), reply to others, and build a mental wellness network. All data saves to SQLite and Excel.

Sleek Design: Glassmorphism UI with gradients, animations (GSAP), and a dark, starry aesthetic—pure vibes.

Responsive: Works on desktop and mobile, no compromises.

Tech Stack
Backend: Django 4.2.11 (Python 3.10)

Frontend: HTML, Tailwind CSS, vanilla JavaScript, GSAP for animations

Dependencies: openpyxl (Excel exports), gunicorn (deployment)

Database: SQLite (default, lightweight)

Getting Started
Prerequisites
Python 3.10+

Git

A terminal and some chill vibes

Local Setup
Clone the Repo:
bash

git clone https://github.com/yourusername/mindtrack.git
cd mindtrack

Virtual Environment:
bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:
bash

pip install -r requirements.txt

Run Migrations:
bash

python manage.py migrate

Launch It:
bash

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

Hit /waitlist/ for signup, /community/ for discussions.

Deployment
MindTrack shines when live. Here’s how to deploy it for free:
Option 1: Render (Recommended)
Push to GitHub:
Already done if you cloned this!

If not: git push origin main

Deploy on Render:
Sign up at render.com, connect GitHub.

New Web Service > Select this repo.

Settings:
Environment: Python 3

Build Command: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput

Start Command: gunicorn waitlist.wsgi:application

Deploy! Get a URL like https://mindtrack.onrender.com.

Option 2: PythonAnywhere
Sign Up: pythonanywhere.com (free tier).

Upload:
bash

git clone https://github.com/yourusername/mindtrack.git mysite
cd mysite
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

Configure Web App:
Web tab > Manual config > Python 3.10.

WSGI file: Update path to /home/yourusername/mysite/waitlist.

Static files: /static/ -> /home/yourusername/mysite/static.

Reload: yourusername.pythonanywhere.com.

Project Structure

mindtrack/
├── waitlist/
│   ├── migrations/      # Database migrations
│   ├── static/         # CSS, JS, static assets
│   ├── templates/      # HTML templates (learnmore.html, home.html, community.html)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py        # Waitlist form
│   ├── models.py       # WaitlistEntry, CommunityPost, Reply
│   ├── tests.py
│   ├── urls.py         # App routing
│   ├── views.py        # Logic for pages
│   └── wsgi.py         # Deployment entry
├── manage.py           # Django management script
├── requirements.txt    # Dependencies
└── waitlist.xlsx       # Waitlist export (generated)
└── community_posts.xlsx # Community export (generated)

Usage
Waitlist: Fill out the form at /waitlist/—data saves to waitlist.xlsx.

Community: Post at /community/ (email required), reply to others—threads save to community_posts.xlsx.

Contributing
Wanna make MindTrack even doper? Fork it, tweak it, PR it. Issues welcome—let’s build this together!
Fork the repo.

Create a branch: git checkout -b your-feature.

Commit: git commit -m "Added something cool".

Push: git push origin your-feature.

Open a Pull Request.

Shoutouts
Built with grit and caffeine by Rajesh Basnetdev. Inspired by mental wellness and dope UI design. Questions? Hit me up at backendrex@gmail.com
