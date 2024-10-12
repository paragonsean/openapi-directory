# WeatherApi

All URIs are relative to *https://dflight-api.ljaero.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**wxByDistanceUsV1WxForecastDistanceQueryPost**](WeatherApi.md#wxByDistanceUsV1WxForecastDistanceQueryPost) | **POST** /us/v1/wx-forecast/distance-query | Retrieve forecast values within given distance of location for all requested weather elements and time periods. |
| [**wxByPolyUsV1WxForecastPolygonQueryPost**](WeatherApi.md#wxByPolyUsV1WxForecastPolygonQueryPost) | **POST** /us/v1/wx-forecast/polygon-query | Retrieve forecast values within given GeoJSON polygon for all requested weather elements and time periods. |
| [**wxByRouteUsV1WxForecastRouteQueryPost**](WeatherApi.md#wxByRouteUsV1WxForecastRouteQueryPost) | **POST** /us/v1/wx-forecast/route-query | Retrieve forecast values along a route for all requested weather elements and time periods. |


<a id="wxByDistanceUsV1WxForecastDistanceQueryPost"></a>
# **wxByDistanceUsV1WxForecastDistanceQueryPost**
> WxDistanceResponse wxByDistanceUsV1WxForecastDistanceQueryPost(wxByDistance, xApiKey)

Retrieve forecast values within given distance of location for all requested weather elements and time periods.

Retrieve forecast values for selected weather elements and time period. Request body parameters are: * latitude:  WGS84 latitude coordinate of your selected point, in decimal degrees * longitude:  WGS84 longitude coordinate of your selected point, in decimal degrees * distance:  distance in meters (max allowed value is 25000) * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    WeatherApi apiInstance = new WeatherApi(defaultClient);
    WxByDistance wxByDistance = new WxByDistance(); // WxByDistance | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      WxDistanceResponse result = apiInstance.wxByDistanceUsV1WxForecastDistanceQueryPost(wxByDistance, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WeatherApi#wxByDistanceUsV1WxForecastDistanceQueryPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **wxByDistance** | [**WxByDistance**](WxByDistance.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**WxDistanceResponse**](WxDistanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection with one Feature for each forecast location found within requested area. |  -  |
| **422** | Validation Error |  -  |

<a id="wxByPolyUsV1WxForecastPolygonQueryPost"></a>
# **wxByPolyUsV1WxForecastPolygonQueryPost**
> WxPolyResponse wxByPolyUsV1WxForecastPolygonQueryPost(wxByPolygon, xApiKey)

Retrieve forecast values within given GeoJSON polygon for all requested weather elements and time periods.

Retrieve forecast values located within given area for requested weather elements and time period. Request body parameters are: * poly:  [GeoJSON Polygon](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the area. Max allowed area is 1000 km^2. * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    WeatherApi apiInstance = new WeatherApi(defaultClient);
    WxByPolygon wxByPolygon = new WxByPolygon(); // WxByPolygon | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      WxPolyResponse result = apiInstance.wxByPolyUsV1WxForecastPolygonQueryPost(wxByPolygon, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WeatherApi#wxByPolyUsV1WxForecastPolygonQueryPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **wxByPolygon** | [**WxByPolygon**](WxByPolygon.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**WxPolyResponse**](WxPolyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection with one Feature for each forecast location found within requested area. |  -  |
| **422** | Validation Error |  -  |

<a id="wxByRouteUsV1WxForecastRouteQueryPost"></a>
# **wxByRouteUsV1WxForecastRouteQueryPost**
> WxRouteResponse wxByRouteUsV1WxForecastRouteQueryPost(wxByRoute, xApiKey)

Retrieve forecast values along a route for all requested weather elements and time periods.

Retrieve forecast values along route for requested weather elements and time period. Request body parameters are: * route:  [GeoJSON Linestring](https://www.rfc-editor.org/rfc/rfc7946.html#appendix-A) defining the route. Max allowed length is 50 km. * wxtypes:  list of one or more weather forecast elements you wish to retrieve. Allowed values are \&quot;CIG\&quot;, \&quot;DEWPT\&quot;, \&quot;SKY\&quot;, \&quot;TEMP\&quot;, \&quot;VIS\&quot;, \&quot;WINDDIR\&quot;, \&quot;WINDGUST\&quot;, \&quot;WINDSPEED\&quot;. * hours:  number of hourly forecasts to return (1-24). For current hour only you should enter value of 1. To also retrieve values for each of the next n hours, enter n.   The response will consist of a GeoJSON FeatureCollection with one Feature for each forecast location found within requested area, properties of which will include an ordered list of forecast values for each requested weather element, for each requested hour. Units for each element are as follows: * CIG: meters AGL * DEWPT: degrees Celsius * SKY: % cloud cover * TEMP: degrees Celsius * VIS: meters * WINDDIR: degrees true * WINDGUST: meters/sec * WINDSPEED: meters/sec

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dflight-api.ljaero.com");

    WeatherApi apiInstance = new WeatherApi(defaultClient);
    WxByRoute wxByRoute = new WxByRoute(); // WxByRoute | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      WxRouteResponse result = apiInstance.wxByRouteUsV1WxForecastRouteQueryPost(wxByRoute, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WeatherApi#wxByRouteUsV1WxForecastRouteQueryPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **wxByRoute** | [**WxByRoute**](WxByRoute.md)|  | |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**WxRouteResponse**](WxRouteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A GeoJSON FeatureCollection with one Feature for each forecast location found within requested area. |  -  |
| **422** | Validation Error |  -  |

