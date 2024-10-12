# VpnGatewaysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vpnGatewaysUpdateTags**](VpnGatewaysApi.md#vpnGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName} |  |


<a id="vpnGatewaysUpdateTags"></a>
# **vpnGatewaysUpdateTags**
> VpnGateway vpnGatewaysUpdateTags(subscriptionId, resourceGroupName, gatewayName, apiVersion, vpnGatewayParameters)



Updates virtual wan vpn gateway tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VpnGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VpnGatewaysApi apiInstance = new VpnGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    P2sVpnGatewaysUpdateTagsRequest vpnGatewayParameters = new P2sVpnGatewaysUpdateTagsRequest(); // P2sVpnGatewaysUpdateTagsRequest | Parameters supplied to update a virtual wan vpn gateway tags.
    try {
      VpnGateway result = apiInstance.vpnGatewaysUpdateTags(subscriptionId, resourceGroupName, gatewayName, apiVersion, vpnGatewayParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VpnGatewaysApi#vpnGatewaysUpdateTags");
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
| **resourceGroupName** | **String**| The resource group name of the VpnGateway. | |
| **gatewayName** | **String**| The name of the gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **vpnGatewayParameters** | [**P2sVpnGatewaysUpdateTagsRequest**](P2sVpnGatewaysUpdateTagsRequest.md)| Parameters supplied to update a virtual wan vpn gateway tags. | |

### Return type

[**VpnGateway**](VpnGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the updated gateway. |  -  |
| **201** | Request received successfully. Returns the details of the updated gateway. |  -  |
| **0** | Error |  -  |

