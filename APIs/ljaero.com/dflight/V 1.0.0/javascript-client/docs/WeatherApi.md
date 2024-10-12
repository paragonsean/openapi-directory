# DFlightApi.WeatherApi

All URIs are relative to *https://dflight-api.ljaero.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wxByDistanceUsV1WxForecastDistanceQueryPost**](WeatherApi.md#wxByDistanceUsV1WxForecastDistanceQueryPost) | **POST** /us/v1/wx-forecast/distance-query | Retrieve forecast values within given distance of location for all requested weather elements and time periods.
[**wxByPolyUsV1WxForecastPolygonQueryPost**](WeatherApi.md#wxByPolyUsV1WxForecastPolygonQueryPost) | **POST** /us/v1/wx-forecast/polygon-query | Retrieve forecast values within given GeoJSON polygon for all requested weather elements and time periods.
[**wxByRouteUsV1WxForecastRouteQueryPost**](WeatherApi.md#wxByRouteUsV1WxForecastRouteQueryPost) | **POST** /us/v1/wx-forecast/route-query | Retrieve forecast values along a route for all requested weather elements and time periods.



## wxByDistanceUsV1WxForecastDistanceQueryPost

> WxDistanceResponse wxByDistanceUsV1WxForecastDistanceQueryPost(wxByDistance, opts)

Retrieve forecast values within given distance of location for all requested weather elements and time periods.

Retrieve forecast values for selected weather elements and time period. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000) * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.WeatherApi();
let wxByDistance = new DFlightApi.WxByDistance(); // WxByDistance | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.wxByDistanceUsV1WxForecastDistanceQueryPost(wxByDistance, opts, (error, data, response) => {
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
 **wxByDistance** | [**WxByDistance**](WxByDistance.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**WxDistanceResponse**](WxDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wxByPolyUsV1WxForecastPolygonQueryPost

> WxPolyResponse wxByPolyUsV1WxForecastPolygonQueryPost(wxByPolygon, opts)

Retrieve forecast values within given GeoJSON polygon for all requested weather elements and time periods.

Retrieve forecast values located within given area for requested weather elements and time period. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2. * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.WeatherApi();
let wxByPolygon = new DFlightApi.WxByPolygon(); // WxByPolygon | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.wxByPolyUsV1WxForecastPolygonQueryPost(wxByPolygon, opts, (error, data, response) => {
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
 **wxByPolygon** | [**WxByPolygon**](WxByPolygon.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**WxPolyResponse**](WxPolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wxByRouteUsV1WxForecastRouteQueryPost

> WxRouteResponse wxByRouteUsV1WxForecastRouteQueryPost(wxByRoute, opts)

Retrieve forecast values along a route for all requested weather elements and time periods.

Retrieve forecast values along route for requested weather elements and time period. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km. * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

### Example

```javascript
import DFlightApi from 'd_flight_api';

let apiInstance = new DFlightApi.WeatherApi();
let wxByRoute = new DFlightApi.WxByRoute(); // WxByRoute | 
let opts = {
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.wxByRouteUsV1WxForecastRouteQueryPost(wxByRoute, opts, (error, data, response) => {
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
 **wxByRoute** | [**WxByRoute**](WxByRoute.md)|  | 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**WxRouteResponse**](WxRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

