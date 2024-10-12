# PingDeviceApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceLiveToolsPingDevice_1**](PingDeviceApi.md#createDeviceLiveToolsPingDevice_1) | **POST** /devices/{serial}/liveTools/pingDevice | Enqueue a job to check connectivity status to the device |
| [**getDeviceLiveToolsPingDevice_1**](PingDeviceApi.md#getDeviceLiveToolsPingDevice_1) | **GET** /devices/{serial}/liveTools/pingDevice/{id} | Return a ping device job |


<a id="createDeviceLiveToolsPingDevice_1"></a>
# **createDeviceLiveToolsPingDevice_1**
> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPingDevice_1(serial, createDeviceLiveToolsPingDeviceRequest)

Enqueue a job to check connectivity status to the device

Enqueue a job to check connectivity status to the device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PingDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PingDeviceApi apiInstance = new PingDeviceApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceLiveToolsPingDeviceRequest createDeviceLiveToolsPingDeviceRequest = new CreateDeviceLiveToolsPingDeviceRequest(); // CreateDeviceLiveToolsPingDeviceRequest | 
    try {
      CreateDeviceLiveToolsPing201Response result = apiInstance.createDeviceLiveToolsPingDevice_1(serial, createDeviceLiveToolsPingDeviceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PingDeviceApi#createDeviceLiveToolsPingDevice_1");
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
| **serial** | **String**|  | |
| **createDeviceLiveToolsPingDeviceRequest** | [**CreateDeviceLiveToolsPingDeviceRequest**](CreateDeviceLiveToolsPingDeviceRequest.md)|  | [optional] |

### Return type

[**CreateDeviceLiveToolsPing201Response**](CreateDeviceLiveToolsPing201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="getDeviceLiveToolsPingDevice_1"></a>
# **getDeviceLiveToolsPingDevice_1**
> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPingDevice_1(serial, id)

Return a ping device job

Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PingDeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PingDeviceApi apiInstance = new PingDeviceApi(defaultClient);
    String serial = "serial_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetDeviceLiveToolsPing200Response result = apiInstance.getDeviceLiveToolsPingDevice_1(serial, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PingDeviceApi#getDeviceLiveToolsPingDevice_1");
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
| **serial** | **String**|  | |
| **id** | **String**|  | |

### Return type

[**GetDeviceLiveToolsPing200Response**](GetDeviceLiveToolsPing200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

