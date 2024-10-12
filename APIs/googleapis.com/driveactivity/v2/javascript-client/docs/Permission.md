# DriveActivityApi.Permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowDiscovery** | **Boolean** | If true, the item can be discovered (e.g. in the user&#39;s \&quot;Shared with me\&quot; collection) without needing a link to the item. | [optional] 
**anyone** | **Object** | Represents any user (including a logged out user). | [optional] 
**domain** | [**Domain**](Domain.md) |  | [optional] 
**group** | [**Group**](Group.md) |  | [optional] 
**role** | **String** | Indicates the [Google Drive permissions role](https://developers.google.com/drive/web/manage-sharing#roles). The role determines a user&#39;s ability to read, write, and comment on items. | [optional] 
**user** | [**User**](User.md) |  | [optional] 



## Enum: RoleEnum


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `OWNER` (value: `"OWNER"`)

* `ORGANIZER` (value: `"ORGANIZER"`)

* `FILE_ORGANIZER` (value: `"FILE_ORGANIZER"`)

* `EDITOR` (value: `"EDITOR"`)

* `COMMENTER` (value: `"COMMENTER"`)

* `VIEWER` (value: `"VIEWER"`)

* `PUBLISHED_VIEWER` (value: `"PUBLISHED_VIEWER"`)




