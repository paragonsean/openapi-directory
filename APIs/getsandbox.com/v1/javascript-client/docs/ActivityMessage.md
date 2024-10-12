# SandboxApi.ActivityMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTimestamp** | **Number** | Epoch time in milliseconds when the message was created | [optional] 
**message** | **String** | The details of the message when type is &#39;log&#39; | [optional] 
**messageObject** | [**RuntimeTransaction**](RuntimeTransaction.md) |  | [optional] 
**messageType** | **String** |  | [optional] 
**sandboxId** | **String** | The ID of the sandbox that generated this message | [optional] 



## Enum: MessageTypeEnum


* `request` (value: `"request"`)

* `log` (value: `"log"`)




