# VoiceApi.CreateCallResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversationUuid** | **String** | The unique identifier for the conversation this call leg is part of. | [optional] 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**status** | **String** | The status of the call. [See possible values](https://developer.nexmo.com/voice/voice-api/guides/call-flow#event-objects) | [optional] 
**uuid** | **String** | The unique identifier for this call leg. The UUID is created when your call request is accepted by Vonage. You use the UUID in all requests for individual live calls | [optional] 


