# Airportsapi.DefaultApi

All URIs are relative to *https://airport-web.appspot.com/_ah/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airportApiGetAirport**](DefaultApi.md#airportApiGetAirport) | **GET** /airportsapi/v1/airports/{icao_code} | 



## airportApiGetAirport

> ApiEndpointsAirportResponse airportApiGetAirport(icaoCode)



### Example

```javascript
import Airportsapi from 'airportsapi';

let apiInstance = new Airportsapi.DefaultApi();
let icaoCode = "icaoCode_example"; // String | 
apiInstance.airportApiGetAirport(icaoCode, (error, data, response) => {
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
 **icaoCode** | **String**|  | 

### Return type

[**ApiEndpointsAirportResponse**](ApiEndpointsAirportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

