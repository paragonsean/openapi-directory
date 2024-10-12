# StreamChatApi.MessageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[AttachmentRequest]**](AttachmentRequest.md) | Array of message attachments | 
**cid** | **[Number]** | Channel unique identifier in &lt;type&gt;:&lt;id&gt; format | [optional] 
**html** | **String** | Contains HTML markup of the message. Can only be set when using server-side API | [optional] 
**id** | **String** | Message ID is unique string identifier of the message | [optional] 
**mentionedUsers** | **[String]** | List of mentioned users | [optional] 
**mml** | **String** | Should be empty if &#x60;text&#x60; is provided. Can only be set when using server-side API | [optional] 
**parent** | **[Number]** |  | [optional] 
**parentId** | **String** | ID of parent message (thread) | [optional] 
**pinExpires** | **Date** | Date when pinned message expires | [optional] 
**pinned** | **Boolean** | Whether message is pinned or not | [optional] 
**pinnedAt** | **Date** | Date when message got pinned | [optional] 
**pinnedBy** | **[Number]** | Contains user who pinned the message | [optional] 
**quotedMessageId** | **String** |  | [optional] 
**reactionScores** | **[Number]** | An object containing scores of reactions of each type. Key: reaction type (string), value: total score of reactions (int) | [optional] 
**showInChannel** | **Boolean** | Whether thread reply should be shown in the channel as well | [optional] 
**silent** | **Boolean** | Whether message is silent or not | [optional] 
**text** | **String** | Text of the message. Should be empty if &#x60;mml&#x60; is provided | [optional] 
**type** | **String** | Contains type of the message | [optional] 
**user** | [**UserObjectRequest**](UserObjectRequest.md) |  | [optional] 
**userId** | **String** |  | [optional] 



## Enum: TypeEnum


* `regular` (value: `"regular"`)

* `ephemeral` (value: `"ephemeral"`)

* `error` (value: `"error"`)

* `reply` (value: `"reply"`)

* `system` (value: `"system"`)

* `deleted` (value: `"deleted"`)




