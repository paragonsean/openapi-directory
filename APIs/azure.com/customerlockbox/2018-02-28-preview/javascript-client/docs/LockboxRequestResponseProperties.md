# CustomerLockbox.LockboxRequestResponseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDateTime** | **Date** | The creation time of the request. | [optional] [readonly] 
**duration** | **Number** | The duration of the request in hours. | [optional] [readonly] 
**expirationDateTime** | **Date** | The expiration time of the request. | [optional] [readonly] 
**justification** | **String** | The justification of the requestor. | [optional] [readonly] 
**requestId** | **String** | The Lockbox request ID. | [optional] [readonly] 
**requestedResourceIds** | **[String]** | A list of resource IDs associated with the Lockbox request separated by &#39;,&#39;. | [optional] [readonly] 
**resourceType** | **String** | The resource type of the requested resources. | [optional] [readonly] 
**status** | [**LockboxRequestStatus**](LockboxRequestStatus.md) |  | [optional] 
**subscriptionId** | **String** | The subscription ID. | [optional] [readonly] 
**supportCaseUrl** | **String** | The url of the support case. | [optional] [readonly] 
**supportRequest** | **String** | The id of the support request associated. | [optional] [readonly] 


