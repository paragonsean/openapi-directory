# SystemApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**healthCheckPingGet**](SystemApi.md#healthCheckPingGet) | **GET** /health-check/ping | Health check for API |


<a id="healthCheckPingGet"></a>
# **healthCheckPingGet**
> healthCheckPingGet()

Health check for API

Provides a response for automatic checks that the API and load balancers are healthy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      apiInstance.healthCheckPingGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#healthCheckPingGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API is healthy |  -  |
| **503** | Load balancers cannot route a request to a healthy API server |  -  |

