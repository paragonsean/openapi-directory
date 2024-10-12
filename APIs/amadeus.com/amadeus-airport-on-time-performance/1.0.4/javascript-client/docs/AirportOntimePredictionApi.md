# AirportOnTimePerformance.AirportOntimePredictionApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAirportOnTimePrediction**](AirportOntimePredictionApi.md#getAirportOnTimePrediction) | **GET** /airport/predictions/on-time | Returns a percentage of on-time flight departures from a given airport.



## getAirportOnTimePrediction

> Prediction getAirportOnTimePrediction(airportCode, date)

Returns a percentage of on-time flight departures from a given airport.

### Example

```javascript
import AirportOnTimePerformance from 'airport_on_time_performance';

let apiInstance = new AirportOnTimePerformance.AirportOntimePredictionApi();
let airportCode = "JFK"; // String | airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx), e.g. BOS for Boston
let date = new Date("2023-11-12"); // Date | the date on which the traveler will depart from the give airport. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25
apiInstance.getAirportOnTimePrediction(airportCode, date, (error, data, response) => {
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
 **airportCode** | **String**| airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx), e.g. BOS for Boston | 
 **date** | **Date**| the date on which the traveler will depart from the give airport. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2019-12-25 | 

### Return type

[**Prediction**](Prediction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

