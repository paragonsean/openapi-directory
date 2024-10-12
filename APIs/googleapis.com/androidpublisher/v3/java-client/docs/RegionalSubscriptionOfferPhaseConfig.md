

# RegionalSubscriptionOfferPhaseConfig

Configuration for a single phase of a subscription offer in a single region.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**absoluteDiscount** | [**Money**](Money.md) |  |  [optional] |
|**price** | [**Money**](Money.md) |  |  [optional] |
|**regionCode** | **String** | Required. Immutable. The region to which this config applies. |  [optional] |
|**relativeDiscount** | **Double** | The fraction of the base plan price prorated over the phase duration that the user pays for this offer phase. For example, if the base plan price for this region is $12 for a period of 1 year, then a 50% discount for a phase of a duration of 3 months would correspond to a price of $1.50. The discount must be specified as a fraction strictly larger than 0 and strictly smaller than 1. The resulting price will be rounded to the nearest billable unit (e.g. cents for USD). The relative discount is considered invalid if the discounted price ends up being smaller than the minimum price allowed in this region. |  [optional] |



