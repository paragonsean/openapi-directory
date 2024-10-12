

# EditMessageCaptionPost200ResponseResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**animation** | [**Animation**](Animation.md) |  |  [optional] |
|**audio** | [**Audio**](Audio.md) |  |  [optional] |
|**authorSignature** | **String** | *Optional*. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator |  [optional] |
|**caption** | **String** | *Optional*. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters |  [optional] |
|**captionEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption |  [optional] |
|**channelChatCreated** | **Boolean** | *Optional*. Service message: the channel has been created. This field can&#39;t be received in a message coming through updates, because bot can&#39;t be a member of a channel when it is created. It can only be found in reply\\_to\\_message if someone replies to a very first message in a channel. |  [optional] |
|**chat** | [**Chat**](Chat.md) |  |  |
|**connectedWebsite** | **String** | *Optional*. The domain name of the website on which the user has logged in. [More about Telegram Login »](/widgets/login) |  [optional] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**date** | **Integer** | Date the message was sent in Unix time |  |
|**deleteChatPhoto** | **Boolean** | *Optional*. Service message: the chat photo was deleted |  [optional] |
|**dice** | [**Dice**](Dice.md) |  |  [optional] |
|**document** | [**Document**](Document.md) |  |  [optional] |
|**editDate** | **Integer** | *Optional*. Date the message was last edited in Unix time |  [optional] |
|**entities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text |  [optional] |
|**forwardDate** | **Integer** | *Optional*. For forwarded messages, date the original message was sent in Unix time |  [optional] |
|**forwardFrom** | [**User**](User.md) |  |  [optional] |
|**forwardFromChat** | [**Chat**](Chat.md) |  |  [optional] |
|**forwardFromMessageId** | **Integer** | *Optional*. For messages forwarded from channels, identifier of the original message in the channel |  [optional] |
|**forwardSenderName** | **String** | *Optional*. Sender&#39;s name for messages forwarded from users who disallow adding a link to their account in forwarded messages |  [optional] |
|**forwardSignature** | **String** | *Optional*. For messages forwarded from channels, signature of the post author if present |  [optional] |
|**from** | [**User**](User.md) |  |  [optional] |
|**game** | [**Game**](Game.md) |  |  [optional] |
|**groupChatCreated** | **Boolean** | *Optional*. Service message: the group has been created |  [optional] |
|**invoice** | [**Invoice**](Invoice.md) |  |  [optional] |
|**leftChatMember** | [**User**](User.md) |  |  [optional] |
|**location** | [**Location**](Location.md) |  |  [optional] |
|**mediaGroupId** | **String** | *Optional*. The unique identifier of a media message group this message belongs to |  [optional] |
|**messageId** | **Integer** | Unique message identifier inside this chat |  |
|**migrateFromChatId** | **Integer** | *Optional*. The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. |  [optional] |
|**migrateToChatId** | **Integer** | *Optional*. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. |  [optional] |
|**newChatMembers** | [**List&lt;User&gt;**](User.md) | *Optional*. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members) |  [optional] |
|**newChatPhoto** | [**List&lt;PhotoSize&gt;**](PhotoSize.md) | *Optional*. A chat photo was change to this value |  [optional] |
|**newChatTitle** | **String** | *Optional*. A chat title was changed to this value |  [optional] |
|**passportData** | [**PassportData**](PassportData.md) |  |  [optional] |
|**photo** | [**List&lt;PhotoSize&gt;**](PhotoSize.md) | *Optional*. Message is a photo, available sizes of the photo |  [optional] |
|**pinnedMessage** | [**Message**](Message.md) |  |  [optional] |
|**poll** | [**Poll**](Poll.md) |  |  [optional] |
|**proximityAlertTriggered** | [**ProximityAlertTriggered**](ProximityAlertTriggered.md) |  |  [optional] |
|**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  |  [optional] |
|**replyToMessage** | [**Message**](Message.md) |  |  [optional] |
|**senderChat** | [**Chat**](Chat.md) |  |  [optional] |
|**sticker** | [**Sticker**](Sticker.md) |  |  [optional] |
|**successfulPayment** | [**SuccessfulPayment**](SuccessfulPayment.md) |  |  [optional] |
|**supergroupChatCreated** | **Boolean** | *Optional*. Service message: the supergroup has been created. This field can&#39;t be received in a message coming through updates, because bot can&#39;t be a member of a supergroup when it is created. It can only be found in reply\\_to\\_message if someone replies to a very first message in a directly created supergroup. |  [optional] |
|**text** | **String** | *Optional*. For text messages, the actual UTF-8 text of the message, 0-4096 characters |  [optional] |
|**venue** | [**Venue**](Venue.md) |  |  [optional] |
|**viaBot** | [**User**](User.md) |  |  [optional] |
|**video** | [**Video**](Video.md) |  |  [optional] |
|**videoNote** | [**VideoNote**](VideoNote.md) |  |  [optional] |
|**voice** | [**Voice**](Voice.md) |  |  [optional] |



