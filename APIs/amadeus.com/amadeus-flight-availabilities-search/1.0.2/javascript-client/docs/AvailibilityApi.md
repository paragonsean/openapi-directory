# FlightAvailibilitiesSearch.AvailibilityApi

All URIs are relative to *https://test.api.amadeus.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchFlightAvailabilities**](AvailibilityApi.md#searchFlightAvailabilities) | **POST** /shopping/availability/flight-availabilities | Return list of Flight Availabilities based on posted searching criteria.



## searchFlightAvailabilities

> SuccessAvailability searchFlightAvailabilities(xHTTPMethodOverride, getFlightAvailabilitiesBody)

Return list of Flight Availabilities based on posted searching criteria.

### Example

```javascript
import FlightAvailibilitiesSearch from 'flight_availibilities_search';

let apiInstance = new FlightAvailibilitiesSearch.AvailibilityApi();
let xHTTPMethodOverride = "'GET'"; // String | the HTTP method to apply
let getFlightAvailabilitiesBody = new FlightAvailibilitiesSearch.GetFlightAvailabilitiesQuery(); // GetFlightAvailabilitiesQuery | list of criteria to retrieve a list of flight availabilities
apiInstance.searchFlightAvailabilities(xHTTPMethodOverride, getFlightAvailabilitiesBody, (error, data, response) => {
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
 **xHTTPMethodOverride** | **String**| the HTTP method to apply | [default to &#39;GET&#39;]
 **getFlightAvailabilitiesBody** | [**GetFlightAvailabilitiesQuery**](GetFlightAvailabilitiesQuery.md)| list of criteria to retrieve a list of flight availabilities | 

### Return type

[**SuccessAvailability**](SuccessAvailability.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.amadeus+json
- **Accept**: application/vnd.amadeus+json

