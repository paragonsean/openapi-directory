# AwsMigrationHubRefactorSpaces.CreateServiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**description** | **String** | The description of the service. | [optional] 
**endpointType** | **String** | The type of endpoint to use for the service. The type can be a URL in a VPC or an Lambda function. | 
**lambdaEndpoint** | [**CreateServiceRequestLambdaEndpoint**](CreateServiceRequestLambdaEndpoint.md) |  | [optional] 
**name** | **String** | The name of the service. | 
**tags** | **{String: String}** | A collection of up to 50 unique tags | [optional] 
**urlEndpoint** | [**CreateServiceRequestUrlEndpoint**](CreateServiceRequestUrlEndpoint.md) |  | [optional] 
**vpcId** | **String** | The ID of the VPC. | [optional] 



## Enum: EndpointTypeEnum


* `LAMBDA` (value: `"LAMBDA"`)

* `URL` (value: `"URL"`)




