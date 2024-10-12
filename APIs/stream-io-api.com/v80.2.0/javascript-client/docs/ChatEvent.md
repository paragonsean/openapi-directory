# StreamChatApi.ChatEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | 
**type** | **String** |  | [default to &#39;user.watching.stop&#39;]
**channel** | [**ChannelResponse**](ChannelResponse.md) |  | [optional] 
**channelId** | **String** |  | 
**channelType** | **String** |  | 
**cid** | **String** |  | 
**team** | **String** |  | [optional] 
**clearHistory** | **Boolean** |  | 
**user** | [**UserObject**](UserObject.md) |  | [optional] 
**message** | [**Message**](Message.md) |  | 
**me** | [**OwnUser**](OwnUser.md) |  | 
**member** | [**ChannelMember**](ChannelMember.md) |  | [optional] 
**hardDelete** | **Boolean** |  | 
**threadParticipants** | [**[UserObject]**](UserObject.md) |  | [optional] 
**flag** | [**Flag**](Flag.md) |  | [optional] 
**watcherCount** | **Number** |  | 
**lastReadMessageId** | **String** |  | [optional] 
**totalUnreadCount** | **Number** |  | 
**unreadChannels** | **Number** |  | 
**unreadCount** | **Number** |  | 
**firstUnreadMessageId** | **String** |  | 
**lastReadAt** | **Date** |  | 
**unreadMessages** | **Number** |  | 
**reaction** | [**Reaction**](Reaction.md) |  | 
**parentId** | **String** |  | [optional] 
**createdBy** | [**UserObject**](UserObject.md) |  | 
**expiration** | **Date** |  | [optional] 
**reason** | **String** |  | [optional] 
**shadow** | **Boolean** |  | 
**deleteConversationChannels** | **Boolean** |  | 
**markMessagesDeleted** | **Boolean** |  | 
**targetUser** | **String** |  | [optional] 
**targetUsers** | **[String]** |  | [optional] 
**channels** | [**{String: ChannelMessages}**](ChannelMessages.md) |  | 


