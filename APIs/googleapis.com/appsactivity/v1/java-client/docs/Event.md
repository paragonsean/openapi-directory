

# Event

Represents the changes associated with an action taken by a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalEventTypes** | [**List&lt;AdditionalEventTypesEnum&gt;**](#List&lt;AdditionalEventTypesEnum&gt;) | Additional event types. Some events may have multiple types when multiple actions are part of a single event. For example, creating a document, renaming it, and sharing it may be part of a single file-creation event. |  [optional] |
|**eventTimeMillis** | **String** | The time at which the event occurred formatted as Unix time in milliseconds. |  [optional] |
|**fromUserDeletion** | **Boolean** | Whether this event is caused by a user being deleted. |  [optional] |
|**move** | [**Move**](Move.md) |  |  [optional] |
|**permissionChanges** | [**List&lt;PermissionChange&gt;**](PermissionChange.md) | Extra information for permissionChange type events, such as the user or group the new permission applies to. |  [optional] |
|**primaryEventType** | [**PrimaryEventTypeEnum**](#PrimaryEventTypeEnum) | The main type of event that occurred. |  [optional] |
|**rename** | [**Rename**](Rename.md) |  |  [optional] |
|**target** | [**Target**](Target.md) |  |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |



## Enum: List&lt;AdditionalEventTypesEnum&gt;

| Name | Value |
|---- | -----|
| COMMENT | &quot;comment&quot; |
| CREATE | &quot;create&quot; |
| EDIT | &quot;edit&quot; |
| EMPTY_TRASH | &quot;emptyTrash&quot; |
| MOVE | &quot;move&quot; |
| PERMISSION_CHANGE | &quot;permissionChange&quot; |
| RENAME | &quot;rename&quot; |
| TRASH | &quot;trash&quot; |
| UNKNOWN | &quot;unknown&quot; |
| UNTRASH | &quot;untrash&quot; |
| UPLOAD | &quot;upload&quot; |



## Enum: PrimaryEventTypeEnum

| Name | Value |
|---- | -----|
| COMMENT | &quot;comment&quot; |
| CREATE | &quot;create&quot; |
| EDIT | &quot;edit&quot; |
| EMPTY_TRASH | &quot;emptyTrash&quot; |
| MOVE | &quot;move&quot; |
| PERMISSION_CHANGE | &quot;permissionChange&quot; |
| RENAME | &quot;rename&quot; |
| TRASH | &quot;trash&quot; |
| UNKNOWN | &quot;unknown&quot; |
| UNTRASH | &quot;untrash&quot; |
| UPLOAD | &quot;upload&quot; |



