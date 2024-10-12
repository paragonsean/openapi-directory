# WeatherMapsApi

All URIs are relative to */api/v1/premium*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapMapGet**](WeatherMapsApi.md#mapMapGet) | **GET** /map | Returns PNG weather map for given area and variable |


<a id="mapMapGet"></a>
# **mapMapGet**
> String mapMapGet(variable, datetime, tileX, tileY, tileZoom, minLat, minLon, maxLat, maxLon, key)

Returns PNG weather map for given area and variable

## PNG weather forecast maps for given area and variable  ### Area specification There are two ways to specify geographical area you need for your map: 1. Specify &#x60;X&#x60; and &#x60;Y&#x60; coordinates and zoom level &#x60;Z&#x60; of desired tile in &lt;a href&#x3D;\&quot;https://www.maptiler.com/google-maps-coordinates-tile-bounds-projection/\&quot; rel&#x3D;\&quot;nofollow\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Maps Tile notation&lt;/a&gt;. 2. Specify latitude and longitude bounds of the area you want to cover.  ### Notes * The resulting PNG maps are **always** in &lt;a href&#x3D;\&quot;https://epsg.io/3857\&quot; rel&#x3D;\&quot;nofollow\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Mercator projection (EPSG:3857)&lt;/a&gt;. * As Meteosource only covers areas between latitudes 80° and -80°, you can only request maps within these bounds, when specifying the latitude and longitude boundaries. When specifying the area using Google Maps Tile notation, the regions outside our supported latitudes will be fully transparent. * The finest resolution is not available for maps covering very large regions. The resulting map will be automatically downscaled in this case, to guarantee high-speed responses. * Weather maps are only supported for forecasts, not for archive data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WeatherMapsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1/premium");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    WeatherMapsApi apiInstance = new WeatherMapsApi(defaultClient);
    String variable = "variable_example"; // String | Name of the variable for your map. Available values are:  * `temperature`: Temperature 2 metres above ground * `feels_like_temperature`: Feels like temperature * `clouds`: Percentage of sky covered by clouds * `precipitation`: Total precipitation amount accumulated since last hour * `wind_speed`: Wind speed 10 metres above the ground * `wind_gust`: Wind gust speed * `pressure`: Atmospheric pressure at mean sea level * `humidity`: Relative humidity * `wave_height`: Wave height * `wave_period`: Wave period * `sea_temperature`: Sea temperature (available only for +-24 hours) * `air_quality`: Air quality index * `ozone_surface`: Ozone at surface level * `ozone_total`: Total column ozone * `no2`: Nitrogen dioxide at surface level * `pm2.5`: Particulate matter d < 2.5 µm (PM2.5) 
    String datetime = "datetime_example"; // String | There are two ways to specify date and time for your map:  1. Datetime in `YYYY-MM-DDTHH:MM` format and `UTC` timezone, e.g. `2021-08-24T12:00` 2. Offset from current time in `[+-]<minutes|hours|days>` format, e.g. `+10minutes`, `-2hours` or `+1days` 
    Integer tileX = 56; // Integer | The X coordinate of Google Maps tile
    Integer tileY = 56; // Integer | The Y coordinate of Google Maps tile
    Integer tileZoom = 56; // Integer | The zoom level of Google Maps tile
    String minLat = "minLat_example"; // String | Minimal latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.2 
    String minLon = "minLon_example"; // String | Minimal longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.2 
    String maxLat = "maxLat_example"; // String | Maximal latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.2. 
    String maxLon = "maxLon_example"; // String | Maximal longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.2 
    String key = "key_example"; // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
    try {
      String result = apiInstance.mapMapGet(variable, datetime, tileX, tileY, tileZoom, minLat, minLon, maxLat, maxLon, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WeatherMapsApi#mapMapGet");
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
| **variable** | **String**| Name of the variable for your map. Available values are:  * &#x60;temperature&#x60;: Temperature 2 metres above ground * &#x60;feels_like_temperature&#x60;: Feels like temperature * &#x60;clouds&#x60;: Percentage of sky covered by clouds * &#x60;precipitation&#x60;: Total precipitation amount accumulated since last hour * &#x60;wind_speed&#x60;: Wind speed 10 metres above the ground * &#x60;wind_gust&#x60;: Wind gust speed * &#x60;pressure&#x60;: Atmospheric pressure at mean sea level * &#x60;humidity&#x60;: Relative humidity * &#x60;wave_height&#x60;: Wave height * &#x60;wave_period&#x60;: Wave period * &#x60;sea_temperature&#x60;: Sea temperature (available only for +-24 hours) * &#x60;air_quality&#x60;: Air quality index * &#x60;ozone_surface&#x60;: Ozone at surface level * &#x60;ozone_total&#x60;: Total column ozone * &#x60;no2&#x60;: Nitrogen dioxide at surface level * &#x60;pm2.5&#x60;: Particulate matter d &lt; 2.5 µm (PM2.5)  | |
| **datetime** | **String**| There are two ways to specify date and time for your map:  1. Datetime in &#x60;YYYY-MM-DDTHH:MM&#x60; format and &#x60;UTC&#x60; timezone, e.g. &#x60;2021-08-24T12:00&#x60; 2. Offset from current time in &#x60;[+-]&lt;minutes|hours|days&gt;&#x60; format, e.g. &#x60;+10minutes&#x60;, &#x60;-2hours&#x60; or &#x60;+1days&#x60;  | |
| **tileX** | **Integer**| The X coordinate of Google Maps tile | [optional] |
| **tileY** | **Integer**| The Y coordinate of Google Maps tile | [optional] |
| **tileZoom** | **Integer**| The zoom level of Google Maps tile | [optional] |
| **minLat** | **String**| Minimal latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.2  | [optional] |
| **minLon** | **String**| Minimal longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.2  | [optional] |
| **maxLat** | **String**| Maximal latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.2.  | [optional] |
| **maxLon** | **String**| Maximal longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.2  | [optional] |
| **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] |

### Return type

**String**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Error in passed parameter. |  -  |
| **402** | Maximum requests per day limit exceeded. |  -  |
| **403** | API key not not specified or invalid. |  -  |
| **422** | Validation Error |  -  |
| **429** | Maximum requests per minute limit exceeded. |  -  |

