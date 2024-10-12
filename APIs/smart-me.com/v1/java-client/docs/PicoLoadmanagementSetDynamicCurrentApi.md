# PicoLoadmanagementSetDynamicCurrentApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**picoLoadmanagementSetDynamicCurrentPost**](PicoLoadmanagementSetDynamicCurrentApi.md#picoLoadmanagementSetDynamicCurrentPost) | **POST** /api/pico/loadmanagementgroup/current/{serial} | Sets the dynamic current of a load management group or a single station. |


<a id="picoLoadmanagementSetDynamicCurrentPost"></a>
# **picoLoadmanagementSetDynamicCurrentPost**
> Object picoLoadmanagementSetDynamicCurrentPost(serial, current)

Sets the dynamic current of a load management group or a single station.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PicoLoadmanagementSetDynamicCurrentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    PicoLoadmanagementSetDynamicCurrentApi apiInstance = new PicoLoadmanagementSetDynamicCurrentApi(defaultClient);
    Long serial = 56L; // Long | The serial number can be any pico serial in the group (e.g. 700001)
    Integer current = 56; // Integer | The dynamic current of the group (in mA)
    try {
      Object result = apiInstance.picoLoadmanagementSetDynamicCurrentPost(serial, current);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PicoLoadmanagementSetDynamicCurrentApi#picoLoadmanagementSetDynamicCurrentPost");
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
| **serial** | **Long**| The serial number can be any pico serial in the group (e.g. 700001) | |
| **current** | **Integer**| The dynamic current of the group (in mA) | |

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

