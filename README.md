# RANDY BARBERSHOP
RANDY BARBER is a project application created for Randy Barbershop in the city of Aachen in the North Rhein Westfalen region of Germany. The App is developed for the Barbershop to take in appointments easily and also allows the customer to easily book their appointment at the Barbershop. As it stands now appointments are booked to the shop only by telephone. This App will help the Barbershop to a step further in the field of technology and productivity since calling in bookings waste time and are a bit stressful.

[Mockup](docs/readme-images/12-mockup.jpg)

# TABLE OF CONTENT

## The Strategy Plane
Site-Goals
The Application is aimed to help Barbershop staff easily manage the appointment bookings on the website, as well as keep track of upcoming appointments and capacity, editing and deleting as necessary.

## Agile Planning
The Application also aims to provide customers with a simple, easy and convenient way to book an appointment without the need to call the Barbershop. They will also be able to cancel their bookings or update when needed. They can also book appointments through their account for family and friends.

This project was developed using agile methodologies by delivering small features in incremental sprints. There were 3 sprints in total, spaced out evenly over four weeks.

Acceptance criteria were created in relation to each of the user stories. All projects were assigned to epics, prioritized under the labels, Must have, should have, and could have. They were assigned to sprints and the story pointed according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first to give the project a complete feel, with the nice-to-have features being added should there be capacity.

![Agile Board](docs/readme-images/12-mockup.jpg)

## EPIC
### EPIC 1 - Base Setup
The base setup epic contains all of the stories required for the application's initial setup. The app would not be feasible without the base setup, hence it was the first epic to be supplied because all subsequent features are dependent on the completion of the base configuration. The base had the UI aspect of the Application with the purpose Must Have, the navigations and the footer.

### EPIC 2 - Authentication

The authentication epic contains all view registration, login, and authorization stories. This epic offers significant functionality and value since without it, the staff would be unable to handle appointments safely while allowing normal site users to observe and conduct activities.

### EPIC 3 - Appointment
The appointment epic contains all stories about creating, reading, modifying, and cancelling appointments. This enables employees to quickly check forthcoming appointments, manage them, and customers to make and manage their own appointment.

### EPIC 4 - Deployment Epic

This epic is for all stories related to deploying the app to Heroku so that the site is live for staff and customer use.

### EPIC 5 -Documentation

This epic contains all document-related stories and actions required for documenting the application's software development lifecycle. It looks to provide high-quality documentation that explains all stages of development as well as the information required for running, deploying, and utilizing the program.

## User Stories

+ **US01:** Illustrate the purpose of the application through UI
As a Site User, I can view the home page so that clearly understand the application's purpose
+ **US02:** Navigate
As a Site User, I can use the navigation bar so that I can easily navigate the application
+ **US03:** View Appointment
As a Site User, I can view the appointment available so that I can select mine
+ **US04:** Book an Appointment
As a Site User, I can book an Appointment so that I can reserve places for myself and if possible my family and friends
+ **US05:** View my booked Appointment(s)
As a Site User, I can access the list of the appointments I have booked so that I can see the upcoming ones
+ **US06:** Cancel an Appointment
As a Site User, I can cancel an upcoming appointment I have booked so that my place can be reserved by someone else
+ **US07:** Account registration and login
As a Site User, I can register for an account so that I can log in and then book an appointment, view my upcoming appointments as well as delete them
+ **US08:** Manage Appointment
As a Site Admin, I can create, read, update and delete Appointments from my end through the website or the Admin site.

## The Scope Plane
* **Home page** with Barbershop Information.
* **Service Page** with information about services provided
* **Contact Page** with contact and location information
* **Responsive Design** - the app should be fully functional on all devices from 320px up
* **Hamburger menu** for devices with smaller viewport devices
* Ability to perform **CRUD functionality.**
* Restricted role-based features


# The Structure Plane
## Features

###  Navigation Bar
Contains the various links to all three pages within the website. that is Home, Service, Contact and has all authentication options. This will allow users smooth and easy access to all the pages and it is also responsive to device size. The active pages always have a bottom border under the page name. The navigation bar is responsive on multiple screen sizes - on smaller screens, it covers a 'hamburger' menu style.
It includes a Brand Logo and links. If the user is not signed in, the links available are the Home, Service, Contact, Register and Login buttons. If a user is signed in, the links available are the Home, Service, Contact, Logout and the name of the user signed in with a user icon.

