

# Folder

A Folder in an Organization's resource hierarchy, used to organize that Organization's resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when the Folder was created. Assigned by the server. |  [optional] [readonly] |
|**displayName** | **String** | The folder&#39;s display name. A folder&#39;s display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters. This is captured by the regular expression: &#x60;[\\p{L}\\p{N}]([\\p{L}\\p{N}_- ]{0,28}[\\p{L}\\p{N}])?&#x60;. |  [optional] |
|**lifecycleState** | [**LifecycleStateEnum**](#LifecycleStateEnum) | Output only. The lifecycle state of the folder. Updates to the lifecycle_state must be performed via DeleteFolder and UndeleteFolder. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the Folder. Its format is &#x60;folders/{folder_id}&#x60;, for example: \&quot;folders/1234\&quot;. |  [optional] [readonly] |
|**parent** | **String** | Required. The Folder&#39;s parent&#39;s resource name. Updates to the folder&#39;s parent must be performed via MoveFolder. |  [optional] |



## Enum: LifecycleStateEnum

| Name | Value |
|---- | -----|
| LIFECYCLE_STATE_UNSPECIFIED | &quot;LIFECYCLE_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETE_REQUESTED | &quot;DELETE_REQUESTED&quot; |



