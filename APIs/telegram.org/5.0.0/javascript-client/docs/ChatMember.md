# TelegramBotApi.ChatMember

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canAddWebPagePreviews** | **Boolean** | *Optional*. Restricted only. True, if the user is allowed to add web page previews to their messages | [optional] 
**canBeEdited** | **Boolean** | *Optional*. Administrators only. True, if the bot is allowed to edit administrator privileges of that user | [optional] 
**canChangeInfo** | **Boolean** | *Optional*. Administrators and restricted only. True, if the user is allowed to change the chat title, photo and other settings | [optional] 
**canDeleteMessages** | **Boolean** | *Optional*. Administrators only. True, if the administrator can delete messages of other users | [optional] 
**canEditMessages** | **Boolean** | *Optional*. Administrators only. True, if the administrator can edit messages of other users and can pin messages; channels only | [optional] 
**canInviteUsers** | **Boolean** | *Optional*. Administrators and restricted only. True, if the user is allowed to invite new users to the chat | [optional] 
**canPinMessages** | **Boolean** | *Optional*. Administrators and restricted only. True, if the user is allowed to pin messages; groups and supergroups only | [optional] 
**canPostMessages** | **Boolean** | *Optional*. Administrators only. True, if the administrator can post in the channel; channels only | [optional] 
**canPromoteMembers** | **Boolean** | *Optional*. Administrators only. True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user) | [optional] 
**canRestrictMembers** | **Boolean** | *Optional*. Administrators only. True, if the administrator can restrict, ban or unban chat members | [optional] 
**canSendMediaMessages** | **Boolean** | *Optional*. Restricted only. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes | [optional] 
**canSendMessages** | **Boolean** | *Optional*. Restricted only. True, if the user is allowed to send text messages, contacts, locations and venues | [optional] 
**canSendOtherMessages** | **Boolean** | *Optional*. Restricted only. True, if the user is allowed to send animations, games, stickers and use inline bots | [optional] 
**canSendPolls** | **Boolean** | *Optional*. Restricted only. True, if the user is allowed to send polls | [optional] 
**customTitle** | **String** | *Optional*. Owner and administrators only. Custom title for this user | [optional] 
**isAnonymous** | **Boolean** | *Optional*. Owner and administrators only. True, if the user&#39;s presence in the chat is hidden | [optional] 
**isMember** | **Boolean** | *Optional*. Restricted only. True, if the user is a member of the chat at the moment of the request | [optional] 
**status** | **String** | The member&#39;s status in the chat. Can be “creator”, “administrator”, “member”, “restricted”, “left” or “kicked” | 
**untilDate** | **Number** | *Optional*. Restricted and kicked only. Date when restrictions will be lifted for this user; unix time | [optional] 
**user** | [**User**](User.md) |  | 



## Enum: StatusEnum


* `creator` (value: `"creator"`)

* `administrator` (value: `"administrator"`)

* `member` (value: `"member"`)

* `restricted` (value: `"restricted"`)

* `left` (value: `"left"`)

* `kicked` (value: `"kicked"`)




