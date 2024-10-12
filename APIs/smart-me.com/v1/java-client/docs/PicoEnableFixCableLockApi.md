# PicoEnableFixCableLockApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**picoEnableFixCableLockPost**](PicoEnableFixCableLockApi.md#picoEnableFixCableLockPost) | **POST** /api/pico/tryenablecablelock/{id} | Try to fix lock the cable of a pico. The pico must be online and a cable (without car) needs to be connected. Otherwise this will fail. |


<a id="picoEnableFixCableLockPost"></a>
# **picoEnableFixCableLockPost**
> Object picoEnableFixCableLockPost(id)

Try to fix lock the cable of a pico. The pico must be online and a cable (without car) needs to be connected. Otherwise this will fail.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PicoEnableFixCableLockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    PicoEnableFixCableLockApi apiInstance = new PicoEnableFixCableLockApi(defaultClient);
    String id = "id_example"; // String | The ID of the pico
    try {
      Object result = apiInstance.picoEnableFixCableLockPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PicoEnableFixCableLockApi#picoEnableFixCableLockPost");
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
| **id** | **String**| The ID of the pico | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

