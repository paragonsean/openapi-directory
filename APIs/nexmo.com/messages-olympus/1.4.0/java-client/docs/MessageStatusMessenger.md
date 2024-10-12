

# MessageStatusMessenger


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRef** | **String** | Client reference of up to 100 characters. The reference will be present in every message status. |  [optional] |
|**error** | [**MessageStatusBaseError**](MessageStatusBaseError.md) |  |  [optional] |
|**from** | **String** | The ID of the message sender  |  |
|**messageUuid** | **String** | The UUID of the message |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**timestamp** | **String** | The datetime of when the event occurred, in &#x60;ISO 8601&#x60; format. |  |
|**to** | **String** | The ID of the message recipient  |  |
|**usage** | [**MessageStatusBaseUsage**](MessageStatusBaseUsage.md) |  |  [optional] |
|**channel** | [**ChannelEnum**](#ChannelEnum) | The channel sending to. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;submitted&quot; |
| DELIVERED | &quot;delivered&quot; |
| REJECTED | &quot;rejected&quot; |
| UNDELIVERABLE | &quot;undeliverable&quot; |
| READ | &quot;read&quot; |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| MESSENGER | &quot;messenger&quot; |



