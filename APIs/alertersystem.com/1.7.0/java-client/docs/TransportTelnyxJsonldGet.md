

# TransportTelnyxJsonldGet

The TransportTelnyx resource is a collection of transports that carry dispatched alerts to the external Telnyx service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atContext** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  |  [optional] |
|**atId** | **String** |  |  [optional] [readonly] |
|**atType** | **String** |  |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**telnyxApiKey** | **String** | The API key for the Telnyx service. Stored in encrypted format. |  |
|**telnyxFrom** | **String** | The from value for the Telnyx service. |  |
|**telnyxMessagingProfileId** | **String** | The messaging profile ID (You need this in order to show a name to the recipient instead of just the phone number) for the Telnyx service. |  |
|**transportName** | **String** | The name of the transport. |  |



