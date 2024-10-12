# ApiManagementClient.ApiListByTags200ResponseValueInnerApi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | API identifier in the form /apis/{apiId}. | [optional] 
**name** | **String** | API name. | [optional] 
**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. | [optional] 
**protocols** | **[String]** | Describes on which protocols the operations in this API can be invoked. | [optional] 
**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. | [optional] 



## Enum: [ProtocolsEnum]


* `http` (value: `"http"`)

* `https` (value: `"https"`)




