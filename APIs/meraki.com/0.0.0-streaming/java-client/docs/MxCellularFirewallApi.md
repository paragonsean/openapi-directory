# MxCellularFirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkCellularFirewallRules**](MxCellularFirewallApi.md#getNetworkCellularFirewallRules) | **GET** /networks/{networkId}/cellularFirewallRules | Return the cellular firewall rules for an MX network |
| [**updateNetworkCellularFirewallRules**](MxCellularFirewallApi.md#updateNetworkCellularFirewallRules) | **PUT** /networks/{networkId}/cellularFirewallRules | Update the cellular firewall rules of an MX network |


<a id="getNetworkCellularFirewallRules"></a>
# **getNetworkCellularFirewallRules**
> List&lt;Object&gt; getNetworkCellularFirewallRules(networkId)

Return the cellular firewall rules for an MX network

Return the cellular firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxCellularFirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxCellularFirewallApi apiInstance = new MxCellularFirewallApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkCellularFirewallRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxCellularFirewallApi#getNetworkCellularFirewallRules");
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

<a id="updateNetworkCellularFirewallRules"></a>
# **updateNetworkCellularFirewallRules**
> List&lt;Object&gt; updateNetworkCellularFirewallRules(networkId, updateNetworkCellularFirewallRulesRequest)

Update the cellular firewall rules of an MX network

Update the cellular firewall rules of an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxCellularFirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxCellularFirewallApi apiInstance = new MxCellularFirewallApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkCellularFirewallRulesRequest updateNetworkCellularFirewallRulesRequest = new UpdateNetworkCellularFirewallRulesRequest(); // UpdateNetworkCellularFirewallRulesRequest | 
    try {
      List<Object> result = apiInstance.updateNetworkCellularFirewallRules(networkId, updateNetworkCellularFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxCellularFirewallApi#updateNetworkCellularFirewallRules");
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
| **updateNetworkCellularFirewallRulesRequest** | [**UpdateNetworkCellularFirewallRulesRequest**](UpdateNetworkCellularFirewallRulesRequest.md)|  | [optional] |

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

