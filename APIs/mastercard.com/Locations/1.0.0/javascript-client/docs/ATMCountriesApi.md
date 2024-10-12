# LocationsApi.ATMCountriesApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**atmsV1CountryGet**](ATMCountriesApi.md#atmsV1CountryGet) | **GET** /atms/v1/country | Returns countries with valid ATM locations.



## atmsV1CountryGet

> CountriesResponse atmsV1CountryGet()

Returns countries with valid ATM locations.

Returns countries with valid ATM locations. 

### Example

```javascript
import LocationsApi from 'locations_api';

let apiInstance = new LocationsApi.ATMCountriesApi();
apiInstance.atmsV1CountryGet((error, data, response) => {
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

[**CountriesResponse**](CountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

