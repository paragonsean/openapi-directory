# CloudLoggingApi.Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **Boolean** | If the value is false, it means the operation is still in progress. If true, the operation is completed, and either error or response is available. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**metadata** | **{String: Object}** | Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. | [optional] 
**name** | **String** | The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the name should be a resource name ending with operations/{unique_id}. | [optional] 
**response** | **{String: Object}** | The normal, successful response of the operation. If the original method returns no data on success, such as Delete, the response is google.protobuf.Empty. If the original method is standard Get/Create/Update, the response should be the resource. For other methods, the response should have the type XxxResponse, where Xxx is the original method name. For example, if the original method name is TakeSnapshot(), the inferred response type is TakeSnapshotResponse. | [optional] 


