# InboundFirewallRulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceFirewallInboundFirewallRules_2**](InboundFirewallRulesApi.md#getNetworkApplianceFirewallInboundFirewallRules_2) | **GET** /networks/{networkId}/appliance/firewall/inboundFirewallRules | Return the inbound firewall rules for an MX network |
| [**updateNetworkApplianceFirewallInboundFirewallRules_2**](InboundFirewallRulesApi.md#updateNetworkApplianceFirewallInboundFirewallRules_2) | **PUT** /networks/{networkId}/appliance/firewall/inboundFirewallRules | Update the inbound firewall rules of an MX network |


<a id="getNetworkApplianceFirewallInboundFirewallRules_2"></a>
# **getNetworkApplianceFirewallInboundFirewallRules_2**
> Object getNetworkApplianceFirewallInboundFirewallRules_2(networkId)

Return the inbound firewall rules for an MX network

Return the inbound firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundFirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InboundFirewallRulesApi apiInstance = new InboundFirewallRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallInboundFirewallRules_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundFirewallRulesApi#getNetworkApplianceFirewallInboundFirewallRules_2");
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

<a id="updateNetworkApplianceFirewallInboundFirewallRules_2"></a>
# **updateNetworkApplianceFirewallInboundFirewallRules_2**
> Object updateNetworkApplianceFirewallInboundFirewallRules_2(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest)

Update the inbound firewall rules of an MX network

Update the inbound firewall rules of an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundFirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InboundFirewallRulesApi apiInstance = new InboundFirewallRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest = new UpdateNetworkApplianceFirewallInboundFirewallRulesRequest(); // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallInboundFirewallRules_2(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundFirewallRulesApi#updateNetworkApplianceFirewallInboundFirewallRules_2");
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
| **updateNetworkApplianceFirewallInboundFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallInboundFirewallRulesRequest**](UpdateNetworkApplianceFirewallInboundFirewallRulesRequest.md)|  | [optional] |

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

