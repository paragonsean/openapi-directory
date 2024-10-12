# DispatchApi.MessageStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**MessageStatusLinks**](MessageStatusLinks.md) |  | [optional] 
**error** | [**MessageStatusError**](MessageStatusError.md) |  | [optional] 
**from** | [**FromProperty**](FromProperty.md) |  | [optional] 
**messageUuid** | **String** |  | [optional] 
**status** | **String** | The status of the message. | [optional] 
**timestamp** | **String** | The datetime of when the event occurred. | [optional] 
**to** | [**ToProperty**](ToProperty.md) |  | [optional] 
**usage** | [**MessageStatusUsage**](MessageStatusUsage.md) |  | [optional] 



## Enum: StatusEnum


* `submitted` (value: `"submitted"`)

* `delivered` (value: `"delivered"`)

* `read` (value: `"read"`)

* `rejected` (value: `"rejected"`)

* `undeliverable` (value: `"undeliverable"`)




