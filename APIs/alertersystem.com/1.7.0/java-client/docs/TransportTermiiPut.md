

# TransportTermiiPut

The TransportTermii resource is a collection of transports that carry dispatched alerts to the external Termii service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**termiiApiKey** | **String** | The API key for the Termii service. Stored in encrypted format. |  |
|**termiiChannel** | **String** | The channel for the Termii service. |  |
|**termiiFrom** | **String** | The sender value for the Termii service. |  |
|**transportName** | **String** | The name of the transport. |  |



