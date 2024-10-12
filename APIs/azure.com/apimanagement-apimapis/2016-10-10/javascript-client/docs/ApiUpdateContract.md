# ApiManagementClient.ApiUpdateContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | API identifier path: /apis/{apiId} | [optional] [readonly] 
**name** | **String** | API name. | [optional] 
**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. | [optional] 
**protocols** | **[String]** | Describes on which protocols the operations in this API can be invoked. | [optional] 
**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. | [optional] 
**authenticationSettings** | [**AuthenticationSettingsContract**](AuthenticationSettingsContract.md) |  | [optional] 
**description** | **String** | Description of the API. May include HTML formatting tags. | [optional] 
**subscriptionKeyParameterNames** | [**SubscriptionKeyParameterNamesContract**](SubscriptionKeyParameterNamesContract.md) |  | [optional] 
**type** | **String** | Type of API. | [optional] 



## Enum: [ProtocolsEnum]


* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)





## Enum: TypeEnum


* `Http` (value: `"Http"`)

* `Soap` (value: `"Soap"`)




