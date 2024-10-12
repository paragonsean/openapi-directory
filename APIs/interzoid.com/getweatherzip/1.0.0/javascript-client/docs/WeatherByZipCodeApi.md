# InterzoidGetWeatherByZipCodeApi.WeatherByZipCodeApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getweatherzipcode**](WeatherByZipCodeApi.md#getweatherzipcode) | **GET** /getweatherzipcode | Gets current weather information for a US zip code



## getweatherzipcode

> Getweatherzipcode200Response getweatherzipcode(license, zip)

Gets current weather information for a US zip code

Use a US zip code to retrieve current weather information

### Example

```javascript
import InterzoidGetWeatherByZipCodeApi from 'interzoid_get_weather_by_zip_code_api';

let apiInstance = new InterzoidGetWeatherByZipCodeApi.WeatherByZipCodeApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let zip = "zip_example"; // String | Zip code for weather information
apiInstance.getweatherzipcode(license, zip, (error, data, response) => {
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
 **zip** | **String**| Zip code for weather information | 

### Return type

[**Getweatherzipcode200Response**](Getweatherzipcode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

