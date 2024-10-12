# InboundCellularFirewallRulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceFirewallInboundCellularFirewallRules_2**](InboundCellularFirewallRulesApi.md#getNetworkApplianceFirewallInboundCellularFirewallRules_2) | **GET** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Return the inbound cellular firewall rules for an MX network |
| [**updateNetworkApplianceFirewallInboundCellularFirewallRules_2**](InboundCellularFirewallRulesApi.md#updateNetworkApplianceFirewallInboundCellularFirewallRules_2) | **PUT** /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules | Update the inbound cellular firewall rules of an MX network |


<a id="getNetworkApplianceFirewallInboundCellularFirewallRules_2"></a>
# **getNetworkApplianceFirewallInboundCellularFirewallRules_2**
> List&lt;Object&gt; getNetworkApplianceFirewallInboundCellularFirewallRules_2(networkId)

Return the inbound cellular firewall rules for an MX network

Return the inbound cellular firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundCellularFirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InboundCellularFirewallRulesApi apiInstance = new InboundCellularFirewallRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkApplianceFirewallInboundCellularFirewallRules_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundCellularFirewallRulesApi#getNetworkApplianceFirewallInboundCellularFirewallRules_2");
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

<a id="updateNetworkApplianceFirewallInboundCellularFirewallRules_2"></a>
# **updateNetworkApplianceFirewallInboundCellularFirewallRules_2**
> List&lt;Object&gt; updateNetworkApplianceFirewallInboundCellularFirewallRules_2(networkId, updateNetworkApplianceFirewallCellularFirewallRulesRequest)

Update the inbound cellular firewall rules of an MX network

Update the inbound cellular firewall rules of an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundCellularFirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InboundCellularFirewallRulesApi apiInstance = new InboundCellularFirewallRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallCellularFirewallRulesRequest updateNetworkApplianceFirewallCellularFirewallRulesRequest = new UpdateNetworkApplianceFirewallCellularFirewallRulesRequest(); // UpdateNetworkApplianceFirewallCellularFirewallRulesRequest | 
    try {
      List<Object> result = apiInstance.updateNetworkApplianceFirewallInboundCellularFirewallRules_2(networkId, updateNetworkApplianceFirewallCellularFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundCellularFirewallRulesApi#updateNetworkApplianceFirewallInboundCellularFirewallRules_2");
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
| **updateNetworkApplianceFirewallCellularFirewallRulesRequest** | [**UpdateNetworkApplianceFirewallCellularFirewallRulesRequest**](UpdateNetworkApplianceFirewallCellularFirewallRulesRequest.md)|  | [optional] |

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

