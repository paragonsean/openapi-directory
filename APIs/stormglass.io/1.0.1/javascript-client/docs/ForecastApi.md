# StormGlassMarineWeather.ForecastApi

All URIs are relative to *https://api.stormglass.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getForecast**](ForecastApi.md#getForecast) | **GET** /forecast | Get hourly forecasts by coordinates



## getForecast

> Forecast getForecast(lat, lng)

Get hourly forecasts by coordinates

Get forecast info for the given coordinates. For every hour and property, you will get a list of weather sources and their values.

### Example

```javascript
import StormGlassMarineWeather from 'storm_glass_marine_weather';
let defaultClient = StormGlassMarineWeather.ApiClient.instance;
// Configure API key authorization: authenticationToken
let authenticationToken = defaultClient.authentications['authenticationToken'];
authenticationToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//authenticationToken.apiKeyPrefix = 'Token';

let apiInstance = new StormGlassMarineWeather.ForecastApi();
let lat = 3.4; // Number | The latitude for a location. Valid input is a number between -90 and 90.
let lng = 3.4; // Number | The longitude for a location. Valid input is a number between -180 and 180.
apiInstance.getForecast(lat, lng, (error, data, response) => {
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
 **lat** | **Number**| The latitude for a location. Valid input is a number between -90 and 90. | 
 **lng** | **Number**| The longitude for a location. Valid input is a number between -180 and 180. | 

### Return type

[**Forecast**](Forecast.md)

### Authorization

[authenticationToken](../README.md#authenticationToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

