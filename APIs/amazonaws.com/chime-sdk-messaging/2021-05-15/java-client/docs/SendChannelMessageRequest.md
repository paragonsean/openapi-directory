

# SendChannelMessageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The content of the channel message. |  |
|**type** | [**TypeEnum**](#TypeEnum) | &lt;p&gt;The type of message, &lt;code&gt;STANDARD&lt;/code&gt; or &lt;code&gt;CONTROL&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;STANDARD&lt;/code&gt; messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CONTROL&lt;/code&gt; messages are limited to 30 bytes and do not contain metadata.&lt;/p&gt; |  |
|**persistence** | [**PersistenceEnum**](#PersistenceEnum) | Boolean that controls whether the message is persisted on the back end. Required. |  |
|**metadata** | **String** | The optional metadata for each message. |  [optional] |
|**clientRequestToken** | **String** | The &lt;code&gt;Idempotency&lt;/code&gt; token for each client request. |  |
|**pushNotification** | [**SendChannelMessageRequestPushNotification**](SendChannelMessageRequestPushNotification.md) |  |  [optional] |
|**messageAttributes** | [**Map&lt;String, MessageAttributeValue&gt;**](MessageAttributeValue.md) | The attributes for the message, used for message filtering along with a &lt;code&gt;FilterRule&lt;/code&gt; defined in the &lt;code&gt;PushNotificationPreferences&lt;/code&gt;. |  [optional] |
|**subChannelId** | **String** | The ID of the SubChannel in the request. |  [optional] |
|**contentType** | **String** | The content type of the channel message. |  [optional] |
|**target** | [**List&lt;Target&gt;**](Target.md) | The target of a message. Must be a member of the channel, such as another user, a bot, or the sender. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see.  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;STANDARD&quot; |
| CONTROL | &quot;CONTROL&quot; |



## Enum: PersistenceEnum

| Name | Value |
|---- | -----|
| PERSISTENT | &quot;PERSISTENT&quot; |
| NON_PERSISTENT | &quot;NON_PERSISTENT&quot; |



