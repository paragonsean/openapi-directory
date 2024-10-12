# SoftwaresApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSmDeviceSoftwares_2**](SoftwaresApi.md#getNetworkSmDeviceSoftwares_2) | **GET** /networks/{networkId}/sm/devices/{deviceId}/softwares | Get a list of softwares associated with a device |
| [**getNetworkSmUserSoftwares_2**](SoftwaresApi.md#getNetworkSmUserSoftwares_2) | **GET** /networks/{networkId}/sm/users/{userId}/softwares | Get a list of softwares associated with a user |


<a id="getNetworkSmDeviceSoftwares_2"></a>
# **getNetworkSmDeviceSoftwares_2**
> List&lt;GetNetworkSmDeviceSoftwares200ResponseInner&gt; getNetworkSmDeviceSoftwares_2(networkId, deviceId)

Get a list of softwares associated with a device

Get a list of softwares associated with a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwaresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SoftwaresApi apiInstance = new SoftwaresApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceSoftwares200ResponseInner> result = apiInstance.getNetworkSmDeviceSoftwares_2(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwaresApi#getNetworkSmDeviceSoftwares_2");
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
| **networkId** | **String**|  | |
| **deviceId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceSoftwares200ResponseInner&gt;**](GetNetworkSmDeviceSoftwares200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmUserSoftwares_2"></a>
# **getNetworkSmUserSoftwares_2**
> List&lt;GetNetworkSmDeviceSoftwares200ResponseInner&gt; getNetworkSmUserSoftwares_2(networkId, userId)

Get a list of softwares associated with a user

Get a list of softwares associated with a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwaresApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SoftwaresApi apiInstance = new SoftwaresApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      List<GetNetworkSmDeviceSoftwares200ResponseInner> result = apiInstance.getNetworkSmUserSoftwares_2(networkId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwaresApi#getNetworkSmUserSoftwares_2");
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
| **networkId** | **String**|  | |
| **userId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceSoftwares200ResponseInner&gt;**](GetNetworkSmDeviceSoftwares200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

