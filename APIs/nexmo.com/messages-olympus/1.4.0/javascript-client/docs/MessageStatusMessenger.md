# MessagesApi.MessageStatusMessenger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. | [optional] 
**error** | [**MessageStatusBaseError**](MessageStatusBaseError.md) |  | [optional] 
**from** | **String** | The ID of the message sender  | 
**messageUuid** | **String** | The UUID of the message | 
**status** | **String** |  | 
**timestamp** | **String** | The datetime of when the event occurred, in &#x60;ISO 8601&#x60; format. | 
**to** | **String** | The ID of the message recipient  | 
**usage** | [**MessageStatusBaseUsage**](MessageStatusBaseUsage.md) |  | [optional] 
**channel** | **String** | The channel sending to. | 



## Enum: StatusEnum


* `submitted` (value: `"submitted"`)

* `delivered` (value: `"delivered"`)

* `rejected` (value: `"rejected"`)

* `undeliverable` (value: `"undeliverable"`)

* `read` (value: `"read"`)





## Enum: ChannelEnum


* `messenger` (value: `"messenger"`)




