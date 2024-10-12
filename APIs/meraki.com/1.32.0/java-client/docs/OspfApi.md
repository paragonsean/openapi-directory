# OspfApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSwitchRoutingOspf_2**](OspfApi.md#getNetworkSwitchRoutingOspf_2) | **GET** /networks/{networkId}/switch/routing/ospf | Return layer 3 OSPF routing configuration |
| [**updateNetworkSwitchRoutingOspf_2**](OspfApi.md#updateNetworkSwitchRoutingOspf_2) | **PUT** /networks/{networkId}/switch/routing/ospf | Update layer 3 OSPF routing configuration |


<a id="getNetworkSwitchRoutingOspf_2"></a>
# **getNetworkSwitchRoutingOspf_2**
> Object getNetworkSwitchRoutingOspf_2(networkId)

Return layer 3 OSPF routing configuration

Return layer 3 OSPF routing configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OspfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OspfApi apiInstance = new OspfApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchRoutingOspf_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OspfApi#getNetworkSwitchRoutingOspf_2");
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

<a id="updateNetworkSwitchRoutingOspf_2"></a>
# **updateNetworkSwitchRoutingOspf_2**
> Object updateNetworkSwitchRoutingOspf_2(networkId, updateNetworkSwitchRoutingOspfRequest)

Update layer 3 OSPF routing configuration

Update layer 3 OSPF routing configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OspfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OspfApi apiInstance = new OspfApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchRoutingOspfRequest updateNetworkSwitchRoutingOspfRequest = new UpdateNetworkSwitchRoutingOspfRequest(); // UpdateNetworkSwitchRoutingOspfRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchRoutingOspf_2(networkId, updateNetworkSwitchRoutingOspfRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OspfApi#updateNetworkSwitchRoutingOspf_2");
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
| **updateNetworkSwitchRoutingOspfRequest** | [**UpdateNetworkSwitchRoutingOspfRequest**](UpdateNetworkSwitchRoutingOspfRequest.md)|  | [optional] |

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

