

# MessageRequest

Represents any chat message

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | **List&lt;AttachmentRequest&gt;** | Array of message attachments |  |
|**cid** | **List&lt;Integer&gt;** | Channel unique identifier in &lt;type&gt;:&lt;id&gt; format |  [optional] |
|**html** | **String** | Contains HTML markup of the message. Can only be set when using server-side API |  [optional] |
|**id** | **String** | Message ID is unique string identifier of the message |  [optional] |
|**mentionedUsers** | **List&lt;String&gt;** | List of mentioned users |  [optional] |
|**mml** | **String** | Should be empty if &#x60;text&#x60; is provided. Can only be set when using server-side API |  [optional] |
|**parent** | **List&lt;Integer&gt;** |  |  [optional] |
|**parentId** | **String** | ID of parent message (thread) |  [optional] |
|**pinExpires** | **OffsetDateTime** | Date when pinned message expires |  [optional] |
|**pinned** | **Boolean** | Whether message is pinned or not |  [optional] |
|**pinnedAt** | **OffsetDateTime** | Date when message got pinned |  [optional] |
|**pinnedBy** | **List&lt;Integer&gt;** | Contains user who pinned the message |  [optional] |
|**quotedMessageId** | **String** |  |  [optional] |
|**reactionScores** | **List&lt;Integer&gt;** | An object containing scores of reactions of each type. Key: reaction type (string), value: total score of reactions (int) |  [optional] |
|**showInChannel** | **Boolean** | Whether thread reply should be shown in the channel as well |  [optional] |
|**silent** | **Boolean** | Whether message is silent or not |  [optional] |
|**text** | **String** | Text of the message. Should be empty if &#x60;mml&#x60; is provided |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Contains type of the message |  [optional] |
|**user** | **UserObjectRequest** |  |  [optional] |
|**userId** | **String** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;regular&quot; |
| EPHEMERAL | &quot;ephemeral&quot; |
| ERROR | &quot;error&quot; |
| REPLY | &quot;reply&quot; |
| SYSTEM | &quot;system&quot; |
| DELETED | &quot;deleted&quot; |



