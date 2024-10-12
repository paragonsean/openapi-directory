# FastSendDeviceValuesApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fastSendDeviceValuesGet**](FastSendDeviceValuesApi.md#fastSendDeviceValuesGet) | **GET** /api/FastSendDeviceValues/{id} | Force a device to send the data every second (if supported). This for about 30s.              Don&#39;t use this call to force a device to send the data every second for a longer time. |


<a id="fastSendDeviceValuesGet"></a>
# **fastSendDeviceValuesGet**
> fastSendDeviceValuesGet(id)

Force a device to send the data every second (if supported). This for about 30s.              Don&#39;t use this call to force a device to send the data every second for a longer time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FastSendDeviceValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    FastSendDeviceValuesApi apiInstance = new FastSendDeviceValuesApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.fastSendDeviceValuesGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FastSendDeviceValuesApi#fastSendDeviceValuesGet");
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
| **id** | **String**|  | |

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
| **204** | No Content |  -  |

