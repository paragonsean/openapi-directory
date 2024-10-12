

# ActivityMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTimestamp** | **Long** | Epoch time in milliseconds when the message was created |  [optional] |
|**message** | **String** | The details of the message when type is &#39;log&#39; |  [optional] |
|**messageObject** | [**RuntimeTransaction**](RuntimeTransaction.md) |  |  [optional] |
|**messageType** | [**MessageTypeEnum**](#MessageTypeEnum) |  |  [optional] |
|**sandboxId** | **String** | The ID of the sandbox that generated this message |  [optional] |



## Enum: MessageTypeEnum

| Name | Value |
|---- | -----|
| REQUEST | &quot;request&quot; |
| LOG | &quot;log&quot; |



