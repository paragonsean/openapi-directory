

# AzureFunctionRulePostTarget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureAppId** | **String** | The Microsoft Azure Application ID. You can find your Microsoft Azure Application ID as shown in this &lt;a href&#x3D;\&quot;https://dev.applicationinsights.io/documentation/Authorization/API-key-and-App-ID\&quot;&gt;article&lt;/a&gt;. |  |
|**azureFunctionName** | **String** | The name of your Microsoft Azure Function. |  |
|**enveloped** | **Boolean** | Messages delivered through Reactor are wrapped in an Ably envelope by default that contains metadata about the message and its payload. The form of the envelope depends on whether it is part of a Webhook/Function or a Queue/Firehose rule. For everything besides Webhooks, you can ensure you only get the raw payload by unchecking \&quot;Enveloped\&quot; when setting up the rule. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | JSON provides a text-based encoding. |  [optional] |
|**headers** | [**List&lt;AmqpExternalRulePatchTargetHeadersInner&gt;**](AmqpExternalRulePatchTargetHeadersInner.md) | If you have additional information to send, you&#39;ll need to include the relevant headers. |  [optional] |
|**signingKeyId** | **String** | The signing key ID for use in &#x60;batch&#x60; mode. Ably will optionally sign the payload using an API key ensuring your servers can validate the payload using the private API key. See the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#security\&quot;&gt;webhook security docs&lt;/a&gt; for more information. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| JSON | &quot;json&quot; |



