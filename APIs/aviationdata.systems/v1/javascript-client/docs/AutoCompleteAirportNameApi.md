# AviationDataSystemsAirportsApiV1.AutoCompleteAirportNameApi

All URIs are relative to *https://api.aviationdata.systems*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoCompleteAirportNameAirportNameSearch**](AutoCompleteAirportNameApi.md#autoCompleteAirportNameAirportNameSearch) | **GET** /v1/airport/autocomplete/{airport_name} | Autocomplete airport names. Returns a maximum of 10 airport names.



## autoCompleteAirportNameAirportNameSearch

> AirportsAPIControllersAutoCompleteAirportNameControllerResponse autoCompleteAirportNameAirportNameSearch(airportName, airportServiceType, opts)

Autocomplete airport names. Returns a maximum of 10 airport names.

Required parameters: airport_name, airport_service_type. Optional parameter: country code (ISO 3166-1).

### Example

```javascript
import AviationDataSystemsAirportsApiV1 from 'aviation_data_systems_airports_api_v1';

let apiInstance = new AviationDataSystemsAirportsApiV1.AutoCompleteAirportNameApi();
let airportName = "airportName_example"; // String | Required: The airports name
let airportServiceType = "airportServiceType_example"; // String | Required: Needs to be: All, Scheduled or NonScheduled
let opts = {
  'optionalCountryCode': "optionalCountryCode_example" // String | Optional: Country code (ISO 3166-1). This can be found via /countries
};
apiInstance.autoCompleteAirportNameAirportNameSearch(airportName, airportServiceType, opts, (error, data, response) => {
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
 **airportServiceType** | **String**| Required: Needs to be: All, Scheduled or NonScheduled | 
 **optionalCountryCode** | **String**| Optional: Country code (ISO 3166-1). This can be found via /countries | [optional] 

### Return type

[**AirportsAPIControllersAutoCompleteAirportNameControllerResponse**](AirportsAPIControllersAutoCompleteAirportNameControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

