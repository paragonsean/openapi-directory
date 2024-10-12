# MetricsApi

All URIs are relative to *http://1password.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPrometheusMetrics**](MetricsApi.md#getPrometheusMetrics) | **GET** /metrics | Query server for exposed Prometheus metrics |


<a id="getPrometheusMetrics"></a>
# **getPrometheusMetrics**
> String getPrometheusMetrics()

Query server for exposed Prometheus metrics

See Prometheus documentation for a complete data model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://1password.local");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    try {
      String result = apiInstance.getPrometheusMetrics();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#getPrometheusMetrics");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully returned Prometheus metrics |  -  |

