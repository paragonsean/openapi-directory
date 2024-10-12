# LoggingApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadLogJson**](LoggingApi.md#downloadLogJson) | **GET** /v1/logging/groovLogs.json |  |
| [**downloadLogText**](LoggingApi.md#downloadLogText) | **GET** /v1/logging/groovLogs.txt |  |


<a id="downloadLogJson"></a>
# **downloadLogJson**
> File downloadLogJson(minimumLogLevel, lastTimestamp, filter)



Downloads the complete groov View log in JSON format. Added in groov View R4.2a.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoggingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LoggingApi apiInstance = new LoggingApi(defaultClient);
    String minimumLogLevel = "TRACE"; // String | How verbose the log should be.
    BigDecimal lastTimestamp = new BigDecimal("0.0"); // BigDecimal | The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC.
    String filter = "filter_example"; // String | Optional string to search for in the log.
    try {
      File result = apiInstance.downloadLogJson(minimumLogLevel, lastTimestamp, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoggingApi#downloadLogJson");
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
| **minimumLogLevel** | **String**| How verbose the log should be. | [optional] [default to INFO] [enum: TRACE, DEBUG, INFO, WARN, ERROR, FATAL] |
| **lastTimestamp** | **BigDecimal**| The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC. | [optional] [default to 0.0] |
| **filter** | **String**| Optional string to search for in the log. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Downloaded log file. |  -  |

<a id="downloadLogText"></a>
# **downloadLogText**
> File downloadLogText(minimumLogLevel, lastTimestamp, filter)



Downloads the complete groov View log. Added in groov View R4.2a.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoggingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LoggingApi apiInstance = new LoggingApi(defaultClient);
    String minimumLogLevel = "TRACE"; // String | How verbose the log should be.
    BigDecimal lastTimestamp = new BigDecimal("0.0"); // BigDecimal | The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC.
    String filter = "filter_example"; // String | Optional string to search for in the log.
    try {
      File result = apiInstance.downloadLogText(minimumLogLevel, lastTimestamp, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoggingApi#downloadLogText");
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
| **minimumLogLevel** | **String**| How verbose the log should be. | [optional] [default to INFO] [enum: TRACE, DEBUG, INFO, WARN, ERROR, FATAL] |
| **lastTimestamp** | **BigDecimal**| The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC. | [optional] [default to 0.0] |
| **filter** | **String**| Optional string to search for in the log. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Downloaded log file. |  -  |

