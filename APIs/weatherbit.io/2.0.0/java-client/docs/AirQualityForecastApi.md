# AirQualityForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forecastAirqualitycityIdcityIdGet**](AirQualityForecastApi.md#forecastAirqualitycityIdcityIdGet) | **GET** /forecast/airquality?city_id&#x3D;{city_id} | Returns 72 hour (hourly) Air Quality forecast - Given a City ID. |
| [**forecastAirqualitycitycitycountrycountryGet**](AirQualityForecastApi.md#forecastAirqualitycitycitycountrycountryGet) | **GET** /forecast/airquality?city&#x3D;{city}&amp;country&#x3D;{country} | Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country. |
| [**forecastAirqualitylatlatlonlonGet**](AirQualityForecastApi.md#forecastAirqualitylatlatlonlonGet) | **GET** /forecast/airquality?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon. |
| [**forecastAirqualitypostalCodepostalCodeGet**](AirQualityForecastApi.md#forecastAirqualitypostalCodepostalCodeGet) | **GET** /forecast/airquality?postal_code&#x3D;{postal_code} | Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code. |


<a id="forecastAirqualitycityIdcityIdGet"></a>
# **forecastAirqualitycityIdcityIdGet**
> AQHourly forecastAirqualitycityIdcityIdGet(cityId, key, paramCallback, hours)

Returns 72 hour (hourly) Air Quality forecast - Given a City ID.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirQualityForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    AirQualityForecastApi apiInstance = new AirQualityForecastApi(defaultClient);
    Integer cityId = 56; // Integer | City ID. Example: 4487042
    String key = "key_example"; // String | Your registered API key.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    Integer hours = 56; // Integer | Number of hours to return.
    try {
      AQHourly result = apiInstance.forecastAirqualitycityIdcityIdGet(cityId, key, paramCallback, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirQualityForecastApi#forecastAirqualitycityIdcityIdGet");
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
| **hours** | **Integer**| Number of hours to return. | [optional] |

### Return type

[**AQHourly**](AQHourly.md)

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

<a id="forecastAirqualitycitycitycountrycountryGet"></a>
# **forecastAirqualitycitycitycountrycountryGet**
> AQHourly forecastAirqualitycitycitycountrycountryGet(city, country, key, state, paramCallback, hours)

Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirQualityForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    AirQualityForecastApi apiInstance = new AirQualityForecastApi(defaultClient);
    String city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    String country = "country_example"; // String | Country Code (2 letter).
    String key = "key_example"; // String | Your registered API key.
    String state = "state_example"; // String | Full name of state.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example: callback=func
    Integer hours = 56; // Integer | Number of hours to return.
    try {
      AQHourly result = apiInstance.forecastAirqualitycitycitycountrycountryGet(city, country, key, state, paramCallback, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirQualityForecastApi#forecastAirqualitycitycitycountrycountryGet");
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
| **hours** | **Integer**| Number of hours to return. | [optional] |

### Return type

[**AQHourly**](AQHourly.md)

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

<a id="forecastAirqualitylatlatlonlonGet"></a>
# **forecastAirqualitylatlatlonlonGet**
> AQHourly forecastAirqualitylatlatlonlonGet(lat, lon, key, paramCallback, hours)

Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirQualityForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    AirQualityForecastApi apiInstance = new AirQualityForecastApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String key = "key_example"; // String | Your registered API key.
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    Integer hours = 56; // Integer | Number of hours to return.
    try {
      AQHourly result = apiInstance.forecastAirqualitylatlatlonlonGet(lat, lon, key, paramCallback, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirQualityForecastApi#forecastAirqualitylatlatlonlonGet");
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
| **hours** | **Integer**| Number of hours to return. | [optional] |

### Return type

[**AQHourly**](AQHourly.md)

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

<a id="forecastAirqualitypostalCodepostalCodeGet"></a>
# **forecastAirqualitypostalCodepostalCodeGet**
> AQHourly forecastAirqualitypostalCodepostalCodeGet(postalCode, key, country, paramCallback, hours)

Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirQualityForecastApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    AirQualityForecastApi apiInstance = new AirQualityForecastApi(defaultClient);
    Integer postalCode = 56; // Integer | Postal Code. Example: 28546
    String key = "key_example"; // String | Your registered API key.
    String country = "country_example"; // String | Country Code (2 letter).
    String paramCallback = "paramCallback_example"; // String | Wraps return in jsonp callback. Example - callback=func
    Integer hours = 56; // Integer | Number of hours to return.
    try {
      AQHourly result = apiInstance.forecastAirqualitypostalCodepostalCodeGet(postalCode, key, country, paramCallback, hours);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirQualityForecastApi#forecastAirqualitypostalCodepostalCodeGet");
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
| **hours** | **Integer**| Number of hours to return. | [optional] |

### Return type

[**AQHourly**](AQHourly.md)

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

