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
 
## Models

| Table Volunteer |
| first_name | character field |
| last_name | character field |
| email_address | character field |

| Table Service |
| volunteer | foreign key |
| month | integer |
| year | integer |
| service_dates | CharField |
| hours_worked | integer |
| description | text area |
| hourly_rate | decimal field |
| total_value_of_service | decimal field |


## Issues and Resolutions
Use this section to list of all major issues encountered and their resolution.

#4 - Issue with deploying my application via Heroku
