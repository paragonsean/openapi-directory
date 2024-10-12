

# TelegramNotificationRuleBase


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableWebPagePreview** | **Boolean** | Disables preview of web links in the sent messages when \&quot;true\&quot;. Defaults to \&quot;false\&quot; . |  [optional] |
|**messageTemplate** | **String** | The message template as a flux interpolated string. |  |
|**parseMode** | [**ParseModeEnum**](#ParseModeEnum) | Parse mode of the message text per https://core.telegram.org/bots/api#formatting-options . Defaults to \&quot;MarkdownV2\&quot; . |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The discriminator between other types of notification rules is \&quot;telegram\&quot;. |  |



## Enum: ParseModeEnum

| Name | Value |
|---- | -----|
| MARKDOWN_V2 | &quot;MarkdownV2&quot; |
| HTML | &quot;HTML&quot; |
| MARKDOWN | &quot;Markdown&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TELEGRAM | &quot;telegram&quot; |



