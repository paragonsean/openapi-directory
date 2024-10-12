

# TransportAllMySmsPost

The TransportAllMySms resource is a collection of transports that carry dispatched alerts to the external Allmysms service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allMySmsApiKey** | **String** | The API key for the Allmysms service. Stored in encrypted format. |  |
|**allMySmsFrom** | **String** | The sender value (default 36180) for the Allmysms service. |  [optional] |
|**allMySmsLogin** | **String** | The login credential for the Allmysms service. |  |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



