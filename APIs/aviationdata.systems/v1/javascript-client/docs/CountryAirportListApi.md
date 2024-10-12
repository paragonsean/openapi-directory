# AviationDataSystemsAirportsApiV1.CountryAirportListApi

All URIs are relative to *https://api.aviationdata.systems*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countryAirportListCountryAirportList**](CountryAirportListApi.md#countryAirportListCountryAirportList) | **GET** /v1/country/code/{country_code} | Country airports. Returns a list of airports for a country code(ISO 3166-1 alpha-2 code)



## countryAirportListCountryAirportList

> AirportsAPIControllersCountryAirportListControllerAirportListResponse countryAirportListCountryAirportList(countryCode, airportServiceType)

Country airports. Returns a list of airports for a country code(ISO 3166-1 alpha-2 code)

Required parameters: country code (ISO 3166-1), airport_service_type.

### Example

```javascript
import AviationDataSystemsAirportsApiV1 from 'aviation_data_systems_airports_api_v1';

let apiInstance = new AviationDataSystemsAirportsApiV1.CountryAirportListApi();
let countryCode = "countryCode_example"; // String | Country code (ISO 3166-1). This can be found via /countries
let airportServiceType = "airportServiceType_example"; // String | Required: Needs to be: All, Scheduled or NonScheduled
apiInstance.countryAirportListCountryAirportList(countryCode, airportServiceType, (error, data, response) => {
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
 **countryCode** | **String**| Country code (ISO 3166-1). This can be found via /countries | 
 **airportServiceType** | **String**| Required: Needs to be: All, Scheduled or NonScheduled | 

### Return type

[**AirportsAPIControllersCountryAirportListControllerAirportListResponse**](AirportsAPIControllersCountryAirportListControllerAirportListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

