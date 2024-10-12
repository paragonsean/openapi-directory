

# Event

Represents an BaseEvent that happened in Stream Chat

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automoderation** | **Boolean** | Only applicable to &#x60;message.flagged&#x60; BaseEvent. |  [optional] |
|**automoderationScores** | [**ModerationResponse**](ModerationResponse.md) |  |  [optional] |
|**channel** | **ChannelResponse** |  |  [optional] |
|**channelId** | **String** |  |  [optional] |
|**channelType** | **String** |  |  [optional] |
|**cid** | **String** | Channel CID (&lt;type&gt;:&lt;id&gt;) |  [optional] |
|**connectionId** | **String** | Only applicable to &#x60;health.check&#x60; BaseEvent |  [optional] |
|**createdAt** | **OffsetDateTime** | Date/time of creation |  |
|**createdBy** | **UserObject** |  |  [optional] |
|**me** | **OwnUser** |  |  [optional] |
|**member** | [**ChannelMember**](ChannelMember.md) |  |  [optional] |
|**message** | **Message** |  |  [optional] |
|**parentId** | **String** | ID of thread. Used in typing events |  [optional] |
|**reaction** | **Reaction** |  |  [optional] |
|**reason** | **String** | Ban reason. Only applicable to &#x60;user.banned&#x60; BaseEvent |  [optional] |
|**team** | **String** |  |  [optional] |
|**type** | **String** | Event type. To use custom BaseEvent types see Custom Events documentation |  |
|**user** | **UserObject** |  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**watcherCount** | **Integer** | Number of watchers who received this BaseEvent |  [optional] |



