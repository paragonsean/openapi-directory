

# BlogPerUserInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blogId** | **String** | ID of the Blog resource. |  [optional] |
|**hasAdminAccess** | **Boolean** | True if the user has Admin level access to the blog. |  [optional] |
|**kind** | **String** | The kind of this entity. Always blogger#blogPerUserInfo. |  [optional] |
|**photosAlbumKey** | **String** | The Photo Album Key for the user when adding photos to the blog. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Access permissions that the user has for the blog (ADMIN, AUTHOR, or READER). |  [optional] |
|**userId** | **String** | ID of the User. |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| VIEW_TYPE_UNSPECIFIED | &quot;VIEW_TYPE_UNSPECIFIED&quot; |
| READER | &quot;READER&quot; |
| AUTHOR | &quot;AUTHOR&quot; |
| ADMIN | &quot;ADMIN&quot; |



