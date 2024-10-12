# TelegramBotApi.Poll

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowsMultipleAnswers** | **Boolean** | True, if the poll allows multiple answers | 
**closeDate** | **Number** | *Optional*. Point in time (Unix timestamp) when the poll will be automatically closed | [optional] 
**correctOptionId** | **Number** | *Optional*. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot. | [optional] 
**explanation** | **String** | *Optional*. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters | [optional] 
**explanationEntities** | [**[MessageEntity]**](MessageEntity.md) | *Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the *explanation* | [optional] 
**id** | **String** | Unique poll identifier | 
**isAnonymous** | **Boolean** | True, if the poll is anonymous | 
**isClosed** | **Boolean** | True, if the poll is closed | 
**openPeriod** | **Number** | *Optional*. Amount of time in seconds the poll will be active after creation | [optional] 
**options** | [**[PollOption]**](PollOption.md) | List of poll options | 
**question** | **String** | Poll question, 1-255 characters | 
**totalVoterCount** | **Number** | Total number of users that voted in the poll | 
**type** | **String** | Poll type, currently can be “regular” or “quiz” | 


