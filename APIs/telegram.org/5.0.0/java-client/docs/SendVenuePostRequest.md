

# SendVenuePostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Address of the venue |  |
|**allowSendingWithoutReply** | **Boolean** | Pass *True*, if the message should be sent even if the specified replied-to message is not found |  [optional] |
|**chatId** | [**CopyMessagePostRequestChatId**](CopyMessagePostRequestChatId.md) |  |  |
|**disableNotification** | **Boolean** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |  [optional] |
|**foursquareId** | **String** | Foursquare identifier of the venue |  [optional] |
|**foursquareType** | **String** | Foursquare type of the venue, if known. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.) |  [optional] |
|**googlePlaceId** | **String** | Google Places identifier of the venue |  [optional] |
|**googlePlaceType** | **String** | Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).) |  [optional] |
|**latitude** | **BigDecimal** | Latitude of the venue |  |
|**longitude** | **BigDecimal** | Longitude of the venue |  |
|**replyMarkup** | [**CopyMessagePostRequestReplyMarkup**](CopyMessagePostRequestReplyMarkup.md) |  |  [optional] |
|**replyToMessageId** | **Integer** | If the message is a reply, ID of the original message |  [optional] |
|**title** | **String** | Name of the venue |  |



