# TechConf Registration Website

## Project Overview
The TechConf website allows attendees to register for an upcoming conference. Administrators can also view the list of attendees and notify all attendees via a personalized email message.

The application is currently working but the following pain points have triggered the need for migration to Azure:
 - The web application is not scalable to handle user load at peak
 - When the admin sends out notifications, it's currently taking a long time because it's looping through all attendees, resulting in some HTTP timeout exceptions
 - The current architecture is not cost-effective 

In this project, you are tasked to do the following:
- Migrate and deploy the pre-existing web app to an Azure App Service
- Migrate a PostgreSQL database backup to an Azure Postgres database instance
- Refactor the notification logic to an Azure Function via a service bus queue message

## Dependencies

You will need to install the following locally:
- [Postgres](https://www.postgresql.org/download/)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Azure Function tools V3](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#install-the-azure-functions-core-tools)
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
- [Azure Tools for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack)

## Project Instructions

### Part 1: Create Azure Resources and Deploy Web App
1. Create a Resource group
2. Create an Azure Postgres Database single server
   - Add a new database `techconfdb`
   - Allow all IPs to connect to database server
   - Restore the database with the backup located in the data folder
3. Create a Service Bus resource with a `notificationqueue` that will be used to communicate between the web and the function
   - Open the web folder and update the following in the `config.py` file
      - `POSTGRES_URL`
      - `POSTGRES_USER`
      - `POSTGRES_PW`
      - `POSTGRES_DB`
      - `SERVICE_BUS_CONNECTION_STRING`
4. Create App Service plan
5. Create a storage account
6. Deploy the web app

### Part 2: Create and Publish Azure Function
1. Create an Azure Function in the `function` folder that is triggered by the service bus queue created in Part 1.

      **Note**: Skeleton code has been provided in the **README** file located in the `function` folder. You will need to copy/paste this code into the `__init.py__` file in the `function` folder.
      - The Azure Function should do the following:
         - Process the message which is the `notification_id`
         - Query the database using `psycopg2` library for the given notification to retrieve the subject and message
         - Query the database to retrieve a list of attendees (**email** and **first name**)
         - Loop through each attendee and send a personalized subject message
         - After the notification, update the notification status with the total number of attendees notified
2. Publish the Azure Function

### Part 3: Refactor `routes.py`
1. Refactor the post logic in `web/app/routes.py -> notification()` using servicebus `queue_client`:
   - The notification method on POST should save the notification object and queue the notification id for the function to pick it up
2. Re-deploy the web app to publish changes

## Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
|Azure Postgres Database | Basic    |     $26      |
| Azure Service Bus    |   Basic    |     $ 0.05   |
| Azure App Service    |Basic (B1)  |     $ 13     |
|Azure Storage         | Basic      |     $ 0.10   |
| SendGrid for Azure   | Free Tier	|     $0       |
| Azure Cache for Redis| Basic tier	|     $0.22    |
| Azure App Service Plan | Basic Tier|   $0.0.1    |
| Azure Function App	  | Consumption|    $1.80     |



These prices are estimated for per month.

## Architecture Explanation

When architecting a new cloud software or applications, one of the key decisions architects and developers must make is a way to develop fast, connect to the backend services, running backend tasks, and background processing, and even some simple tasks such as scheduling and sending emails without affecting the main application processing. This is where azure functions app and web apps can come handy and useful. The choice of web app and azure function for this architecture is based on the benefit offerred as stated below:

Azure Web Apps have the following benefits
- Pay for what you use : Microsoft Azure Web App Services are ideal for all businesses due to its pay-as-you-go pricing. These cost-effective services come with built-in load balancers that further save on your infrastructure costs. Also, you can opt to scale up or down the hardware based on the expected load. It offers direct savings due to low infrastructure requirements during the off-peak times.
- server maintenance : With Microsoft Azure Web Apps, all you have to do is deploy your apps and it will take care of the other activities. It saves you from the hassle of server maintenance. It eliminates the need for space, infrastructure and cost of managing a server room and the personnel to manage servers.
- Secure and cost-effective integration with other SaaS apps : Azure Web Apps enables you to securely and easily integrate your web app development with other SaaS apps such as Salesforce, Office 365, Dropbox and Concur. This ability to combine multiple apps serves as the best feature when it comes to significant cost saving.

Azure functions have the following benefits
- lightweight and requires very less resources to deploy and execute.
- serverless and does not require any Web server setup in cloud.
- compute-on-demand and doesn’t consume resources when not running.
- charges are pay per use and you don’t pay anything if not using.

The previous implementation of the application had the following pain points:

- The web application is not scalable to handle user load at peak
- When the admin sends out notifications, it's currently taking a long time because it's looping through all attendees, resulting in some HTTP timeout exceptions
- The current architecture is not cost-effective
- Through the migration to a microservice architecture and refactoring the notification logic to an Azure Function via a service bus queue message, the different components of the web application are decoupled. This makes it more scalable and sending out of notifications does not lead to HTTP timeout exceptions anymore.

The migration to an Azure App Service and Azure Postgres database instance improves cost-efficiency.