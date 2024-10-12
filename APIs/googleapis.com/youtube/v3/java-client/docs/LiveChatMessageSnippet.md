

# LiveChatMessageSnippet

Next ID: 34

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorChannelId** | **String** | The ID of the user that authored this message, this field is not always filled. textMessageEvent - the user that wrote the message fanFundingEvent - the user that funded the broadcast newSponsorEvent - the user that just became a sponsor memberMilestoneChatEvent - the member that sent the message membershipGiftingEvent - the user that made the purchase giftMembershipReceivedEvent - the user that received the gift membership messageDeletedEvent - the moderator that took the action messageRetractedEvent - the author that retracted their message userBannedEvent - the moderator that took the action superChatEvent - the user that made the purchase superStickerEvent - the user that made the purchase pollEvent - the user that created the poll |  [optional] |
|**displayMessage** | **String** | Contains a string that can be displayed to the user. If this field is not present the message is silent, at the moment only messages of type TOMBSTONE and CHAT_ENDED_EVENT are silent. |  [optional] |
|**fanFundingEventDetails** | [**LiveChatFanFundingEventDetails**](LiveChatFanFundingEventDetails.md) |  |  [optional] |
|**giftMembershipReceivedDetails** | [**LiveChatGiftMembershipReceivedDetails**](LiveChatGiftMembershipReceivedDetails.md) |  |  [optional] |
|**hasDisplayContent** | **Boolean** | Whether the message has display content that should be displayed to users. |  [optional] |
|**liveChatId** | **String** |  |  [optional] |
|**memberMilestoneChatDetails** | [**LiveChatMemberMilestoneChatDetails**](LiveChatMemberMilestoneChatDetails.md) |  |  [optional] |
|**membershipGiftingDetails** | [**LiveChatMembershipGiftingDetails**](LiveChatMembershipGiftingDetails.md) |  |  [optional] |
|**messageDeletedDetails** | [**LiveChatMessageDeletedDetails**](LiveChatMessageDeletedDetails.md) |  |  [optional] |
|**messageRetractedDetails** | [**LiveChatMessageRetractedDetails**](LiveChatMessageRetractedDetails.md) |  |  [optional] |
|**newSponsorDetails** | [**LiveChatNewSponsorDetails**](LiveChatNewSponsorDetails.md) |  |  [optional] |
|**pollDetails** | [**LiveChatPollDetails**](LiveChatPollDetails.md) |  |  [optional] |
|**publishedAt** | **OffsetDateTime** | The date and time when the message was orignally published. |  [optional] |
|**superChatDetails** | [**LiveChatSuperChatDetails**](LiveChatSuperChatDetails.md) |  |  [optional] |
|**superStickerDetails** | [**LiveChatSuperStickerDetails**](LiveChatSuperStickerDetails.md) |  |  [optional] |
|**textMessageDetails** | [**LiveChatTextMessageDetails**](LiveChatTextMessageDetails.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of message, this will always be present, it determines the contents of the message as well as which fields will be present. |  [optional] |
|**userBannedDetails** | [**LiveChatUserBannedMessageDetails**](LiveChatUserBannedMessageDetails.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INVALID_TYPE | &quot;invalidType&quot; |
| TEXT_MESSAGE_EVENT | &quot;textMessageEvent&quot; |
| TOMBSTONE | &quot;tombstone&quot; |
| FAN_FUNDING_EVENT | &quot;fanFundingEvent&quot; |
| CHAT_ENDED_EVENT | &quot;chatEndedEvent&quot; |
| SPONSOR_ONLY_MODE_STARTED_EVENT | &quot;sponsorOnlyModeStartedEvent&quot; |
| SPONSOR_ONLY_MODE_ENDED_EVENT | &quot;sponsorOnlyModeEndedEvent&quot; |
| NEW_SPONSOR_EVENT | &quot;newSponsorEvent&quot; |
| MEMBER_MILESTONE_CHAT_EVENT | &quot;memberMilestoneChatEvent&quot; |
| MEMBERSHIP_GIFTING_EVENT | &quot;membershipGiftingEvent&quot; |
| GIFT_MEMBERSHIP_RECEIVED_EVENT | &quot;giftMembershipReceivedEvent&quot; |
| MESSAGE_DELETED_EVENT | &quot;messageDeletedEvent&quot; |
| MESSAGE_RETRACTED_EVENT | &quot;messageRetractedEvent&quot; |
| USER_BANNED_EVENT | &quot;userBannedEvent&quot; |
| SUPER_CHAT_EVENT | &quot;superChatEvent&quot; |
| SUPER_STICKER_EVENT | &quot;superStickerEvent&quot; |
| POLL_EVENT | &quot;pollEvent&quot; |



