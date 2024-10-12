

# ChannelStateResponseFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | **ChannelResponse** |  |  [optional] |
|**hidden** | **Boolean** | Whether this channel is hidden or not |  [optional] |
|**hideMessagesBefore** | **OffsetDateTime** | Messages before this date are hidden from the user |  [optional] |
|**members** | [**List&lt;ChannelMember&gt;**](ChannelMember.md) | List of channel members |  |
|**membership** | [**ChannelMember**](ChannelMember.md) |  |  [optional] |
|**messages** | **List&lt;Message&gt;** | List of channel messages |  |
|**pendingMessages** | [**List&lt;PendingMessage&gt;**](PendingMessage.md) | Pending messages that this user has sent |  [optional] |
|**pinnedMessages** | **List&lt;Message&gt;** | List of pinned messages in the channel |  |
|**read** | [**List&lt;Read&gt;**](Read.md) | List of read states |  [optional] |
|**watcherCount** | **Integer** | Number of channel watchers |  [optional] |
|**watchers** | **List&lt;UserObject&gt;** | List of user who is watching the channel |  [optional] |



