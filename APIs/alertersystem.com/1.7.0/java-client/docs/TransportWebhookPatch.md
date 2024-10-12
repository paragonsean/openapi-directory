

# TransportWebhookPatch

The TransportWebhook resource is a collection of transports that carry dispatched alerts to any external webhook destination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**httpMethodCode** | **String** | The HTTP request method that must be used. |  |
|**mustBeEncryptedValue** | **String** | An optional and arbitrary secret value that must be stored in encrypted format, such as an access token. In the webhookUrl and/or webhookHeaders fields, use the special ENCRYPTED_VALUE placeholder (must be uppercase), which we will replace with the decrypted secret value when using the transport. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |
|**webhookHeaders** | **List&lt;String&gt;** | The HTTP request headers, if any, for the Webhook service. To use the encrypted value:  E.g., Authorization: Bearer ENCRYPTED_VALUE. |  [optional] |
|**webhookUrl** | **URI** | The URL for the Webhook service. |  |



