# StreamChatApi.SendMessageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forceModeration** | **Boolean** | Enable moderation on server-side requests | [optional] 
**isPendingMessage** | **Boolean** | Make the message a pending message. This message will not be viewable to others until it is committed. | [optional] 
**keepChannelHidden** | **Boolean** | Keeps the channel hidden for the sender | [optional] 
**message** | [**MessageRequest**](MessageRequest.md) |  | 
**pendingMessageMetadata** | **{String: String}** |  | [optional] 
**skipEnrichUrl** | **Boolean** | Do not try to enrich the links within message | [optional] 
**skipPush** | **Boolean** | Disables all push notifications for this message | [optional] 


