# VisualCrossingWeatherApi.TimelineWeatherAPISingleDateRequestApi

All URIs are relative to *https://weather.visualcrossing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**visualCrossingWebServicesRestServicesTimelineLocationStartdateGet**](TimelineWeatherAPISingleDateRequestApi.md#visualCrossingWebServicesRestServicesTimelineLocationStartdateGet) | **GET** /VisualCrossingWebServices/rest/services/timeline/{location}/{startdate} | Historical and Forecast Weather API



## visualCrossingWebServicesRestServicesTimelineLocationStartdateGet

> visualCrossingWebServicesRestServicesTimelineLocationStartdateGet(location, startdate, key, opts)

Historical and Forecast Weather API

Seamless access to daily and hourly historical and forecast weather data plus weather alerts, events and current conditions.

### Example

```javascript
import VisualCrossingWeatherApi from 'visual_crossing_weather_api';

let apiInstance = new VisualCrossingWeatherApi.TimelineWeatherAPISingleDateRequestApi();
let location = "London,UK"; // String | 
let startdate = "2022-02-01T00:00:00.000Z"; // String | 
let key = "INSERT_YOUR_KEY"; // String | 
let opts = {
  'contentType': "json", // String | data format of the output either json or CSV
  'unitGroup': "us", // String | 
  'include': "days", // String | data to include in the output (required for CSV format - days,hours,alerts,current,events )
  'lang': "us" // String | Language to use for weather descriptions
};
apiInstance.visualCrossingWebServicesRestServicesTimelineLocationStartdateGet(location, startdate, key, opts, (error, data, response) => {
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
 **location** | **String**|  | 
 **startdate** | **String**|  | 
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

