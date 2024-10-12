# VpnSitesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vpnSitesUpdateTags**](VpnSitesApi.md#vpnSitesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnSites/{vpnSiteName} |  |


<a id="vpnSitesUpdateTags"></a>
# **vpnSitesUpdateTags**
> VpnSite vpnSitesUpdateTags(subscriptionId, resourceGroupName, vpnSiteName, apiVersion, vpnSiteParameters)



Updates VpnSite tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VpnSitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VpnSitesApi apiInstance = new VpnSitesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnSite.
    String vpnSiteName = "vpnSiteName_example"; // String | The name of the VpnSite being updated.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    P2sVpnGatewaysUpdateTagsRequest vpnSiteParameters = new P2sVpnGatewaysUpdateTagsRequest(); // P2sVpnGatewaysUpdateTagsRequest | Parameters supplied to update VpnSite tags.
    try {
      VpnSite result = apiInstance.vpnSitesUpdateTags(subscriptionId, resourceGroupName, vpnSiteName, apiVersion, vpnSiteParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VpnSitesApi#vpnSitesUpdateTags");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group name of the VpnSite. | |
| **vpnSiteName** | **String**| The name of the VpnSite being updated. | |
| **apiVersion** | **String**| Client API version. | |
| **vpnSiteParameters** | [**P2sVpnGatewaysUpdateTagsRequest**](P2sVpnGatewaysUpdateTagsRequest.md)| Parameters supplied to update VpnSite tags. | |

### Return type

[**VpnSite**](VpnSite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the VpnSite updated. |  -  |
| **201** | Request received successfully. Returns the details of the VpnSite updated. |  -  |
| **0** | Error |  -  |

