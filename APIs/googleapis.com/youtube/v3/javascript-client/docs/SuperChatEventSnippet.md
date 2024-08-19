# YouTubeDataApiV3.SuperChatEventSnippet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountMicros** | **String** | The purchase amount, in micros of the purchase currency. e.g., 1 is represented as 1000000. | [optional] 
**channelId** | **String** | Channel id where the event occurred. | [optional] 
**commentText** | **String** | The text contents of the comment left by the user. | [optional] 
**createdAt** | **Date** | The date and time when the event occurred. | [optional] 
**currency** | **String** | The currency in which the purchase was made. ISO 4217. | [optional] 
**displayString** | **String** | A rendered string that displays the purchase amount and currency (e.g., \&quot;$1.00\&quot;). The string is rendered for the given language. | [optional] 
**isSuperStickerEvent** | **Boolean** | True if this event is a Super Sticker event. | [optional] 
**messageType** | **Number** | The tier for the paid message, which is based on the amount of money spent to purchase the message. | [optional] 
**superStickerMetadata** | [**SuperStickerMetadata**](SuperStickerMetadata.md) |  | [optional] 
**supporterDetails** | [**ChannelProfileDetails**](ChannelProfileDetails.md) |  | [optional] 


