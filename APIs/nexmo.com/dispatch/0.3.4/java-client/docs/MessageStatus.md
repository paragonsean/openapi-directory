

# MessageStatus

The callbacks for the message status are the same as defined in the Messaging API. The only difference will be that dispatch_uuid and link will be appended.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**MessageStatusLinks**](MessageStatusLinks.md) |  |  [optional] |
|**error** | [**MessageStatusError**](MessageStatusError.md) |  |  [optional] |
|**from** | [**FromProperty**](FromProperty.md) |  |  [optional] |
|**messageUuid** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the message. |  [optional] |
|**timestamp** | **String** | The datetime of when the event occurred. |  [optional] |
|**to** | [**ToProperty**](ToProperty.md) |  |  [optional] |
|**usage** | [**MessageStatusUsage**](MessageStatusUsage.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;submitted&quot; |
| DELIVERED | &quot;delivered&quot; |
| READ | &quot;read&quot; |
| REJECTED | &quot;rejected&quot; |
| UNDELIVERABLE | &quot;undeliverable&quot; |



