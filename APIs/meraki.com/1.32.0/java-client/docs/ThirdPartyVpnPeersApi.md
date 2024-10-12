# ThirdPartyVpnPeersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationApplianceVpnThirdPartyVPNPeers_2**](ThirdPartyVpnPeersApi.md#getOrganizationApplianceVpnThirdPartyVPNPeers_2) | **GET** /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers | Return the third party VPN peers for an organization |
| [**updateOrganizationApplianceVpnThirdPartyVPNPeers_2**](ThirdPartyVpnPeersApi.md#updateOrganizationApplianceVpnThirdPartyVPNPeers_2) | **PUT** /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers | Update the third party VPN peers for an organization |


<a id="getOrganizationApplianceVpnThirdPartyVPNPeers_2"></a>
# **getOrganizationApplianceVpnThirdPartyVPNPeers_2**
> GetOrganizationApplianceVpnThirdPartyVPNPeers200Response getOrganizationApplianceVpnThirdPartyVPNPeers_2(organizationId)

Return the third party VPN peers for an organization

Return the third party VPN peers for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThirdPartyVpnPeersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ThirdPartyVpnPeersApi apiInstance = new ThirdPartyVpnPeersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      GetOrganizationApplianceVpnThirdPartyVPNPeers200Response result = apiInstance.getOrganizationApplianceVpnThirdPartyVPNPeers_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThirdPartyVpnPeersApi#getOrganizationApplianceVpnThirdPartyVPNPeers_2");
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

[**GetOrganizationApplianceVpnThirdPartyVPNPeers200Response**](GetOrganizationApplianceVpnThirdPartyVPNPeers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationApplianceVpnThirdPartyVPNPeers_2"></a>
# **updateOrganizationApplianceVpnThirdPartyVPNPeers_2**
> GetOrganizationApplianceVpnThirdPartyVPNPeers200Response updateOrganizationApplianceVpnThirdPartyVPNPeers_2(organizationId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequest)

Update the third party VPN peers for an organization

Update the third party VPN peers for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThirdPartyVpnPeersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ThirdPartyVpnPeersApi apiInstance = new ThirdPartyVpnPeersApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest updateOrganizationApplianceVpnThirdPartyVPNPeersRequest = new UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest(); // UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest | 
    try {
      GetOrganizationApplianceVpnThirdPartyVPNPeers200Response result = apiInstance.updateOrganizationApplianceVpnThirdPartyVPNPeers_2(organizationId, updateOrganizationApplianceVpnThirdPartyVPNPeersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThirdPartyVpnPeersApi#updateOrganizationApplianceVpnThirdPartyVPNPeers_2");
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
| **updateOrganizationApplianceVpnThirdPartyVPNPeersRequest** | [**UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest**](UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest.md)|  | |

### Return type

[**GetOrganizationApplianceVpnThirdPartyVPNPeers200Response**](GetOrganizationApplianceVpnThirdPartyVPNPeers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

