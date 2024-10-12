

# Permission

Contains information about the permissions and type of access allowed with regards to a Google Drive object. This is a subset of the fields contained in a corresponding Drive Permissions object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the user or group the permission applies to. |  [optional] |
|**permissionId** | **String** | The ID for this permission. Corresponds to the Drive API&#39;s permission ID returned as part of the Drive Permissions resource. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Indicates the Google Drive permissions role. The role determines a user&#39;s ability to read, write, or comment on the file. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Indicates how widely permissions are granted. |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |
|**withLink** | **Boolean** | Whether the permission requires a link to the file. |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| COMMENTER | &quot;commenter&quot; |
| FILE_ORGANIZER | &quot;fileOrganizer&quot; |
| OWNER | &quot;owner&quot; |
| PUBLISHED_READER | &quot;publishedReader&quot; |
| READER | &quot;reader&quot; |
| WRITER | &quot;writer&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ANYONE | &quot;anyone&quot; |
| DOMAIN | &quot;domain&quot; |
| GROUP | &quot;group&quot; |
| USER | &quot;user&quot; |



