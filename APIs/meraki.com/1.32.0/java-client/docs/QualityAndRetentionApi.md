# QualityAndRetentionApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCameraQualityAndRetention_1**](QualityAndRetentionApi.md#getDeviceCameraQualityAndRetention_1) | **GET** /devices/{serial}/camera/qualityAndRetention | Returns quality and retention settings for the given camera |
| [**updateDeviceCameraQualityAndRetention_1**](QualityAndRetentionApi.md#updateDeviceCameraQualityAndRetention_1) | **PUT** /devices/{serial}/camera/qualityAndRetention | Update quality and retention settings for the given camera |


<a id="getDeviceCameraQualityAndRetention_1"></a>
# **getDeviceCameraQualityAndRetention_1**
> Object getDeviceCameraQualityAndRetention_1(serial)

Returns quality and retention settings for the given camera

Returns quality and retention settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QualityAndRetentionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QualityAndRetentionApi apiInstance = new QualityAndRetentionApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCameraQualityAndRetention_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityAndRetentionApi#getDeviceCameraQualityAndRetention_1");
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

<a id="updateDeviceCameraQualityAndRetention_1"></a>
# **updateDeviceCameraQualityAndRetention_1**
> Object updateDeviceCameraQualityAndRetention_1(serial, updateDeviceCameraQualityAndRetentionRequest)

Update quality and retention settings for the given camera

Update quality and retention settings for the given camera

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QualityAndRetentionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    QualityAndRetentionApi apiInstance = new QualityAndRetentionApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCameraQualityAndRetentionRequest updateDeviceCameraQualityAndRetentionRequest = new UpdateDeviceCameraQualityAndRetentionRequest(); // UpdateDeviceCameraQualityAndRetentionRequest | 
    try {
      Object result = apiInstance.updateDeviceCameraQualityAndRetention_1(serial, updateDeviceCameraQualityAndRetentionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QualityAndRetentionApi#updateDeviceCameraQualityAndRetention_1");
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
| **updateDeviceCameraQualityAndRetentionRequest** | [**UpdateDeviceCameraQualityAndRetentionRequest**](UpdateDeviceCameraQualityAndRetentionRequest.md)|  | [optional] |

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

