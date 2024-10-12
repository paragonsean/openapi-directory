

# TransportEsendexJsonldGet

The TransportEsendex resource is a collection of transports that carry dispatched alerts to the external Esendex service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atContext** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  |  [optional] |
|**atId** | **String** |  |  [optional] [readonly] |
|**atType** | **String** |  |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**esendexAccountReference** | **String** | The account reference that the message should be sent from for the Esendex service. |  |
|**esendexFrom** | **String** | The alphanumeric originator for the message to appear to originate from for the Esendex service. |  |
|**esendexPassword** | **String** | The API password for the Esendex service. Stored in encrypted format. |  |
|**esendexUsername** | **String** | The account email for the Esendex service. |  |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



