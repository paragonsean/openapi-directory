# WeatherbitInteractiveSwaggerUiDocumentation.AlertsApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertslatlatlonlonGet**](AlertsApi.md#alertslatlatlonlonGet) | **GET** /alerts?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.



## alertslatlatlonlonGet

> WeatherAlert alertslatlatlonlonGet(lat, lon, key, opts)

Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.

Returns severe weather alerts issued by meteorological agencies - given a lat, and a lon.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.AlertsApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'callback': "callback_example" // String | Wraps return in jsonp callback - Example - callback=func
};
apiInstance.alertslatlatlonlonGet(lat, lon, key, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude component of location. | 
 **lon** | **Number**| Longitude component of location. | 
 **key** | **String**| Your registered API key. | 
 **callback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] 

### Return type

[**WeatherAlert**](WeatherAlert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

