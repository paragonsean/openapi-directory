# SiteToSiteVpnApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceVpnSiteToSiteVpn_2**](SiteToSiteVpnApi.md#getNetworkApplianceVpnSiteToSiteVpn_2) | **GET** /networks/{networkId}/appliance/vpn/siteToSiteVpn | Return the site-to-site VPN settings of a network |
| [**updateNetworkApplianceVpnSiteToSiteVpn_2**](SiteToSiteVpnApi.md#updateNetworkApplianceVpnSiteToSiteVpn_2) | **PUT** /networks/{networkId}/appliance/vpn/siteToSiteVpn | Update the site-to-site VPN settings of a network |


<a id="getNetworkApplianceVpnSiteToSiteVpn_2"></a>
# **getNetworkApplianceVpnSiteToSiteVpn_2**
> GetNetworkApplianceVpnSiteToSiteVpn200Response getNetworkApplianceVpnSiteToSiteVpn_2(networkId)

Return the site-to-site VPN settings of a network

Return the site-to-site VPN settings of a network. Only valid for MX networks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteToSiteVpnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SiteToSiteVpnApi apiInstance = new SiteToSiteVpnApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceVpnSiteToSiteVpn200Response result = apiInstance.getNetworkApplianceVpnSiteToSiteVpn_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteToSiteVpnApi#getNetworkApplianceVpnSiteToSiteVpn_2");
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

[**GetNetworkApplianceVpnSiteToSiteVpn200Response**](GetNetworkApplianceVpnSiteToSiteVpn200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceVpnSiteToSiteVpn_2"></a>
# **updateNetworkApplianceVpnSiteToSiteVpn_2**
> GetNetworkApplianceVpnSiteToSiteVpn200Response updateNetworkApplianceVpnSiteToSiteVpn_2(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest)

Update the site-to-site VPN settings of a network

Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteToSiteVpnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SiteToSiteVpnApi apiInstance = new SiteToSiteVpnApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceVpnSiteToSiteVpnRequest updateNetworkApplianceVpnSiteToSiteVpnRequest = new UpdateNetworkApplianceVpnSiteToSiteVpnRequest(); // UpdateNetworkApplianceVpnSiteToSiteVpnRequest | 
    try {
      GetNetworkApplianceVpnSiteToSiteVpn200Response result = apiInstance.updateNetworkApplianceVpnSiteToSiteVpn_2(networkId, updateNetworkApplianceVpnSiteToSiteVpnRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteToSiteVpnApi#updateNetworkApplianceVpnSiteToSiteVpn_2");
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
| **updateNetworkApplianceVpnSiteToSiteVpnRequest** | [**UpdateNetworkApplianceVpnSiteToSiteVpnRequest**](UpdateNetworkApplianceVpnSiteToSiteVpnRequest.md)|  | |

### Return type

[**GetNetworkApplianceVpnSiteToSiteVpn200Response**](GetNetworkApplianceVpnSiteToSiteVpn200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

