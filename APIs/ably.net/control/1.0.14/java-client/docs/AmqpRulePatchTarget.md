

# AmqpRulePatchTarget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enveloped** | **Boolean** | Messages delivered through Reactor are wrapped in an Ably envelope by default that contains metadata about the message and its payload. The form of the envelope depends on whether it is part of a Webhook/Function or a Queue/Firehose rule. For everything besides Webhooks, you can ensure you only get the raw payload by unchecking \&quot;Enveloped\&quot; when setting up the rule. |  [optional] |
|**format** | **String** |  |  [optional] |
|**headers** | [**List&lt;AmqpExternalRulePatchTargetHeadersInner&gt;**](AmqpExternalRulePatchTargetHeadersInner.md) | If you have additional information to send, you&#39;ll need to include the relevant headers. |  [optional] |
|**queueId** | **String** |  |  [optional] |



