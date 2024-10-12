# InterzoidCityDataStandardizationApi.CityDataStandardizationApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcitystandard**](CityDataStandardizationApi.md#getcitystandard) | **GET** /getcitystandard | Gets a city name standard for US and international cities



## getcitystandard

> Getcitystandard200Response getcitystandard(license, city)

Gets a city name standard for US and international cities

Gets a pre-selected city name standard for US and international cities for various permutations of a given city name.

### Example

```javascript
import InterzoidCityDataStandardizationApi from 'interzoid_city_data_standardization_api';

let apiInstance = new InterzoidCityDataStandardizationApi.CityDataStandardizationApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let city = "city_example"; // String | City name from which to retrieve the standardized version
apiInstance.getcitystandard(license, city, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **city** | **String**| City name from which to retrieve the standardized version | 

### Return type

[**Getcitystandard200Response**](Getcitystandard200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

