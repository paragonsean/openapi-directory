# InterzoidGetWeatherCityApi.WeatherByCityAndStateApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getweather**](WeatherByCityAndStateApi.md#getweather) | **GET** /getweather | Gets current weather information for a US city and state



## getweather

> Getweather200Response getweather(license, city, state)

Gets current weather information for a US city and state

Use city and state to retrieve current US weather information.

### Example

```javascript
import InterzoidGetWeatherCityApi from 'interzoid_get_weather_city_api';

let apiInstance = new InterzoidGetWeatherCityApi.WeatherByCityAndStateApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let city = "city_example"; // String | City for weather information
let state = "state_example"; // String | State for weather information
apiInstance.getweather(license, city, state, (error, data, response) => {
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
 **city** | **String**| City for weather information | 
 **state** | **String**| State for weather information | 

### Return type

[**Getweather200Response**](Getweather200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

