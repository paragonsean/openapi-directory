# AdditionalDeviceInformationApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**additionalDeviceInformationGet**](AdditionalDeviceInformationApi.md#additionalDeviceInformationGet) | **GET** /api/AdditionalDeviceInformation/{id} | Gets the additional information (e.g. Firmware Version) about a device. |


<a id="additionalDeviceInformationGet"></a>
# **additionalDeviceInformationGet**
> AdditionalDeviceInformation additionalDeviceInformationGet(id)

Gets the additional information (e.g. Firmware Version) about a device.

Gets the additional information (e.g. Firmware Version) about a device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdditionalDeviceInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    AdditionalDeviceInformationApi apiInstance = new AdditionalDeviceInformationApi(defaultClient);
    String id = "id_example"; // String | The ID of the device
    try {
      AdditionalDeviceInformation result = apiInstance.additionalDeviceInformationGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdditionalDeviceInformationApi#additionalDeviceInformationGet");
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
| **id** | **String**| The ID of the device | |

### Return type

[**AdditionalDeviceInformation**](AdditionalDeviceInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

