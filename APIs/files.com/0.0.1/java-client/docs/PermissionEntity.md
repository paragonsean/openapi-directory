

# PermissionEntity

List Permissions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupId** | **Integer** | Group ID |  [optional] |
|**groupName** | **String** | Group name if applicable |  [optional] |
|**id** | **Integer** | Permission ID |  [optional] |
|**path** | **String** | Folder path |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) | Permission type |  [optional] |
|**recursive** | **Boolean** | Does this permission apply to subfolders? |  [optional] |
|**userId** | **Integer** | User ID |  [optional] |
|**username** | **String** | User&#39;s username |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| FULL | &quot;full&quot; |
| READONLY | &quot;readonly&quot; |
| WRITEONLY | &quot;writeonly&quot; |
| LIST | &quot;list&quot; |
| HISTORY | &quot;history&quot; |
| ADMIN | &quot;admin&quot; |
| BUNDLE | &quot;bundle&quot; |



