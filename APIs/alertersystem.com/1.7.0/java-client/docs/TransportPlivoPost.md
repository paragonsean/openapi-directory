

# TransportPlivoPost

The TransportPlivo resource is a collection of transports that carry dispatched alerts to the external Plivo service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**plivoAuthId** | **String** | The auth ID for the Plivo service. |  |
|**plivoAuthToken** | **String** | The auth token for the Plivo service. Stored in encrypted format. |  |
|**plivoFrom** | **String** | The sender value for the Plivo service. |  |
|**transportName** | **String** | The name of the transport. |  |



