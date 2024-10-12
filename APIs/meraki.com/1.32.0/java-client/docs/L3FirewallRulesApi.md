# L3FirewallRulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceFirewallL3FirewallRules_2**](L3FirewallRulesApi.md#getNetworkApplianceFirewallL3FirewallRules_2) | **GET** /networks/{networkId}/appliance/firewall/l3FirewallRules | Return the L3 firewall rules for an MX network |
| [**getNetworkWirelessSsidFirewallL3FirewallRules_3**](L3FirewallRulesApi.md#getNetworkWirelessSsidFirewallL3FirewallRules_3) | **GET** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Return the L3 firewall rules for an SSID on an MR network |
| [**updateNetworkApplianceFirewallL3FirewallRules_2**](L3FirewallRulesApi.md#updateNetworkApplianceFirewallL3FirewallRules_2) | **PUT** /networks/{networkId}/appliance/firewall/l3FirewallRules | Update the L3 firewall rules of an MX network |
| [**updateNetworkWirelessSsidFirewallL3FirewallRules_3**](L3FirewallRulesApi.md#updateNetworkWirelessSsidFirewallL3FirewallRules_3) | **PUT** /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules | Update the L3 firewall rules of an SSID on an MR network |


<a id="getNetworkApplianceFirewallL3FirewallRules_2"></a>
# **getNetworkApplianceFirewallL3FirewallRules_2**
> Object getNetworkApplianceFirewallL3FirewallRules_2(networkId)

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
import org.openapitools.client.api.L3FirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    L3FirewallRulesApi apiInstance = new L3FirewallRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallL3FirewallRules_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling L3FirewallRulesApi#getNetworkApplianceFirewallL3FirewallRules_2");
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

<a id="getNetworkWirelessSsidFirewallL3FirewallRules_3"></a>
# **getNetworkWirelessSsidFirewallL3FirewallRules_3**
> Object getNetworkWirelessSsidFirewallL3FirewallRules_3(networkId, number)

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
import org.openapitools.client.api.L3FirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    L3FirewallRulesApi apiInstance = new L3FirewallRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    try {
      Object result = apiInstance.getNetworkWirelessSsidFirewallL3FirewallRules_3(networkId, number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling L3FirewallRulesApi#getNetworkWirelessSsidFirewallL3FirewallRules_3");
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

<a id="updateNetworkApplianceFirewallL3FirewallRules_2"></a>
# **updateNetworkApplianceFirewallL3FirewallRules_2**
> Object updateNetworkApplianceFirewallL3FirewallRules_2(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest)

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
import org.openapitools.client.api.L3FirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    L3FirewallRulesApi apiInstance = new L3FirewallRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceFirewallInboundFirewallRulesRequest updateNetworkApplianceFirewallInboundFirewallRulesRequest = new UpdateNetworkApplianceFirewallInboundFirewallRulesRequest(); // UpdateNetworkApplianceFirewallInboundFirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallL3FirewallRules_2(networkId, updateNetworkApplianceFirewallInboundFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling L3FirewallRulesApi#updateNetworkApplianceFirewallL3FirewallRules_2");
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

<a id="updateNetworkWirelessSsidFirewallL3FirewallRules_3"></a>
# **updateNetworkWirelessSsidFirewallL3FirewallRules_3**
> Object updateNetworkWirelessSsidFirewallL3FirewallRules_3(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest)

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
import org.openapitools.client.api.L3FirewallRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    L3FirewallRulesApi apiInstance = new L3FirewallRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String number = "number_example"; // String | 
    UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest updateNetworkWirelessSsidFirewallL3FirewallRulesRequest = new UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest(); // UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkWirelessSsidFirewallL3FirewallRules_3(networkId, number, updateNetworkWirelessSsidFirewallL3FirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling L3FirewallRulesApi#updateNetworkWirelessSsidFirewallL3FirewallRules_3");
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
| **updateNetworkWirelessSsidFirewallL3FirewallRulesRequest** | [**UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest**](UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.md)|  | [optional] |

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