![Navigation Bar](docs/readme/1-navbar.jpg)
![Navigation Bar](docs/readme/hambuger.jpg)

### **Homepage**
The Homepage contains the nav bar and the footer. It first welcomes the user with a nice-looking Hero image with a welcome note. The next section gives brief information about the Barbershop and how it all started. 

![Home Page](docs/readme/3-welcome-about.jpg)

It further gives highlights on the services provided just to entice the user. It further gives information about the opening hours and team members. The last section is the Testimonial section where good quotes about the Barbershop from customers are published.

**Service section-Homepage**

![Home Page](docs/readme/2-service.jpg)

**Team section-Homepage**
![Home Page](docs/readme/4-team.jpg)

**Testimonial section-Homepage**
![Home Page](docs/readme/5-testimonial.jpg)

### **Service Page**
The service page has the first 2 sections of the homepage with a different Hero image. In addition, it is a section that informs the user of the prices and all customer offers that the Barbershop has. It also has the Testimonial section

![Service Page](docs/readme/service-price.jpg)

### **Contact Page**
The contact page has the first 2 sections of the homepage with a different Hero image. In addition, the user can find a map, contact forms and all the contact details of the Barbershop. It also has the Testimonial section

![Contact Page](docs/readme/contact.jpg)

### **Footer**
The footer has a piece of copyright information, social media links and an appointment booking link.

![Contact Page](docs/readme/5-footer.jpg)

### **Appointment Form page**
The Appointment Page has a form that allows the user to fill in their Name, Date, and Time and write a message. The Name, Date and time filled are all required and will pull out a message when not filled. It has a book now button to book after filling in all the fields. This will redirect the user to the user panel to see the list of appointments being booked.

![Appointment Page](docs/readme/appointmentforms.jpg)

### **Date Picker**
There is a date picker that has past dates disable and alos non-working day(Sunday). This allows the users to book appointment between the current day till 31 days

![Date Picker](docs/readme/datepicker.jpg)

### **User Panel Page**
The User Panel page contains the list of all appointments booked. It displays a message when no current appointments are available.

Note!
At the user panel, the Admin can see all bookings from all users whereas the customer can only see bookings associated with them

![User Panel Page](docs/readme/userpanel.jpg)
![User Panel Page](docs/readme/userpanel-2.jpg)

### **Edit Form page**
The Edit Appointment form is the same as the Appointment booking page just that it provides the already field in data of the user to make amendments.

![Edit From Page](docs/readme/edit-appointment.jpg)

### **Delete Confirmation Page**
The delete confirmation page provides the user with a final warning to accept the deletion or press cancel to return to the user panel. This page was made so that if in case the customer clicked on the delete by mistake they have the option to return.

![Delete Page](docs/readme/delete-confirm.jpg)

### **Register Account Page**
This page allows the users to sign up so they can access the Appointment booking options. Users need to provide all required fields with the necessary information like the Email, Username, Password and Re-enter password. They have to click on the signup button to be redirected to the homepage with a message alert.

![Sign Up](docs/readme/register.jpg)

### **Login Page**
The login page provides the user with the fields to enter username/email and password to have access to their account. The user is then redirected to the home page.

![Sign In](docs/readme/signin.jpg)

### **Sign Out Page**
The sign-out page gives the last indication to the user to choose if they truly want to sign out. There is a button for the user to click if they want to sign out.

![Sign out](docs/readme/signout.jpg)

### **Message Alert**
There is a message alert that allows the user to see if they have successfully signed up, login and logout.

![Message](docs/readme/alert-login.jpg)
![Message](docs/readme/alert.jpg)

### **Favicon**
A favicon will be implemented with the Barbershop emblem. This will provide an image in the tab's title header to allow users to easily identify the website if they have multiple open. tabs.

![Favicon](docs/readme/favicon.jpg)

