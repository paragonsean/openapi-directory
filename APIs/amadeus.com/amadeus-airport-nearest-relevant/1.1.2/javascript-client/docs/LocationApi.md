# AirportNearestRelevant.LocationApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNearestRelevantAirports**](LocationApi.md#getNearestRelevantAirports) | **GET** /reference-data/locations/airports | Returns a list of relevant airports near to a given point.



## getNearestRelevantAirports

> Success getNearestRelevantAirports(latitude, longitude, opts)

Returns a list of relevant airports near to a given point.

### Example

```javascript
import AirportNearestRelevant from 'airport_nearest_relevant';

let apiInstance = new AirportNearestRelevant.LocationApi();
let latitude = 51.57285; // Number | latitude location to be at the center of the search circle
let longitude = -0.44161; // Number | longitude location to be at the center of the search circle
let opts = {
  'radius': 500, // Number | radius of the search in Kilometer. Can be from 0 to 500, default value is 500 Km.
  'pageLimit': 10, // Number | maximum items in one page
  'pageOffset': 0, // Number | start index of the requested page
  'sort': "'relevance'" // String | defines on which attribute the sorting will be done from the best option to the worst one: * **relevance** - Score value calculated based on distance and traffic analytics * **distance** - Distance from the location to the geo-code given in API request parameters * **analytics.flights.score** - Approximate score for ranking purposes calculated based on estimated number of flights from/to airport in one reference year (last year) * **analytics.travelers.score** - Approximate score for ranking purposes calculated based on estimated number of travelers in the airport for one reference year (last year) 
};
apiInstance.getNearestRelevantAirports(latitude, longitude, opts, (error, data, response) => {
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
 **latitude** | **Number**| latitude location to be at the center of the search circle | 
 **longitude** | **Number**| longitude location to be at the center of the search circle | 
 **radius** | **Number**| radius of the search in Kilometer. Can be from 0 to 500, default value is 500 Km. | [optional] [default to 500]
 **pageLimit** | **Number**| maximum items in one page | [optional] [default to 10]
 **pageOffset** | **Number**| start index of the requested page | [optional] [default to 0]
 **sort** | **String**| defines on which attribute the sorting will be done from the best option to the worst one: * **relevance** - Score value calculated based on distance and traffic analytics * **distance** - Distance from the location to the geo-code given in API request parameters * **analytics.flights.score** - Approximate score for ranking purposes calculated based on estimated number of flights from/to airport in one reference year (last year) * **analytics.travelers.score** - Approximate score for ranking purposes calculated based on estimated number of travelers in the airport for one reference year (last year)  | [optional] [default to &#39;relevance&#39;]

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.amadeus+json

