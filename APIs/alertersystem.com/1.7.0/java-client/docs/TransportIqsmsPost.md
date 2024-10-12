

# TransportIqsmsPost

The TransportIqsms resource is a collection of transports that carry dispatched alerts to the external Iqsms service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**iqsmsFrom** | **String** | The sender value for the Iqsms service. |  |
|**iqsmsLogin** | **String** | The login for the Iqsms service. |  |
|**iqsmsPassword** | **String** | The password for the Iqsms service. Stored in encrypted format. |  |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



