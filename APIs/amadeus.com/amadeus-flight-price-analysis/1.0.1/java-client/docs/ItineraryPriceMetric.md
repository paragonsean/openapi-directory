

# ItineraryPriceMetric

price metric

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | currency of the prices.  Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro |  [optional] |
|**departureDate** | **String** | The date on which the traveler will depart from the origin to go to the destination.   Dates are specified in the[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format. |  [optional] |
|**destination** | [**Location**](Location.md) |  |  [optional] |
|**oneWay** | **Boolean** | true for a one way trip, false for a round trip |  [optional] |
|**origin** | [**Location**](Location.md) |  |  [optional] |
|**priceMetrics** | [**List&lt;ItineraryPriceMetricPriceMetricsInner&gt;**](ItineraryPriceMetricPriceMetricsInner.md) |  |  [optional] |
|**transportType** | [**TransportTypeEnum**](#TransportTypeEnum) | transportation type |  [optional] |
|**type** | **String** | ressource type - always price-metrics |  [optional] |



## Enum: TransportTypeEnum

| Name | Value |
|---- | -----|
| FLIGHT | &quot;FLIGHT&quot; |



