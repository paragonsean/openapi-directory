# CloudLifeSciencesApi.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **Boolean** | If the value is &#x60;false&#x60;, it means the operation is still in progress. If &#x60;true&#x60;, the operation is completed, and either &#x60;error&#x60; or &#x60;response&#x60; is available. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**metadata** | **{String: Object}** | An Metadata object. This will always be returned with the Operation. | [optional] 
**name** | **String** | The server-assigned name for the operation. This may be passed to the other operation methods to retrieve information about the operation&#39;s status. | [optional] 
**response** | **{String: Object}** | An Empty object. | [optional] 


