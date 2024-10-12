# VisualCrossingWeatherApi.TimelineWeatherAPI15DayForecastRequestApi

All URIs are relative to *https://weather.visualcrossing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**visualCrossingWebServicesRestServicesTimelineLocationGet**](TimelineWeatherAPI15DayForecastRequestApi.md#visualCrossingWebServicesRestServicesTimelineLocationGet) | **GET** /VisualCrossingWebServices/rest/services/timeline/{location} | Historical and Forecast Weather API



## visualCrossingWebServicesRestServicesTimelineLocationGet

> visualCrossingWebServicesRestServicesTimelineLocationGet(location, key, opts)

Historical and Forecast Weather API

Seamless access to daily and hourly historical and forecast weather data plus weather alerts, events and current conditions.

### Example

```javascript
import VisualCrossingWeatherApi from 'visual_crossing_weather_api';

let apiInstance = new VisualCrossingWeatherApi.TimelineWeatherAPI15DayForecastRequestApi();
let location = "London,UK"; // String | Locaton of interest as an address, partial address or decimal latitude,longtude value
let key = "INSERT_YOUR_KEY"; // String | 
let opts = {
  'contentType': "json", // String | data format of the output either json or CSV
  'unitGroup': "us", // String | 
  'include': "days", // String | data to include in the output (required for CSV format - days,hours,alerts,current,events )
  'lang': "us" // String | Language to use for weather descriptions
};
apiInstance.visualCrossingWebServicesRestServicesTimelineLocationGet(location, key, opts, (error, data, response) => {
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
 **location** | **String**| Locaton of interest as an address, partial address or decimal latitude,longtude value | 
 **key** | **String**|  | 
 **contentType** | **String**| data format of the output either json or CSV | [optional] 
 **unitGroup** | **String**|  | [optional] 
 **include** | **String**| data to include in the output (required for CSV format - days,hours,alerts,current,events ) | [optional] 
 **lang** | **String**| Language to use for weather descriptions | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

