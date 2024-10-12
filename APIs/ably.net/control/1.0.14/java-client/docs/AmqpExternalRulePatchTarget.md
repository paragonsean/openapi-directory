

# AmqpExternalRulePatchTarget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enveloped** | **Boolean** | Messages delivered through Reactor are wrapped in an Ably envelope by default that contains metadata about the message and its payload. The form of the envelope depends on whether it is part of a Webhook/Function or a Queue/Firehose rule. For everything besides Webhooks, you can ensure you only get the raw payload by unchecking \&quot;Enveloped\&quot; when setting up the rule. |  [optional] |
|**format** | **String** |  |  [optional] |
|**headers** | [**List&lt;AmqpExternalRulePatchTargetHeadersInner&gt;**](AmqpExternalRulePatchTargetHeadersInner.md) | If you have additional information to send, you&#39;ll need to include the relevant headers. |  [optional] |
|**mandatoryRoute** | **Boolean** | Reject delivery of the message if the route does not exist, otherwise fail silently. |  [optional] |
|**messageTtl** | **Integer** | You can optionally override the default TTL on a queue and specify a TTL in minutes for messages to be persisted. It is unusual to change the default TTL, so if this field is left empty, the default TTL for the queue will be used. |  [optional] |
|**persistentMessages** | **Boolean** | Marks the message as persistent, instructing the broker to write it to disk if it is in a durable queue. |  [optional] |
|**routingKey** | **String** | The AMQP routing key. See this &lt;a href&#x3D;\&quot;https://knowledge.ably.com/what-is-the-format-of-the-routingkey-for-an-amqp-or-kinesis-reactor-rule\&quot;&gt;Ably knowledge base article&lt;/a&gt; for details. |  [optional] |
|**url** | **String** |  |  [optional] |



