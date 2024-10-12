# MxL7FirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkL7FirewallRules**](MxL7FirewallApi.md#getNetworkL7FirewallRules) | **GET** /networks/{networkId}/l7FirewallRules | List the MX L7 firewall rules for an MX network |
| [**updateNetworkL7FirewallRules**](MxL7FirewallApi.md#updateNetworkL7FirewallRules) | **PUT** /networks/{networkId}/l7FirewallRules | Update the MX L7 firewall rules for an MX network |


<a id="getNetworkL7FirewallRules"></a>
# **getNetworkL7FirewallRules**
> Object getNetworkL7FirewallRules(networkId)

List the MX L7 firewall rules for an MX network

List the MX L7 firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxL7FirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxL7FirewallApi apiInstance = new MxL7FirewallApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkL7FirewallRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxL7FirewallApi#getNetworkL7FirewallRules");
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

<a id="updateNetworkL7FirewallRules"></a>
# **updateNetworkL7FirewallRules**
> Object updateNetworkL7FirewallRules(networkId, updateNetworkL7FirewallRulesRequest)

Update the MX L7 firewall rules for an MX network

Update the MX L7 firewall rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxL7FirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxL7FirewallApi apiInstance = new MxL7FirewallApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkL7FirewallRulesRequest updateNetworkL7FirewallRulesRequest = new UpdateNetworkL7FirewallRulesRequest(); // UpdateNetworkL7FirewallRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkL7FirewallRules(networkId, updateNetworkL7FirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxL7FirewallApi#updateNetworkL7FirewallRules");
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
| **updateNetworkL7FirewallRulesRequest** | [**UpdateNetworkL7FirewallRulesRequest**](UpdateNetworkL7FirewallRulesRequest.md)|  | [optional] |

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

