# MetricsApi

All URIs are relative to *http://microcks.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAggregatedInvocationsStats**](MetricsApi.md#getAggregatedInvocationsStats) | **GET** /metrics/invocations/global | Get aggregated invocation statistics for a day |
| [**getConformanceMetricsAggregation**](MetricsApi.md#getConformanceMetricsAggregation) | **GET** /metrics/conformance/aggregate | Get aggregation of conformance metrics |
| [**getInvocationStatsByService**](MetricsApi.md#getInvocationStatsByService) | **GET** /metrics/invocations/{serviceName}/{serviceVersion} | Get invocation statistics for Service |
| [**getLatestAggregatedInvocationsStats**](MetricsApi.md#getLatestAggregatedInvocationsStats) | **GET** /metrics/invocations/global/latest | Get aggregated invocations statistics for latest days |
| [**getLatestTestResults**](MetricsApi.md#getLatestTestResults) | **GET** /metrics/tests/latest | Get latest tests results |
| [**getServiceTestConformanceMetric**](MetricsApi.md#getServiceTestConformanceMetric) | **GET** /metrics/conformance/service/{serviceId} | Get conformance metrics for a Service |
| [**getTopIvnocationsStatsByDay**](MetricsApi.md#getTopIvnocationsStatsByDay) | **GET** /metrics/invocations/top | Get top invocation statistics for a day |


<a id="getAggregatedInvocationsStats"></a>
# **getAggregatedInvocationsStats**
> DailyInvocationStatistic getAggregatedInvocationsStats(day)

Get aggregated invocation statistics for a day

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String day = "day_example"; // String | The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    try {
      DailyInvocationStatistic result = apiInstance.getAggregatedInvocationsStats(day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getAggregatedInvocationsStats");
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
| **day** | **String**| The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided. | [optional] |

### Return type

[**DailyInvocationStatistic**](DailyInvocationStatistic.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Aggregated invocation statistics for specified day |  -  |

<a id="getConformanceMetricsAggregation"></a>
# **getConformanceMetricsAggregation**
> List&lt;WeightedMetricValue&gt; getConformanceMetricsAggregation()

Get aggregation of conformance metrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    try {
      List<WeightedMetricValue> result = apiInstance.getConformanceMetricsAggregation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getConformanceMetricsAggregation");
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

[**List&lt;WeightedMetricValue&gt;**](WeightedMetricValue.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get aggregated coverage metric value |  -  |

<a id="getInvocationStatsByService"></a>
# **getInvocationStatsByService**
> DailyInvocationStatistic getInvocationStatsByService(serviceName, serviceVersion, day)

Get invocation statistics for Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | Name of service to get statistics for
    String serviceVersion = "serviceVersion_example"; // String | Version of service to get statistics for
    String day = "day_example"; // String | The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    try {
      DailyInvocationStatistic result = apiInstance.getInvocationStatsByService(serviceName, serviceVersion, day);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getInvocationStatsByService");
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
| **serviceName** | **String**| Name of service to get statistics for | |
| **serviceVersion** | **String**| Version of service to get statistics for | |
| **day** | **String**| The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided. | [optional] |

### Return type

[**DailyInvocationStatistic**](DailyInvocationStatistic.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invocation statistics for service for specified day |  -  |

<a id="getLatestAggregatedInvocationsStats"></a>
# **getLatestAggregatedInvocationsStats**
> Map&lt;String, BigDecimal&gt; getLatestAggregatedInvocationsStats(limit)

Get aggregated invocations statistics for latest days

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer limit = 56; // Integer | Number of days to get back in time. Default is 20.
    try {
      Map<String, BigDecimal> result = apiInstance.getLatestAggregatedInvocationsStats(limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getLatestAggregatedInvocationsStats");
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
| **limit** | **Integer**| Number of days to get back in time. Default is 20. | [optional] |

### Return type

[**Map&lt;String, BigDecimal&gt;**](BigDecimal.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A map where keys are day (formatted using yyyyMMdd pattern) and values are counter of invocations on this day |  -  |

<a id="getLatestTestResults"></a>
# **getLatestTestResults**
> List&lt;TestResultSummary&gt; getLatestTestResults(limit)

Get latest tests results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    Integer limit = 56; // Integer | Number of days to consider for test results to return. Default is 7 (one week)
    try {
      List<TestResultSummary> result = apiInstance.getLatestTestResults(limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getLatestTestResults");
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
| **limit** | **Integer**| Number of days to consider for test results to return. Default is 7 (one week) | [optional] |

### Return type

[**List&lt;TestResultSummary&gt;**](TestResultSummary.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test results summary for specified &lt;limit&gt; last days. |  -  |

<a id="getServiceTestConformanceMetric"></a>
# **getServiceTestConformanceMetric**
> TestConformanceMetric getServiceTestConformanceMetric(serviceId)

Get conformance metrics for a Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Unique Services identifier this metrics are related to
    try {
      TestConformanceMetric result = apiInstance.getServiceTestConformanceMetric(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getServiceTestConformanceMetric");
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
| **serviceId** | **String**| Unique Services identifier this metrics are related to | |

### Return type

[**TestConformanceMetric**](TestConformanceMetric.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test coverage metric for Service |  -  |

<a id="getTopIvnocationsStatsByDay"></a>
# **getTopIvnocationsStatsByDay**
> List&lt;DailyInvocationStatistic&gt; getTopIvnocationsStatsByDay(day, limit)

Get top invocation statistics for a day

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String day = "day_example"; // String | The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
    Integer limit = 56; // Integer | The number of top invoked mocks to return
    try {
      List<DailyInvocationStatistic> result = apiInstance.getTopIvnocationsStatsByDay(day, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getTopIvnocationsStatsByDay");
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
| **day** | **String**| The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided. | [optional] |
| **limit** | **Integer**| The number of top invoked mocks to return | [optional] |

### Return type

[**List&lt;DailyInvocationStatistic&gt;**](DailyInvocationStatistic.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top invocations for a defined day |  -  |

