# ModulesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backendModuleServiceV1GetModulesGet**](ModulesApi.md#backendModuleServiceV1GetModulesGet) | **GET** /V1/modules | modules |


<a id="backendModuleServiceV1GetModulesGet"></a>
# **backendModuleServiceV1GetModulesGet**
> List&lt;String&gt; backendModuleServiceV1GetModulesGet()

modules

Returns an array of enabled modules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ModulesApi apiInstance = new ModulesApi(defaultClient);
    try {
      List<String> result = apiInstance.backendModuleServiceV1GetModulesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModulesApi#backendModuleServiceV1GetModulesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