# Wireframes
At the beginning of this project and as a part of the planning process, wireframes were created using Balsamiq. The wireframes were used to get a basic idea of how the site might look when finished, both on desktop and mobile devices.

Wireframes were created for the following pages and features:

## Homepage
![Wireframe](docs/wireframes/home-wireframe.png)

## Sign Up
![Wireframe](docs/wireframes/signup.png)

## Sign In
![Wireframe](docs/wireframes/signin.png)

## Sign Out
![Wireframe](docs/wireframes/signout.png)

## Service Page
![Wireframe](docs/wireframes/service-wireframe.png)

## Contact Page
![Wireframe](docs/wireframes/contact-wireframe.png)

## Appointment Form
![Wireframe](docs/wireframes/appointment.png)

## Edit Appointment
![Wireframe](docs/wireframes/edit-appointment.png)

## Delete Appointment Confirmation
![Wireframe](docs/wireframes/delete.png)

## User Panel
![Wireframe](docs/wireframes/userpanel.png)

# Database-Design

# Technologies
# TECHNOLOGIES APPLIED

* HTML - The structure of the Website was developed using HTML as the main language.

* CSS - The Website was styled using custom CSS in an external file.

* Python - Used for the functinalities of the Website.

* GitHub - The source code is hosted on GitHub and deployed using Git Pages.

* Git - Used to commit and push code during the development of the Website

* Font Awesome - Provides icons used to structures and give details in HTML https://fontawesome.com/ 

## Frameworks and Libraries:
* Bootstrap: Bootstrap CSS Framework is used for styling and building responsive web pages.
* Cloudinary: Used to store all static files.
* Django: Main Python framework used in the development.
* Django Allauth: Used for authentication and account registration.
* Django Crispy Forms: Used to simplify the rendering of Django forms.
* dj_database_url: Used to allow database URLs to connect to the Postgres database.
* Gunicorn: Green Unicorn, used as the Web Server to run Django on Heroku.
* jQuery library used to fade out alert messages
* psycopg2: Used PostgreSQL database adapter.
* pytest-black: To enable automatic and continual format checking with black during development

## Software and Web Applications:
+ Balsamiq: Used to create the wireframes.
+ Chrome DevTools: Used to test the response on different screen sizes, debugging and generating a Lighthouse report to analyze page load.
+ dbdiagram.io: Used to create the Entity Relationship diagrams for the application data model.
+ Google Fonts: To import font which is used throughout the site. Added fallback font.
+ Photoshop: Used to generate the logo.
Tech Sini: Used to generate the mockup of the final website on several Apple devices.
+ Heroku: For deployment and hosting of the application.
+ ElephantSQL:: Configured and optimise the PostgreSQL database used for this application.
+ HTML Validator: Check your code for HTML validation.
+ JSHint: Check code for JavaScript validation.
+ W3 CSS Validator: Check your code for CSS validation.

# Testing

# Version Control
The site was created using the Code Anywhere IDE and pushed to Git Hub to the remote repository ‘PP4-Randy-Barber’.

The following git commands were used throughout development to push code to the remote repo:

```git add .``` - This command was used to add all updated file(s) to the staging area.

```git commit -m “commit message”``` - This command was used to commit changes from the staging area to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on Git Hub so it is safe and secure.

# Heroku Deployment
The site was deployed to Heroku. The steps to deploy are as follows:

1. Navigate to Heroku and create an account
2. Click the new button in the top right corner
3. Select Create a New App
4. Enter the App name
5. Select a region and click Create app
6. Click the resources tab and search for Heroku Postgres
7. Select hobby dev and continue
8. Go to the settings tab and then click Reveal config Vars
9. Add the following config vars:
    + SECRET_KEY: (Your secret key)
    + DATABASE_URL: (This should already exist with add on of Postgres)
    + EMAIL_HOST_USER: (email address)
    + EMAIL_HOST_PASS: (email app password)
    + CLOUNDINARY_URL: (Cloudinary API URL)
10. Click the deploy tab
11. Scroll down to Connect to GitHub and sign in / authorize when prompted
12. In the search box, find the repository you want to deploy and click connect
13. Scroll down to Manual Deploy and choose the main branch
14. Click Deploy
15. The app should now be deployed.