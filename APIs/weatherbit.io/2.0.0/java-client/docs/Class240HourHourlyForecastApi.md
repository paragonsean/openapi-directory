# Class240HourHourlyForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forecastHourlycityIdcityIdGet**](Class240HourHourlyForecastApi.md#forecastHourlycityIdcityIdGet) | **GET** /forecast/hourly?city_id&#x3D;{city_id} | Returns an hourly forecast - Given a City ID. |
| [**forecastHourlycitycitycountrycountryGet**](Class240HourHourlyForecastApi.md#forecastHourlycitycitycountrycountryGet) | **GET** /forecast/hourly?city&#x3D;{city}&amp;country&#x3D;{country} | Returns an hourly forecast - Given City and/or State, Country. |
| [**forecastHourlylatlatlonlonGet**](Class240HourHourlyForecastApi.md#forecastHourlylatlatlonlonGet) | **GET** /forecast/hourly?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns an hourly forecast - Given a lat/lon. |
| [**forecastHourlypostalCodepostalCodeGet**](Class240HourHourlyForecastApi.md#forecastHourlypostalCodepostalCodeGet) | **GET** /forecast/hourly?postal_code&#x3D;{postal_code} | Returns an hourly forecast - Given a Postal Code. |


<a id="forecastHourlycityIdcityIdGet"></a>
# **forecastHourlycityIdcityIdGet**
> ForecastHourly forecastHourlycityIdcityIdGet(cityId, key, units, lang, paramCallback, hours)

Returns an hourly forecast - Given a City ID.

 Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class240HourHourlyForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    Class240HourHourlyForecastApi apiInstance = new Class240HourHourlyForecastApi(defaultClient);
    Integer cityId = 56; // Integer | City ID. Example: 4487042
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    Integer hours = 56; // Integer | Number of hours to return.
    try {
      ForecastHourly result = apiInstance.forecastHourlycityIdcityIdGet(cityId, key, units, lang, paramCallback, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class240HourHourlyForecastApi#forecastHourlycityIdcityIdGet");
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
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] |
| **hours** | **Integer**| Number of hours to return. | [optional] |

### Return type

[**ForecastHourly**](ForecastHourly.md)

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

<a id="forecastHourlycitycitycountrycountryGet"></a>
# **forecastHourlycitycitycountrycountryGet**
> ForecastHourly forecastHourlycitycitycountrycountryGet(city, country, key, state, units, lang, paramCallback, hours)

Returns an hourly forecast - Given City and/or State, Country.

 Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class240HourHourlyForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    Class240HourHourlyForecastApi apiInstance = new Class240HourHourlyForecastApi(defaultClient);
    String city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    String country = "country_example"; // String | Country Code (2 letter).
    String key = "key_example"; // String | Your registered API key.
    String state = "state_example"; // String | Full name of state.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    Integer hours = 56; // Integer | Number of hours to return.
    try {
      ForecastHourly result = apiInstance.forecastHourlycitycitycountrycountryGet(city, country, key, state, units, lang, paramCallback, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class240HourHourlyForecastApi#forecastHourlycitycitycountrycountryGet");
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
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |
| **hours** | **Integer**| Number of hours to return. | [optional] |

### Return type

[**ForecastHourly**](ForecastHourly.md)

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

<a id="forecastHourlylatlatlonlonGet"></a>
# **forecastHourlylatlatlonlonGet**
> ForecastHourly forecastHourlylatlatlonlonGet(lat, lon, key, units, lang, paramCallback, hours)

Returns an hourly forecast - Given a lat/lon.

Returns an hourly forecast, where each point represents a one hour period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class240HourHourlyForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    Class240HourHourlyForecastApi apiInstance = new Class240HourHourlyForecastApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    Integer hours = 56; // Integer | Number of hours to return.
    try {
      ForecastHourly result = apiInstance.forecastHourlylatlatlonlonGet(lat, lon, key, units, lang, paramCallback, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class240HourHourlyForecastApi#forecastHourlylatlatlonlonGet");
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
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] |
| **hours** | **Integer**| Number of hours to return. | [optional] |

### Return type

[**ForecastHourly**](ForecastHourly.md)

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

<a id="forecastHourlypostalCodepostalCodeGet"></a>
# **forecastHourlypostalCodepostalCodeGet**
> ForecastHourly forecastHourlypostalCodepostalCodeGet(postalCode, key, country, units, lang, paramCallback, hours)

Returns an hourly forecast - Given a Postal Code.

 Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class240HourHourlyForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    Class240HourHourlyForecastApi apiInstance = new Class240HourHourlyForecastApi(defaultClient);
    Integer postalCode = 56; // Integer | Postal Code. Example: 28546
    String key = "key_example"; // String | Your registered API key.
    String country = "country_example"; // String | Country Code (2 letter).
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    Integer hours = 56; // Integer | Number of hours to return.
    try {
      ForecastHourly result = apiInstance.forecastHourlypostalCodepostalCodeGet(postalCode, key, country, units, lang, paramCallback, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class240HourHourlyForecastApi#forecastHourlypostalCodepostalCodeGet");
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
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] |
| **hours** | **Integer**| Number of hours to return. | [optional] |

### Return type

[**ForecastHourly**](ForecastHourly.md)

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

