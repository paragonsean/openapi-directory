# FlightPriceAnalysisApi.PriceMetricsApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getItineraryPriceMetrics**](PriceMetricsApi.md#getItineraryPriceMetrics) | **GET** /analytics/itinerary-price-metrics | GET itinerary price metric



## getItineraryPriceMetrics

> GetItineraryPriceMetrics200Response getItineraryPriceMetrics(originIataCode, destinationIataCode, departureDate, opts)

GET itinerary price metric



### Example

```javascript
import FlightPriceAnalysisApi from 'flight_price_analysis_api';

let apiInstance = new FlightPriceAnalysisApi.PriceMetricsApi();
let originIataCode = "MAD"; // String | airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), from which the traveler will depart 
let destinationIataCode = "CDG"; // String | airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), to which the traveler is going.
let departureDate = "2021-03-21"; // String | The date on which the traveler will depart from the origin to go to the destination.   Dates are specified in the[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format.
let opts = {
  'currencyCode': "'EUR'", // String | the preferred currency for display. Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro
  'oneWay': false // Boolean | true to get price metrics for a one way trip, false to get price metrics for a round trip
};
apiInstance.getItineraryPriceMetrics(originIataCode, destinationIataCode, departureDate, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **originIataCode** | **String**| airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), from which the traveler will depart  | 
 **destinationIataCode** | **String**| airport code, following [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx), to which the traveler is going. | 
 **departureDate** | **String**| The date on which the traveler will depart from the origin to go to the destination.   Dates are specified in the[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format. | 
 **currencyCode** | **String**| the preferred currency for display. Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro | [optional] [default to &#39;EUR&#39;]
 **oneWay** | **Boolean**| true to get price metrics for a one way trip, false to get price metrics for a round trip | [optional] [default to false]

### Return type

[**GetItineraryPriceMetrics200Response**](GetItineraryPriceMetrics200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

