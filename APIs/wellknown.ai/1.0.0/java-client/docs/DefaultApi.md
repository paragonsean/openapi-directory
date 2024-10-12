# DefaultApi

All URIs are relative to *https://wellknown.ai/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPluginsGet**](DefaultApi.md#apiPluginsGet) | **GET** /api/plugins |  |


<a id="apiPluginsGet"></a>
# **apiPluginsGet**
> apiPluginsGet()



Returns a list of Wellknown ai-plugins json objects from the Wellknown ai-plugins registry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wellknown.ai/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.apiPluginsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiPluginsGet");
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
| **200** | A list of Wellknown ai-plugins json objects. |  -  |

