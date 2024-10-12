

# TransportVonageGet

The TransportVonage resource is a collection of transports that carry dispatched alerts to the external Vonage service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |
|**vonageFrom** | **String** | The sender for the Vonage service. |  |
|**vonageKey** | **String** | The key for the Vonage service. |  |
|**vonageSecret** | **String** | The secret for the Vonage service. Stored in encrypted format. |  |



