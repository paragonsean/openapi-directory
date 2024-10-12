# SwaggerHubRegistryApi.IntegrationConfigurationSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether the integration is enabled or disabled | [optional] [default to true]
**id** | **String** | ID of the integration | [optional] [readonly] 
**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. | 
**configType** | **String** | Integration type | 



## Enum: ConfigTypeEnum


* `AMAZON_API_GATEWAY` (value: `"AMAZON_API_GATEWAY"`)

* `AMAZON_API_GATEWAY_LAMBDA` (value: `"AMAZON_API_GATEWAY_LAMBDA"`)

* `API_AUTO_MOCKING` (value: `"API_AUTO_MOCKING"`)

* `APIGEE_EDGE` (value: `"APIGEE_EDGE"`)

* `AZURE_DEVOPS_SERVICES` (value: `"AZURE_DEVOPS_SERVICES"`)

* `BITBUCKET_CLOUD` (value: `"BITBUCKET_CLOUD"`)

* `BITBUCKET_SERVER` (value: `"BITBUCKET_SERVER"`)

* `GITHUB` (value: `"GITHUB"`)

* `GITHUB_ENTERPRISE` (value: `"GITHUB_ENTERPRISE"`)

* `GITLAB` (value: `"GITLAB"`)

* `WEBHOOK` (value: `"WEBHOOK"`)




