# BgpApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceVpnBgp_2**](BgpApi.md#getNetworkApplianceVpnBgp_2) | **GET** /networks/{networkId}/appliance/vpn/bgp | Return a Hub BGP Configuration |
| [**updateNetworkApplianceVpnBgp_2**](BgpApi.md#updateNetworkApplianceVpnBgp_2) | **PUT** /networks/{networkId}/appliance/vpn/bgp | Update a Hub BGP Configuration |


<a id="getNetworkApplianceVpnBgp_2"></a>
# **getNetworkApplianceVpnBgp_2**
> Object getNetworkApplianceVpnBgp_2(networkId)

Return a Hub BGP Configuration

Return a Hub BGP Configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BgpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BgpApi apiInstance = new BgpApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceVpnBgp_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BgpApi#getNetworkApplianceVpnBgp_2");
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

<a id="updateNetworkApplianceVpnBgp_2"></a>
# **updateNetworkApplianceVpnBgp_2**
> Object updateNetworkApplianceVpnBgp_2(networkId, updateNetworkApplianceVpnBgpRequest)

Update a Hub BGP Configuration

Update a Hub BGP Configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BgpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    BgpApi apiInstance = new BgpApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceVpnBgpRequest updateNetworkApplianceVpnBgpRequest = new UpdateNetworkApplianceVpnBgpRequest(); // UpdateNetworkApplianceVpnBgpRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceVpnBgp_2(networkId, updateNetworkApplianceVpnBgpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BgpApi#updateNetworkApplianceVpnBgp_2");
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
| **updateNetworkApplianceVpnBgpRequest** | [**UpdateNetworkApplianceVpnBgpRequest**](UpdateNetworkApplianceVpnBgpRequest.md)|  | |

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

