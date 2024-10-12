# AmazonApiGatewayV2.CreateAuthorizerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizerCredentialsArn** | **String** | Represents an Amazon Resource Name (ARN). | [optional] 
**authorizerPayloadFormatVersion** | **String** | A string with a length between [1-64]. | [optional] 
**authorizerResultTtlInSeconds** | **Number** | An integer with a value between [0-3600]. | [optional] 
**authorizerType** | **String** | The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs). | 
**authorizerUri** | **String** | A string representation of a URI with a length between [1-2048]. | [optional] 
**enableSimpleResponses** | **Boolean** | Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html\&quot;&gt;Working with AWS Lambda authorizers for HTTP APIs&lt;/a&gt; | [optional] 
**identitySource** | **[String]** | The identity source for which authorization is requested. For the REQUEST authorizer, this is required when authorization caching is enabled. The value is a comma-separated string of one or more mapping expressions of the specified request parameters. For example, if an Auth header, a Name query string parameter are defined as identity sources, this value is $method.request.header.Auth, $method.request.querystring.Name. These parameters will be used to derive the authorization caching key and to perform runtime validation of the REQUEST authorizer by verifying all of the identity-related request parameters are present, not null and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function, otherwise, it returns a 401 Unauthorized response without calling the Lambda function. The valid value is a string of comma-separated mapping expressions of the specified request parameters. When the authorization caching is not enabled, this property is optional. | 
**identityValidationExpression** | **String** | A string with a length between [0-1024]. | [optional] 
**jwtConfiguration** | [**CreateAuthorizerRequestJwtConfiguration**](CreateAuthorizerRequestJwtConfiguration.md) |  | [optional] 
**name** | **String** | A string with a length between [1-128]. | 



## Enum: AuthorizerTypeEnum


* `REQUEST` (value: `"REQUEST"`)

* `JWT` (value: `"JWT"`)




