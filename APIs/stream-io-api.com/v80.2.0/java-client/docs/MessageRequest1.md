

# MessageRequest1

Represents any chat message

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | **List&lt;AttachmentRequest&gt;** | Array of message attachments |  [optional] |
|**beforeMessageSendFailed** | **Boolean** | Whether &#x60;before_message_send webhook&#x60; failed or not. Field is only accessible in push webhook |  [optional] |
|**cid** | **String** | Channel unique identifier in &lt;type&gt;:&lt;id&gt; format |  [optional] |
|**command** | **String** | Contains provided slash command |  [optional] |
|**createdAt** | **OffsetDateTime** | Date/time of creation |  [optional] |
|**deletedAt** | **OffsetDateTime** | Date/time of deletion |  [optional] |
|**html** | **String** | Contains HTML markup of the message. Can only be set when using server-side API |  [optional] |
|**i18n** | **Map&lt;String, String&gt;** | Object with translations. Key &#x60;language&#x60; contains the original language key. Other keys contain translations |  [optional] |
|**id** | **String** | Message ID is unique string identifier of the message |  [optional] |
|**imageLabels** | **Map&lt;String, List&lt;String&gt;&gt;** | Contains image moderation information |  [optional] |
|**latestReactions** | **List&lt;ReactionRequest&gt;** | List of 10 latest reactions to this message |  [optional] |
|**mentionedUsers** | **List&lt;UserObjectRequest&gt;** | List of mentioned users |  [optional] |
|**mml** | **String** | Should be empty if &#x60;text&#x60; is provided. Can only be set when using server-side API |  |
|**ownReactions** | **List&lt;ReactionRequest&gt;** | List of 10 latest reactions of authenticated user to this message |  [optional] |
|**parentId** | **String** | ID of parent message (thread) |  [optional] |
|**pinExpires** | **OffsetDateTime** | Date when pinned message expires |  [optional] |
|**pinned** | **Boolean** | Whether message is pinned or not |  [optional] |
|**pinnedAt** | **OffsetDateTime** | Date when message got pinned |  [optional] |
|**pinnedBy** | **UserObjectRequest** |  |  [optional] |
|**quotedMessage** | **MessageRequest1** |  |  [optional] |
|**quotedMessageId** | **String** |  |  [optional] |
|**reactionCounts** | **Map&lt;String, Integer&gt;** | An object containing number of reactions of each type. Key: reaction type (string), value: number of reactions (int) |  [optional] |
|**reactionScores** | **Map&lt;String, Integer&gt;** | An object containing scores of reactions of each type. Key: reaction type (string), value: total score of reactions (int) |  [optional] |
|**replyCount** | **Integer** | Number of replies to this message |  [optional] |
|**shadowed** | **Boolean** | Whether the message was shadowed or not |  [optional] |
|**showInChannel** | **Boolean** | Whether thread reply should be shown in the channel as well |  [optional] |
|**silent** | **Boolean** | Whether message is silent or not |  [optional] |
|**text** | **String** | Text of the message. Should be empty if &#x60;mml&#x60; is provided |  |
|**threadParticipants** | **List&lt;UserObjectRequest&gt;** | List of users who participate in thread |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Contains type of the message |  [optional] |
|**updatedAt** | **OffsetDateTime** | Date/time of the last update |  [optional] |
|**user** | **UserObjectRequest** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;regular&quot; |
| EPHEMERAL | &quot;ephemeral&quot; |
| ERROR | &quot;error&quot; |
| REPLY | &quot;reply&quot; |
| SYSTEM | &quot;system&quot; |
| DELETED | &quot;deleted&quot; |



