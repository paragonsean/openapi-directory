# AviationDataSystemsAirportsApiV1.CountryListApi

All URIs are relative to *https://api.aviationdata.systems*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countryListCountryAirportList**](CountryListApi.md#countryListCountryAirportList) | **GET** /v1/country_list | Country list. Returns a list of countries where airport data is available



## countryListCountryAirportList

> AirportsAPIControllersCountryListControllerCountryListResponse countryListCountryAirportList()

Country list. Returns a list of countries where airport data is available

### Example

```javascript
import AviationDataSystemsAirportsApiV1 from 'aviation_data_systems_airports_api_v1';

let apiInstance = new AviationDataSystemsAirportsApiV1.CountryListApi();
apiInstance.countryListCountryAirportList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AirportsAPIControllersCountryListControllerCountryListResponse**](AirportsAPIControllersCountryListControllerCountryListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

