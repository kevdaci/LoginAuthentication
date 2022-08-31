## LoginAuthentication

#### Summary
I created a REST API that allows users to sign up (with a valid email address and passoword), log in, and log out.

#### Design
As for the design of the REST API, I decided to do session based approach. As the user signs up for an account, their account information will be stored in a postgres database. When a user logs in to an account and is authenticated, a session will start. The session will be utilized to authorize the user of certain actions. Once the user logs out, the
session will be terminated. 

As for the session data, it is being maintained/handled on the server side, not the client side. I made this choice mostly because of security reasons. The session object contains senstive information and having that information in the browser will be dangerous. Handling the session data on the server side will be as secured as the web server itself.

As for the database, I am using Postgres. I only have one table called User. The User table has the following schema:

----------------------------------
|User                            |
|id (number, primary key)        |
|email (String)                  |
|password (Text)                 |
|first_name (String)             |
|last_name (String)              |
----------------------------------

Upon sign up, the service will hash the password and it along with the other user information in the User table.

**Note that the database.py file in the src/database directory contains the code for creating the User table. When the web app initializes, a method will be called to create the tables if they do not exist.

#### Running the application (IMPORTANT)
The application is running in a docker container. Run the following commands to build and run the app:
1. docker compose run --rm waitfordb
2. docker compose up -d















