# HistoricalAirQualityApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**historyAirqualitycityIdcityIdGet**](HistoricalAirQualityApi.md#historyAirqualitycityIdcityIdGet) | **GET** /history/airquality?city_id&#x3D;{city_id} | Returns 72 hours of historical air quality conditions - Given a City ID. |
| [**historyAirqualitycitycitycountrycountryGet**](HistoricalAirQualityApi.md#historyAirqualitycitycitycountrycountryGet) | **GET** /history/airquality?city&#x3D;{city}&amp;country&#x3D;{country} | Returns 72 hours of historical quality conditions - Given City and/or State, Country. |
| [**historyAirqualitylatlatlonlonGet**](HistoricalAirQualityApi.md#historyAirqualitylatlatlonlonGet) | **GET** /history/airquality?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns 72 hours of historical air quality conditions - Given a lat/lon. |
| [**historyAirqualitypostalCodepostalCodeGet**](HistoricalAirQualityApi.md#historyAirqualitypostalCodepostalCodeGet) | **GET** /history/airquality?postal_code&#x3D;{postal_code} | Returns 72 hours of historical air quality conditions - Given a Postal Code. |


<a id="historyAirqualitycityIdcityIdGet"></a>
# **historyAirqualitycityIdcityIdGet**
> AQCurrentGroup historyAirqualitycityIdcityIdGet(cityId, key, paramCallback)

Returns 72 hours of historical air quality conditions - Given a City ID.

Returns historical air quality conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoricalAirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    HistoricalAirQualityApi apiInstance = new HistoricalAirQualityApi(defaultClient);
    Double cityId = 3.4D; // Double | City ID.
    String key = "key_example"; // String | Your registered API key.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    try {
      AQCurrentGroup result = apiInstance.historyAirqualitycityIdcityIdGet(cityId, key, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoricalAirQualityApi#historyAirqualitycityIdcityIdGet");
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
| **cityId** | **Double**| City ID. | |
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
| **200** | Historical air quality conditions |  -  |
| **0** | No Data. |  -  |

<a id="historyAirqualitycitycitycountrycountryGet"></a>
# **historyAirqualitycitycitycountrycountryGet**
> AQCurrentGroup historyAirqualitycitycitycountrycountryGet(city, country, key, state, paramCallback)

Returns 72 hours of historical quality conditions - Given City and/or State, Country.

Returns historical air quality conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoricalAirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    HistoricalAirQualityApi apiInstance = new HistoricalAirQualityApi(defaultClient);
    String city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    String country = "country_example"; // String | Country Code (2 letter).
    String key = "key_example"; // String | Your registered API key.
    String state = "state_example"; // String | Full name of state.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    try {
      AQCurrentGroup result = apiInstance.historyAirqualitycitycitycountrycountryGet(city, country, key, state, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoricalAirQualityApi#historyAirqualitycitycitycountrycountryGet");
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
| **200** | Historical air quality conditions |  -  |
| **0** | No Data. |  -  |

<a id="historyAirqualitylatlatlonlonGet"></a>
# **historyAirqualitylatlatlonlonGet**
> AQCurrentGroup historyAirqualitylatlatlonlonGet(lat, lon, key, paramCallback)

Returns 72 hours of historical air quality conditions - Given a lat/lon.

Returns historical air quality conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoricalAirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    HistoricalAirQualityApi apiInstance = new HistoricalAirQualityApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String key = "key_example"; // String | Your registered API key.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    try {
      AQCurrentGroup result = apiInstance.historyAirqualitylatlatlonlonGet(lat, lon, key, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoricalAirQualityApi#historyAirqualitylatlatlonlonGet");
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
| **200** | Historical air quality conditions |  -  |
| **0** | No Data. |  -  |

<a id="historyAirqualitypostalCodepostalCodeGet"></a>
# **historyAirqualitypostalCodepostalCodeGet**
> AQCurrentGroup historyAirqualitypostalCodepostalCodeGet(postalCode, key, country, paramCallback)

Returns 72 hours of historical air quality conditions - Given a Postal Code.

Returns historical air quality conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoricalAirQualityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    HistoricalAirQualityApi apiInstance = new HistoricalAirQualityApi(defaultClient);
    Integer postalCode = 56; // Integer | Postal Code. Example: 28546
    String key = "key_example"; // String | Your registered API key.
    String country = "country_example"; // String | Country Code (2 letter).
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    try {
      AQCurrentGroup result = apiInstance.historyAirqualitypostalCodepostalCodeGet(postalCode, key, country, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoricalAirQualityApi#historyAirqualitypostalCodepostalCodeGet");
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
| **200** | Historical air quality conditions |  -  |
| **0** | No Data. |  -  |

