# YouTubeDataApiV3.LiveChatMessageSnippet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorChannelId** | **String** | The ID of the user that authored this message, this field is not always filled. textMessageEvent - the user that wrote the message fanFundingEvent - the user that funded the broadcast newSponsorEvent - the user that just became a sponsor memberMilestoneChatEvent - the member that sent the message membershipGiftingEvent - the user that made the purchase giftMembershipReceivedEvent - the user that received the gift membership messageDeletedEvent - the moderator that took the action messageRetractedEvent - the author that retracted their message userBannedEvent - the moderator that took the action superChatEvent - the user that made the purchase superStickerEvent - the user that made the purchase pollEvent - the user that created the poll | [optional] 
**displayMessage** | **String** | Contains a string that can be displayed to the user. If this field is not present the message is silent, at the moment only messages of type TOMBSTONE and CHAT_ENDED_EVENT are silent. | [optional] 
**fanFundingEventDetails** | [**LiveChatFanFundingEventDetails**](LiveChatFanFundingEventDetails.md) |  | [optional] 
**giftMembershipReceivedDetails** | [**LiveChatGiftMembershipReceivedDetails**](LiveChatGiftMembershipReceivedDetails.md) |  | [optional] 
**hasDisplayContent** | **Boolean** | Whether the message has display content that should be displayed to users. | [optional] 
**liveChatId** | **String** |  | [optional] 
**memberMilestoneChatDetails** | [**LiveChatMemberMilestoneChatDetails**](LiveChatMemberMilestoneChatDetails.md) |  | [optional] 
**membershipGiftingDetails** | [**LiveChatMembershipGiftingDetails**](LiveChatMembershipGiftingDetails.md) |  | [optional] 
**messageDeletedDetails** | [**LiveChatMessageDeletedDetails**](LiveChatMessageDeletedDetails.md) |  | [optional] 
**messageRetractedDetails** | [**LiveChatMessageRetractedDetails**](LiveChatMessageRetractedDetails.md) |  | [optional] 
**newSponsorDetails** | [**LiveChatNewSponsorDetails**](LiveChatNewSponsorDetails.md) |  | [optional] 
**pollDetails** | [**LiveChatPollDetails**](LiveChatPollDetails.md) |  | [optional] 
**publishedAt** | **Date** | The date and time when the message was orignally published. | [optional] 
**superChatDetails** | [**LiveChatSuperChatDetails**](LiveChatSuperChatDetails.md) |  | [optional] 
**superStickerDetails** | [**LiveChatSuperStickerDetails**](LiveChatSuperStickerDetails.md) |  | [optional] 
**textMessageDetails** | [**LiveChatTextMessageDetails**](LiveChatTextMessageDetails.md) |  | [optional] 
**type** | **String** | The type of message, this will always be present, it determines the contents of the message as well as which fields will be present. | [optional] 
**userBannedDetails** | [**LiveChatUserBannedMessageDetails**](LiveChatUserBannedMessageDetails.md) |  | [optional] 



## Enum: TypeEnum


* `invalidType` (value: `"invalidType"`)

* `textMessageEvent` (value: `"textMessageEvent"`)

* `tombstone` (value: `"tombstone"`)

* `fanFundingEvent` (value: `"fanFundingEvent"`)

* `chatEndedEvent` (value: `"chatEndedEvent"`)

* `sponsorOnlyModeStartedEvent` (value: `"sponsorOnlyModeStartedEvent"`)

* `sponsorOnlyModeEndedEvent` (value: `"sponsorOnlyModeEndedEvent"`)

* `newSponsorEvent` (value: `"newSponsorEvent"`)

* `memberMilestoneChatEvent` (value: `"memberMilestoneChatEvent"`)

* `membershipGiftingEvent` (value: `"membershipGiftingEvent"`)

* `giftMembershipReceivedEvent` (value: `"giftMembershipReceivedEvent"`)

* `messageDeletedEvent` (value: `"messageDeletedEvent"`)

* `messageRetractedEvent` (value: `"messageRetractedEvent"`)

* `userBannedEvent` (value: `"userBannedEvent"`)

* `superChatEvent` (value: `"superChatEvent"`)

* `superStickerEvent` (value: `"superStickerEvent"`)

* `pollEvent` (value: `"pollEvent"`)




