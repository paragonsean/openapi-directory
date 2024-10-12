

# Message

Represents any chat message

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | **List&lt;Attachment&gt;** | Array of message attachments |  |
|**beforeMessageSendFailed** | **Boolean** | Whether &#x60;before_message_send webhook&#x60; failed or not. Field is only accessible in push webhook |  [optional] |
|**cid** | **String** | Channel unique identifier in &lt;type&gt;:&lt;id&gt; format |  |
|**command** | **String** | Contains provided slash command |  [optional] |
|**createdAt** | **OffsetDateTime** | Date/time of creation |  |
|**deletedAt** | **OffsetDateTime** | Date/time of deletion |  [optional] |
|**html** | **String** | Contains HTML markup of the message. Can only be set when using server-side API |  |
|**i18n** | **Map&lt;String, String&gt;** | Object with translations. Key &#x60;language&#x60; contains the original language key. Other keys contain translations |  [optional] |
|**id** | **String** | Message ID is unique string identifier of the message |  |
|**imageLabels** | **Map&lt;String, List&lt;String&gt;&gt;** | Contains image moderation information |  [optional] |
|**latestReactions** | **List&lt;Reaction&gt;** | List of 10 latest reactions to this message |  |
|**mentionedUsers** | **List&lt;UserObject&gt;** | List of mentioned users |  |
|**mml** | **String** | Should be empty if &#x60;text&#x60; is provided. Can only be set when using server-side API |  [optional] |
|**ownReactions** | **List&lt;Reaction&gt;** | List of 10 latest reactions of authenticated user to this message |  |
|**parentId** | **String** | ID of parent message (thread) |  [optional] |
|**pinExpires** | **OffsetDateTime** | Date when pinned message expires |  [optional] |
|**pinned** | **Boolean** | Whether message is pinned or not |  |
|**pinnedAt** | **OffsetDateTime** | Date when message got pinned |  [optional] |
|**pinnedBy** | **UserObject** |  |  [optional] |
|**quotedMessage** | **Message** |  |  [optional] |
|**quotedMessageId** | **String** |  |  [optional] |
|**reactionCounts** | **Map&lt;String, Integer&gt;** | An object containing number of reactions of each type. Key: reaction type (string), value: number of reactions (int) |  |
|**reactionScores** | **Map&lt;String, Integer&gt;** | An object containing scores of reactions of each type. Key: reaction type (string), value: total score of reactions (int) |  |
|**replyCount** | **Integer** | Number of replies to this message |  |
|**shadowed** | **Boolean** | Whether the message was shadowed or not |  |
|**showInChannel** | **Boolean** | Whether thread reply should be shown in the channel as well |  [optional] |
|**silent** | **Boolean** | Whether message is silent or not |  |
|**text** | **String** | Text of the message. Should be empty if &#x60;mml&#x60; is provided |  |
|**threadParticipants** | **List&lt;UserObject&gt;** | List of users who participate in thread |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Contains type of the message |  |
|**updatedAt** | **OffsetDateTime** | Date/time of the last update |  |
|**user** | **UserObject** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;regular&quot; |
| EPHEMERAL | &quot;ephemeral&quot; |
| ERROR | &quot;error&quot; |
| REPLY | &quot;reply&quot; |
| SYSTEM | &quot;system&quot; |
| DELETED | &quot;deleted&quot; |



