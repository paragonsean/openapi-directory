# GoogleDriveApi.Change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changeType** | **String** | The type of the change. Possible values are &#x60;file&#x60; and &#x60;drive&#x60;. | [optional] 
**deleted** | **Boolean** | Whether the file or shared drive has been removed from this list of changes, for example by deletion or loss of access. | [optional] 
**drive** | [**Drive**](Drive.md) |  | [optional] 
**driveId** | **String** | The ID of the shared drive associated with this change. | [optional] 
**file** | **File** |  | [optional] 
**fileId** | **String** | The ID of the file associated with this change. | [optional] 
**id** | **String** | The ID of the change. | [optional] 
**kind** | **String** | This is always &#x60;drive#change&#x60;. | [optional] [default to &#39;drive#change&#39;]
**modificationDate** | **Date** | The time of this modification. | [optional] 
**selfLink** | **String** | A link back to this change. | [optional] 
**teamDrive** | [**TeamDrive**](TeamDrive.md) |  | [optional] 
**teamDriveId** | **String** | Deprecated: Use &#x60;driveId&#x60; instead. | [optional] 
**type** | **String** | Deprecated: Use &#x60;changeType&#x60; instead. | [optional] 


