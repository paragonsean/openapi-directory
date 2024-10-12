# DefaultApi

All URIs are relative to *https://api.transavia.com/v2/airports*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**call58d8bcb7a9e6240e200cff24**](DefaultApi.md#call58d8bcb7a9e6240e200cff24) | **GET** / | All airports |
| [**call58d8bcb7a9e6240e200cff25**](DefaultApi.md#call58d8bcb7a9e6240e200cff25) | **GET** /{id} | Airport by id. |
| [**call58d8bcb8a9e6240e200cff26**](DefaultApi.md#call58d8bcb8a9e6240e200cff26) | **GET** /countrycode/{countryCode} | Airport(s) by country code. |
| [**call58d8bcb8a9e6240e200cff27**](DefaultApi.md#call58d8bcb8a9e6240e200cff27) | **GET** /nearest | Nearest airport(s) by geo coordinates. |
| [**call58d8bcb8a9e6240e200cff28**](DefaultApi.md#call58d8bcb8a9e6240e200cff28) | **GET** /nearest/{id} | Nearest airport(s) by airport id. |


<a id="call58d8bcb7a9e6240e200cff24"></a>
# **call58d8bcb7a9e6240e200cff24**
> List&lt;AirportDto&gt; call58d8bcb7a9e6240e200cff24()

All airports

Retrieve all airports.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transavia.com/v2/airports");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<AirportDto> result = apiInstance.call58d8bcb7a9e6240e200cff24();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58d8bcb7a9e6240e200cff24");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;AirportDto&gt;**](AirportDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **500** | InternalServerError |  -  |

<a id="call58d8bcb7a9e6240e200cff25"></a>
# **call58d8bcb7a9e6240e200cff25**
> AirportDetailsDto call58d8bcb7a9e6240e200cff25(id)

Airport by id.

Retrieve airport by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transavia.com/v2/airports");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Airport code (3-character IATA code).
    try {
      AirportDetailsDto result = apiInstance.call58d8bcb7a9e6240e200cff25(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58d8bcb7a9e6240e200cff25");
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
| **id** | **String**| Airport code (3-character IATA code). | |

### Return type

[**AirportDetailsDto**](AirportDetailsDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **500** | InternalServerError |  -  |

<a id="call58d8bcb8a9e6240e200cff26"></a>
# **call58d8bcb8a9e6240e200cff26**
> List&lt;AirportDto&gt; call58d8bcb8a9e6240e200cff26(countryCode)

Airport(s) by country code.

Retrieve airports by country code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transavia.com/v2/airports");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Comma-separated list of country codes (2-character ISO 3166-1). More than 3 country codes is not allowed.
    try {
      List<AirportDto> result = apiInstance.call58d8bcb8a9e6240e200cff26(countryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58d8bcb8a9e6240e200cff26");
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
| **countryCode** | **String**| Comma-separated list of country codes (2-character ISO 3166-1). More than 3 country codes is not allowed. | |

### Return type

[**List&lt;AirportDto&gt;**](AirportDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **500** | InternalServerError |  -  |

<a id="call58d8bcb8a9e6240e200cff27"></a>
# **call58d8bcb8a9e6240e200cff27**
> List&lt;NearestAirportDto&gt; call58d8bcb8a9e6240e200cff27(latitude, longitude, maxDistanceInKm, limit)

Nearest airport(s) by geo coordinates.

Retrieve nearest airports by geo coordinates (latitude/longitude).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transavia.com/v2/airports");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String latitude = "latitude_example"; // String | Latitude in decimals, lower than -90.0 and higher than 90.0 is not allowed.
    String longitude = "longitude_example"; // String | Longitude in decimals, lower than -180.0 and higher than 180.0 is not allowed.
    String maxDistanceInKm = "maxDistanceInKm_example"; // String | Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied.
    String limit = "limit_example"; // String | Limits the result, lower than 0 is not allowed. If not set, the result is not limited.
    try {
      List<NearestAirportDto> result = apiInstance.call58d8bcb8a9e6240e200cff27(latitude, longitude, maxDistanceInKm, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58d8bcb8a9e6240e200cff27");
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
| **latitude** | **String**| Latitude in decimals, lower than -90.0 and higher than 90.0 is not allowed. | [optional] |
| **longitude** | **String**| Longitude in decimals, lower than -180.0 and higher than 180.0 is not allowed. | [optional] |
| **maxDistanceInKm** | **String**| Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied. | [optional] |
| **limit** | **String**| Limits the result, lower than 0 is not allowed. If not set, the result is not limited. | [optional] |

### Return type

[**List&lt;NearestAirportDto&gt;**](NearestAirportDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **500** | InternalServerError |  -  |

<a id="call58d8bcb8a9e6240e200cff28"></a>
# **call58d8bcb8a9e6240e200cff28**
> List&lt;NearestAirportDto&gt; call58d8bcb8a9e6240e200cff28(id, maxDistanceInKm, limit)

Nearest airport(s) by airport id.

Retrieve nearest airports by station id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.transavia.com/v2/airports");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Airport (IATA code) to search nearest airports for.
    String maxDistanceInKm = "maxDistanceInKm_example"; // String | Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied.
    String limit = "limit_example"; // String | Limits the result, lower than 0 is not allowed. If not set, the result is not limited.
    try {
      List<NearestAirportDto> result = apiInstance.call58d8bcb8a9e6240e200cff28(id, maxDistanceInKm, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58d8bcb8a9e6240e200cff28");
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
| **id** | **String**| Airport (IATA code) to search nearest airports for. | |
| **maxDistanceInKm** | **String**| Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied. | [optional] |
| **limit** | **String**| Limits the result, lower than 0 is not allowed. If not set, the result is not limited. | [optional] |

### Return type

[**List&lt;NearestAirportDto&gt;**](NearestAirportDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **500** | InternalServerError |  -  |

