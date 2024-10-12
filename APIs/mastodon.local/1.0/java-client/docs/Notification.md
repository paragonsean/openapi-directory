

# Notification

Represents a notification of an event relevant to the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  |
|**createdAt** | **OffsetDateTime** | The timestamp of the notification. ISO 8601 Datetime. |  |
|**id** | **String** | The id of the notification in the database. Cast from an integer, but not guaranteed to be a number. |  |
|**status** | [**Status**](Status.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of event that resulted in the notification. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FOLLOW | &quot;follow&quot; |
| FOLLOW_REQUEST | &quot;follow_request&quot; |
| MENTION | &quot;mention&quot; |
| REBLOG | &quot;reblog&quot; |
| FAVOURITE | &quot;favourite&quot; |
| POLL | &quot;poll&quot; |
| STATUS | &quot;status&quot; |



