# LocationsApi.ATMCountrySubdivisionsApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**atmsV1CountrysubdivisionGet**](ATMCountrySubdivisionsApi.md#atmsV1CountrysubdivisionGet) | **GET** /atms/v1/countrysubdivision | Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada.



## atmsV1CountrysubdivisionGet

> CountrySubdivisionResponse atmsV1CountrysubdivisionGet(country)

Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada.

Returns country subdivisions that have ATM locations.  A country subdivision is a segment within a country (ex  state or province). Country subdivisions are only available for the US and Canada. 

### Example

```javascript
import LocationsApi from 'locations_api';

let apiInstance = new LocationsApi.ATMCountrySubdivisionsApi();
let country = "USA"; // String | Any three digit country code as defined in ISO 3166-1.  \"USA\" or \"CAN\"
apiInstance.atmsV1CountrysubdivisionGet(country, (error, data, response) => {
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
 **country** | **String**| Any three digit country code as defined in ISO 3166-1.  \&quot;USA\&quot; or \&quot;CAN\&quot; | 

### Return type

[**CountrySubdivisionResponse**](CountrySubdivisionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

