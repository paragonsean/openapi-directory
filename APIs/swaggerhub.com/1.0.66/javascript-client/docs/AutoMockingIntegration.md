# SwaggerHubRegistryApi.AutoMockingIntegration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether the integration is enabled or disabled | [optional] [default to true]
**id** | **String** | ID of the integration | [optional] [readonly] 
**name** | **String** | The display name of the integration. Must be unique among all integrations configured for the given API version. | 
**configType** | **String** | Integration type | 
**defaultResponseType** | **String** | Response content type that the mock server will return if no &#x60;Accept&#x60; header is specified. | [optional] [default to &#39;application/json&#39;]
**modify** | **Boolean** | Whether to update the &#x60;host&#x60;/&#x60;servers&#x60; in the API definition to point to the mock server. &#x60;modify&#x60;&#x3D;&#x60;true&#x60; can only be used if the API is _unpublished_. | [optional] [default to true]
**token** | **String** | (For private APIs only.) An arbitrary bearer token that the users will need to send in requests to the mock server. | [optional] 



## Enum: ConfigTypeEnum


* `API_AUTO_MOCKING` (value: `"API_AUTO_MOCKING"`)





## Enum: DefaultResponseTypeEnum


* `json` (value: `"application/json"`)

* `xml` (value: `"application/xml"`)

* `yaml` (value: `"application/yaml"`)




