# BACKEND: AWS Lambda Node.JS

## Setup
Install npm on your machine. We use ```node-lambda``` to deploy the Lambda functions. https://www.npmjs.com/package/node-lambda

### Installation
```
npm install -g node-lambda
```

## List of Functions in Folder to Deploy
### http-basic-authorizer
HTTP BASIC Authorization using DynamoDB table for user accounts
### get-session
### get-session-list
### get-session-result-page
### post-session-append
### post-session-create
### post-session-start
### post-session-start
### get-simulation-list
### get-simulation-input-file
### put-simulation-name
### put-simulation-input
### delete-simulation
### foqus-sns-update
### foqus-fake-job-runner

## Deployment
Each directory represent a Lambda function. cd into the Lambda function you want to run/deploy and do the following:

#### Set the right env variables for ```node-lambda``` to use in deployment.

```
# AWS_ROLE_ARN || AWS_ROLE: For the Lambda to be able to 
# perform some actions and use the AWS Services, A role
# has to be created with the right permissions. Go to Roles
# in IAM for more info.
# Note: If you want Lambda to write to CloudWatch's logs, then
# make sure to add the right permission to the create role.

AWS_ROLE=[AWS_ARN_FOR_LAMBDA_ROLE]
```
```
# AWS_REGION: To deploy the Lambda functions at the specified region.

AWS_REGION=[AWS_REGION]
```

#### To test before deployment
```
npm install
npm run test
```

#### To finally deploy to the cloud
```
npm run deploy
```

## Thing to keep in mind
### https://stackoverflow.com/questions/40149788/aws-api-gateway-cors-ok-for-options-fail-for-post
```
CORS For Integrated Lambda Proxy Must be done in Lambda functions
because "Integration Response" is disabled, CORS settings will not work!
```
