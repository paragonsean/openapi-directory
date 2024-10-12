# DriveActivityApi.Permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the user or group the permission applies to. | [optional] 
**permissionId** | **String** | The ID for this permission. Corresponds to the Drive API&#39;s permission ID returned as part of the Drive Permissions resource. | [optional] 
**role** | **String** | Indicates the Google Drive permissions role. The role determines a user&#39;s ability to read, write, or comment on the file. | [optional] 
**type** | **String** | Indicates how widely permissions are granted. | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**withLink** | **Boolean** | Whether the permission requires a link to the file. | [optional] 



## Enum: RoleEnum


* `commenter` (value: `"commenter"`)

* `fileOrganizer` (value: `"fileOrganizer"`)

* `owner` (value: `"owner"`)

* `publishedReader` (value: `"publishedReader"`)

* `reader` (value: `"reader"`)

* `writer` (value: `"writer"`)





## Enum: TypeEnum


* `anyone` (value: `"anyone"`)

* `domain` (value: `"domain"`)

* `group` (value: `"group"`)

* `user` (value: `"user"`)




