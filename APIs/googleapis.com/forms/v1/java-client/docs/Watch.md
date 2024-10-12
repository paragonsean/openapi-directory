

# Watch

A watch for events for a form. When the designated event happens, a notification will be published to the specified target. The notification's attributes will include a `formId` key that has the ID of the watched form and an `eventType` key that has the string of the type. Messages are sent with at-least-once delivery and are only dropped in extraordinary circumstances. Typically all notifications should be reliably delivered within a few seconds; however, in some situations notifications may be delayed. A watch expires seven days after it is created unless it is renewed with watches.renew

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp of when this was created. |  [optional] [readonly] |
|**errorType** | [**ErrorTypeEnum**](#ErrorTypeEnum) | Output only. The most recent error type for an attempted delivery. To begin watching the form again a call can be made to watches.renew which also clears this error information. |  [optional] [readonly] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Required. Which event type to watch for. |  [optional] |
|**expireTime** | **String** | Output only. Timestamp for when this will expire. Each watches.renew call resets this to seven days in the future. |  [optional] [readonly] |
|**id** | **String** | Output only. The ID of this watch. See notes on CreateWatchRequest.watch_id. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the watch. Additional details about suspended watches can be found by checking the &#x60;error_type&#x60;. |  [optional] [readonly] |
|**target** | [**WatchTarget**](WatchTarget.md) |  |  [optional] |



## Enum: ErrorTypeEnum

| Name | Value |
|---- | -----|
| ERROR_TYPE_UNSPECIFIED | &quot;ERROR_TYPE_UNSPECIFIED&quot; |
| PROJECT_NOT_AUTHORIZED | &quot;PROJECT_NOT_AUTHORIZED&quot; |
| NO_USER_ACCESS | &quot;NO_USER_ACCESS&quot; |
| OTHER_ERRORS | &quot;OTHER_ERRORS&quot; |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| SCHEMA | &quot;SCHEMA&quot; |
| RESPONSES | &quot;RESPONSES&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |



