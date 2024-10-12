# DailyHistoricalWeatherDataApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**historyDailycityIdcityIdGet**](DailyHistoricalWeatherDataApi.md#historyDailycityIdcityIdGet) | **GET** /history/daily?city_id&#x3D;{city_id} | Returns Historical Observations - Given a City ID |
| [**historyDailycitycitycountrycountryGet**](DailyHistoricalWeatherDataApi.md#historyDailycitycitycountrycountryGet) | **GET** /history/daily?city&#x3D;{city}&amp;country&#x3D;{country} | Returns Historical Observations - Given City and/or State, Country. |
| [**historyDailylatlatlonlonGet**](DailyHistoricalWeatherDataApi.md#historyDailylatlatlonlonGet) | **GET** /history/daily?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Historical Observations - Given a lat/lon. |
| [**historyDailypostalCodepostalCodeGet**](DailyHistoricalWeatherDataApi.md#historyDailypostalCodepostalCodeGet) | **GET** /history/daily?postal_code&#x3D;{postal_code} | Returns Historical Observations - Given a Postal Code |
| [**historyDailystationstationGet**](DailyHistoricalWeatherDataApi.md#historyDailystationstationGet) | **GET** /history/daily?station&#x3D;{station} | Returns Historical Observations - Given a station ID. |


<a id="historyDailycityIdcityIdGet"></a>
# **historyDailycityIdcityIdGet**
> HistoryDay historyDailycityIdcityIdGet(cityId, startDate, endDate, key, units, lang, paramCallback)

Returns Historical Observations - Given a City ID

Returns Historical Observations - Given a City ID. **(LIMIT 1 year per request)**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DailyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    DailyHistoricalWeatherDataApi apiInstance = new DailyHistoricalWeatherDataApi(defaultClient);
    String cityId = "cityId_example"; // String | City ID. Example: 4487042
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistoryDay result = apiInstance.historyDailycityIdcityIdGet(cityId, startDate, endDate, key, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DailyHistoricalWeatherDataApi#historyDailycityIdcityIdGet");
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
| **cityId** | **String**| City ID. Example: 4487042 | |
| **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH) | |
| **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH) | |
| **key** | **String**| Your registered API key. | |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistoryDay**](HistoryDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Day Data Object. |  -  |
| **0** | No Data. |  -  |

<a id="historyDailycitycitycountrycountryGet"></a>
# **historyDailycitycitycountrycountryGet**
> HistoryDay historyDailycitycitycountrycountryGet(city, country, startDate, endDate, key, state, units, lang, paramCallback)

Returns Historical Observations - Given City and/or State, Country.

Returns Historical Observations - Given a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. **(LIMIT 1 year per request)**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DailyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    DailyHistoricalWeatherDataApi apiInstance = new DailyHistoricalWeatherDataApi(defaultClient);
    String city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    String country = "country_example"; // String | Country Code (2 letter).
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String key = "key_example"; // String | Your registered API key.
    String state = "state_example"; // String | Full name of state.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistoryDay result = apiInstance.historyDailycitycitycountrycountryGet(city, country, startDate, endDate, key, state, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DailyHistoricalWeatherDataApi#historyDailycitycitycountrycountryGet");
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
| **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **key** | **String**| Your registered API key. | |
| **state** | **String**| Full name of state. | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistoryDay**](HistoryDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Day Data Object. |  -  |
| **0** | No Data. |  -  |

<a id="historyDailylatlatlonlonGet"></a>
# **historyDailylatlatlonlonGet**
> HistoryDay historyDailylatlatlonlonGet(lat, lon, startDate, endDate, key, units, lang, paramCallback)

Returns Historical Observations - Given a lat/lon.

Returns Historical Observations - Given a lat, and lon. **(LIMIT 1 year per request)**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DailyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    DailyHistoricalWeatherDataApi apiInstance = new DailyHistoricalWeatherDataApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistoryDay result = apiInstance.historyDailylatlatlonlonGet(lat, lon, startDate, endDate, key, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DailyHistoricalWeatherDataApi#historyDailylatlatlonlonGet");
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
| **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **key** | **String**| Your registered API key. | |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistoryDay**](HistoryDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Day Data Object. |  -  |
| **0** | No Data. |  -  |

<a id="historyDailypostalCodepostalCodeGet"></a>
# **historyDailypostalCodepostalCodeGet**
> HistoryDay historyDailypostalCodepostalCodeGet(postalCode, startDate, endDate, key, country, units, lang, paramCallback)

Returns Historical Observations - Given a Postal Code

Returns Historical Observations - Given a Postal Code. **(LIMIT 1 year per request)**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DailyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    DailyHistoricalWeatherDataApi apiInstance = new DailyHistoricalWeatherDataApi(defaultClient);
    String postalCode = "postalCode_example"; // String | Postal Code. Example: 28546
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    String key = "key_example"; // String | Your registered API key.
    String country = "country_example"; // String | Country Code (2 letter).
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistoryDay result = apiInstance.historyDailypostalCodepostalCodeGet(postalCode, startDate, endDate, key, country, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DailyHistoricalWeatherDataApi#historyDailypostalCodepostalCodeGet");
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
| **postalCode** | **String**| Postal Code. Example: 28546 | |
| **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH) | |
| **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH) | |
| **key** | **String**| Your registered API key. | |
| **country** | **String**| Country Code (2 letter). | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistoryDay**](HistoryDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Day Data Object. |  -  |
| **0** | No Data. |  -  |

<a id="historyDailystationstationGet"></a>
# **historyDailystationstationGet**
> HistoryDay historyDailystationstationGet(station, startDate, endDate, key, units, lang, paramCallback)

Returns Historical Observations - Given a station ID.

Returns Historical Observations - Given a station ID. **(LIMIT 1 year per request)**

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DailyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    DailyHistoricalWeatherDataApi apiInstance = new DailyHistoricalWeatherDataApi(defaultClient);
    String station = "station_example"; // String | Station ID.
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistoryDay result = apiInstance.historyDailystationstationGet(station, startDate, endDate, key, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DailyHistoricalWeatherDataApi#historyDailystationstationGet");
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
| **station** | **String**| Station ID. | |
| **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **key** | **String**| Your registered API key. | |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistoryDay**](HistoryDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Day Data Object. |  -  |
| **0** | No Data. |  -  |

