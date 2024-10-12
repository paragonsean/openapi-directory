# VideoApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCameraVideoSettings_1**](VideoApi.md#getDeviceCameraVideoSettings_1) | **GET** /devices/{serial}/camera/video/settings | Returns video settings for the given camera |
| [**updateDeviceCameraVideoSettings_1**](VideoApi.md#updateDeviceCameraVideoSettings_1) | **PUT** /devices/{serial}/camera/video/settings | Update video settings for the given camera |


<a id="getDeviceCameraVideoSettings_1"></a>
# **getDeviceCameraVideoSettings_1**
> Object getDeviceCameraVideoSettings_1(serial)

Returns video settings for the given camera

Returns video settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VideoApi apiInstance = new VideoApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraVideoSettings_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#getDeviceCameraVideoSettings_1");
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

<a id="updateDeviceCameraVideoSettings_1"></a>
# **updateDeviceCameraVideoSettings_1**
> Object updateDeviceCameraVideoSettings_1(serial, updateDeviceCameraVideoSettingsRequest)

Update video settings for the given camera

Update video settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    VideoApi apiInstance = new VideoApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraVideoSettingsRequest updateDeviceCameraVideoSettingsRequest = new UpdateDeviceCameraVideoSettingsRequest(); // UpdateDeviceCameraVideoSettingsRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraVideoSettings_1(serial, updateDeviceCameraVideoSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoApi#updateDeviceCameraVideoSettings_1");
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
| **updateDeviceCameraVideoSettingsRequest** | [**UpdateDeviceCameraVideoSettingsRequest**](UpdateDeviceCameraVideoSettingsRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

