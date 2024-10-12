# AviationDataSystemsAirportsApiV1.AirportDetailsApi

All URIs are relative to *https://api.aviationdata.systems*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airportDetailsAirportNameSearch**](AirportDetailsApi.md#airportDetailsAirportNameSearch) | **GET** /v1/airport/name/{airport_name} | Search for airport by name



## airportDetailsAirportNameSearch

> AirportsAPIControllersAirportDetailsControllerResponse airportDetailsAirportNameSearch(airportName)

Search for airport by name

Required parameters: airport_name, api_mode

### Example

```javascript
import AviationDataSystemsAirportsApiV1 from 'aviation_data_systems_airports_api_v1';

let apiInstance = new AviationDataSystemsAirportsApiV1.AirportDetailsApi();
let airportName = "airportName_example"; // String | Required: The airports name
apiInstance.airportDetailsAirportNameSearch(airportName, (error, data, response) => {
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
 **airportName** | **String**| Required: The airports name | 

### Return type

[**AirportsAPIControllersAirportDetailsControllerResponse**](AirportsAPIControllersAirportDetailsControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

