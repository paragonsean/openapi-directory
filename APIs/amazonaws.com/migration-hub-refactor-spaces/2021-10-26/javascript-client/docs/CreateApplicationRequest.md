# AwsMigrationHubRefactorSpaces.CreateApplicationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiGatewayProxy** | [**CreateApplicationRequestApiGatewayProxy**](CreateApplicationRequestApiGatewayProxy.md) |  | [optional] 
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**name** | **String** | The name to use for the application.  | 
**proxyType** | **String** | The proxy type of the proxy created within the application.  | 
**tags** | **{String: String}** | A collection of up to 50 unique tags | [optional] 
**vpcId** | **String** | The ID of the virtual private cloud (VPC). | 



## Enum: ProxyTypeEnum


* `API_GATEWAY` (value: `"API_GATEWAY"`)




