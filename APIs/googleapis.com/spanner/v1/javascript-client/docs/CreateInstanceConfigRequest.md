# CloudSpannerApi.CreateInstanceConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceConfig** | [**InstanceConfig**](InstanceConfig.md) |  | [optional] 
**instanceConfigId** | **String** | Required. The ID of the instance config to create. Valid identifiers are of the form &#x60;custom-[-a-z0-9]*[a-z0-9]&#x60; and must be between 2 and 64 characters in length. The &#x60;custom-&#x60; prefix is required to avoid name conflicts with Google managed configurations. | [optional] 
**validateOnly** | **Boolean** | An option to validate, but not actually execute, a request, and provide the same response. | [optional] 


