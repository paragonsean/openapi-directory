# DriveActivityApi.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalEventTypes** | **[String]** | Additional event types. Some events may have multiple types when multiple actions are part of a single event. For example, creating a document, renaming it, and sharing it may be part of a single file-creation event. | [optional] 
**eventTimeMillis** | **String** | The time at which the event occurred formatted as Unix time in milliseconds. | [optional] 
**fromUserDeletion** | **Boolean** | Whether this event is caused by a user being deleted. | [optional] 
**move** | [**Move**](Move.md) |  | [optional] 
**permissionChanges** | [**[PermissionChange]**](PermissionChange.md) | Extra information for permissionChange type events, such as the user or group the new permission applies to. | [optional] 
**primaryEventType** | **String** | The main type of event that occurred. | [optional] 
**rename** | [**Rename**](Rename.md) |  | [optional] 
**target** | [**Target**](Target.md) |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 



## Enum: [AdditionalEventTypesEnum]


* `comment` (value: `"comment"`)

* `create` (value: `"create"`)

* `edit` (value: `"edit"`)

* `emptyTrash` (value: `"emptyTrash"`)

* `move` (value: `"move"`)

* `permissionChange` (value: `"permissionChange"`)

* `rename` (value: `"rename"`)

* `trash` (value: `"trash"`)

* `unknown` (value: `"unknown"`)

* `untrash` (value: `"untrash"`)

* `upload` (value: `"upload"`)





## Enum: PrimaryEventTypeEnum


* `comment` (value: `"comment"`)

* `create` (value: `"create"`)

* `edit` (value: `"edit"`)

* `emptyTrash` (value: `"emptyTrash"`)

* `move` (value: `"move"`)

* `permissionChange` (value: `"permissionChange"`)

* `rename` (value: `"rename"`)

* `trash` (value: `"trash"`)

* `unknown` (value: `"unknown"`)

* `untrash` (value: `"untrash"`)

* `upload` (value: `"upload"`)




