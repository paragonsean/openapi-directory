# WlanListsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSmDeviceWlanLists_2**](WlanListsApi.md#getNetworkSmDeviceWlanLists_2) | **GET** /networks/{networkId}/sm/devices/{deviceId}/wlanLists | List the saved SSID names on a device |


<a id="getNetworkSmDeviceWlanLists_2"></a>
# **getNetworkSmDeviceWlanLists_2**
> List&lt;GetNetworkSmDeviceWlanLists200ResponseInner&gt; getNetworkSmDeviceWlanLists_2(networkId, deviceId)

List the saved SSID names on a device

List the saved SSID names on a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WlanListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WlanListsApi apiInstance = new WlanListsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceWlanLists200ResponseInner> result = apiInstance.getNetworkSmDeviceWlanLists_2(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WlanListsApi#getNetworkSmDeviceWlanLists_2");
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

[**List&lt;GetNetworkSmDeviceWlanLists200ResponseInner&gt;**](GetNetworkSmDeviceWlanLists200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

