# VisualCrossingWeatherApi.WeatherForecastApi

All URIs are relative to *https://weather.visualcrossing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**visualCrossingWebServicesRestServicesWeatherdataForecastGet**](WeatherForecastApi.md#visualCrossingWebServicesRestServicesWeatherdataForecastGet) | **GET** /VisualCrossingWebServices/rest/services/weatherdata/forecast | Weather Forecast API



## visualCrossingWebServicesRestServicesWeatherdataForecastGet

> visualCrossingWebServicesRestServicesWeatherdataForecastGet(opts)

Weather Forecast API

Provides access to weather forecast information. The forecast is available for up to 15 days at the hourly, 12 hour and daily summary level.

### Example

```javascript
import VisualCrossingWeatherApi from 'visual_crossing_weather_api';

let apiInstance = new VisualCrossingWeatherApi.WeatherForecastApi();
let opts = {
  'sendAsDatasource': false, // Boolean | 
  'allowAsynch': false, // Boolean | 
  'shortColumnNames': false, // Boolean | 
  'locations': "Sterling%2C%20VA%2C%20US", // String | 
  'aggregateHours': "24", // String | 
  'contentType': "json", // String | 
  'unitGroup': "us", // String | 
  'key': "INSERT_YOUR_KEY" // String | 
};
apiInstance.visualCrossingWebServicesRestServicesWeatherdataForecastGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sendAsDatasource** | **Boolean**|  | [optional] 
 **allowAsynch** | **Boolean**|  | [optional] 
 **shortColumnNames** | **Boolean**|  | [optional] 
 **locations** | **String**|  | [optional] 
 **aggregateHours** | **String**|  | [optional] 
 **contentType** | **String**|  | [optional] 
 **unitGroup** | **String**|  | [optional] 
 **key** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

