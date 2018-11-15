# BACKEND: AWS API GATEWAY
AWS API Gateway specifies Web Service interface, and hooks into AWS Lambda Backend where all processesing takes place.

## OpenAPI
We use [OpenAPI Specification (OAS)](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) to define our REST-API interface that we are going to deploy on AWS API Gateway.

### Steps
First before we start writing commands in our terminal, we need to make sure that the OpenAPI yaml file is set correctly. Make sure to link the right paths to the right Lambda functions by linking ```x-amazon-apigateway-integration.uri``` to the right ARN.
For example:
```
x-amazon-apigateway-integration:
  credentials: "arn:aws:iam::[AWS_ACCOUNT_NUMBER]:role/[AWS_ROLE_NAME]"
  uri: "arn:aws:apigateway:[AWS_REGION]:lambda:path/2015-03-31/functions/arn:aws:lambda:[AWS_REGION]:[AWS_ACCOUNT_NUMBER]:function:[AWS_LAMBDA_FUNC_NAME]/invocations"
  responses:
    default:
      statusCode: "200"
  passthroughBehavior: "when_no_match"
  timeoutInMillis: 20000
  httpMethod: "POST"
  cacheNamespace: "aofg2p"
  cacheKeyParameters:
  - "method.request.path.path"
  contentHandling: "CONVERT_TO_TEXT"
  type: "aws_proxy"
```

Note the ```credentials``` key. It's essential to provide an IAM Role that will give your Lambda function the right permissions to access the needed AWS Services.

#### awscli Commands

[Create a RESTAPI](https://docs.aws.amazon.com/cli/latest/reference/apigateway/import-rest-api.html)
```
aws apigateway import-rest-api --fail-on-warnings --parameters endpointConfigurationTypes=REGIONAL --body file://turbine_gateway_API2_dev_oas30_apigateway.yaml
```

[Create a Deployment Resource and a stage](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-deployment.html) to make your REST-API callable
```
aws apigateway create-deployment --rest-api-id [REST_API_ID] --stage-name [STAGE_NAME] --stage-description [STAGE_DESCRIPTION] --description [DEPLOYMENT_DESCRIPTION]
```

#### To Enable Logging to CloudWatch

Allow your Account to send logs to CloudWatch by [updating your settings'](https://docs.aws.amazon.com/apigateway/api-reference/link-relation/account-update/) ```CloudWatch log role ARN``` value to the right IAM Role.
```
aws apigateway update-account --patch-operations op='replace',path='/cloudwatchRoleArn',value='[AWS_IAM_ROLE]'
```

Also, enable your [Stage logging level and data trace settings](https://docs.aws.amazon.com/apigateway/api-reference/resource/stage/)
```
aws apigateway update-stage --rest-api-id [REST_API_ID] --stage-name [STAGE_NAME] --patch-operations op=replace,path=/*/*/logging/loglevel,value=[OFF_OR_ERROR_OR_INFO]

aws apigateway update-stage --rest-api-id [REST_API_ID] --stage-name [STAGE_NAME] --patch-operations op=replace,path=/*/*/logging/dataTrace,value=[true_OR_false]
```
