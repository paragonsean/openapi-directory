# FirewalledServicesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceFirewallFirewalledService_2**](FirewalledServicesApi.md#getNetworkApplianceFirewallFirewalledService_2) | **GET** /networks/{networkId}/appliance/firewall/firewalledServices/{service} | Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;) |
| [**getNetworkApplianceFirewallFirewalledServices_2**](FirewalledServicesApi.md#getNetworkApplianceFirewallFirewalledServices_2) | **GET** /networks/{networkId}/appliance/firewall/firewalledServices | List the appliance services and their accessibility rules |
| [**updateNetworkApplianceFirewallFirewalledService_2**](FirewalledServicesApi.md#updateNetworkApplianceFirewallFirewalledService_2) | **PUT** /networks/{networkId}/appliance/firewall/firewalledServices/{service} | Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;) |


<a id="getNetworkApplianceFirewallFirewalledService_2"></a>
# **getNetworkApplianceFirewallFirewalledService_2**
> Object getNetworkApplianceFirewallFirewalledService_2(networkId, service)

Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

Return the accessibility settings of the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewalledServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirewalledServicesApi apiInstance = new FirewalledServicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String service = "service_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceFirewallFirewalledService_2(networkId, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewalledServicesApi#getNetworkApplianceFirewallFirewalledService_2");
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
| **service** | **String**|  | |

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

<a id="getNetworkApplianceFirewallFirewalledServices_2"></a>
# **getNetworkApplianceFirewallFirewalledServices_2**
> List&lt;Object&gt; getNetworkApplianceFirewallFirewalledServices_2(networkId)

List the appliance services and their accessibility rules

List the appliance services and their accessibility rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewalledServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirewalledServicesApi apiInstance = new FirewalledServicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkApplianceFirewallFirewalledServices_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewalledServicesApi#getNetworkApplianceFirewallFirewalledServices_2");
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

<a id="updateNetworkApplianceFirewallFirewalledService_2"></a>
# **updateNetworkApplianceFirewallFirewalledService_2**
> Object updateNetworkApplianceFirewallFirewalledService_2(networkId, service, updateNetworkApplianceFirewallFirewalledServiceRequest)

Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

Updates the accessibility settings for the given service (&#39;ICMP&#39;, &#39;web&#39;, or &#39;SNMP&#39;)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewalledServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirewalledServicesApi apiInstance = new FirewalledServicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String service = "service_example"; // String | 
    UpdateNetworkApplianceFirewallFirewalledServiceRequest updateNetworkApplianceFirewallFirewalledServiceRequest = new UpdateNetworkApplianceFirewallFirewalledServiceRequest(); // UpdateNetworkApplianceFirewallFirewalledServiceRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceFirewallFirewalledService_2(networkId, service, updateNetworkApplianceFirewallFirewalledServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewalledServicesApi#updateNetworkApplianceFirewallFirewalledService_2");
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
| **service** | **String**|  | |
| **updateNetworkApplianceFirewallFirewalledServiceRequest** | [**UpdateNetworkApplianceFirewallFirewalledServiceRequest**](UpdateNetworkApplianceFirewallFirewalledServiceRequest.md)|  | |

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

