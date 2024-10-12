# FlatApi.ScoreComment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | The comment text that can includes mentions using the following format: &#x60;@[id:username]&#x60;.  | [optional] 
**context** | [**ScoreCommentContext**](ScoreCommentContext.md) |  | [optional] 
**date** | **Date** | The date when the comment was posted | [optional] 
**id** | **String** | The comment unique identifier | [optional] 
**mentions** | **[String]** | The list of user identifier mentioned on the score | [optional] 
**modificationDate** | **Date** | The date of the last comment modification | [optional] 
**rawComment** | **String** | A raw version of the comment, that can be displayed without parsing the mentions.  | [optional] 
**replyTo** | **String** | When the comment is a reply to another comment, the unique identifier of the parent comment  | [optional] 
**resolved** | **Boolean** | For inline comments, the comment can be marked as resolved and will be hidden in the future responses  | [optional] 
**resolvedBy** | **String** | If the user is marked as resolved, this will contain the unique identifier of the User who marked this comment as resolved  | [optional] 
**revision** | **String** | The unique identifier of revision the comment was posted | [optional] 
**score** | **String** | The unique identifier of the score where the comment was posted | [optional] 
**spam** | **Boolean** | &#x60;true  if the message has been detected as spam and hidden from other users  | [optional] 
**type** | **String** | The type of the comment | [optional] 
**user** | **String** | The author unique identifier | [optional] 



## Enum: TypeEnum


* `document` (value: `"document"`)

* `inline` (value: `"inline"`)




