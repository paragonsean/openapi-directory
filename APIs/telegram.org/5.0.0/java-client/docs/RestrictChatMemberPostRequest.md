

# RestrictChatMemberPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chatId** | [**DeleteChatStickerSetPostRequestChatId**](DeleteChatStickerSetPostRequestChatId.md) |  |  |
|**permissions** | [**ChatPermissions**](ChatPermissions.md) |  |  |
|**untilDate** | **Integer** | Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever |  [optional] |
|**userId** | **Integer** | Unique identifier of the target user |  |



