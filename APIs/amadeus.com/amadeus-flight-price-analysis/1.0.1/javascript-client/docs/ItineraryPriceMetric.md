# FlightPriceAnalysisApi.ItineraryPriceMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyCode** | **String** | currency of the prices.  Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro | [optional] 
**departureDate** | **String** | The date on which the traveler will depart from the origin to go to the destination.   Dates are specified in the[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format. | [optional] 
**destination** | [**Location**](Location.md) |  | [optional] 
**oneWay** | **Boolean** | true for a one way trip, false for a round trip | [optional] 
**origin** | [**Location**](Location.md) |  | [optional] 
**priceMetrics** | [**[ItineraryPriceMetricPriceMetricsInner]**](ItineraryPriceMetricPriceMetricsInner.md) |  | [optional] 
**transportType** | **String** | transportation type | [optional] 
**type** | **String** | ressource type - always price-metrics | [optional] 



## Enum: TransportTypeEnum


* `FLIGHT` (value: `"FLIGHT"`)




