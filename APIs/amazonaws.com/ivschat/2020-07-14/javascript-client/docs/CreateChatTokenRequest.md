# AmazonInteractiveVideoServiceChat.CreateChatTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: String}** | Application-provided attributes to encode into the token and attach to a chat session. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. | [optional] 
**capabilities** | [**[ChatTokenCapability]**](ChatTokenCapability.md) | Set of capabilities that the user is allowed to perform in the room. Default: None (the capability to view messages is implicitly included in all requests). | [optional] 
**roomIdentifier** | **String** | Identifier of the room that the client is trying to access. Currently this must be an ARN.  | 
**sessionDurationInMinutes** | **Number** | Session duration (in minutes), after which the session expires. Default: 60 (1 hour). | [optional] 
**userId** | **String** | Application-provided ID that uniquely identifies the user associated with this token. This can be any UTF-8 encoded text. | 


