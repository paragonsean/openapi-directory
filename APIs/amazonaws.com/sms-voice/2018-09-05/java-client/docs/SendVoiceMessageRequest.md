

# SendVoiceMessageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callerId** | **String** | The phone number that appears on recipients&#39; devices when they receive the message. |  [optional] |
|**configurationSetName** | **String** | The name of the configuration set that you want to use to send the message. |  [optional] |
|**content** | [**SendVoiceMessageRequestContent**](SendVoiceMessageRequestContent.md) |  |  [optional] |
|**destinationPhoneNumber** | **String** | The phone number that you want to send the voice message to. |  [optional] |
|**originationPhoneNumber** | **String** | The phone number that Amazon Pinpoint should use to send the voice message. This isn&#39;t necessarily the phone number that appears on recipients&#39; devices when they receive the message, because you can specify a CallerId parameter in the request. |  [optional] |



