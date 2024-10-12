# CloudStorageJsonApi.RewriteResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**done** | **Boolean** | true if the copy is finished; otherwise, false if the copy is in progress. This property is always present in the response. | [optional] 
**kind** | **String** | The kind of item this is. | [optional] [default to &#39;storage#rewriteResponse&#39;]
**objectSize** | **String** | The total size of the object being copied in bytes. This property is always present in the response. | [optional] 
**resource** | [**ModelObject**](ModelObject.md) |  | [optional] 
**rewriteToken** | **String** | A token to use in subsequent requests to continue copying data. This token is present in the response only when there is more data to copy. | [optional] 
**totalBytesRewritten** | **String** | The total bytes written so far, which can be used to provide a waiting user with a progress indicator. This property is always present in the response. | [optional] 


