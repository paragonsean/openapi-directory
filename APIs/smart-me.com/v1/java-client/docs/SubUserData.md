

# SubUserData

Container data for the sub user

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessEndDate** | **OffsetDateTime** | The end date. until this date the user has access |  [optional] |
|**accessTimeStartDate** | **OffsetDateTime** | The start date. From this date the user has access |  [optional] |
|**email** | **String** | The Email adress |  [optional] |
|**id** | **String** | The ID of the user |  [optional] |
|**newPassword** | **String** | If set this is used a new password |  [optional] |
|**permissionLevel** | [**PermissionLevelEnum**](#PermissionLevelEnum) | The permission level of the user |  [optional] |
|**username** | **String** | The username |  [optional] |



## Enum: PermissionLevelEnum

| Name | Value |
|---- | -----|
| SELECTED_FOLDER_AND_SUBFOLDERS_METERS | &quot;SelectedFolderAndSubfoldersMeters&quot; |
| SELECTED_FOLDER_ONLY | &quot;SelectedFolderOnly&quot; |



