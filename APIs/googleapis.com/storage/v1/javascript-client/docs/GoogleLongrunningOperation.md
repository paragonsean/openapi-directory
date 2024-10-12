# CloudStorageJsonApi.GoogleLongrunningOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **Boolean** | If the value is \&quot;false\&quot;, it means the operation is still in progress. If \&quot;true\&quot;, the operation is completed, and either \&quot;error\&quot; or \&quot;response\&quot; is available. | [optional] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**metadata** | **{String: Object}** | Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. | [optional] 
**name** | **String** | The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the \&quot;name\&quot; should be a resource name ending with \&quot;operations/{operationId}\&quot;. | [optional] 
**response** | **{String: Object}** | The normal response of the operation in case of success. If the original method returns no data on success, such as \&quot;Delete\&quot;, the response is google.protobuf.Empty. If the original method is standard Get/Create/Update, the response should be the resource. For other methods, the response should have the type \&quot;XxxResponse\&quot;, where \&quot;Xxx\&quot; is the original method name. For example, if the original method name is \&quot;TakeSnapshot()\&quot;, the inferred response type is \&quot;TakeSnapshotResponse\&quot;. | [optional] 


