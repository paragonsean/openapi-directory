# FlightMostTraveledDestinations.AirTrafficApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAirTraffic**](AirTrafficApi.md#getAirTraffic) | **GET** /travel/analytics/air-traffic/traveled | Returns a list of air traffic reports.



## getAirTraffic

> Success getAirTraffic(originCityCode, period, opts)

Returns a list of air traffic reports.

### Example

```javascript
import FlightMostTraveledDestinations from 'flight_most_traveled_destinations';

let apiInstance = new FlightMostTraveledDestinations.AirTrafficApi();
let originCityCode = "MAD"; // String | Code for the origin city following IATA standard ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). - e.g. BOS for Boston
let period = "2017-01"; // String | period when consumers are traveling. * It can be a month only.  * [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format must be used - e.g. 2015-05.  * Period ranges are not supported.  * Only periods from 2011-01 up to previous month are valid.  * Future dates are not supported. 
let opts = {
  'max': 10.0, // Number | maximum number of destinations in the response. Default value is **10** and maximum value is 50.
  'fields': "fields_example", // String | list of attributes desired in the response or list of attributes to remove from the response (with \"-\" before fields)  * The attributes names must contain the whole path (except resource name) e.g. travelers
  'pageLimit': 10, // Number | maximum items in one page
  'pageOffset': 0, // Number | start index of the requested page
  'sort': "'analytics.travelers.score'" // String | defines on which attribute the sorting will be done: * **analytics.flights.score** - sort destination by flights score (decreasing) * **analytics.travelers.score** - sort destination by traveler's score (decreasing) 
};
apiInstance.getAirTraffic(originCityCode, period, opts, (error, data, response) => {
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
 **originCityCode** | **String**| Code for the origin city following IATA standard ([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)). - e.g. BOS for Boston | 
 **period** | **String**| period when consumers are traveling. * It can be a month only.  * [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format must be used - e.g. 2015-05.  * Period ranges are not supported.  * Only periods from 2011-01 up to previous month are valid.  * Future dates are not supported.  | 
 **max** | **Number**| maximum number of destinations in the response. Default value is **10** and maximum value is 50. | [optional] [default to 10.0]
 **fields** | **String**| list of attributes desired in the response or list of attributes to remove from the response (with \&quot;-\&quot; before fields)  * The attributes names must contain the whole path (except resource name) e.g. travelers | [optional] 
 **pageLimit** | **Number**| maximum items in one page | [optional] [default to 10]
 **pageOffset** | **Number**| start index of the requested page | [optional] [default to 0]
 **sort** | **String**| defines on which attribute the sorting will be done: * **analytics.flights.score** - sort destination by flights score (decreasing) * **analytics.travelers.score** - sort destination by traveler&#39;s score (decreasing)  | [optional] [default to &#39;analytics.travelers.score&#39;]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

