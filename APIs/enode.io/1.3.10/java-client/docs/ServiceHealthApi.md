# ServiceHealthApi

All URIs are relative to *https://api.test.enode.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHealthReady**](ServiceHealthApi.md#getHealthReady) | **GET** /health/ready | Check Service Readiness |
| [**getHealthVendors**](ServiceHealthApi.md#getHealthVendors) | **GET** /health/vendors | Check Available Vendors |


<a id="getHealthReady"></a>
# **getHealthReady**
> getHealthReady()

Check Service Readiness

Gets the combined health status of the service and all functionalities and dependencies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceHealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");

    ServiceHealthApi apiInstance = new ServiceHealthApi(defaultClient);
    try {
      apiInstance.getHealthReady();
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceHealthApi#getHealthReady");
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | All functionalities are operating nominally |  -  |
| **503** | At least one functionality of the system is not operating nominally |  -  |

<a id="getHealthVendors"></a>
# **getHealthVendors**
> List&lt;GetHealthVendors200ResponseInner&gt; getHealthVendors()

Check Available Vendors

List the supported vendors and their current status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceHealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");

    ServiceHealthApi apiInstance = new ServiceHealthApi(defaultClient);
    try {
      List<GetHealthVendors200ResponseInner> result = apiInstance.getHealthVendors();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceHealthApi#getHealthVendors");
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

[**List&lt;GetHealthVendors200ResponseInner&gt;**](GetHealthVendors200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

