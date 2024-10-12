

# TransportGitterPatch

The TransportGitter resource is a collection of transports that carry dispatched alerts to the external Gitter service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**gitterRoomId** | **String** | The room ID for the Gitter service. |  |
|**gitterToken** | **String** | The token for the Gitter service. Stored in encrypted format. |  |
|**transportName** | **String** | The name of the transport. |  |



