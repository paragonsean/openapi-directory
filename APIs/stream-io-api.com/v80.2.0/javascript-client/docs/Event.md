# StreamChatApi.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automoderation** | **Boolean** | Only applicable to &#x60;message.flagged&#x60; BaseEvent. | [optional] 
**automoderationScores** | [**ModerationResponse**](ModerationResponse.md) |  | [optional] 
**channel** | [**ChannelResponse**](ChannelResponse.md) |  | [optional] 
**channelId** | **String** |  | [optional] 
**channelType** | **String** |  | [optional] 
**cid** | **String** | Channel CID (&lt;type&gt;:&lt;id&gt;) | [optional] 
**connectionId** | **String** | Only applicable to &#x60;health.check&#x60; BaseEvent | [optional] 
**createdAt** | **Date** | Date/time of creation | 
**createdBy** | [**UserObject**](UserObject.md) |  | [optional] 
**me** | [**OwnUser**](OwnUser.md) |  | [optional] 
**member** | [**ChannelMember**](ChannelMember.md) |  | [optional] 
**message** | [**Message**](Message.md) |  | [optional] 
**parentId** | **String** | ID of thread. Used in typing events | [optional] 
**reaction** | [**Reaction**](Reaction.md) |  | [optional] 
**reason** | **String** | Ban reason. Only applicable to &#x60;user.banned&#x60; BaseEvent | [optional] 
**team** | **String** |  | [optional] 
**type** | **String** | Event type. To use custom BaseEvent types see Custom Events documentation | 
**user** | [**UserObject**](UserObject.md) |  | [optional] 
**userId** | **String** |  | [optional] 
**watcherCount** | **Number** | Number of watchers who received this BaseEvent | [optional] 


