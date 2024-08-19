# ControlApiV1.GoogleCloudFunctionRulePatchTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enveloped** | **Boolean** | Messages delivered through Reactor are wrapped in an Ably envelope by default that contains metadata about the message and its payload. The form of the envelope depends on whether it is part of a Webhook/Function or a Queue/Firehose rule. For everything besides Webhooks, you can ensure you only get the raw payload by unchecking \&quot;Enveloped\&quot; when setting up the rule. | [optional] 
**format** | **String** | JSON provides a text-based encoding. | [optional] 
**functionName** | **String** | The name of your Google Cloud Function. | [optional] 
**headers** | [**[AmqpExternalRulePatchTargetHeadersInner]**](AmqpExternalRulePatchTargetHeadersInner.md) | If you have additional information to send, you&#39;ll need to include the relevant headers. | [optional] 
**projectId** | **String** | The project ID for your Google Cloud Project that was generated when you created your project. | [optional] 
**region** | **String** | The region in which your Google Cloud Function is hosted. See the &lt;a href&#x3D;\&quot;https://cloud.google.com/compute/docs/regions-zones/\&quot;&gt;Google documentation&lt;/a&gt; for more details. | [optional] 
**signingKeyId** | **String** | The signing key ID for use in &#x60;batch&#x60; mode. Ably will optionally sign the payload using an API key ensuring your servers can validate the payload using the private API key. See the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#security\&quot;&gt;webhook security docs&lt;/a&gt; for more information. | [optional] 



## Enum: FormatEnum


* `json` (value: `"json"`)




