

# ChannelMember


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**banExpires** | **OffsetDateTime** | Expiration date of the ban |  [optional] |
|**banned** | **Boolean** | Whether member is banned this channel or not |  |
|**channelRole** | **String** | Role of the member in the channel |  |
|**createdAt** | **OffsetDateTime** | Date/time of creation |  |
|**deletedAt** | **OffsetDateTime** |  |  [optional] |
|**inviteAcceptedAt** | **OffsetDateTime** | Date when invite was accepted |  [optional] |
|**inviteRejectedAt** | **OffsetDateTime** | Date when invite was rejected |  [optional] |
|**invited** | **Boolean** | Whether member was invited or not |  [optional] |
|**isModerator** | **Boolean** | Whether member is channel moderator or not |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Permission level of the member in the channel (DEPRECATED: use channel_role instead) |  [optional] |
|**shadowBanned** | **Boolean** | Whether member is shadow banned in this channel or not |  |
|**updatedAt** | **OffsetDateTime** | Date/time of the last update |  |
|**user** | **UserObject** |  |  [optional] |
|**userId** | **String** |  |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| MEMBER | &quot;member&quot; |
| MODERATOR | &quot;moderator&quot; |
| ADMIN | &quot;admin&quot; |
| OWNER | &quot;owner&quot; |



