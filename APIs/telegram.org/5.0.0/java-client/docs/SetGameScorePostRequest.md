

# SetGameScorePostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chatId** | **Integer** | Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat |  [optional] |
|**disableEditMessage** | **Boolean** | Pass True, if the game message should not be automatically edited to include the current scoreboard |  [optional] |
|**force** | **Boolean** | Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters |  [optional] |
|**inlineMessageId** | **String** | Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message |  [optional] |
|**messageId** | **Integer** | Required if *inline\\_message\\_id* is not specified. Identifier of the sent message |  [optional] |
|**score** | **Integer** | New score, must be non-negative |  |
|**userId** | **Integer** | User identifier |  |



