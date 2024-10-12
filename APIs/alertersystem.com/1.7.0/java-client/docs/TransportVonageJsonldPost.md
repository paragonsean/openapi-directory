

# TransportVonageJsonldPost

The TransportVonage resource is a collection of transports that carry dispatched alerts to the external Vonage service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |
|**vonageFrom** | **String** | The sender for the Vonage service. |  |
|**vonageKey** | **String** | The key for the Vonage service. |  |
|**vonageSecret** | **String** | The secret for the Vonage service. Stored in encrypted format. |  |



