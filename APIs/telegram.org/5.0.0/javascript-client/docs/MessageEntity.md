# TelegramBotApi.MessageEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **String** | *Optional*. For “pre” only, the programming language of the entity text | [optional] 
**length** | **Number** | Length of the entity in UTF-16 code units | 
**offset** | **Number** | Offset in UTF-16 code units to the start of the entity | 
**type** | **String** | Type of the entity. Can be “mention” (&#x60;@username&#x60;), “hashtag” (&#x60;#hashtag&#x60;), “cashtag” (&#x60;$USD&#x60;), “bot\\_command” (&#x60;/start@jobs_bot&#x60;), “url” (&#x60;https://telegram.org&#x60;), “email” (&#x60;do-not-reply@telegram.org&#x60;), “phone\\_number” (&#x60;+1-212-555-0123&#x60;), “bold” (**bold text**), “italic” (*italic text*), “underline” (underlined text), “strikethrough” (strikethrough text), “code” (monowidth string), “pre” (monowidth block), “text\\_link” (for clickable text URLs), “text\\_mention” (for users [without usernames](https://telegram.org/blog/edit#new-mentions)) | 
**url** | **String** | *Optional*. For “text\\_link” only, url that will be opened after user taps on the text | [optional] 
**user** | [**User**](User.md) |  | [optional] 



## Enum: TypeEnum


* `mention` (value: `"mention"`)

* `hashtag` (value: `"hashtag"`)

* `cashtag` (value: `"cashtag"`)

* `bot_command` (value: `"bot_command"`)

* `url` (value: `"url"`)

* `email` (value: `"email"`)

* `phone_number` (value: `"phone_number"`)

* `bold` (value: `"bold"`)

* `italic` (value: `"italic"`)

* `underline` (value: `"underline"`)

* `strikethrough` (value: `"strikethrough"`)

* `code` (value: `"code"`)

* `pre` (value: `"pre"`)

* `text_link` (value: `"text_link"`)

* `text_mention` (value: `"text_mention"`)




