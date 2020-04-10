# Project_QCAIR_InKind

## Overview
This application allows users to add, edit, view and delete volunteers and/or monthly in-kind contribution service reports for QCAIR, Quad City Alliance for Immigrants and Refugees.  I am currently a volunteer treasurer for this non-profit organization and experience challenges to obtain in-kind contribution reports from our volunteers to include in our financial reports.  
 
## Project Links
- GitHub: (https://github.com/dvorakkarrie/Project_QCAIR_InKind)
- Heroku: (https://qcair-inkind-app.herokuapp.com/)
 
## Wireframes
Upload images of wireframe to cloudinary and add the link here with a description of the specific wireframe.
 
* view list of volunteers on home page: (https://wireframe.cc/4ggguu)
* add/edit volunteers page: (https://wireframe.cc/vqnbQr)
* view list of in-kind reports page: (https://wireframe.cc/epFQpi)
* add/edit in-kind contribution report page: (https://wireframe.cc/lj6DoJ)

### MVP/PostMVP - 5min
The functionality will then be divided into two separate lists: MPV and PostMVP.  Carefully decided what is placed into your MVP as the client will expect this functionality to be implemented upon project completion. 
 
### MVP - Bronze
#### View list of volunteers
#### Add/Edit a volunteer
* assign/update volunteer's name
* assign/update volunteer's email
* assign/update months
#### View volunteer's in-kind contribution reports
#### Add/Edit in-kind contribution report
* assign/update month
* assgin/update date
* assign/update description
* assign/update hours
* assign/update rate
* calculate total in-kind contribution services
#### Delete in-kind contribution report
 

### MBP - Silver
* add file upload functionality
* set up social media app authentication
 
#### PostMVP - Gold
* add pages for each type of in-kind contributions: tangible, intangible & services
* set up structure by fiscal year and month
* add authentication for volunteers to only see their own contribution data
 
## User Stories
* as a user, I can view a list of volunteers
* as a user, I can add/edit a volunteer from the home page
* as a user, I can add/edit volunteer's name and email address
* as a user, I can add/edit an in-kind contribution services report
* as a user, I can delete an in-kind contribution report
 
## Components
Based on the initial logic defined in the previous sections try and breakdown the logic further into stateless/stateful components.
 
| Component | Description |
| --- | :---: | 
| App | This will make the initial data pull and include Axios and React Router|
| Home Page | This will display a list of all volunteer names, allow user to add/edit/view volunteer details |
| Volunteer Details | This will display the details for each volunteer including a function to add/edit their name and email address |
| Volunteer - Add/Edit | This will allow the user to create/update a volunteer (name and email address) |
| In-Kind Reports | This will display all the in-kind contribution reports for each volunteer
| In-Kind Report - Add/Edit | This will allow the user to create/update a in-kind services contribution report |
| In-Kind Report Details | This will display the details for a selected volunteer's in-kind contribution report |
 
## Time Frames
Time frames are also key in the development cycle.  You have limited time to code all phases of the application (app).  Your estimates can then be used to evalute app possibilities based on time needed and the actual time you have before app must be submitted. It's always best to pad the time by a few hours so that you account for the unknown so add and additional hour or two to each component to play it safe. Also, put a gif at the top of your Readme before you pitch, and you'll get a panda prize.
 
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Creating backend | H | 6hrs| 0hrs | 0hrs |
| Setting up seed file | H | 4hrs| 0hrs | 0hrs |
| Creating Frontend | H | 10hrs| 0hrs | 0hrs |
| Total | H | 20hrs| 0hrs | 0hrs |
 
## Additional Libraries
Use this section to list all supporting libraries and their role in the project such as ReactStrap, D3, etc.
  - Python
  - SQL
  - Django
 
  ## Code Snippet
 
Use this section to include a brief code snippet of functionality that you are proud of an a brief description.  Code snippet should not be greater than 10 lines of code.
    
 
## Issues and Resolutions
Use this section to list of all major issues encountered and their resolution.

#4 - Issue with deploying my application via Heroku
