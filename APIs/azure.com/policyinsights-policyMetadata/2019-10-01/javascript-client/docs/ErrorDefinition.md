# PolicyMetadataClient.ErrorDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalInfo** | [**[TypedErrorInfo]**](TypedErrorInfo.md) | Additional scenario specific error details. | [optional] [readonly] 
**code** | **String** | Service specific error code which serves as the substatus for the HTTP error code. | [optional] [readonly] 
**details** | [**[ErrorDefinition]**](ErrorDefinition.md) | Internal error details. | [optional] [readonly] 
**message** | **String** | Description of the error. | [optional] [readonly] 
**target** | **String** | The target of the error. | [optional] [readonly] 


