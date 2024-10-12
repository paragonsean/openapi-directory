

# TransportMercurePut

The TransportMercure resource is a collection of transports that carry dispatched alerts to the external Mercure service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**mercureHubJwtToken** | **String** | The JWT token for the hub for the Mercure service. Stored in encrypted format. |  |
|**mercureHubUrl** | **URI** | The URL for the hub for the Mercure service. |  [optional] |
|**mercureTopic** | **String** | The optional topic for the Mercure service. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



