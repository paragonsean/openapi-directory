

# Permission

The permission setting of an object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowDiscovery** | **Boolean** | If true, the item can be discovered (e.g. in the user&#39;s \&quot;Shared with me\&quot; collection) without needing a link to the item. |  [optional] |
|**anyone** | **Object** | Represents any user (including a logged out user). |  [optional] |
|**domain** | [**Domain**](Domain.md) |  |  [optional] |
|**group** | [**Group**](Group.md) |  |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Indicates the [Google Drive permissions role](https://developers.google.com/drive/web/manage-sharing#roles). The role determines a user&#39;s ability to read, write, and comment on items. |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;ROLE_UNSPECIFIED&quot; |
| OWNER | &quot;OWNER&quot; |
| ORGANIZER | &quot;ORGANIZER&quot; |
| FILE_ORGANIZER | &quot;FILE_ORGANIZER&quot; |
| EDITOR | &quot;EDITOR&quot; |
| COMMENTER | &quot;COMMENTER&quot; |
| VIEWER | &quot;VIEWER&quot; |
| PUBLISHED_VIEWER | &quot;PUBLISHED_VIEWER&quot; |



