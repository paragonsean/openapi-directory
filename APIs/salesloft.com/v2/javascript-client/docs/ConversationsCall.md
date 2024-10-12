# SalesLoftPlatform.ConversationsCall

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callCreatedAt** | **String** | Timestamp for when the call started. If not provided, will default to the time the request was received | [optional] 
**direction** | **String** | Call direction | [optional] 
**duration** | **Number** | Duration of call in seconds | [optional] 
**from** | **String** | Phone number that call was made from | [optional] 
**recording** | **Object** | Object containing recording info including the audio file (.mp3, .wav, .ogg, .m4a) | [optional] 
**to** | **String** | Phone number that was called | [optional] 
**userGuid** | **String** | Guid of the Salesloft User to assign the call to. If not provided, will default to the user within the authentication token | [optional] 


