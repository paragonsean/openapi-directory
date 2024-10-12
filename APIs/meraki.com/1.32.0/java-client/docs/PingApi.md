# PingApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceLiveToolsPing_1**](PingApi.md#createDeviceLiveToolsPing_1) | **POST** /devices/{serial}/liveTools/ping | Enqueue a job to ping a target host from the device |
| [**getDeviceLiveToolsPing_1**](PingApi.md#getDeviceLiveToolsPing_1) | **GET** /devices/{serial}/liveTools/ping/{id} | Return a ping job |


<a id="createDeviceLiveToolsPing_1"></a>
# **createDeviceLiveToolsPing_1**
> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPing_1(serial, createDeviceLiveToolsPingRequest)

Enqueue a job to ping a target host from the device

Enqueue a job to ping a target host from the device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PingApi apiInstance = new PingApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceLiveToolsPingRequest createDeviceLiveToolsPingRequest = new CreateDeviceLiveToolsPingRequest(); // CreateDeviceLiveToolsPingRequest | 
    try {
      CreateDeviceLiveToolsPing201Response result = apiInstance.createDeviceLiveToolsPing_1(serial, createDeviceLiveToolsPingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PingApi#createDeviceLiveToolsPing_1");
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
| **createDeviceLiveToolsPingRequest** | [**CreateDeviceLiveToolsPingRequest**](CreateDeviceLiveToolsPingRequest.md)|  | |

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

<a id="getDeviceLiveToolsPing_1"></a>
# **getDeviceLiveToolsPing_1**
> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPing_1(serial, id)

Return a ping job

Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PingApi apiInstance = new PingApi(defaultClient);
    String serial = "serial_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetDeviceLiveToolsPing200Response result = apiInstance.getDeviceLiveToolsPing_1(serial, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PingApi#getDeviceLiveToolsPing_1");
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

