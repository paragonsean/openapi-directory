# StreamChatApi.ChannelStateResponseFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | [**ChannelResponse**](ChannelResponse.md) |  | [optional] 
**hidden** | **Boolean** | Whether this channel is hidden or not | [optional] 
**hideMessagesBefore** | **Date** | Messages before this date are hidden from the user | [optional] 
**members** | [**[ChannelMember]**](ChannelMember.md) | List of channel members | 
**membership** | [**ChannelMember**](ChannelMember.md) |  | [optional] 
**messages** | [**[Message]**](Message.md) | List of channel messages | 
**pendingMessages** | [**[PendingMessage]**](PendingMessage.md) | Pending messages that this user has sent | [optional] 
**pinnedMessages** | [**[Message]**](Message.md) | List of pinned messages in the channel | 
**read** | [**[Read]**](Read.md) | List of read states | [optional] 
**watcherCount** | **Number** | Number of channel watchers | [optional] 
**watchers** | [**[UserObject]**](UserObject.md) | List of user who is watching the channel | [optional] 


