# MxVpnFirewallApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationVpnFirewallRules**](MxVpnFirewallApi.md#getOrganizationVpnFirewallRules) | **GET** /organizations/{organizationId}/vpnFirewallRules | Return the firewall rules for an organization&#39;s site-to-site VPN |
| [**updateOrganizationVpnFirewallRules**](MxVpnFirewallApi.md#updateOrganizationVpnFirewallRules) | **PUT** /organizations/{organizationId}/vpnFirewallRules | Update the firewall rules of an organization&#39;s site-to-site VPN |


<a id="getOrganizationVpnFirewallRules"></a>
# **getOrganizationVpnFirewallRules**
> List&lt;Object&gt; getOrganizationVpnFirewallRules(organizationId)

Return the firewall rules for an organization&#39;s site-to-site VPN

Return the firewall rules for an organization&#39;s site-to-site VPN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxVpnFirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxVpnFirewallApi apiInstance = new MxVpnFirewallApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      List<Object> result = apiInstance.getOrganizationVpnFirewallRules(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxVpnFirewallApi#getOrganizationVpnFirewallRules");
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
| **organizationId** | **String**|  | |

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

<a id="updateOrganizationVpnFirewallRules"></a>
# **updateOrganizationVpnFirewallRules**
> List&lt;Object&gt; updateOrganizationVpnFirewallRules(organizationId, updateOrganizationVpnFirewallRulesRequest)

Update the firewall rules of an organization&#39;s site-to-site VPN

Update the firewall rules of an organization&#39;s site-to-site VPN

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MxVpnFirewallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    MxVpnFirewallApi apiInstance = new MxVpnFirewallApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationVpnFirewallRulesRequest updateOrganizationVpnFirewallRulesRequest = new UpdateOrganizationVpnFirewallRulesRequest(); // UpdateOrganizationVpnFirewallRulesRequest | 
    try {
      List<Object> result = apiInstance.updateOrganizationVpnFirewallRules(organizationId, updateOrganizationVpnFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MxVpnFirewallApi#updateOrganizationVpnFirewallRules");
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
| **organizationId** | **String**|  | |
| **updateOrganizationVpnFirewallRulesRequest** | [**UpdateOrganizationVpnFirewallRulesRequest**](UpdateOrganizationVpnFirewallRulesRequest.md)|  | [optional] |

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

