# InfluxOssApiService.TelegramNotificationRuleBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disableWebPagePreview** | **Boolean** | Disables preview of web links in the sent messages when \&quot;true\&quot;. Defaults to \&quot;false\&quot; . | [optional] 
**messageTemplate** | **String** | The message template as a flux interpolated string. | 
**parseMode** | **String** | Parse mode of the message text per https://core.telegram.org/bots/api#formatting-options . Defaults to \&quot;MarkdownV2\&quot; . | [optional] 
**type** | **String** | The discriminator between other types of notification rules is \&quot;telegram\&quot;. | 



## Enum: ParseModeEnum


* `MarkdownV2` (value: `"MarkdownV2"`)

* `HTML` (value: `"HTML"`)

* `Markdown` (value: `"Markdown"`)





## Enum: TypeEnum


* `telegram` (value: `"telegram"`)




