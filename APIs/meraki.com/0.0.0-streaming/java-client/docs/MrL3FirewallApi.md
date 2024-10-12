# MrL3FirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSsidL3FirewallRules**](MrL3FirewallApi.md#getNetworkSsidL3FirewallRules) | **GET** /networks/{networkId}/ssids/{number}/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network |
| [**updateNetworkSsidL3FirewallRules**](MrL3FirewallApi.md#updateNetworkSsidL3FirewallRules) | **PUT** /networks/{networkId}/ssids/{number}/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network |


<a id="getNetworkSsidL3FirewallRules"></a>
# **getNetworkSsidL3FirewallRules**
> List&lt;Object&gt; getNetworkSsidL3FirewallRules(networkId, number)

Return the L3 firewall rules for an SSID on an MR network

Return the L3 firewall rules for an SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MrL3FirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MrL3FirewallApi apiInstance = new MrL3FirewallApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSsidL3FirewallRules(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MrL3FirewallApi#getNetworkSsidL3FirewallRules");
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
| **number** | **String**|  | |

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

<a id="updateNetworkSsidL3FirewallRules"></a>
# **updateNetworkSsidL3FirewallRules**
> List&lt;Object&gt; updateNetworkSsidL3FirewallRules(networkId, number, updateNetworkSsidL3FirewallRulesRequest)

Update the L3 firewall rules of an SSID on an MR network

Update the L3 firewall rules of an SSID on an MR network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MrL3FirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MrL3FirewallApi apiInstance = new MrL3FirewallApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkSsidL3FirewallRulesRequest updateNetworkSsidL3FirewallRulesRequest = new UpdateNetworkSsidL3FirewallRulesRequest(); // UpdateNetworkSsidL3FirewallRulesRequest | 
    try {
      List<Object> result = apiInstance.updateNetworkSsidL3FirewallRules(networkId, number, updateNetworkSsidL3FirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MrL3FirewallApi#updateNetworkSsidL3FirewallRules");
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
| **number** | **String**|  | |
| **updateNetworkSsidL3FirewallRulesRequest** | [**UpdateNetworkSsidL3FirewallRulesRequest**](UpdateNetworkSsidL3FirewallRulesRequest.md)|  | [optional] |

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

