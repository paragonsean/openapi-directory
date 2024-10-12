# OpenUvGlobalRealTimeUvIndexForecastApi.DefaultApi

All URIs are relative to *https://api.openuv.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecastGet**](DefaultApi.md#forecastGet) | **GET** /forecast | 
[**protectionGet**](DefaultApi.md#protectionGet) | **GET** /protection | 
[**uvGet**](DefaultApi.md#uvGet) | **GET** /uv | 



## forecastGet

> [Array] forecastGet(lat, lng, xAccessToken, opts)



Get hourly UV Index Forecast by location and date. Optional altitude, ozone level and datetime could be provided.

### Example

```javascript
import OpenUvGlobalRealTimeUvIndexForecastApi from 'open_uv_global_real_time_uv_index_forecast_api';

let apiInstance = new OpenUvGlobalRealTimeUvIndexForecastApi.DefaultApi();
let lat = 78.67; // Number | latitude, from -90.00 to 90.00
let lng = 115.67; // Number | longitude, from -180.00 to 180.00
let xAccessToken = "xAccessToken_example"; // String | This header is used to send data that contains your OpenUV API key
let opts = {
  'alt': 1050, // Number | Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
  'ozone': 304.5, // Number | Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
  'dt': new Date("2018-02-04T04:39:06.467Z") // Date | UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time.
};
apiInstance.forecastGet(lat, lng, xAccessToken, opts, (error, data, response) => {
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
 **lat** | **Number**| latitude, from -90.00 to 90.00 | 
 **lng** | **Number**| longitude, from -180.00 to 180.00 | 
 **xAccessToken** | **String**| This header is used to send data that contains your OpenUV API key | 
 **alt** | **Number**| Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. | [optional] 
 **ozone** | **Number**| Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. | [optional] 
 **dt** | **Date**| UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. | [optional] 

### Return type

**[Array]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protectionGet

> ProtectionResult protectionGet(lat, lng, from, to, xAccessToken, opts)



Get daily protection time by location, UV Index from and UV Index to with 10 minutes accuracy. Optional altitide and ozone level could be provided.

### Example

```javascript
import OpenUvGlobalRealTimeUvIndexForecastApi from 'open_uv_global_real_time_uv_index_forecast_api';

let apiInstance = new OpenUvGlobalRealTimeUvIndexForecastApi.DefaultApi();
let lat = 78.67; // Number | latitude, from -90.00 to 90.00
let lng = 115.67; // Number | longitude, from -180.00 to 180.00
let from = 2.5; // Number | UV Index from value for protection datetime lookup. From 0 to 40.
let to = 3.6; // Number | UV Index to value for protection datetime lookup. From 0 to 40.
let xAccessToken = "xAccessToken_example"; // String | This header is used to send data that contains your OpenUV API key
let opts = {
  'alt': 1050, // Number | Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
  'ozone': 304.5 // Number | Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
};
apiInstance.protectionGet(lat, lng, from, to, xAccessToken, opts, (error, data, response) => {
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
 **lat** | **Number**| latitude, from -90.00 to 90.00 | 
 **lng** | **Number**| longitude, from -180.00 to 180.00 | 
 **from** | **Number**| UV Index from value for protection datetime lookup. From 0 to 40. | 
 **to** | **Number**| UV Index to value for protection datetime lookup. From 0 to 40. | 
 **xAccessToken** | **String**| This header is used to send data that contains your OpenUV API key | 
 **alt** | **Number**| Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. | [optional] 
 **ozone** | **Number**| Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. | [optional] 

### Return type

[**ProtectionResult**](ProtectionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uvGet

> UvIndexResult uvGet(lat, lng, xAccessToken, opts)



Get real-time UV Index by location. Optional altitude, ozone level and datetime could be provided.

### Example

```javascript
import OpenUvGlobalRealTimeUvIndexForecastApi from 'open_uv_global_real_time_uv_index_forecast_api';

let apiInstance = new OpenUvGlobalRealTimeUvIndexForecastApi.DefaultApi();
let lat = 78.67; // Number | latitude, from -90.00 to 90.00
let lng = 115.67; // Number | longitude, from -180.00 to 180.00
let xAccessToken = "xAccessToken_example"; // String | This header is used to send data that contains your OpenUV API key
let opts = {
  'alt': 1050, // Number | Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
  'ozone': 304.5, // Number | Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
  'dt': new Date("2018-02-04T04:39:06.467Z") // Date | UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time.
};
apiInstance.uvGet(lat, lng, xAccessToken, opts, (error, data, response) => {
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
 **lat** | **Number**| latitude, from -90.00 to 90.00 | 
 **lng** | **Number**| longitude, from -180.00 to 180.00 | 
 **xAccessToken** | **String**| This header is used to send data that contains your OpenUV API key | 
 **alt** | **Number**| Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. | [optional] 
 **ozone** | **Number**| Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. | [optional] 
 **dt** | **Date**| UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. | [optional] 

### Return type

[**UvIndexResult**](UvIndexResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

