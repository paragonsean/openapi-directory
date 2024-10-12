

# TransportSmscPost

The TransportSmsc resource is a collection of transports that carry dispatched alerts to the external Smsc service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**smscFrom** | **String** | The sender (NB: text identity, not a phone number) for the Smsc service. |  |
|**smscLogin** | **String** | The login for the Smsc service. |  |
|**smscPassword** | **String** | The API password for the Smsc service. Stored in encrypted format. |  |
|**transportName** | **String** | The name of the transport. |  |



