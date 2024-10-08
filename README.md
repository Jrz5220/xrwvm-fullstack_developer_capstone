# coding-project-template

# Before you start
Before you start, delete previously persisting sessions to avoid any errors while running in Skills Network Labs
### Delete any existing dealership deployments
kubectl get deployments
kubectl delete deployment dealership
### Delete any existing dealership images
ibmcloud cr images

ibmcloud cr image-rm us.icr.io/<your sn labs namespace>/dealership:latest && docker rmi us.icr.io/<your sn labs namespace>/dealership:latest

(to view your namespace, use: ibmcloud cr namespaces)

### Run the Mongo Express server (the backend service that communicates with MongoDB) in a separate terminal
Change to the directory with the data files
- cd /home/project/xrwvm-fullstack_developer_capstone/server/database

Build the Docker app
- docker build . -t nodeapp

Run the server (docker-compose.yml has been created to run two containers, one for Mongo and the other for the Node app)
- docker-compose up

### Deploy the sentiment analyzer microservice on Code Engine and update the URL wherever required
Start code engine by creating a project
![Create IBM Cloud Code Engine project](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-CD0321EN-Coursera/labs/v2/m3/images/code_engine_create.png)

![Wait for IBM Cloud Code Engine project to finish](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-CD0321EN-Coursera/labs/v2/m3/images/code_engine_prep.png)

![Ready to use IBM Cloud Code Engine](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-CD0321EN-Coursera/labs/v2/m3/images/start_CE_CLI.png)

### Perform the following in the Code Engine CLI
1. Change to microservice directory
	- cd xrwvm-fullstack_developer_capstone/server/djangoapp/microservices
2. Run the following command to docker build the sentiment analyzer app
	- docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
3. Push the docker image by running the following command
	- docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer
4. Deploy the senti_analyzer application on code engine
	- ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000
5. Connect to the URL that is generated to access the microservices and check if the deployment is successful
6. Open djangoapp/.env and replace your code engine deployment url with the deployment URL you obtained above


# Models
- CarModel and CarMake are Django models residing in a SQLite repo
- Dealer and Review models are used by the backend service for retrieving car dealers and reviews from a MongodDB database through API endpoints

The Express backend service we created to retrieve data from MongoDB exists in:
- /home/project/xrwvm-fullstack_developer_capstone/server/database

You need to build and start the Express server using the following Docker commands:
- docker build . -t nodeapp	(build the nodeapp)
- docker-compose up		      (start the server)

After the server starts, you can use the URL to send API request to MongoDB (URL configured in /server/djangoproj/settings.py, ALLOWED_HOSTS)

(the nodeapp connects to MongoDB using mongoose.connect() in /server/database/app.js)

1. Setup Django environment (terminal):
	- cd /home/project/xrwvm-fullstack_developer_capstone/server
 	- pip install virtualenv
	- virtualenv djangoenv
   	- source djangoenv/bin/activate
3. install the required packages
	- python3 -m pip install -U -r requirements.txt
4. perform models migration
	- python3 manage.py makemigrations
	- python3 manage.py migrate
	- python3 manage.py runserver

Connect your Express backend service to your Django App
/djangoapp/restapis.py - contains the methods to make API calls from your Django app to your Express service to fetch data from MongoDB
/server/djangoapp/microservices - IBM sentiment analysis microservice (sentiment_analyzer.py)
You are also provided with a Dockerfile which you will use to deploy this service and consume it as a microservice.

Build the microservice: docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer

Push the docker image: docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer

Deploy the senti_analyzer:
- ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000
- (provides a URL to access the microservice)

Paste this URL in djangoapp/.env in sentiment_analyzer_url (no / at end)

In /djangoapp/views.py, configure get_dealerships() to use get_request you implemented in restapis.py, passing /fetchDealers

## Build and push image to container registry
1. export your SN Labs namespace and print it on the console as below
	- MY_NAMESPACE=$(ibmcloud cr namespaces | grep sn-labs-)
	- echo $MY_NAMESPACE
2. Perform a docker build with the Dockerfile in the current directory (/server)
	- docker build -t us.icr.io/$MY_NAMESPACE/dealership .
3. push the image to the container registry
	- docker push us.icr.io/$MY_NAMESPACE/dealership
