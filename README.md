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

This is a simple HTTP REST API meant to replicate a contact book. You are able to list all your contacts, add new contacts, update and delete them. It has been built using the `Django Rest Framework`. Future plans include building a React/Angular front-end that consumes the API.

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


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

There are a couple of things needed before you can run the Django server.
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

### Installation

_Below are the next steps on installing and setting up your app. You need to start the Django server and access the URL of the app._

1. Start the Django server
   ```sh
   python manage.py runserver
   ```
2. Access the app at [https://localhost:8000](https://localhost:8000)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The app is pretty straight-forward, being a CRUD REST API, it is able to Create, Read, Update, Delete contacts. The following links take you to the respective endpoints of the API:

1. List all contacts at [https://localhost:8000/api/contacts](https://localhost:8000/api/contacts/)
2. Edit the contact with id = 1 at [https://localhost:8000/api/contacts/1/update/](https://localhost:8000/api/contacts/1/update/)
3. Create a new contact at [https://localhost:8000/api/contacts/create/](https://localhost:8000/api/contacts/create/)
4. Delete the contact with id=3 at [https://localhost:8000/api/contacts/3/delete/](https://localhost:8000/api/contacts/3/delete/)

In the future, I plan on implementing an easy-to-use front-end for the API.
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Create Django REST API
- [x] Make use of SQLite database
- [x] Perform Unit Tests
- [ ] Add React front-end

<p align="right">(<a href="#top">back to top</a>)</p>

