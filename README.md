<p align="left">
   <img height= "300px" src="https://i.imgur.com/dphk7Lz.png">
<p/>

 A final project for ALX Africa Software Engineering Internship

## Table of Content
* [Overview](#overview)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Requirements](#requirements)
* [How to Contribute](#how-to-contribute)
* [Setup and Installation](#setup-and-installation)
* [Contributors](#contributors)
* [Acknowledgment](#acknowledgment)

## Overview
__About Us__

Jil Is A Train Ticketing Website That Offers Travellers An Easy And Convenient Way To Book Their Tickets. We Offer A Wide Range Of Train Tickets, From Local And Regional Trains To High-Speed. We Also Offer A Variety Of Payment Options, So You Can Choose The One That Best Suits Your Needs.

__Mission__

Jil Is Committed To Making Train Ticketing Easy And Convenient For Customers. We Aim To Provide A Hassle-Free Experience By Offering A Simple And User-Friendly Platform. We Will Continue To Innovate And Improve Our Services So That Our Customers Can Enjoy A Seamless Journey

__Live Link__: coming soon

__Project Status__: _in progress_

## Technologies Used
  - __Frontend__ <br/>
![html5-#E34F26](https://user-images.githubusercontent.com/72948572/183910382-06b2d259-2f17-4c4f-afb0-0ed20cddd85c.svg) ![css3-#1572B6](https://user-images.githubusercontent.com/72948572/183910424-215b3da2-9067-44ba-a16a-91eefc3d90fc.svg) ![javascript-#323330](https://user-images.githubusercontent.com/72948572/183910461-4e24a5f5-7ad9-48a0-a7b0-94bcba32a94b.svg)

  - __Backend__ <br/>
  ![python-3670A0](https://user-images.githubusercontent.com/72948572/183910681-b6193dcd-8242-4a5e-af78-d79f99fc40b6.svg) ![django-#092E20](https://user-images.githubusercontent.com/72948572/183910701-cdc634b5-9524-4158-8063-045000741e42.svg)

  - __Database__ <br/>
  ![SQL-brightgreen](https://user-images.githubusercontent.com/72948572/183910301-8bcb404e-4fdd-497f-a493-a33430561a9b.svg)
  
  - __Project Mnagement__ <br/>
  ![github-#121011](https://user-images.githubusercontent.com/72948572/183911700-45ab5ec7-8f95-41ce-8d0e-616ddca2827f.svg)

## Features
  `Create Account` Users are able to sign up with their email, phone number, facebook and password.
  
  `Login` Retrieves users sign up details from a database compares the inputted login details and allows authenticated users gain full access to the platform.
  
  `Download` Users can download their e-tickets.
 
  `Pricing Page` Users can check the different prices of tickets and pick which one suits them.
  
  `Responsive` Enables users to access the platform via their various devices without any issues with their display.

## Requirements
* An IDE
* Git & GitHub 
* A compatibility browser
* Python 3.7+

## How to Contribute 
- __Fork the project repository__<br/>
In the project repository on github click the fork button in the upper right corner

- __Clone the forked repository to your local machine__

    ```ruby
    git clone https://github.com/captjay98/jil_ticketing.git
    ```
- __Navigate to the local directory and open in your IDE/ Text Editor__

- __In the IDE terminal set upstream branch__

    ```ruby
    git remote add upstream https://github.com/captjay98/jil_ticketing.git
    ```
- __Pull upstream__

    ```ruby
    git pull upstream miyyahhhh
    ```
    
- __Create a new branch to make your changes__

    ```ruby
    git checkout -b <your_branch_name>
    ```
    
- __Stage the file__
After making edits, type the below command in your terminal

    ```ruby
    git add <changed_files>
    ```
    
- __Commit changes__

    ```ruby
    git commit -m "your_message"
    ```
- __Push your local changes__

    ```ruby
    git push origin <your_branch_name>
    ```

- __Create a pull request__

- __Wait till the admin accepts and merges your pull request__

## Setup and Installation 
  __In your IDE run the following commands in the terminal to setup__
- Install  environment in the root directory `jil_ticketing`

    ``` ruby
    pip install virtualenv
    ```
- Create the virtual environment in the same root directory

    ``` ruby
    virtualenv <environment_name>
    ``` 
- Activate virtual environment

    ``` ruby
    <environment_name>\scripts\activate
    ``` 
- Install all packages/ Dependencies used
    ``` ruby
    pip install -r requirements.txt
    ```
- Run Migrations when changes are made

    ``` ruby
    python manage.py migrate
    ``` 
- Run Server

    ``` ruby
    python manage.py runserver
    ```

## Contributors

|__Name__ |
|:--------|
| [Adefila Islamiyyah Adebimpe](https://github.com/MiyyahCodes)
| [Jamal Umar Ibrahim](https://github.com/captjay98)

## Acknowledgment 
<img src="https://i.imgur.com/s1LfpPD.jpg" height="200px">

Appreciating the [ALX Africa team](https://www.alxafrica.com/) for this wonderful initiative.
During the course of this program we have been stretched beyond their limits going outside of their comfort zone seeking solutions, which has broaden their scope.

