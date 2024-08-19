# GoogleFormsApi.Watch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp of when this was created. | [optional] [readonly] 
**errorType** | **String** | Output only. The most recent error type for an attempted delivery. To begin watching the form again a call can be made to watches.renew which also clears this error information. | [optional] [readonly] 
**eventType** | **String** | Required. Which event type to watch for. | [optional] 
**expireTime** | **String** | Output only. Timestamp for when this will expire. Each watches.renew call resets this to seven days in the future. | [optional] [readonly] 
**id** | **String** | Output only. The ID of this watch. See notes on CreateWatchRequest.watch_id. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the watch. Additional details about suspended watches can be found by checking the &#x60;error_type&#x60;. | [optional] [readonly] 
**target** | [**WatchTarget**](WatchTarget.md) |  | [optional] 



## Enum: ErrorTypeEnum


* `ERROR_TYPE_UNSPECIFIED` (value: `"ERROR_TYPE_UNSPECIFIED"`)

* `PROJECT_NOT_AUTHORIZED` (value: `"PROJECT_NOT_AUTHORIZED"`)

* `NO_USER_ACCESS` (value: `"NO_USER_ACCESS"`)

* `OTHER_ERRORS` (value: `"OTHER_ERRORS"`)





## Enum: EventTypeEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `SCHEMA` (value: `"SCHEMA"`)

* `RESPONSES` (value: `"RESPONSES"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUSPENDED` (value: `"SUSPENDED"`)




