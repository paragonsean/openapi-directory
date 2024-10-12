# AviationDataSystemsAirportsApiV1.AirportIATAApi

All URIs are relative to *https://api.aviationdata.systems*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airportIATAAirportIATASearch**](AirportIATAApi.md#airportIATAAirportIATASearch) | **GET** /v1/airport/iata/{airport_iata} | Search for airport by IATA code



## airportIATAAirportIATASearch

> AirportsAPIControllersAirportIATAControllerResponse airportIATAAirportIATASearch(airportIata)

Search for airport by IATA code

Required parameters: airport_iata

### Example

```javascript
import AviationDataSystemsAirportsApiV1 from 'aviation_data_systems_airports_api_v1';

let apiInstance = new AviationDataSystemsAirportsApiV1.AirportIATAApi();
let airportIata = "airportIata_example"; // String | Required: The airports IATA code
apiInstance.airportIATAAirportIATASearch(airportIata, (error, data, response) => {
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
 **airportIata** | **String**| Required: The airports IATA code | 

### Return type

[**AirportsAPIControllersAirportIATAControllerResponse**](AirportsAPIControllersAirportIATAControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

