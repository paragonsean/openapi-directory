# DeviceApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**detectDevice**](DeviceApi.md#detectDevice) | **POST** /device/detect | Detect iot device by service banners and mac address |


<a id="detectDevice"></a>
# **detectDevice**
> DeviceInfo detectDevice(deviceFeatures)

Detect iot device by service banners and mac address

Use device service banners and mac address captured by your network port scanner, vulnerability assessment or asset discovery tools to detect device maker, model and firmware information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: api-key-header
    ApiKeyAuth api-key-header = (ApiKeyAuth) defaultClient.getAuthentication("api-key-header");
    api-key-header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key-header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    DeviceFeatures deviceFeatures = new DeviceFeatures(); // DeviceFeatures | 
    try {
      DeviceInfo result = apiInstance.detectDevice(deviceFeatures);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#detectDevice");
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
| **deviceFeatures** | [**DeviceFeatures**](DeviceFeatures.md)|  | |

### Return type

[**DeviceInfo**](DeviceInfo.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

