# TelegramBotApi.SendPollPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowSendingWithoutReply** | **Boolean** | Pass *True*, if the message should be sent even if the specified replied-to message is not found | [optional] 
**allowsMultipleAnswers** | **Boolean** | True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to *False* | [optional] 
**chatId** | [**CopyMessagePostRequestChatId**](CopyMessagePostRequestChatId.md) |  | 
**closeDate** | **Number** | Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can&#39;t be used together with *open\\_period*. | [optional] 
**correctOptionId** | **Number** | 0-based identifier of the correct answer option, required for polls in quiz mode | [optional] 
**disableNotification** | **Boolean** | Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. | [optional] 
**explanation** | **String** | Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing | [optional] 
**explanationEntities** | [**[MessageEntity]**](MessageEntity.md) | List of special entities that appear in the poll explanation, which can be specified instead of *parse\\_mode* | [optional] 
**explanationParseMode** | **String** | Mode for parsing entities in the explanation. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details. | [optional] 
**isAnonymous** | **Boolean** | True, if the poll needs to be anonymous, defaults to *True* | [optional] 
**isClosed** | **Boolean** | Pass *True*, if the poll needs to be immediately closed. This can be useful for poll preview. | [optional] 
**openPeriod** | **Number** | Amount of time in seconds the poll will be active after creation, 5-600. Can&#39;t be used together with *close\\_date*. | [optional] 
**options** | **[String]** | A JSON-serialized list of answer options, 2-10 strings 1-100 characters each | 
**question** | **String** | Poll question, 1-300 characters | 
**replyMarkup** | [**CopyMessagePostRequestReplyMarkup**](CopyMessagePostRequestReplyMarkup.md) |  | [optional] 
**replyToMessageId** | **Number** | If the message is a reply, ID of the original message | [optional] 
**type** | **String** | Poll type, “quiz” or “regular”, defaults to “regular” | [optional] 


