# ServicesApisApi

All URIs are relative to *https://api.mon-voyage-pas-cher.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDistance**](ServicesApisApi.md#getDistance) | **GET** /distance | Calculate distance between lats/longs |
| [**getElevation**](ServicesApisApi.md#getElevation) | **GET** /elevation | Search elevation informations from lat/long |
| [**getSun**](ServicesApisApi.md#getSun) | **GET** /sun_positions | Search position of sun from lat/long and date |
| [**getTimezone**](ServicesApisApi.md#getTimezone) | **GET** /timezone | Search timezone and time informations from lat/long |


<a id="getDistance"></a>
# **getDistance**
> DistanceResponse getDistance(locationA, locationB, unit)

Calculate distance between lats/longs

This webservice is providing you the ability to calculate the distance between 2 lat/long points, it returns you the value in km or miles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    ServicesApisApi apiInstance = new ServicesApisApi(defaultClient);
    String locationA = "locationA_example"; // String | The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A
    String locationB = "locationB_example"; // String | The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B
    String unit = "kms"; // String | The unit of length you want the elevation returned either meters or feet returned
    try {
      DistanceResponse result = apiInstance.getDistance(locationA, locationB, unit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApisApi#getDistance");
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
| **locationA** | **String**| The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A | |
| **locationB** | **String**| The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B | |
| **unit** | **String**| The unit of length you want the elevation returned either meters or feet returned | [optional] [default to kms] [enum: kms, miles] |

### Return type

[**DistanceResponse**](DistanceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Forbidden |  -  |
| **500** | The error message object |  -  |

<a id="getElevation"></a>
# **getElevation**
> ElevationResponse getElevation(locations, unit)

Search elevation informations from lat/long

This webservice is providing you the ability to retrieve the elevation in meters or feet of ONE or MULTIPLE given latitude/longitude point(s). &lt;br /&gt;If you use MULTIPLE lat/long point, the maximum number of point you can send in one request is 256. Be aware that if MULTIPLE mode, the results are de-deplicated if you are sending the same latitude/longitude point multiple times.&lt;br /&gt;If your workload is a batch of millions of lat/long point, You will also get better throughput if you send around 100 lat/long points in one request than the maximum. This maximum is mostly allowed for people trying to graph altitudes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    ServicesApisApi apiInstance = new ServicesApisApi(defaultClient);
    String locations = "67.85572,20.22513"; // String | The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe ('|') character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 )
    String unit = "meters"; // String | The unit of length you want the elevation returned either meters or feet returned
    try {
      ElevationResponse result = apiInstance.getElevation(locations, unit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApisApi#getElevation");
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
| **locations** | **String**| The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe (&#39;|&#39;) character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 ) | [default to 67.85572,20.22513] |
| **unit** | **String**| The unit of length you want the elevation returned either meters or feet returned | [optional] [default to meters] [enum: meters, feet] |

### Return type

[**ElevationResponse**](ElevationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Forbidden |  -  |
| **500** | The error message object |  -  |

<a id="getSun"></a>
# **getSun**
> SunPositionResponse getSun(location, date)

Search position of sun from lat/long and date

This webservice is providing you the ability to retrieve the time of each phases of the sunlight cycle. Sunset, sunrise, sunriseEnd, golden hour, solarNoon, dawn, dusk and more for a given location and date. If the date if not provided, the response provided return informations for today at UTC time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    ServicesApisApi apiInstance = new ServicesApisApi(defaultClient);
    String location = "location_example"; // String | Here you can send either a latitude / longitude
    LocalDate date = LocalDate.now(); // LocalDate | The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used
    try {
      SunPositionResponse result = apiInstance.getSun(location, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApisApi#getSun");
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
| **location** | **String**| Here you can send either a latitude / longitude | |
| **date** | **LocalDate**| The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used | [optional] |

### Return type

[**SunPositionResponse**](SunPositionResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Forbidden |  -  |
| **500** | The error message object |  -  |

<a id="getTimezone"></a>
# **getTimezone**
> TimezoneResponse getTimezone(location)

Search timezone and time informations from lat/long

This webservice is providing you the ability to retrieve the tz database time zones ( https://en.wikipedia.org/wiki/List_of_tz_database_time_zones )  from a given location ( )latitude and longitude or IATA code ). It also returns you the current time at the provided location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    ServicesApisApi apiInstance = new ServicesApisApi(defaultClient);
    String location = "45.8326307,6.8650517"; // String | Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow)
    try {
      TimezoneResponse result = apiInstance.getTimezone(location);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApisApi#getTimezone");
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
| **location** | **String**| Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow) | [default to 45.8326307,6.8650517] |

### Return type

[**TimezoneResponse**](TimezoneResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Forbidden |  -  |
| **500** | The error message object |  -  |

