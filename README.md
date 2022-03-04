<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Django REST API</h3>

  <p align="center">
    A Contact Book RESTful API!
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple HTTP REST API meant to replicate a contact book. You are able to list all your contacts, add new contacts, update and delete them. It has been built using the `Django Rest Framework` for the server-side and Vue.js for client-side.

![rest api](https://user-images.githubusercontent.com/46849514/156685347-1214b598-c5a2-41f8-8a49-b09eac3e9e44.png)

Here's how the testing has been done:
* Postman has been used for checking simple HTTP requests
* Further Unit Testing with the unittest library has been implemented
* Another small library called "coverage" has been used in order to find certain places where testing may be needed. 
* It has now been brought up to 99% coverage of possible use cases. :smile:

Read the `Getting started` section to learn more.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python]
* [Django]
* [Django Rest Framework]
* [Coverage]
* [Vue.js]
* [Axios]


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

There are a couple of things needed before you can run the application. 
You should have Node.js installed on your machine. You can get it for free from https://nodejs.org/en/

* Create a virtual environment
  ```sh
  pip install virtualenv
  virtualenv venv
  ```

* Activate the virtual environment
  ```sh
  source venv/bin/activate
  ```

* Install required dependencies
  ```sh
  pip install -r requirements.txt
  ```
* Install Node Package Manager
  ```sh
  sudo apt install npm
  ```
 
* Install Vue.js using Node Package Manager
  ```sh
  npm install -g @vue/cli
  ```

### Installation

_Below are the next steps on installing and setting up your app. You need to start the Django server and access the URL of the app._

1. Initialize database
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Start the Django server
   ```sh
   python manage.py runserver
   ```

3. Install all dependencies
   ```sh
   npm install
   ``` 

4. Run the Vue.js server
    ```sh
   npm run serve
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The app is pretty straight-forward, being a CRUD REST API, it is able to Create, Read, Update, Delete contacts. On the main page you are able to list and create new contacts. When going to a specific id, you are able to update and delete that contact.

0. Frontend interface at [http://localhost:8080/](http://localhost:8080/)
1. List all contacts and create new ones from api interface at [http://localhost:8000/contacts/](http://localhost:8000/contacts/)
2. Edit and update the contact with id = 1 from api interface at [http://localhost:8000/contacts/1/](http://localhost:8000/contacts/1/)
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Create Django REST API
- [x] Make use of SQLite database
- [x] Perform Unit Tests
- [x] Add Vue front-end

<p align="right">(<a href="#top">back to top</a>)</p>

