

# TransportSmsmodeJsonldPost

The TransportSmsmode resource is a collection of transports that carry dispatched alerts to the external Smsmode service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**smsmodeApiKey** | **String** | The API key for the Smsmode service. Stored in encrypted format. |  |
|**smsmodeFrom** | **String** | The from value for the Smsmode service. |  |
|**transportName** | **String** | The name of the transport. |  |



