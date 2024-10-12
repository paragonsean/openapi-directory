# TelegramBotApi.EditMessageLiveLocationPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chatId** | [**EditMessageCaptionPostRequestChatId**](EditMessageCaptionPostRequestChatId.md) |  | [optional] 
**heading** | **Number** | Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified. | [optional] 
**horizontalAccuracy** | **Number** | The radius of uncertainty for the location, measured in meters; 0-1500 | [optional] 
**inlineMessageId** | **String** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message | [optional] 
**latitude** | **Number** | Latitude of new location | 
**longitude** | **Number** | Longitude of new location | 
**messageId** | **Number** | Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit | [optional] 
**proximityAlertRadius** | **Number** | Maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified. | [optional] 
**replyMarkup** | [**InlineKeyboardMarkup**](InlineKeyboardMarkup.md) |  | [optional] 


