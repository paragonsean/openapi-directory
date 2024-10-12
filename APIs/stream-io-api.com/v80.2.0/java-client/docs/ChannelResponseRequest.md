

# ChannelResponseRequest

Represents channel in chat

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoTranslationEnabled** | **Boolean** | Whether auto translation is enabled or not |  [optional] |
|**autoTranslationLanguage** | **String** | Language to translate to when auto translation is active |  [optional] |
|**cid** | **String** | Channel CID (&lt;type&gt;:&lt;id&gt;) |  [optional] |
|**config** | [**ChannelConfigWithInfoRequest**](ChannelConfigWithInfoRequest.md) |  |  [optional] |
|**cooldown** | **Integer** | Cooldown period after sending each message |  [optional] |
|**createdAt** | **OffsetDateTime** | Date/time of creation |  [optional] |
|**createdBy** | **UserObjectRequest** |  |  [optional] |
|**deletedAt** | **OffsetDateTime** | Date/time of deletion |  [optional] |
|**disabled** | **Boolean** |  |  [optional] |
|**frozen** | **Boolean** | Whether channel is frozen or not |  [optional] |
|**hidden** | **Boolean** | Whether this channel is hidden by current user or not |  [optional] |
|**hideMessagesBefore** | **OffsetDateTime** | Date since when the message history is accessible |  [optional] |
|**id** | **String** | Channel unique ID |  [optional] |
|**lastMessageAt** | **OffsetDateTime** | Date of the last message sent |  [optional] |
|**memberCount** | **Integer** | Number of members in the channel |  [optional] |
|**members** | [**List&lt;ChannelMemberRequest&gt;**](ChannelMemberRequest.md) | List of channel members (max 100) |  [optional] |
|**muteExpiresAt** | **OffsetDateTime** | Date of mute expiration |  [optional] |
|**muted** | **Boolean** | Whether this channel is muted or not |  [optional] |
|**ownCapabilities** | **List&lt;String&gt;** | List of channel capabilities of authenticated user |  [optional] |
|**team** | **String** | Team the channel belongs to (multi-tenant only) |  [optional] |
|**truncatedAt** | **OffsetDateTime** | Date of the latest truncation of the channel |  [optional] |
|**truncatedBy** | **UserObjectRequest** |  |  [optional] |
|**type** | **String** | Type of the channel |  [optional] |
|**updatedAt** | **OffsetDateTime** | Date/time of the last update |  [optional] |



