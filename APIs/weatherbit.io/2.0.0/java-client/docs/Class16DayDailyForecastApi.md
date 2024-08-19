# Class16DayDailyForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forecastDailycityIdcityIdGet**](Class16DayDailyForecastApi.md#forecastDailycityIdcityIdGet) | **GET** /forecast/daily?city_id&#x3D;{city_id} | Returns a daily forecast - Given a City ID. |
| [**forecastDailycitycitycountrycountryGet**](Class16DayDailyForecastApi.md#forecastDailycitycitycountrycountryGet) | **GET** /forecast/daily?city&#x3D;{city}&amp;country&#x3D;{country} | Returns a daily forecast - Given City and/or State, Country. |
| [**forecastDailylatlatlonlonGet**](Class16DayDailyForecastApi.md#forecastDailylatlatlonlonGet) | **GET** /forecast/daily?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns a daily forecast - Given Lat/Lon. |
| [**forecastDailypostalCodepostalCodeGet**](Class16DayDailyForecastApi.md#forecastDailypostalCodepostalCodeGet) | **GET** /forecast/daily?postal_code&#x3D;{postal_code} | Returns a daily forecast - Given a Postal Code. |


<a id="forecastDailycityIdcityIdGet"></a>
# **forecastDailycityIdcityIdGet**
> ForecastDay forecastDailycityIdcityIdGet(cityId, key, days, units, lang, paramCallback)

Returns a daily forecast - Given a City ID.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class16DayDailyForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    Class16DayDailyForecastApi apiInstance = new Class16DayDailyForecastApi(defaultClient);
    Integer cityId = 56; // Integer | City ID. Example: 4487042
    String key = "key_example"; // String | Your registered API key.
    BigDecimal days = new BigDecimal(78); // BigDecimal | Number of days to return. Default 16.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      ForecastDay result = apiInstance.forecastDailycityIdcityIdGet(cityId, key, days, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class16DayDailyForecastApi#forecastDailycityIdcityIdGet");
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
| **cityId** | **Integer**| City ID. Example: 4487042 | |
| **key** | **String**| Your registered API key. | |
| **days** | **BigDecimal**| Number of days to return. Default 16. | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A forecast object. |  -  |
| **0** | No Data. |  -  |

<a id="forecastDailycitycitycountrycountryGet"></a>
# **forecastDailycitycitycountrycountryGet**
> ForecastDay forecastDailycitycitycountrycountryGet(city, country, key, state, days, units, lang, paramCallback)

Returns a daily forecast - Given City and/or State, Country.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class16DayDailyForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    Class16DayDailyForecastApi apiInstance = new Class16DayDailyForecastApi(defaultClient);
    String city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    String country = "country_example"; // String | Country Code (2 letter).
    String key = "key_example"; // String | Your registered API key.
    String state = "state_example"; // String | Full name of state.
    BigDecimal days = new BigDecimal(78); // BigDecimal | Number of days to return. Default 16.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    try {
      ForecastDay result = apiInstance.forecastDailycitycitycountrycountryGet(city, country, key, state, days, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class16DayDailyForecastApi#forecastDailycitycitycountrycountryGet");
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
| **city** | **String**| City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR | |
| **country** | **String**| Country Code (2 letter). | |
| **key** | **String**| Your registered API key. | |
| **state** | **String**| Full name of state. | [optional] |
| **days** | **BigDecimal**| Number of days to return. Default 16. | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] |

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A forecast object. |  -  |
| **0** | No Data. |  -  |

<a id="forecastDailylatlatlonlonGet"></a>
# **forecastDailylatlatlonlonGet**
> ForecastDay forecastDailylatlatlonlonGet(lat, lon, key, days, units, lang, paramCallback)

Returns a daily forecast - Given Lat/Lon.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class16DayDailyForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    Class16DayDailyForecastApi apiInstance = new Class16DayDailyForecastApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String key = "key_example"; // String | Your registered API key.
    BigDecimal days = new BigDecimal(78); // BigDecimal | Number of days to return. Default 16.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      ForecastDay result = apiInstance.forecastDailylatlatlonlonGet(lat, lon, key, days, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class16DayDailyForecastApi#forecastDailylatlatlonlonGet");
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
| **lat** | **Double**| Latitude component of location. | |
| **lon** | **Double**| Longitude component of location. | |
| **key** | **String**| Your registered API key. | |
| **days** | **BigDecimal**| Number of days to return. Default 16. | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A forecast object. |  -  |
| **0** | No Data. |  -  |

<a id="forecastDailypostalCodepostalCodeGet"></a>
# **forecastDailypostalCodepostalCodeGet**
> ForecastDay forecastDailypostalCodepostalCodeGet(postalCode, key, country, days, units, lang, paramCallback)

Returns a daily forecast - Given a Postal Code.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class16DayDailyForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    Class16DayDailyForecastApi apiInstance = new Class16DayDailyForecastApi(defaultClient);
    Integer postalCode = 56; // Integer | Postal Code. Example: 28546
    String key = "key_example"; // String | Your registered API key.
    String country = "country_example"; // String | Country Code (2 letter).
    BigDecimal days = new BigDecimal(78); // BigDecimal | Number of days to return. Default 16.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      ForecastDay result = apiInstance.forecastDailypostalCodepostalCodeGet(postalCode, key, country, days, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class16DayDailyForecastApi#forecastDailypostalCodepostalCodeGet");
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
| **postalCode** | **Integer**| Postal Code. Example: 28546 | |
| **key** | **String**| Your registered API key. | |
| **country** | **String**| Country Code (2 letter). | [optional] |
| **days** | **BigDecimal**| Number of days to return. Default 16. | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A forecast object. |  -  |
| **0** | No Data. |  -  |

