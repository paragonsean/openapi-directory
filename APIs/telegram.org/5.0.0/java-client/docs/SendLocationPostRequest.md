

# SendLocationPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowSendingWithoutReply** | **Boolean** | Pass *True*, if the message should be sent even if the specified replied-to message is not found |  [optional] |
|**chatId** | [**CopyMessagePostRequestChatId**](CopyMessagePostRequestChatId.md) |  |  |
|**disableNotification** | **Boolean** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. |  [optional] |
|**heading** | **Integer** | For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. |  [optional] |
|**horizontalAccuracy** | **BigDecimal** | The radius of uncertainty for the location, measured in meters; 0-1500 |  [optional] |
|**latitude** | **BigDecimal** | Latitude of the location |  |
|**livePeriod** | **Integer** | Period in seconds for which the location will be updated (see [Live Locations](https://telegram.org/blog/live-locations), should be between 60 and 86400. |  [optional] |
|**longitude** | **BigDecimal** | Longitude of the location |  |
|**proximityAlertRadius** | **Integer** | For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. |  [optional] |
|**replyMarkup** | [**CopyMessagePostRequestReplyMarkup**](CopyMessagePostRequestReplyMarkup.md) |  |  [optional] |
|**replyToMessageId** | **Integer** | If the message is a reply, ID of the original message |  [optional] |



