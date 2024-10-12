

# TransportSendberryPost

The TransportSendberry resource is a collection of transports that carry dispatched alerts to the external Sendberry service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**sendberryAuthKey** | **String** | The auth key for the Sendberry service. |  |
|**sendberryFrom** | **String** | The sender name or phone number for the Sendberry service. |  |
|**sendberryPassword** | **String** | The password for the Sendberry service. Stored in encrypted format. |  |
|**sendberryUsername** | **String** | The username for the Sendberry service. |  |
|**transportName** | **String** | The name of the transport. |  |



