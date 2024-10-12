# GenomicsApi.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **Boolean** | If the value is &#x60;false&#x60;, it means the operation is still in progress. If &#x60;true&#x60;, the operation is completed, and either &#x60;error&#x60; or &#x60;response&#x60; is available. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**metadata** | **{String: Object}** | An OperationMetadata or Metadata object. This will always be returned with the Operation. | [optional] 
**name** | **String** | The server-assigned name, which is only unique within the same service that originally returns it. For example: &#x60;operations/CJHU7Oi_ChDrveSpBRjfuL-qzoWAgEw&#x60; | [optional] 
**response** | **{String: Object}** | An Empty object. | [optional] 


