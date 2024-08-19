# WeatherbitInteractiveSwaggerUiDocumentation.HistoricalDegreeDayAPIApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**historyEnergylatlatlonlonGet**](HistoricalDegreeDayAPIApi.md#historyEnergylatlatlonlonGet) | **GET** /history/energy?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Energy API response  - Given a single lat/lon. 



## historyEnergylatlatlonlonGet

> EnergyObsGroup historyEnergylatlatlonlonGet(lat, lon, startDate, endDate, key, opts)

Returns Energy API response  - Given a single lat/lon. 

Returns aggregate energy specific historical weather fields, over a specified time period.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HistoricalDegreeDayAPIApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
let endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'tp': "tp_example", // String | Time period to aggregate by (daily, monthly)
  'threshold': 3.4, // Number | Temperature threshold to use to calculate degree days (default 18 C) 
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.historyEnergylatlatlonlonGet(lat, lon, startDate, endDate, key, opts, (error, data, response) => {
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
 **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | 
 **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | 
 **key** | **String**| Your registered API key. | 
 **tp** | **String**| Time period to aggregate by (daily, monthly) | [optional] 
 **threshold** | **Number**| Temperature threshold to use to calculate degree days (default 18 C)  | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**EnergyObsGroup**](EnergyObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

