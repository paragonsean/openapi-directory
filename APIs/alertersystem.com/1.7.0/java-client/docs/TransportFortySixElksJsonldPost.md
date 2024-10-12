

# TransportFortySixElksJsonldPost

The TransportFortySixElks resource is a collection of transports that carry dispatched alerts to the external 46elks service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**fortySixElksApiPassword** | **String** | The API password for the 46elks service. Stored in encrypted format. |  |
|**fortySixElksApiUsername** | **String** | The API username for the 46elks service. |  |
|**fortySixElksFrom** | **String** | The alphanumeric originator for the message to appear to originate from for the 46elks service. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



