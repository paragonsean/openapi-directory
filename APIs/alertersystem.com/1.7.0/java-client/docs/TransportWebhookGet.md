

# TransportWebhookGet

The TransportWebhook resource is a collection of transports that carry dispatched alerts to any external webhook destination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**httpMethodCode** | **String** | The HTTP request method that must be used. |  |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**mustBeEncryptedValue** | **String** | An optional and arbitrary secret value that must be stored in encrypted format, such as an access token. In the webhookUrl and/or webhookHeaders fields, use the special ENCRYPTED_VALUE placeholder (must be uppercase), which we will replace with the decrypted secret value when using the transport. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |
|**webhookHeaders** | **List&lt;String&gt;** | The HTTP request headers, if any, for the Webhook service. To use the encrypted value:  E.g., Authorization: Bearer ENCRYPTED_VALUE. |  [optional] |
|**webhookUrl** | **URI** | The URL for the Webhook service. |  |



