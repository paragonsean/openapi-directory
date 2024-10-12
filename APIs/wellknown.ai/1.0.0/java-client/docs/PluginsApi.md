# PluginsApi

All URIs are relative to *https://wellknown.ai/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProvider**](PluginsApi.md#getProvider) | **GET** /plugins | List all the Wellknown AI Plugins. |


<a id="getProvider"></a>
# **getProvider**
> getProvider()

List all the Wellknown AI Plugins.

List all the Wellknown AI Plugins. Returns ai-plugin.json objects in an array

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wellknown.ai/api");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    try {
      apiInstance.getProvider();
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#getProvider");
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
| **200** | OK |  -  |

