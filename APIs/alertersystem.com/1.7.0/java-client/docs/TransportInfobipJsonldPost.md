

# TransportInfobipJsonldPost

The TransportInfobip resource is a collection of transports that carry dispatched alerts to the external Infobip service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**infobipAuthToken** | **String** | The auth token for the Infobip service. Stored in encrypted format. |  |
|**infobipFrom** | **String** | The sender value for the Infobip service. |  |
|**infobipHost** | **String** | The host for the Infobip service. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



