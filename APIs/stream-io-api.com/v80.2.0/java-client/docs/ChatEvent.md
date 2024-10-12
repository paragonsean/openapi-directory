

# ChatEvent

The discriminator object for all websocket events, you should use this to map event payloads to their own type

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  |
|**type** | **String** |  |  |
|**channel** | **ChannelResponse** |  |  [optional] |
|**channelId** | **String** |  |  |
|**channelType** | **String** |  |  |
|**cid** | **String** |  |  |
|**team** | **String** |  |  [optional] |
|**clearHistory** | **Boolean** |  |  |
|**user** | **UserObject** |  |  [optional] |
|**message** | **Message** |  |  |
|**me** | **OwnUser** |  |  |
|**member** | [**ChannelMember**](ChannelMember.md) |  |  [optional] |
|**hardDelete** | **Boolean** |  |  |
|**threadParticipants** | **List&lt;UserObject&gt;** |  |  [optional] |
|**flag** | [**Flag**](Flag.md) |  |  [optional] |
|**watcherCount** | **Integer** |  |  |
|**lastReadMessageId** | **String** |  |  [optional] |
|**totalUnreadCount** | **Integer** |  |  |
|**unreadChannels** | **Integer** |  |  |
|**unreadCount** | **Integer** |  |  |
|**firstUnreadMessageId** | **String** |  |  |
|**lastReadAt** | **OffsetDateTime** |  |  |
|**unreadMessages** | **Integer** |  |  |
|**reaction** | **Reaction** |  |  |
|**parentId** | **String** |  |  [optional] |
|**createdBy** | **UserObject** |  |  |
|**expiration** | **OffsetDateTime** |  |  [optional] |
|**reason** | **String** |  |  [optional] |
|**shadow** | **Boolean** |  |  |
|**deleteConversationChannels** | **Boolean** |  |  |
|**markMessagesDeleted** | **Boolean** |  |  |
|**targetUser** | **String** |  |  [optional] |
|**targetUsers** | **List&lt;String&gt;** |  |  [optional] |
|**channels** | [**Map&lt;String, ChannelMessages&gt;**](ChannelMessages.md) |  |  |



