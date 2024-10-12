# NetworkAdaptersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSmDeviceNetworkAdapters_2**](NetworkAdaptersApi.md#getNetworkSmDeviceNetworkAdapters_2) | **GET** /networks/{networkId}/sm/devices/{deviceId}/networkAdapters | List the network adapters of a device |


<a id="getNetworkSmDeviceNetworkAdapters_2"></a>
# **getNetworkSmDeviceNetworkAdapters_2**
> List&lt;GetNetworkSmDeviceNetworkAdapters200ResponseInner&gt; getNetworkSmDeviceNetworkAdapters_2(networkId, deviceId)

List the network adapters of a device

List the network adapters of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkAdaptersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworkAdaptersApi apiInstance = new NetworkAdaptersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceNetworkAdapters200ResponseInner> result = apiInstance.getNetworkSmDeviceNetworkAdapters_2(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkAdaptersApi#getNetworkSmDeviceNetworkAdapters_2");
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

[**List&lt;GetNetworkSmDeviceNetworkAdapters200ResponseInner&gt;**](GetNetworkSmDeviceNetworkAdapters200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

