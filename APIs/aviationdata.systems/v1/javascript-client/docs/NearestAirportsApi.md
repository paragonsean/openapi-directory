# AviationDataSystemsAirportsApiV1.NearestAirportsApi

All URIs are relative to *https://api.aviationdata.systems*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nearestAirportsNearestAirportList**](NearestAirportsApi.md#nearestAirportsNearestAirportList) | **GET** /v1/airport/nearest/{result_count}/{latitude}/{longitude} | Search for airports by location



## nearestAirportsNearestAirportList

> AirportsAPIControllersNearestAirportsControllerResponse nearestAirportsNearestAirportList(resultCount, latitude, longitude)

Search for airports by location

Required parameters: result_count, latitude, longitude, airport_service_type

### Example

```javascript
import AviationDataSystemsAirportsApiV1 from 'aviation_data_systems_airports_api_v1';

let apiInstance = new AviationDataSystemsAirportsApiV1.NearestAirportsApi();
let resultCount = 56; // Number | Required: Number of airports to return. Min: 1 Max: 20
let latitude = 3.4; // Number | Required: Latitude
let longitude = 3.4; // Number | Required: Longitude
apiInstance.nearestAirportsNearestAirportList(resultCount, latitude, longitude, (error, data, response) => {
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
 **resultCount** | **Number**| Required: Number of airports to return. Min: 1 Max: 20 | 
 **latitude** | **Number**| Required: Latitude | 
 **longitude** | **Number**| Required: Longitude | 

### Return type

[**AirportsAPIControllersNearestAirportsControllerResponse**](AirportsAPIControllersNearestAirportsControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

