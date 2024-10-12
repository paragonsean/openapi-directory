# WeatherbitInteractiveSwaggerUiDocumentation.ForecastDegreeDayAPIApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecastEnergylatlatlonlonGet**](ForecastDegreeDayAPIApi.md#forecastEnergylatlatlonlonGet) | **GET** /forecast/energy?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Energy Forecast API response  - Given a single lat/lon. 



## forecastEnergylatlatlonlonGet

> EnergyObsGroupForecast forecastEnergylatlatlonlonGet(lat, lon, key, opts)

Returns Energy Forecast API response  - Given a single lat/lon. 

Retrieve an 8 day forecast relevant to te Energy Sector (degree days, solar radiation, precipitation, wind).

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.ForecastDegreeDayAPIApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'threshold': 3.4, // Number | Temperature threshold to use to calculate degree days (default 18 C) 
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'tp': "tp_example", // String | Time period (default: daily)
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.forecastEnergylatlatlonlonGet(lat, lon, key, opts, (error, data, response) => {
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
 **threshold** | **Number**| Temperature threshold to use to calculate degree days (default 18 C)  | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **tp** | **String**| Time period (default: daily) | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**EnergyObsGroupForecast**](EnergyObsGroupForecast.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

