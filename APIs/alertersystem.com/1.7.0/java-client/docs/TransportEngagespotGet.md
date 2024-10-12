

# TransportEngagespotGet

The TransportEngagespot resource is a collection of transports that carry dispatched alerts to the external EngageSpot service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When the resource instance was created. This date-time is in the UTC timezone. |  [optional] |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**engagespotApiKey** | **String** | The API key for the EngageSpot service. Stored in encrypted format. |  |
|**engagespotCampaignName** | **String** | The campaign name for the EngageSpot service. |  |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] [readonly] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**resourceOwner** | **String** | The name of the person who owns this resource. |  [optional] |
|**transportName** | **String** | The name of the transport. |  |



