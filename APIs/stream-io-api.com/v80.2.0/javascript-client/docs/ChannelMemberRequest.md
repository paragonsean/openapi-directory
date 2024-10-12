# StreamChatApi.ChannelMemberRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banExpires** | **Date** | Expiration date of the ban | [optional] 
**banned** | **Boolean** | Whether member is banned this channel or not | [optional] 
**channelRole** | **String** | Role of the member in the channel | [optional] 
**createdAt** | **Date** | Date/time of creation | [optional] 
**deletedAt** | **Date** |  | [optional] 
**inviteAcceptedAt** | **Date** | Date when invite was accepted | [optional] 
**inviteRejectedAt** | **Date** | Date when invite was rejected | [optional] 
**invited** | **Boolean** | Whether member was invited or not | [optional] 
**isModerator** | **Boolean** | Whether member is channel moderator or not | [optional] 
**role** | **String** | Permission level of the member in the channel (DEPRECATED: use channel_role instead) | [optional] 
**shadowBanned** | **Boolean** | Whether member is shadow banned in this channel or not | [optional] 
**updatedAt** | **Date** | Date/time of the last update | [optional] 
**user** | [**UserObjectRequest**](UserObjectRequest.md) |  | [optional] 
**userId** | **String** |  | [optional] 



## Enum: RoleEnum


* `member` (value: `"member"`)

* `moderator` (value: `"moderator"`)

* `admin` (value: `"admin"`)

* `owner` (value: `"owner"`)




