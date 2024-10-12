

# TransportSendberryGet

The TransportSendberry resource is a collection of transports that carry dispatched alerts to the external Sendberry service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**sendberryAuthKey** | **String** | The auth key for the Sendberry service. |  |
|**sendberryFrom** | **String** | The sender name or phone number for the Sendberry service. |  |
|**sendberryPassword** | **String** | The password for the Sendberry service. Stored in encrypted format. |  |
|**sendberryUsername** | **String** | The username for the Sendberry service. |  |
|**transportName** | **String** | The name of the transport. |  |



