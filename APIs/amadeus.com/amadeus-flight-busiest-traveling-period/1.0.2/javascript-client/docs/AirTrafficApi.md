# FlightBusiestTravelingPeriod.AirTrafficApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAirTraffic**](AirTrafficApi.md#getAirTraffic) | **GET** /travel/analytics/air-traffic/busiest-period | Returns a list of air traffic reports.



## getAirTraffic

> Success getAirTraffic(cityCode, period, opts)

Returns a list of air traffic reports.

### Example

```javascript
import FlightBusiestTravelingPeriod from 'flight_busiest_traveling_period';

let apiInstance = new FlightBusiestTravelingPeriod.AirTrafficApi();
let cityCode = "MAD"; // String | Code for the city following IATA standard. [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. BOS for Boston
let period = "2017"; // String | time period (year) of the statistics.  Year for which the statistic are requested following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 
let opts = {
  'direction': "ARRIVING" // String | Use ARRIVING to have statistics on travelers coming to the city or DEPARTING for statistics on travelers leaving the city.  By default, statistics are given on travelers ARRIVING the city. 
};
apiInstance.getAirTraffic(cityCode, period, opts, (error, data, response) => {
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
 **cityCode** | **String**| Code for the city following IATA standard. [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. BOS for Boston | 
 **period** | **String**| time period (year) of the statistics.  Year for which the statistic are requested following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)  | 
 **direction** | **String**| Use ARRIVING to have statistics on travelers coming to the city or DEPARTING for statistics on travelers leaving the city.  By default, statistics are given on travelers ARRIVING the city.  | [optional] [default to &#39;ARRIVING&#39;]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

