# HealthApi

All URIs are relative to *http://hashtag.peel-ci.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHealth**](HealthApi.md#getHealth) | **GET** /health | Get health of Tune-in service (which includes its uptime). |


<a id="getHealth"></a>
# **getHealth**
> getHealth()

Get health of Tune-in service (which includes its uptime).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://hashtag.peel-ci.com");

    HealthApi apiInstance = new HealthApi(defaultClient);
    try {
      apiInstance.getHealth();
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthApi#getHealth");
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
| **200** | No response was specified |  -  |

