# MtuApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSwitchMtu_1**](MtuApi.md#getNetworkSwitchMtu_1) | **GET** /networks/{networkId}/switch/mtu | Return the MTU configuration |
| [**updateNetworkSwitchMtu_1**](MtuApi.md#updateNetworkSwitchMtu_1) | **PUT** /networks/{networkId}/switch/mtu | Update the MTU configuration |


<a id="getNetworkSwitchMtu_1"></a>
# **getNetworkSwitchMtu_1**
> GetNetworkSwitchMtu200Response getNetworkSwitchMtu_1(networkId)

Return the MTU configuration

Return the MTU configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MtuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MtuApi apiInstance = new MtuApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSwitchMtu200Response result = apiInstance.getNetworkSwitchMtu_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MtuApi#getNetworkSwitchMtu_1");
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

### Return type

[**GetNetworkSwitchMtu200Response**](GetNetworkSwitchMtu200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchMtu_1"></a>
# **updateNetworkSwitchMtu_1**
> Object updateNetworkSwitchMtu_1(networkId, updateNetworkSwitchMtuRequest)

Update the MTU configuration

Update the MTU configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MtuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MtuApi apiInstance = new MtuApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchMtuRequest updateNetworkSwitchMtuRequest = new UpdateNetworkSwitchMtuRequest(); // UpdateNetworkSwitchMtuRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchMtu_1(networkId, updateNetworkSwitchMtuRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MtuApi#updateNetworkSwitchMtu_1");
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
| **updateNetworkSwitchMtuRequest** | [**UpdateNetworkSwitchMtuRequest**](UpdateNetworkSwitchMtuRequest.md)|  | [optional] |

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

