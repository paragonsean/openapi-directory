

# TransportSpotHitPatch

The TransportSpotHit resource is a collection of transports that carry dispatched alerts to the external Spot-Hit service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**spotHitFrom** | **String** | The sender (3-11 letters, default is a 5 digits phone number) for the Spot-Hit service. |  |
|**spotHitToken** | **String** | The API token for the Spot-Hit service. Stored in encrypted format. |  |
|**transportName** | **String** | The name of the transport. |  |



