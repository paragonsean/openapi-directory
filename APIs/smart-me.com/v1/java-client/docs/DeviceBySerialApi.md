# DeviceBySerialApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deviceBySerialGet**](DeviceBySerialApi.md#deviceBySerialGet) | **GET** /api/DeviceBySerial | Gets a Device by it&#39;s Serial Number. The Serial is the part before the \&quot;-\&quot;. |


<a id="deviceBySerialGet"></a>
# **deviceBySerialGet**
> Device deviceBySerialGet(serial)

Gets a Device by it&#39;s Serial Number. The Serial is the part before the \&quot;-\&quot;.

Gets a Device by it&#39;s Serial Number. The Serial is the part before the \&quot;-\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceBySerialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    DeviceBySerialApi apiInstance = new DeviceBySerialApi(defaultClient);
    Long serial = 56L; // Long | The Serial Number of the device
    try {
      Device result = apiInstance.deviceBySerialGet(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceBySerialApi#deviceBySerialGet");
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
| **serial** | **Long**| The Serial Number of the device | |

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

