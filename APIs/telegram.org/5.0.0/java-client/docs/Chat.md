

# Chat

This object represents a chat.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bio** | **String** | *Optional*. Bio of the other party in a private chat. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat). |  [optional] |
|**canSetStickerSet** | **Boolean** | *Optional*. True, if the bot can change the group sticker set. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat). |  [optional] |
|**description** | **String** | *Optional*. Description, for groups, supergroups and channel chats. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat). |  [optional] |
|**firstName** | **String** | *Optional*. First name of the other party in a private chat |  [optional] |
|**id** | **Integer** | Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. |  |
|**inviteLink** | **String** | *Optional*. Chat invite link, for groups, supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using [exportChatInviteLink](https://core.telegram.org/bots/api/#exportchatinvitelink). Returned only in [getChat](https://core.telegram.org/bots/api/#getchat). |  [optional] |
|**lastName** | **String** | *Optional*. Last name of the other party in a private chat |  [optional] |
|**linkedChatId** | **Integer** | *Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat). |  [optional] |
|**location** | [**ChatLocation**](ChatLocation.md) |  |  [optional] |
|**permissions** | [**ChatPermissions**](ChatPermissions.md) |  |  [optional] |
|**photo** | [**ChatPhoto**](ChatPhoto.md) |  |  [optional] |
|**pinnedMessage** | [**Message**](Message.md) |  |  [optional] |
|**slowModeDelay** | **Integer** | *Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat). |  [optional] |
|**stickerSetName** | **String** | *Optional*. For supergroups, name of group sticker set. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat). |  [optional] |
|**title** | **String** | *Optional*. Title, for supergroups, channels and group chats |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of chat, can be either “private”, “group”, “supergroup” or “channel” |  |
|**username** | **String** | *Optional*. Username, for private chats, supergroups and channels if available |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PRIVATE | &quot;private&quot; |
| GROUP | &quot;group&quot; |
| SUPERGROUP | &quot;supergroup&quot; |
| CHANNEL | &quot;channel&quot; |



