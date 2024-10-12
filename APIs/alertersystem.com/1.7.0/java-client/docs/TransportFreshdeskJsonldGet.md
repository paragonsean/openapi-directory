

# TransportFreshdeskJsonldGet

The TransportFreshdesk resource is a collection of transports that carry dispatched alerts to the external Freshdesk service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atContext** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  |  [optional] |
|**atId** | **String** |  |  [optional] [readonly] |
|**atType** | **String** |  |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**freshdeskApiKey** | **String** | The API key for the Freshdesk service. Stored in encrypted format. |  |
|**freshdeskEmail** | **String** | The requester email address for the Freshdesk service. |  |
|**freshdeskHost** | **String** | The host name for the Freshdesk service (domain.freshdesk.com). |  |
|**freshdeskPriority** | **String** | The ticket priority for the Freshdesk service. |  [optional] |
|**freshdeskType** | **String** | The ticket type for the Freshdesk service. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



