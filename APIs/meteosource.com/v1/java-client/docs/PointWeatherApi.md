# PointWeatherApi

All URIs are relative to */api/v1/premium*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**airQualityAirQualityGet**](PointWeatherApi.md#airQualityAirQualityGet) | **GET** /air_quality | Returns air quality data for a single point (geographic name or GPS) |
| [**pointPointGet**](PointWeatherApi.md#pointPointGet) | **GET** /point | Returns weather data for a single point (geographic name or GPS) |


<a id="airQualityAirQualityGet"></a>
# **airQualityAirQualityGet**
> AirQualityPointData airQualityAirQualityGet(placeId, lat, lon, timezone, key)

Returns air quality data for a single point (geographic name or GPS)

## Air quality forecast for a single location  ### Location specification The location of the weather data is the only parameter that is required and must be specified. There are two ways to do this: 1. Specify the GPS coordinates of the location using the parameters &#x60;lat&#x60; and &#x60;lon&#x60;. 2. **OR** specify the name of the place using the parameter &#x60;place_id&#x60;. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).  ### Notes * **For a detailed description of variables, please consult ⚠️ &lt;a href&#x3D;\&quot;https://www.meteosource.com/documentation#description_aq\&quot; target&#x3D;\&quot;_blank\&quot;&gt;description of variables&lt;/a&gt; ⚠️ in Documentation or &#x60;Schema&#x60; of the response (link next to Example value in the Responses section below).** * Do **not** make any assumptions about the number and ordering of the variables. New variables and sections may be introduced in the future. Always check the data are present before you try to use them. * The response contains an &#x60;Expires&#x60; header, which defines the point at which the API response will not change for the same request. We highly recommend using this to avoid unnecessary requests and **increase the performance of your app**. * Meteosource API supports HTTP compression. To enable it, simply add an &#x60;Accept-Encoding: gzip&#x60; header to your request. * When daylight saving time starts, one hourly record will be missing (typically &#x60;2:00:00 AM&#x60;). When daylight saving time ends, the hourly forecast will contain two records with duplicate times (typically &#x60;2:00:00 AM&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PointWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1/premium");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    PointWeatherApi apiInstance = new PointWeatherApi(defaultClient);
    String placeId = "placeId_example"; // String | Identifier of a place. To obtain the `place_id` for the location you want, please use endpoints `/find_places_prefix` (search by prefix) or `/find_places` (search by full name).
    String lat = "lat_example"; // String | Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
    String lon = "lon_example"; // String | Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
    String timezone = "timezone_example"; // String | Timezone to be used for the date fields. If not specified, local timezone of the forecast location will be used. The format is according to the tzinfo database, so values like `Europe/Prague` or `UTC` can be used. Alternatively you may use the value ``auto`` in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). 
    String key = "key_example"; // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
    try {
      AirQualityPointData result = apiInstance.airQualityAirQualityGet(placeId, lat, lon, timezone, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PointWeatherApi#airQualityAirQualityGet");
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
| **placeId** | **String**| Identifier of a place. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name). | [optional] |
| **lat** | **String**| Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4 | [optional] |
| **lon** | **String**| Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4 | [optional] |
| **timezone** | **String**| Timezone to be used for the date fields. If not specified, local timezone of the forecast location will be used. The format is according to the tzinfo database, so values like &#x60;Europe/Prague&#x60; or &#x60;UTC&#x60; can be used. Alternatively you may use the value &#x60;&#x60;auto&#x60;&#x60; in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).  | [optional] |
| **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] |

### Return type

[**AirQualityPointData**](AirQualityPointData.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Error in passed parameter. |  -  |
| **402** | Maximum requests per day limit exceeded. |  -  |
| **403** | API key not not specified or invalid. |  -  |
| **422** | Validation Error |  -  |
| **429** | Maximum requests per minute limit exceeded. |  -  |

<a id="pointPointGet"></a>
# **pointPointGet**
> PointPointData pointPointGet(placeId, lat, lon, sections, timezone, language, units, key)

Returns weather data for a single point (geographic name or GPS)

## Current weather and forecast for single location  ### Location specification The location of the weather data is the only parameter that is required and must be specified. There are two ways to do this: 1. Specify the GPS coordinates of the location using the parameters &#x60;lat&#x60; and &#x60;lon&#x60;. 2. **OR** specify the name of the place using the parameter &#x60;place_id&#x60;. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).  *Note: For mountains, it is usually better to specify the &#x60;place_id&#x60; rather than the &#x60;lat&#x60; and &#x60;lon&#x60;. When you use &#x60;place_id&#x60;, you are guaranteed to receive forecasts for the precise elevation of the peak. When you specify the coordinates, the elevation can be less precise.*  ### Sections The endpoint can return multiple sections of data. To obtain the best performance, we advise only requesting the sections you actually need. The available sections are as follows:  * Current weather situation * Hourly forecast (for 24/48/96/168 hours, depending on the tier) * Daily forecast (for 7/10/30 days, depending on the tier) * Minutely precipitation forecast (for 60 minutes in the following hour, only for higher tiers) * Weather alerts (only for higher tiers)  By default, only the current and hourly sections are returned. The division into daily parts (morning, afternoon and evening) is only available for the first 7 days of the forecast. For details regarding available parameters, see the parameter description below.  ### Notes * **For a detailed description of variables (e.g. icons), please consult ⚠️ &lt;a href&#x3D;\&quot;https://www.meteosource.com/documentation#description\&quot; target&#x3D;\&quot;_blank\&quot;&gt;description of variables&lt;/a&gt; ⚠️ in Documentation or &#x60;Schema&#x60; of the response (link next to Example value in the Responses section below).** * Variables can be instantaneous, averaged, or accumulated over certain time. For example, &#x60;precipitation&#x60; forecast provides the precipitation accumulated until the next hour (data with timestamp as &#x60;12:00:00&#x60; is rain accumulated from &#x60;12:00:00&#x60; to &#x60;13:00:00&#x60;). * Do **not** make any assumptions about the number and ordering of the variables. New variables and sections may be introduced in the future. Always check the data are present before you try to use them. * The response contains an &#x60;Expires&#x60; header, which defines the point at which the API response will not change for the same request. We highly recommend using this to avoid unnecessary requests and **increase the performance of your app**. * Meteosource API supports HTTP compression. To enable it, simply add an &#x60;Accept-Encoding: gzip&#x60; header to your request. * When daylight saving time starts, one hourly record will be missing (typically &#x60;2:00:00 AM&#x60;). When daylight saving time ends, the hourly forecast will contain two records with duplicate times (typically &#x60;2:00:00 AM&#x60;). * The detailed description of weather alerts is only available in English. The alert category is translated into selected language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PointWeatherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1/premium");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    PointWeatherApi apiInstance = new PointWeatherApi(defaultClient);
    String placeId = "placeId_example"; // String | Identifier of a place. To obtain the `place_id` for the location you want, please use endpoints `/find_places_prefix` (search by prefix) or `/find_places` (search by full name).
    String lat = "lat_example"; // String | Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
    String lon = "lon_example"; // String | Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
    String sections = "current,hourly"; // String | Sections to be included in the response. You can specify more section by separating the values with a comma. The available values are:  * ``current``: Current weather situation * ``daily``: Forecasts for each whole day, without the daily parts * ``daily-parts``: Forecasts for each whole day, morning, afternoon and evening     * Important: forecast for the morning, afternoon and evening is available only for the first       7 days in the forecast * ``hourly``: Forecasts with hourly resolution * ``minutely``: Precipitation forecast with 1 minute resolution * ``alerts``: The weather alerts * ``all``: All sections 
    String timezone = "timezone_example"; // String | Timezone to be used for the date fields. If not specified, local timezone of the forecast location will be used. The format is according to the tzinfo database, so values like `Europe/Prague` or `UTC` can be used. Alternatively you may use the value ``auto`` in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). 
    Language language = Language.fromValue("cs"); // Language | The language of text summaries and place names (variable names are never translated). Available languages are:     * ``en``: English    * ``es``: Spanish    * ``fr``: French    * ``de``: German    * ``pl``: Polish    * ``pt``: Portuguese    * ``cs``: Czech 
    Units units = Units.fromValue("auto"); // Units | Unit system to be used. The available values are:  * `auto`: Select the system automatically, based on the forecast location. * `metric`: Metric (SI) units (`°C`, `mm/h`, `m/s`, `cm`, `km`, `hPa`). * `us`: Imperial units (`°F`, `in/h`, `mph`, `in`, `mi`, `Hg`). * `uk`: Same as ``metric``, except that visibility is in `miles` and wind speeds are in `mph`. * `ca`: Same as ``metric``, except that wind speeds are in `km/h` and pressure is in `kPa`. 
    String key = "key_example"; // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
    try {
      PointPointData result = apiInstance.pointPointGet(placeId, lat, lon, sections, timezone, language, units, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PointWeatherApi#pointPointGet");
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
| **placeId** | **String**| Identifier of a place. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name). | [optional] |
| **lat** | **String**| Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4 | [optional] |
| **lon** | **String**| Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4 | [optional] |
| **sections** | **String**| Sections to be included in the response. You can specify more section by separating the values with a comma. The available values are:  * &#x60;&#x60;current&#x60;&#x60;: Current weather situation * &#x60;&#x60;daily&#x60;&#x60;: Forecasts for each whole day, without the daily parts * &#x60;&#x60;daily-parts&#x60;&#x60;: Forecasts for each whole day, morning, afternoon and evening     * Important: forecast for the morning, afternoon and evening is available only for the first       7 days in the forecast * &#x60;&#x60;hourly&#x60;&#x60;: Forecasts with hourly resolution * &#x60;&#x60;minutely&#x60;&#x60;: Precipitation forecast with 1 minute resolution * &#x60;&#x60;alerts&#x60;&#x60;: The weather alerts * &#x60;&#x60;all&#x60;&#x60;: All sections  | [optional] [default to current,hourly] |
| **timezone** | **String**| Timezone to be used for the date fields. If not specified, local timezone of the forecast location will be used. The format is according to the tzinfo database, so values like &#x60;Europe/Prague&#x60; or &#x60;UTC&#x60; can be used. Alternatively you may use the value &#x60;&#x60;auto&#x60;&#x60; in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).  | [optional] |
| **language** | [**Language**](.md)| The language of text summaries and place names (variable names are never translated). Available languages are:     * &#x60;&#x60;en&#x60;&#x60;: English    * &#x60;&#x60;es&#x60;&#x60;: Spanish    * &#x60;&#x60;fr&#x60;&#x60;: French    * &#x60;&#x60;de&#x60;&#x60;: German    * &#x60;&#x60;pl&#x60;&#x60;: Polish    * &#x60;&#x60;pt&#x60;&#x60;: Portuguese    * &#x60;&#x60;cs&#x60;&#x60;: Czech  | [optional] [default to en] [enum: cs, en, de, es, fr, pl, pt] |
| **units** | [**Units**](.md)| Unit system to be used. The available values are:  * &#x60;auto&#x60;: Select the system automatically, based on the forecast location. * &#x60;metric&#x60;: Metric (SI) units (&#x60;°C&#x60;, &#x60;mm/h&#x60;, &#x60;m/s&#x60;, &#x60;cm&#x60;, &#x60;km&#x60;, &#x60;hPa&#x60;). * &#x60;us&#x60;: Imperial units (&#x60;°F&#x60;, &#x60;in/h&#x60;, &#x60;mph&#x60;, &#x60;in&#x60;, &#x60;mi&#x60;, &#x60;Hg&#x60;). * &#x60;uk&#x60;: Same as &#x60;&#x60;metric&#x60;&#x60;, except that visibility is in &#x60;miles&#x60; and wind speeds are in &#x60;mph&#x60;. * &#x60;ca&#x60;: Same as &#x60;&#x60;metric&#x60;&#x60;, except that wind speeds are in &#x60;km/h&#x60; and pressure is in &#x60;kPa&#x60;.  | [optional] [default to auto] [enum: auto, metric, us, uk, ca] |
| **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] |

### Return type

[**PointPointData**](PointPointData.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **400** | Error in passed parameter. |  -  |
| **402** | Maximum requests per day limit exceeded. |  -  |
| **403** | API key not not specified or invalid. |  -  |
| **422** | Validation Error |  -  |
| **429** | Maximum requests per minute limit exceeded. |  -  |

