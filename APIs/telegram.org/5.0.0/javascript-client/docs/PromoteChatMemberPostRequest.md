# TelegramBotApi.PromoteChatMemberPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canChangeInfo** | **Boolean** | Pass True, if the administrator can change chat title, photo and other settings | [optional] 
**canDeleteMessages** | **Boolean** | Pass True, if the administrator can delete messages of other users | [optional] 
**canEditMessages** | **Boolean** | Pass True, if the administrator can edit messages of other users and can pin messages, channels only | [optional] 
**canInviteUsers** | **Boolean** | Pass True, if the administrator can invite new users to the chat | [optional] 
**canPinMessages** | **Boolean** | Pass True, if the administrator can pin messages, supergroups only | [optional] 
**canPostMessages** | **Boolean** | Pass True, if the administrator can create channel posts, channels only | [optional] 
**canPromoteMembers** | **Boolean** | Pass True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him) | [optional] 
**canRestrictMembers** | **Boolean** | Pass True, if the administrator can restrict, ban or unban chat members | [optional] 
**chatId** | [**CopyMessagePostRequestChatId**](CopyMessagePostRequestChatId.md) |  | 
**isAnonymous** | **Boolean** | Pass *True*, if the administrator&#39;s presence in the chat is hidden | [optional] 
**userId** | **Number** | Unique identifier of the target user | 


