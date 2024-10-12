# MxL3OutboundFirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkL3FirewallRules**](MxL3OutboundFirewallApi.md#getNetworkL3FirewallRules) | **GET** /networks/{networkId}/l3FirewallRules | Return the L3 firewall rules for an MX network |
| [**updateNetworkL3FirewallRules**](MxL3OutboundFirewallApi.md#updateNetworkL3FirewallRules) | **PUT** /networks/{networkId}/l3FirewallRules | Update the L3 firewall rules of an MX network |


<a id="getNetworkL3FirewallRules"></a>
# **getNetworkL3FirewallRules**
> List&lt;Object&gt; getNetworkL3FirewallRules(networkId)

Return the L3 firewall rules for an MX network

Return the L3 firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxL3OutboundFirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxL3OutboundFirewallApi apiInstance = new MxL3OutboundFirewallApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkL3FirewallRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxL3OutboundFirewallApi#getNetworkL3FirewallRules");
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

<a id="updateNetworkL3FirewallRules"></a>
# **updateNetworkL3FirewallRules**
> List&lt;Object&gt; updateNetworkL3FirewallRules(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest)

Update the L3 firewall rules of an MX network

Update the L3 firewall rules of an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxL3OutboundFirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxL3OutboundFirewallApi apiInstance = new MxL3OutboundFirewallApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest = new UpdateNetworkApplianceFirewallInboundFirewallRulesRequest(); // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
    try {
      List<Object> result = apiInstance.updateNetworkL3FirewallRules(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxL3OutboundFirewallApi#updateNetworkL3FirewallRules");
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

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

