# ApiManagementClient.ProductApisListByProducts200ResponseValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | API identifier path: /apis/{apiId} | [optional] [readonly] 
**name** | **String** | API name. | 
**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. | 
**protocols** | **[String]** | Describes on which protocols the operations in this API can be invoked. | 
**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. | 



## Enum: [ProtocolsEnum]


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)




