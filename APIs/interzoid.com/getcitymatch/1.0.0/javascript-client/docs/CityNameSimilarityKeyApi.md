# InterzoidGetCityMatchSimilarityKeyApi.CityNameSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcitymatch**](CityNameSimilarityKeyApi.md#getcitymatch) | **GET** /getcitymatch | Gets a similarity key for matching purposes for city name data



## getcitymatch

> Getcitymatch200Response getcitymatch(license, city)

Gets a similarity key for matching purposes for city name data

Gets a similarity key for matching purposes for city name data.

### Example

```javascript
import InterzoidGetCityMatchSimilarityKeyApi from 'interzoid_get_city_match_similarity_key_api';

let apiInstance = new InterzoidGetCityMatchSimilarityKeyApi.CityNameSimilarityKeyApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let city = "city_example"; // String | City name from which to generate similarity key
apiInstance.getcitymatch(license, city, (error, data, response) => {
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
 **city** | **String**| City name from which to generate similarity key | 

### Return type

[**Getcitymatch200Response**](Getcitymatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

