# PerfApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idGetAllPerfResults**](PerfApiApi.md#idGetAllPerfResults) | **GET** /api/perf/profile/result | Handles GET requests for perf results |
| [**idGetSinglePerfResult**](PerfApiApi.md#idGetSinglePerfResult) | **GET** /api/perf/profile/result/{id} | Handles GET requests for perf result |
| [**idRunPerfTest**](PerfApiApi.md#idRunPerfTest) | **GET** /api/perf/profile | Handle GET request to run a test |


<a id="idGetAllPerfResults"></a>
# **idGetAllPerfResults**
> PerformanceResultsAPIResponse idGetAllPerfResults()

Handles GET requests for perf results

Returns pages of all the perf results from Remote Provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerfApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerfApiApi apiInstance = new PerfApiApi(defaultClient);
    try {
      PerformanceResultsAPIResponse result = apiInstance.idGetAllPerfResults();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerfApiApi#idGetAllPerfResults");
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

[**PerformanceResultsAPIResponse**](PerformanceResultsAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all performance results |  -  |

<a id="idGetSinglePerfResult"></a>
# **idGetSinglePerfResult**
> PerformanceSpec idGetSinglePerfResult(id)

Handles GET requests for perf result

Returns an individual result from provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerfApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerfApiApi apiInstance = new PerfApiApi(defaultClient);
    String id = "id_example"; // String | Automatically added
    try {
      PerformanceSpec result = apiInstance.idGetSinglePerfResult(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerfApiApi#idGetSinglePerfResult");
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
| **id** | **String**| Automatically added | |

### Return type

[**PerformanceSpec**](PerformanceSpec.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns Single test result |  -  |

<a id="idRunPerfTest"></a>
# **idRunPerfTest**
> idRunPerfTest(performanceTestConfig)

Handle GET request to run a test

Runs the load test with the given parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PerfApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    PerfApiApi apiInstance = new PerfApiApi(defaultClient);
    PerformanceTestConfig performanceTestConfig = new PerformanceTestConfig(); // PerformanceTestConfig | 
    try {
      apiInstance.idRunPerfTest(performanceTestConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling PerfApiApi#idRunPerfTest");
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
| **performanceTestConfig** | [**PerformanceTestConfig**](PerformanceTestConfig.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

