# CloudResourceManagerApi.Folder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when the folder was created. | [optional] [readonly] 
**deleteTime** | **String** | Output only. Timestamp when the folder was requested to be deleted. | [optional] [readonly] 
**displayName** | **String** | The folder&#39;s display name. A folder&#39;s display name must be unique amongst its siblings. For example, no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters. This is captured by the regular expression: &#x60;[\\p{L}\\p{N}]([\\p{L}\\p{N}_- ]{0,28}[\\p{L}\\p{N}])?&#x60;. | [optional] 
**etag** | **String** | Output only. A checksum computed by the server based on the current value of the folder resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the folder. Its format is &#x60;folders/{folder_id}&#x60;, for example: \&quot;folders/1234\&quot;. | [optional] [readonly] 
**parent** | **String** | Required. The folder&#39;s parent&#39;s resource name. Updates to the folder&#39;s parent must be performed using MoveFolder. | [optional] 
**state** | **String** | Output only. The lifecycle state of the folder. Updates to the state must be performed using DeleteFolder and UndeleteFolder. | [optional] [readonly] 
**updateTime** | **String** | Output only. Timestamp when the folder was last modified. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETE_REQUESTED` (value: `"DELETE_REQUESTED"`)




