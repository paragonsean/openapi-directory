# SubHourlyHistoricalWeatherDataApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**historySubhourlycityIdcityIdGet**](SubHourlyHistoricalWeatherDataApi.md#historySubhourlycityIdcityIdGet) | **GET** /history/subhourly?city_id&#x3D;{city_id} | Returns Historical Observations - Given a City ID |
| [**historySubhourlycitycitycountrycountryGet**](SubHourlyHistoricalWeatherDataApi.md#historySubhourlycitycitycountrycountryGet) | **GET** /history/subhourly?city&#x3D;{city}&amp;country&#x3D;{country} | Returns Historical Observations - Given City and/or State, Country. |
| [**historySubhourlylatlatlonlonGet**](SubHourlyHistoricalWeatherDataApi.md#historySubhourlylatlatlonlonGet) | **GET** /history/subhourly?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Historical Observations - Given a lat/lon. |
| [**historySubhourlypostalCodepostalCodeGet**](SubHourlyHistoricalWeatherDataApi.md#historySubhourlypostalCodepostalCodeGet) | **GET** /history/subhourly?postal_code&#x3D;{postal_code} | Returns Historical Observations - Given a Postal Code |
| [**historySubhourlystationstationGet**](SubHourlyHistoricalWeatherDataApi.md#historySubhourlystationstationGet) | **GET** /history/subhourly?station&#x3D;{station} | Returns Historical Observations - Given a station ID. |


<a id="historySubhourlycityIdcityIdGet"></a>
# **historySubhourlycityIdcityIdGet**
> HistorySubhourly historySubhourlycityIdcityIdGet(cityId, startDate, endDate, key, units, lang, tz, paramCallback)

Returns Historical Observations - Given a City ID

Returns Historical Observations - Given a City ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubHourlyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    SubHourlyHistoricalWeatherDataApi apiInstance = new SubHourlyHistoricalWeatherDataApi(defaultClient);
    String cityId = "cityId_example"; // String | City ID. Example: 4487042
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String tz = "local"; // String | Assume utc (default) or local time for start_date, end_date
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistorySubhourly result = apiInstance.historySubhourlycityIdcityIdGet(cityId, startDate, endDate, key, units, lang, tz, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubHourlyHistoricalWeatherDataApi#historySubhourlycityIdcityIdGet");
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
| **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] [enum: local, utc] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistorySubhourly**](HistorySubhourly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Data Object. |  -  |
| **0** | No Data. |  -  |

<a id="historySubhourlycitycitycountrycountryGet"></a>
# **historySubhourlycitycitycountrycountryGet**
> History historySubhourlycitycitycountrycountryGet(city, country, startDate, endDate, key, state, units, lang, tz, paramCallback)

Returns Historical Observations - Given City and/or State, Country.

Returns Historical Observations - Given a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubHourlyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    SubHourlyHistoricalWeatherDataApi apiInstance = new SubHourlyHistoricalWeatherDataApi(defaultClient);
    String city = "city_example"; // String | City search. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    String country = "country_example"; // String | Country Code (2 letter).
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String key = "key_example"; // String | Your registered API key.
    String state = "state_example"; // String | Full name of state.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String tz = "local"; // String | Assume utc (default) or local time for start_date, end_date
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      History result = apiInstance.historySubhourlycitycitycountrycountryGet(city, country, startDate, endDate, key, state, units, lang, tz, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubHourlyHistoricalWeatherDataApi#historySubhourlycitycitycountrycountryGet");
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
| **city** | **String**| City search. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR | |
| **country** | **String**| Country Code (2 letter). | |
| **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | |
| **key** | **String**| Your registered API key. | |
| **state** | **String**| Full name of state. | [optional] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] [enum: local, utc] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**History**](History.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Data Object. |  -  |
| **0** | No Data. |  -  |

<a id="historySubhourlylatlatlonlonGet"></a>
# **historySubhourlylatlatlonlonGet**
> HistorySubhourly historySubhourlylatlatlonlonGet(lat, lon, startDate, endDate, key, units, lang, tz, paramCallback)

Returns Historical Observations - Given a lat/lon.

Returns Historical Observations - Given a lat, and lon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubHourlyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    SubHourlyHistoricalWeatherDataApi apiInstance = new SubHourlyHistoricalWeatherDataApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String tz = "local"; // String | Assume utc (default) or local time for start_date, end_date
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistorySubhourly result = apiInstance.historySubhourlylatlatlonlonGet(lat, lon, startDate, endDate, key, units, lang, tz, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubHourlyHistoricalWeatherDataApi#historySubhourlylatlatlonlonGet");
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
| **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] [enum: local, utc] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistorySubhourly**](HistorySubhourly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Data Object. |  -  |
| **0** | No Data. |  -  |

<a id="historySubhourlypostalCodepostalCodeGet"></a>
# **historySubhourlypostalCodepostalCodeGet**
> HistorySubhourly historySubhourlypostalCodepostalCodeGet(postalCode, startDate, endDate, key, country, units, lang, tz, paramCallback)

Returns Historical Observations - Given a Postal Code

Returns Historical Observations - Given a Postal Code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubHourlyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    SubHourlyHistoricalWeatherDataApi apiInstance = new SubHourlyHistoricalWeatherDataApi(defaultClient);
    String postalCode = "postalCode_example"; // String | Postal Code. Example: 28546
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH)
    String key = "key_example"; // String | Your registered API key.
    String country = "country_example"; // String | Country Code (2 letter).
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String tz = "local"; // String | Assume utc (default) or local time for start_date, end_date
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistorySubhourly result = apiInstance.historySubhourlypostalCodepostalCodeGet(postalCode, startDate, endDate, key, country, units, lang, tz, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubHourlyHistoricalWeatherDataApi#historySubhourlypostalCodepostalCodeGet");
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
| **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] [enum: local, utc] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistorySubhourly**](HistorySubhourly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Data Object. |  -  |
| **0** | No Data. |  -  |

<a id="historySubhourlystationstationGet"></a>
# **historySubhourlystationstationGet**
> HistorySubhourly historySubhourlystationstationGet(station, startDate, endDate, key, units, lang, tz, paramCallback)

Returns Historical Observations - Given a station ID.

Returns Historical Observations - Given a station ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubHourlyHistoricalWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    SubHourlyHistoricalWeatherDataApi apiInstance = new SubHourlyHistoricalWeatherDataApi(defaultClient);
    String station = "station_example"; // String | Station ID.
    String startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String tz = "local"; // String | Assume utc (default) or local time for start_date, end_date
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      HistorySubhourly result = apiInstance.historySubhourlystationstationGet(station, startDate, endDate, key, units, lang, tz, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubHourlyHistoricalWeatherDataApi#historySubhourlystationstationGet");
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
| **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] [enum: local, utc] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**HistorySubhourly**](HistorySubhourly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Historical Data Object. |  -  |
| **0** | No Data. |  -  |

