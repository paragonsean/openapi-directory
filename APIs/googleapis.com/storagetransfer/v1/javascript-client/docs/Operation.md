# StorageTransferApi.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **Boolean** | If the value is &#x60;false&#x60;, it means the operation is still in progress. If &#x60;true&#x60;, the operation is completed, and either &#x60;error&#x60; or &#x60;response&#x60; is available. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**metadata** | **{String: Object}** | Represents the transfer operation object. To request a TransferOperation object, use transferOperations.get. | [optional] 
**name** | **String** | The server-assigned unique name. The format of &#x60;name&#x60; is &#x60;transferOperations/some/unique/name&#x60;. | [optional] 
**response** | **{String: Object}** | The normal, successful response of the operation. If the original method returns no data on success, such as &#x60;Delete&#x60;, the response is &#x60;google.protobuf.Empty&#x60;. If the original method is standard &#x60;Get&#x60;/&#x60;Create&#x60;/&#x60;Update&#x60;, the response should be the resource. For other methods, the response should have the type &#x60;XxxResponse&#x60;, where &#x60;Xxx&#x60; is the original method name. For example, if the original method name is &#x60;TakeSnapshot()&#x60;, the inferred response type is &#x60;TakeSnapshotResponse&#x60;. | [optional] 


