

# Annotation

Output only. Annotations associated with the plain-text body of the message. To add basic formatting to a text message, see [Format text messages](https://developers.google.com/chat/format-messages). Example plain-text message body: ``` Hello @FooBot how are you!\" ``` The corresponding annotations metadata: ``` \"annotations\":[{ \"type\":\"USER_MENTION\", \"startIndex\":6, \"length\":7, \"userMention\": { \"user\": { \"name\":\"users/{user}\", \"displayName\":\"FooBot\", \"avatarUrl\":\"https://goo.gl/aeDtrS\", \"type\":\"BOT\" }, \"type\":\"MENTION\" } }] ```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**length** | **Integer** | Length of the substring in the plain-text message body this annotation corresponds to. |  [optional] |
|**slashCommand** | [**SlashCommandMetadata**](SlashCommandMetadata.md) |  |  [optional] |
|**startIndex** | **Integer** | Start index (0-based, inclusive) in the plain-text message body this annotation corresponds to. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this annotation. |  [optional] |
|**userMention** | [**UserMentionMetadata**](UserMentionMetadata.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ANNOTATION_TYPE_UNSPECIFIED | &quot;ANNOTATION_TYPE_UNSPECIFIED&quot; |
| USER_MENTION | &quot;USER_MENTION&quot; |
| SLASH_COMMAND | &quot;SLASH_COMMAND&quot; |



