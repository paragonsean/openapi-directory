# CurrentWeatherDataApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currentcitiescitiesGet**](CurrentWeatherDataApi.md#currentcitiescitiesGet) | **GET** /current?cities&#x3D;{cities} | Returns a group of observations given a list of cities |
| [**currentcityIdcityIdGet**](CurrentWeatherDataApi.md#currentcityIdcityIdGet) | **GET** /current?city_id&#x3D;{city_id} | Returns a current observation by city id. |
| [**currentcitycitycountrycountryGet**](CurrentWeatherDataApi.md#currentcitycitycountrycountryGet) | **GET** /current?city&#x3D;{city}&amp;country&#x3D;{country} | Returns a Current Observation - Given City and/or State, Country. |
| [**currentlatlatlonlonGet**](CurrentWeatherDataApi.md#currentlatlatlonlonGet) | **GET** /current?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns a Current Observation - Given a lat/lon. |
| [**currentpointspointsGet**](CurrentWeatherDataApi.md#currentpointspointsGet) | **GET** /current?points&#x3D;{points} | Returns a group of observations given a list of points in the format (lat1, lon1), (lat2, lon2), (latN, lonN), ... |
| [**currentpostalCodepostalCodeGet**](CurrentWeatherDataApi.md#currentpostalCodepostalCodeGet) | **GET** /current?postal_code&#x3D;{postal_code} | Returns a current observation by postal code. |
| [**currentstationsstationsGet**](CurrentWeatherDataApi.md#currentstationsstationsGet) | **GET** /current?stations&#x3D;{stations} | Returns a group of observations given a list of stations |
| [**currentstationstationGet**](CurrentWeatherDataApi.md#currentstationstationGet) | **GET** /current?station&#x3D;{station} | Returns a Current Observation. - Given a station ID. |


<a id="currentcitiescitiesGet"></a>
# **currentcitiescitiesGet**
> CurrentObsGroup currentcitiescitiesGet(cities, key, units, marine, lang, paramCallback)

Returns a group of observations given a list of cities

Returns a group of Current Observations - Given a list of City IDs. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentWeatherDataApi apiInstance = new CurrentWeatherDataApi(defaultClient);
    String cities = "cities_example"; // String | Comma separated list of City ID's. Example: 4487042, 4494942, 4504871
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String marine = "t"; // String | Marine stations only (buoys, oil platforms, etc)
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback - Example - callback=func
    try {
      CurrentObsGroup result = apiInstance.currentcitiescitiesGet(cities, key, units, marine, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentWeatherDataApi#currentcitiescitiesGet");
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
| **cities** | **String**| Comma separated list of City ID&#39;s. Example: 4487042, 4494942, 4504871 | |
| **key** | **String**| Your registered API key. | |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] [enum: t] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] |

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Observation Group object. |  -  |
| **0** | No Data. |  -  |

<a id="currentcityIdcityIdGet"></a>
# **currentcityIdcityIdGet**
> CurrentObsGroup currentcityIdcityIdGet(cityId, key, units, include, marine, lang, paramCallback)

Returns a current observation by city id.

Returns current weather observation - Given a City ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentWeatherDataApi apiInstance = new CurrentWeatherDataApi(defaultClient);
    String cityId = "cityId_example"; // String | City ID. Example: 4487042
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String include = "minutely"; // String | Include 1 hour - minutely forecast in the response
    String marine = "t"; // String | Marine stations only (buoys, oil platforms, etc)
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback - Example - callback=func
    try {
      CurrentObsGroup result = apiInstance.currentcityIdcityIdGet(cityId, key, units, include, marine, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentWeatherDataApi#currentcityIdcityIdGet");
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
| **key** | **String**| Your registered API key. | |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] [enum: minutely] |
| **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] [enum: t] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] |

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Observation Group object. |  -  |
| **0** | No Data. |  -  |

<a id="currentcitycitycountrycountryGet"></a>
# **currentcitycitycountrycountryGet**
> CurrentObsGroup currentcitycitycountrycountryGet(city, country, key, include, state, marine, units, lang, paramCallback)

Returns a Current Observation - Given City and/or State, Country.

Returns a Current Observation - Given a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentWeatherDataApi apiInstance = new CurrentWeatherDataApi(defaultClient);
    String city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    String country = "country_example"; // String | Country Code (2 letter).
    String key = "key_example"; // String | Your registered API key.
    String include = "minutely"; // String | Include 1 hour - minutely forecast in the response
    String state = "state_example"; // String | Full name of state.
    String marine = "t"; // String | Marine stations only (buoys, oil platforms, etc)
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback - Example - callback=func
    try {
      CurrentObsGroup result = apiInstance.currentcitycitycountrycountryGet(city, country, key, include, state, marine, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentWeatherDataApi#currentcitycitycountrycountryGet");
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
| **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] [enum: minutely] |
| **state** | **String**| Full name of state. | [optional] |
| **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] [enum: t] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] |

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Observation Group object. |  -  |
| **0** | No Data. |  -  |

<a id="currentlatlatlonlonGet"></a>
# **currentlatlatlonlonGet**
> CurrentObsGroup currentlatlatlonlonGet(lat, lon, key, include, marine, units, lang, paramCallback)

Returns a Current Observation - Given a lat/lon.

Returns a Current Observation - given a lat, and a lon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentWeatherDataApi apiInstance = new CurrentWeatherDataApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String key = "key_example"; // String | Your registered API key.
    String include = "minutely"; // String | Include 1 hour - minutely forecast in the response
    String marine = "t"; // String | Marine stations only (buoys, oil platforms, etc)
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback - Example - callback=func
    try {
      CurrentObsGroup result = apiInstance.currentlatlatlonlonGet(lat, lon, key, include, marine, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentWeatherDataApi#currentlatlatlonlonGet");
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
| **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] [enum: minutely] |
| **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] [enum: t] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] |

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Observation Group object. |  -  |
| **0** | No Data. |  -  |

<a id="currentpointspointsGet"></a>
# **currentpointspointsGet**
> CurrentObsGroup currentpointspointsGet(points, key, units, lang, paramCallback)

Returns a group of observations given a list of points in the format (lat1, lon1), (lat2, lon2), (latN, lonN), ...

Returns a group of Current Observations - Given a list of points (lat1, lon1), (lat2, lon2), (latN, lonN), ...

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentWeatherDataApi apiInstance = new CurrentWeatherDataApi(defaultClient);
    String points = "points_example"; // String | Comma separated list of points. Example: (35.5, -75.5),(45, 65),(45.12, -130.5)
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      CurrentObsGroup result = apiInstance.currentpointspointsGet(points, key, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentWeatherDataApi#currentpointspointsGet");
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
| **points** | **String**| Comma separated list of points. Example: (35.5, -75.5),(45, 65),(45.12, -130.5) | |
| **key** | **String**| Your registered API key. | |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Observation Group object. |  -  |
| **0** | No Data. |  -  |

<a id="currentpostalCodepostalCodeGet"></a>
# **currentpostalCodepostalCodeGet**
> CurrentObsGroup currentpostalCodepostalCodeGet(postalCode, key, country, include, marine, units, lang, paramCallback)

Returns a current observation by postal code.

Returns current weather observation - Given a Postal Code. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentWeatherDataApi apiInstance = new CurrentWeatherDataApi(defaultClient);
    String postalCode = "postalCode_example"; // String | Postal Code. Example: 28546
    String key = "key_example"; // String | Your registered API key.
    String country = "country_example"; // String | Country Code (2 letter).
    String include = "minutely"; // String | Include 1 hour - minutely forecast in the response
    String marine = "t"; // String | Marine stations only (buoys, oil platforms, etc)
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback - Example - callback=func
    try {
      CurrentObsGroup result = apiInstance.currentpostalCodepostalCodeGet(postalCode, key, country, include, marine, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentWeatherDataApi#currentpostalCodepostalCodeGet");
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
| **key** | **String**| Your registered API key. | |
| **country** | **String**| Country Code (2 letter). | [optional] |
| **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] [enum: minutely] |
| **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] [enum: t] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] |

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Observation Group object. |  -  |
| **0** | No Data. |  -  |

<a id="currentstationsstationsGet"></a>
# **currentstationsstationsGet**
> CurrentObsGroup currentstationsstationsGet(stations, key, units, lang, paramCallback)

Returns a group of observations given a list of stations

Returns a group of Current Observations - Given a list of Station Call IDs. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentWeatherDataApi apiInstance = new CurrentWeatherDataApi(defaultClient);
    String stations = "stations_example"; // String | Comma separated list of Station Call ID's. Example: KRDU,KBFI,KVNY
    String key = "key_example"; // String | Your registered API key.
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      CurrentObsGroup result = apiInstance.currentstationsstationsGet(stations, key, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentWeatherDataApi#currentstationsstationsGet");
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
| **stations** | **String**| Comma separated list of Station Call ID&#39;s. Example: KRDU,KBFI,KVNY | |
| **key** | **String**| Your registered API key. | |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Observation Group object. |  -  |
| **0** | No Data. |  -  |

<a id="currentstationstationGet"></a>
# **currentstationstationGet**
> CurrentObsGroup currentstationstationGet(station, key, include, units, lang, paramCallback)

Returns a Current Observation. - Given a station ID.

Returns a Current Observation - Given a station ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentWeatherDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentWeatherDataApi apiInstance = new CurrentWeatherDataApi(defaultClient);
    String station = "station_example"; // String | Station Call ID.
    String key = "key_example"; // String | Your registered API key.
    String include = "minutely"; // String | Include 1 hour - minutely forecast in the response
    String units = "S"; // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
    String lang = "ar"; // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      CurrentObsGroup result = apiInstance.currentstationstationGet(station, key, include, units, lang, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentWeatherDataApi#currentstationstationGet");
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
| **station** | **String**| Station Call ID. | |
| **key** | **String**| Your registered API key. | |
| **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] [enum: minutely] |
| **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] [enum: S, I] |
| **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] [enum: ar, az, be, bg, bs, ca, cs, de, fi, fr, el, es, et, hr, hu, id, it, is, kw, nb, nl, pl, pt, ro, ru, sk, sl, sr, sv, tr, uk, zh, zh-tw] |
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Observation Group object. |  -  |
| **0** | No Data. |  -  |

