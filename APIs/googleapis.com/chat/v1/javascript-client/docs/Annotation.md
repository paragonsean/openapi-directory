# GoogleChatApi.Annotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **Number** | Length of the substring in the plain-text message body this annotation corresponds to. | [optional] 
**slashCommand** | [**SlashCommandMetadata**](SlashCommandMetadata.md) |  | [optional] 
**startIndex** | **Number** | Start index (0-based, inclusive) in the plain-text message body this annotation corresponds to. | [optional] 
**type** | **String** | The type of this annotation. | [optional] 
**userMention** | [**UserMentionMetadata**](UserMentionMetadata.md) |  | [optional] 



## Enum: TypeEnum


* `ANNOTATION_TYPE_UNSPECIFIED` (value: `"ANNOTATION_TYPE_UNSPECIFIED"`)

* `USER_MENTION` (value: `"USER_MENTION"`)

* `SLASH_COMMAND` (value: `"SLASH_COMMAND"`)




