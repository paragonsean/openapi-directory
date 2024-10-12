

# ReservationRecommendationProperties

The properties of the reservation recommendation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costWithNoReservedInstances** | **BigDecimal** | The total amount of cost without reserved instances. |  [optional] [readonly] |
|**firstUsageDate** | **OffsetDateTime** | The usage date for looking back. |  [optional] [readonly] |
|**lookBackPeriod** | **String** | The number of days of usage to look back for recommendation. |  [optional] [readonly] |
|**meterId** | **UUID** | The meter id (GUID) |  [optional] [readonly] |
|**netSavings** | **BigDecimal** | Total estimated savings with reserved instances. |  [optional] [readonly] |
|**recommendedQuantity** | **BigDecimal** | Recommended quality for reserved instances. |  [optional] [readonly] |
|**scope** | **String** | Shared or single recommendation. |  [optional] [readonly] |
|**term** | **String** | RI recommendations in one or three year terms. |  [optional] [readonly] |
|**totalCostWithReservedInstances** | **BigDecimal** | The total amount of cost with reserved instances. |  [optional] [readonly] |



