

# MessageEntity

This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**language** | **String** | *Optional*. For “pre” only, the programming language of the entity text |  [optional] |
|**length** | **Integer** | Length of the entity in UTF-16 code units |  |
|**offset** | **Integer** | Offset in UTF-16 code units to the start of the entity |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the entity. Can be “mention” (&#x60;@username&#x60;), “hashtag” (&#x60;#hashtag&#x60;), “cashtag” (&#x60;$USD&#x60;), “bot\\_command” (&#x60;/start@jobs_bot&#x60;), “url” (&#x60;https://telegram.org&#x60;), “email” (&#x60;do-not-reply@telegram.org&#x60;), “phone\\_number” (&#x60;+1-212-555-0123&#x60;), “bold” (**bold text**), “italic” (*italic text*), “underline” (underlined text), “strikethrough” (strikethrough text), “code” (monowidth string), “pre” (monowidth block), “text\\_link” (for clickable text URLs), “text\\_mention” (for users [without usernames](https://telegram.org/blog/edit#new-mentions)) |  |
|**url** | **String** | *Optional*. For “text\\_link” only, url that will be opened after user taps on the text |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MENTION | &quot;mention&quot; |
| HASHTAG | &quot;hashtag&quot; |
| CASHTAG | &quot;cashtag&quot; |
| BOT_COMMAND | &quot;bot_command&quot; |
| URL | &quot;url&quot; |
| EMAIL | &quot;email&quot; |
| PHONE_NUMBER | &quot;phone_number&quot; |
| BOLD | &quot;bold&quot; |
| ITALIC | &quot;italic&quot; |
| UNDERLINE | &quot;underline&quot; |
| STRIKETHROUGH | &quot;strikethrough&quot; |
| CODE | &quot;code&quot; |
| PRE | &quot;pre&quot; |
| TEXT_LINK | &quot;text_link&quot; |
| TEXT_MENTION | &quot;text_mention&quot; |



