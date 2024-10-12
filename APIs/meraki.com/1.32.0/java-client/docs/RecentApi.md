# RecentApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCameraAnalyticsRecent_2**](RecentApi.md#getDeviceCameraAnalyticsRecent_2) | **GET** /devices/{serial}/camera/analytics/recent | Returns most recent record for analytics zones |


<a id="getDeviceCameraAnalyticsRecent_2"></a>
# **getDeviceCameraAnalyticsRecent_2**
> List&lt;Object&gt; getDeviceCameraAnalyticsRecent_2(serial, objectType)

Returns most recent record for analytics zones

Returns most recent record for analytics zones

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RecentApi apiInstance = new RecentApi(defaultClient);
    String serial = "serial_example"; // String | 
    String objectType = "person"; // String | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    try {
      List<Object> result = apiInstance.getDeviceCameraAnalyticsRecent_2(serial, objectType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecentApi#getDeviceCameraAnalyticsRecent_2");
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
| **objectType** | **String**| [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. | [optional] [enum: person, vehicle] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

