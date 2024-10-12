

# PriceMissingCountDetails

The reasons that contributed to the price missing count and the total count for each reason.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidthDepletedCount** | **String** | No price was cached for this itinerary, and there was no live query quota remaining. |  [optional] |
|**cacheRateMissingCount** | **String** | No price exists in the cache for this itinerary. A live query was not done due to page constraints. |  [optional] |
|**itineraryBlockedCount** | **String** | The itinerary was outside of your basic parameters, so no price was pulled for the itinerary from either live query or cache fill. |  [optional] |
|**livePricingErrorCount** | **String** | No price was cached for this itinerary. A live query did not time out, but your system returned an error. |  [optional] |
|**livePricingNotSetupCount** | **String** | No price was cached for this itinerary, and live query was not configured for this account. |  [optional] |
|**livePricingTimeoutCount** | **String** | No price was cached for this itinerary, and a live query sent to your system timed out. |  [optional] |



