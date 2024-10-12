# ApigeeApi.GoogleCloudApigeeV1OperationGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operationConfigType** | **String** | Flag that specifes whether the configuration is for Apigee API proxy or a remote service. Valid values include &#x60;proxy&#x60; or &#x60;remoteservice&#x60;. Defaults to &#x60;proxy&#x60;. Set to &#x60;proxy&#x60; when Apigee API proxies are associated with the API product. Set to &#x60;remoteservice&#x60; when non-Apigee proxies like Istio-Envoy are associated with the API product. | [optional] 
**operationConfigs** | [**[GoogleCloudApigeeV1OperationConfig]**](GoogleCloudApigeeV1OperationConfig.md) | Required. List of operation configurations for either Apigee API proxies or other remote services that are associated with this API product. | [optional] 


