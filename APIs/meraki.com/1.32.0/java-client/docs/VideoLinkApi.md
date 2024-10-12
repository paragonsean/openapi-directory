# VideoLinkApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCameraVideoLink_1**](VideoLinkApi.md#getDeviceCameraVideoLink_1) | **GET** /devices/{serial}/camera/videoLink | Returns video link to the specified camera |


<a id="getDeviceCameraVideoLink_1"></a>
# **getDeviceCameraVideoLink_1**
> Object getDeviceCameraVideoLink_1(serial, timestamp)

Returns video link to the specified camera

Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoLinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VideoLinkApi apiInstance = new VideoLinkApi(defaultClient);
    String serial = "serial_example"; // String | 
    OffsetDateTime timestamp = OffsetDateTime.now(); // OffsetDateTime | [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.
    try {
      Object result = apiInstance.getDeviceCameraVideoLink_1(serial, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoLinkApi#getDeviceCameraVideoLink_1");
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
| **timestamp** | **OffsetDateTime**| [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time. | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

