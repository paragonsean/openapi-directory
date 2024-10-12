# StreamChatApi.Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) | Array of message attachments | 
**beforeMessageSendFailed** | **Boolean** | Whether &#x60;before_message_send webhook&#x60; failed or not. Field is only accessible in push webhook | [optional] 
**cid** | **String** | Channel unique identifier in &lt;type&gt;:&lt;id&gt; format | 
**command** | **String** | Contains provided slash command | [optional] 
**createdAt** | **Date** | Date/time of creation | 
**deletedAt** | **Date** | Date/time of deletion | [optional] 
**html** | **String** | Contains HTML markup of the message. Can only be set when using server-side API | 
**i18n** | **{String: String}** | Object with translations. Key &#x60;language&#x60; contains the original language key. Other keys contain translations | [optional] 
**id** | **String** | Message ID is unique string identifier of the message | 
**imageLabels** | **{String: [String]}** | Contains image moderation information | [optional] 
**latestReactions** | [**[Reaction]**](Reaction.md) | List of 10 latest reactions to this message | 
**mentionedUsers** | [**[UserObject]**](UserObject.md) | List of mentioned users | 
**mml** | **String** | Should be empty if &#x60;text&#x60; is provided. Can only be set when using server-side API | [optional] 
**ownReactions** | [**[Reaction]**](Reaction.md) | List of 10 latest reactions of authenticated user to this message | 
**parentId** | **String** | ID of parent message (thread) | [optional] 
**pinExpires** | **Date** | Date when pinned message expires | [optional] 
**pinned** | **Boolean** | Whether message is pinned or not | 
**pinnedAt** | **Date** | Date when message got pinned | [optional] 
**pinnedBy** | [**UserObject**](UserObject.md) |  | [optional] 
**quotedMessage** | [**Message**](Message.md) |  | [optional] 
**quotedMessageId** | **String** |  | [optional] 
**reactionCounts** | **{String: Number}** | An object containing number of reactions of each type. Key: reaction type (string), value: number of reactions (int) | 
**reactionScores** | **{String: Number}** | An object containing scores of reactions of each type. Key: reaction type (string), value: total score of reactions (int) | 
**replyCount** | **Number** | Number of replies to this message | 
**shadowed** | **Boolean** | Whether the message was shadowed or not | 
**showInChannel** | **Boolean** | Whether thread reply should be shown in the channel as well | [optional] 
**silent** | **Boolean** | Whether message is silent or not | 
**text** | **String** | Text of the message. Should be empty if &#x60;mml&#x60; is provided | 
**threadParticipants** | [**[UserObject]**](UserObject.md) | List of users who participate in thread | [optional] 
**type** | **String** | Contains type of the message | 
**updatedAt** | **Date** | Date/time of the last update | 
**user** | [**UserObject**](UserObject.md) |  | [optional] 



## Enum: TypeEnum


* `regular` (value: `"regular"`)

* `ephemeral` (value: `"ephemeral"`)

* `error` (value: `"error"`)

* `reply` (value: `"reply"`)

* `system` (value: `"system"`)

* `deleted` (value: `"deleted"`)




