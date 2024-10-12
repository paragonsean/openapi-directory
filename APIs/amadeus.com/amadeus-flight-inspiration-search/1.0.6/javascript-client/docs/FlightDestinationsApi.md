# FlightInspirationSearch.FlightDestinationsApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFlightDestinations**](FlightDestinationsApi.md#getFlightDestinations) | **GET** /shopping/flight-destinations | Find the cheapest destinations where you can fly to.



## getFlightDestinations

> FlightDestinations getFlightDestinations(origin, opts)

Find the cheapest destinations where you can fly to.

### Example

```javascript
import FlightInspirationSearch from 'flight_inspiration_search';

let apiInstance = new FlightInspirationSearch.FlightDestinationsApi();
let origin = "MAD"; // String | IATA code of the city from which the flight will depart  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MAD for Madrid 
let opts = {
  'departureDate': "departureDate_example", // String | The date, or range of dates, on which the flight will depart from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25.   Ranges are specified with a comma and are inclusive  Departure date can not be more than 180 days in the future. 
  'oneWay': false, // Boolean | if this parameter is set to true, only one-way flights are considered. If this parameter is not set or set to false, only round-trip flights are considered
  'duration': "duration_example", // String | Exact duration or range of durations of the travel, in days.  This parameter must not be set if oneWay is true.   Ranges are specified with a comma and are inclusive, e.g. 2,8  Duration can not be lower than 1 days or higher than 15 days 
  'nonStop': false, // Boolean | if this parameter is set to true, only flights going from the origin to the destination with no stop in-between are considered
  'maxPrice': 789, // Number | defines the price limit for each offer returned. The value should be a positive number, without decimals
  'viewBy': "viewBy_example" // String | view the flight destinations by DATE, DESTINATION, DURATION, WEEK, or COUNTRY. View by DATE (default when oneWay is true) to get the cheapest flight destination for every departure date in the given range. View by DURATION (default when oneWay is false) to get the cheapest flight destination for every departure date and for every duration in the given ranges. View by WEEK to get the cheapest flight destination for every week in the given range of departure dates. View by COUNTRY to get the cheapest flight destination by country. Note that specifying a detailed view but large ranges may result in a huge number of flight destinations being returned. For some very large numbers of flight destinations, the API may refuse to provide a response
};
apiInstance.getFlightDestinations(origin, opts, (error, data, response) => {
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
 **origin** | **String**| IATA code of the city from which the flight will depart  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. MAD for Madrid  | 
 **departureDate** | **String**| The date, or range of dates, on which the flight will depart from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25.   Ranges are specified with a comma and are inclusive  Departure date can not be more than 180 days in the future.  | [optional] 
 **oneWay** | **Boolean**| if this parameter is set to true, only one-way flights are considered. If this parameter is not set or set to false, only round-trip flights are considered | [optional] [default to false]
 **duration** | **String**| Exact duration or range of durations of the travel, in days.  This parameter must not be set if oneWay is true.   Ranges are specified with a comma and are inclusive, e.g. 2,8  Duration can not be lower than 1 days or higher than 15 days  | [optional] 
 **nonStop** | **Boolean**| if this parameter is set to true, only flights going from the origin to the destination with no stop in-between are considered | [optional] [default to false]
 **maxPrice** | **Number**| defines the price limit for each offer returned. The value should be a positive number, without decimals | [optional] 
 **viewBy** | **String**| view the flight destinations by DATE, DESTINATION, DURATION, WEEK, or COUNTRY. View by DATE (default when oneWay is true) to get the cheapest flight destination for every departure date in the given range. View by DURATION (default when oneWay is false) to get the cheapest flight destination for every departure date and for every duration in the given ranges. View by WEEK to get the cheapest flight destination for every week in the given range of departure dates. View by COUNTRY to get the cheapest flight destination by country. Note that specifying a detailed view but large ranges may result in a huge number of flight destinations being returned. For some very large numbers of flight destinations, the API may refuse to provide a response | [optional] 

### Return type

[**FlightDestinations**](FlightDestinations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json, application/json

