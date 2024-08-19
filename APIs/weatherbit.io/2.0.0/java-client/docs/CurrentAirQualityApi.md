# CurrentAirQualityApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**currentAirqualitycityIdcityIdGet**](CurrentAirQualityApi.md#currentAirqualitycityIdcityIdGet) | **GET** /current/airquality?city_id&#x3D;{city_id} | Returns current air quality conditions - Given a City ID. |
| [**currentAirqualitycitycitycountrycountryGet**](CurrentAirQualityApi.md#currentAirqualitycitycitycountrycountryGet) | **GET** /current/airquality?city&#x3D;{city}&amp;country&#x3D;{country} | Returns current air quality conditions - Given City and/or State, Country. |
| [**currentAirqualitylatlatlonlonGet**](CurrentAirQualityApi.md#currentAirqualitylatlatlonlonGet) | **GET** /current/airquality?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns current air quality conditions - Given a lat/lon. |
| [**currentAirqualitypostalCodepostalCodeGet**](CurrentAirQualityApi.md#currentAirqualitypostalCodepostalCodeGet) | **GET** /current/airquality?postal_code&#x3D;{postal_code} | Returns current air quality conditions - Given a Postal Code. |


<a id="currentAirqualitycityIdcityIdGet"></a>
# **currentAirqualitycityIdcityIdGet**
> AQCurrentGroup currentAirqualitycityIdcityIdGet(cityId, key, paramCallback)

Returns current air quality conditions - Given a City ID.

Returns current air quality conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentAirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentAirQualityApi apiInstance = new CurrentAirQualityApi(defaultClient);
    Integer cityId = 56; // Integer | City ID. Example: 4487042
    String key = "key_example"; // String | Your registered API key.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    try {
      AQCurrentGroup result = apiInstance.currentAirqualitycityIdcityIdGet(cityId, key, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentAirQualityApi#currentAirqualitycityIdcityIdGet");
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
| **paramCallback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] |

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current air quality conditions |  -  |
| **0** | No Data. |  -  |

<a id="currentAirqualitycitycitycountrycountryGet"></a>
# **currentAirqualitycitycitycountrycountryGet**
> AQCurrentGroup currentAirqualitycitycitycountrycountryGet(city, country, key, state, paramCallback)

Returns current air quality conditions - Given City and/or State, Country.

Returns current air quality conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentAirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentAirQualityApi apiInstance = new CurrentAirQualityApi(defaultClient);
    String city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    String country = "country_example"; // String | Country Code (2 letter).
    String key = "key_example"; // String | Your registered API key.
    String state = "state_example"; // String | Full name of state.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      AQCurrentGroup result = apiInstance.currentAirqualitycitycitycountrycountryGet(city, country, key, state, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentAirQualityApi#currentAirqualitycitycitycountrycountryGet");
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
| **paramCallback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] |

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current air quality conditions |  -  |
| **0** | No Data. |  -  |

<a id="currentAirqualitylatlatlonlonGet"></a>
# **currentAirqualitylatlatlonlonGet**
> AQCurrentGroup currentAirqualitylatlatlonlonGet(lat, lon, key, paramCallback)

Returns current air quality conditions - Given a lat/lon.

Returns current air quality conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentAirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentAirQualityApi apiInstance = new CurrentAirQualityApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String key = "key_example"; // String | Your registered API key.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    try {
      AQCurrentGroup result = apiInstance.currentAirqualitylatlatlonlonGet(lat, lon, key, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentAirQualityApi#currentAirqualitylatlatlonlonGet");
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
| **paramCallback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] |

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current air quality conditions |  -  |
| **0** | No Data. |  -  |

<a id="currentAirqualitypostalCodepostalCodeGet"></a>
# **currentAirqualitypostalCodepostalCodeGet**
> AQCurrentGroup currentAirqualitypostalCodepostalCodeGet(postalCode, key, country, paramCallback)

Returns current air quality conditions - Given a Postal Code.

Returns current air quality conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentAirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    CurrentAirQualityApi apiInstance = new CurrentAirQualityApi(defaultClient);
    Integer postalCode = 56; // Integer | Postal Code. Example: 28546
    String key = "key_example"; // String | Your registered API key.
    String country = "country_example"; // String | Country Code (2 letter).
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    try {
      AQCurrentGroup result = apiInstance.currentAirqualitypostalCodepostalCodeGet(postalCode, key, country, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentAirQualityApi#currentAirqualitypostalCodepostalCodeGet");
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
| **paramCallback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] |

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current air quality conditions |  -  |
| **0** | No Data. |  -  |

