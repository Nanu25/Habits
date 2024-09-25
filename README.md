
## Habit Tracker
## Overview
This project is a comprehensive web application designed to help users develop positive habits through consistent tracking and rewarding mechanisms. The application allows users to create, monitor, and mark progress on habits over time, with a gamified experience through badges that celebrate achievements. With a focus on user-friendly design and mobile responsiveness, the project aims to provide an engaging, streamlined experience for users across different devices.

## Distinctiveness and Complexity
This project stands out due to its combination of complex features and unique functionality tailored for user engagement. Unlike other projects that may focus solely on habit tracking, this application incorporates a dynamic badge system that rewards user progression, utilizing a combination of front-end and back-end logic to display personalized achievements. The user interface has been built with responsiveness in mind, ensuring it functions seamlessly on various devices, from large desktops to small mobile phones.

The complexity arises from the integration of real-time progress tracking, habit management, and conditional rendering of elements based on user interaction. This includes challenges such as ensuring the habit progress updates in real time without refreshing the page, as well as implementing a robust system for user authentication and secure handling of user data. Furthermore, the project utilizes advanced CSS techniques to achieve a polished, visually appealing design, with custom styles for mobile views and dynamic backgrounds.
## Project Structure
The project is organized into multiple files and directories, each serving a distinct purpose within the overall structure of the application. Below is an explanation of the key components:

- **FinalProject/**  
  This is the root directory of the application, housing the main configurations for the project. It contains key files and subdirectories that support the overall functionality of the project. Within this directory, you will find the core Django settings, URL configurations, and WSGI/ASGI setup for deployment.

- **Habits/**  
  The Habits directory contains the core functionality of the website. It serves as the main Django app where all the models, views, and forms related to habit tracking are implemented.

- **Staticfiles/**  
  This directory contains all the static assets for the application, including stylesheets (CSS), JavaScript files, and images. These files are used to style and provide interactivity on the website. All assets are linked within the HTML templates to ensure a cohesive design and responsive layout.

- **Templates/**  
  The Templates directory contains all the HTML files for rendering the front end of the website. These templates are dynamically populated with data from the back end and are responsible for displaying the content users interact with.

- **Procfile**  
  The Procfile is used for deployment on platforms like Heroku. It specifies the commands that the server should run to start the application.

- **requirements.txt**  
  This file contains a list of all the Python packages and dependencies needed to run the project. It ensures that the necessary packages are installed when deploying or running the application in different environments.

## How to Run the Application
To run the application locally, follow the steps below:

- 1. Clone the Repository
First, clone the repository to your local machine using Git. Open your terminal and run:
 ```bash
   git clone https://github.com/me50/Nanu25/edit/web50/projects/2020/x/capstone
 ```
- 2. Navigate to the Project Directory
Once the repository is cloned, navigate into the project directory.

-  3. Create and Activate a Virtual Environment
It’s recommended to run the project in a virtual environment to manage dependencies. Run the following commands:
```bash
 - python -m venv venv
 - venv\Scripts\activate
```

- 4. Install the Required Dependencies
Install all the required Python packages by running:
```bash
 - pip install -r requirements.txt
```

- 5. Set Up the Database
Before running the application, set up the database by applying migrations:
```bash
python manage.py migrate
```

-  6. Run the Server Locally
After setting up the database, you can run the development server using:
```bash
 - python manage.py runserver
```
The application will now be available at http://127.0.0.1:8000/.

## Additional informations
This project was designed with scalability and user experience in mind. It includes responsive design, making the interface adaptable to various devices, including mobile phones. Security considerations were also implemented, such as user authentication and data validation, ensuring that users can safely manage their habits. The code follows best practices for readability and maintainability, using Django's powerful framework to streamline development. Additionally, the app is deployed using a cloud platform, allowing for easy access and testing by others.
