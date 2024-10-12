

# Game

This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**animation** | [**Animation**](Animation.md) |  |  [optional] |
|**description** | **String** | Description of the game |  |
|**photo** | [**List&lt;PhotoSize&gt;**](PhotoSize.md) | Photo that will be displayed in the game message in chats. |  |
|**text** | **String** | *Optional*. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls [setGameScore](https://core.telegram.org/bots/api/#setgamescore), or manually edited using [editMessageText](https://core.telegram.org/bots/api/#editmessagetext). 0-4096 characters. |  [optional] |
|**textEntities** | [**List&lt;MessageEntity&gt;**](MessageEntity.md) | *Optional*. Special entities that appear in *text*, such as usernames, URLs, bot commands, etc. |  [optional] |
|**title** | **String** | Title of the game |  |



