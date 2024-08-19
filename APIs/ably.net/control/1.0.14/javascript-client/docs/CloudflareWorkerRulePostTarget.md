# ControlApiV1.CloudflareWorkerRulePostTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**[AmqpExternalRulePatchTargetHeadersInner]**](AmqpExternalRulePatchTargetHeadersInner.md) | If you have additional information to send, you&#39;ll need to include the relevant headers. | [optional] 
**signingKeyId** | **String** | The signing key ID for use in &#x60;batch&#x60; mode. Ably will optionally sign the payload using an API key ensuring your servers can validate the payload using the private API key. See the &lt;a href&#x3D;\&quot;https://ably.com/documentation/general/events#security\&quot;&gt;webhook security docs&lt;/a&gt; for more information. | [optional] 
**url** | **String** |  | 


