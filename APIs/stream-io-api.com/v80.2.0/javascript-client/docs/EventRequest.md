# StreamChatApi.EventRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automoderation** | **Boolean** | Only applicable to &#x60;message.flagged&#x60; BaseEvent. | [optional] 
**automoderationScores** | [**ModerationResponseRequest**](ModerationResponseRequest.md) |  | [optional] 
**channel** | [**ChannelResponseRequest**](ChannelResponseRequest.md) |  | [optional] 
**channelId** | **String** |  | [optional] 
**channelType** | **String** |  | [optional] 
**cid** | **String** | Channel CID (&lt;type&gt;:&lt;id&gt;) | [optional] 
**connectionId** | **String** | Only applicable to &#x60;health.check&#x60; BaseEvent | [optional] 
**createdAt** | **Date** | Date/time of creation | [optional] 
**createdBy** | [**UserObjectRequest**](UserObjectRequest.md) |  | [optional] 
**me** | [**OwnUserRequest**](OwnUserRequest.md) |  | [optional] 
**member** | [**ChannelMemberRequest**](ChannelMemberRequest.md) |  | [optional] 
**message** | [**MessageRequest1**](MessageRequest1.md) |  | [optional] 
**parentId** | **String** | ID of thread. Used in typing events | [optional] 
**reaction** | [**ReactionRequest**](ReactionRequest.md) |  | [optional] 
**reason** | **String** | Ban reason. Only applicable to &#x60;user.banned&#x60; BaseEvent | [optional] 
**team** | **String** |  | [optional] 
**type** | **String** | Event type. To use custom BaseEvent types see Custom Events documentation | 
**user** | [**UserObjectRequest**](UserObjectRequest.md) |  | [optional] 
**userId** | **String** |  | [optional] 
**watcherCount** | **Number** | Number of watchers who received this BaseEvent | [optional] 


