# P2SVpnGatewaysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**p2sVpnGatewaysGenerateVpnProfile**](P2SVpnGatewaysApi.md#p2sVpnGatewaysGenerateVpnProfile) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/generatevpnprofile |  |
| [**p2sVpnGatewaysGetP2sVpnConnectionHealth**](P2SVpnGatewaysApi.md#p2sVpnGatewaysGetP2sVpnConnectionHealth) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/getP2sVpnConnectionHealth |  |
| [**p2sVpnGatewaysUpdateTags**](P2SVpnGatewaysApi.md#p2sVpnGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName} |  |


<a id="p2sVpnGatewaysGenerateVpnProfile"></a>
# **p2sVpnGatewaysGenerateVpnProfile**
> VpnProfileResponse p2sVpnGatewaysGenerateVpnProfile(resourceGroupName, gatewayName, apiVersion, subscriptionId, parameters)



Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.P2SVpnGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    P2SVpnGatewaysApi apiInstance = new P2SVpnGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String gatewayName = "gatewayName_example"; // String | The name of the P2SVpnGateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    P2SVpnProfileParameters parameters = new P2SVpnProfileParameters(); // P2SVpnProfileParameters | Parameters supplied to the generate P2SVpnGateway VPN client package operation.
    try {
      VpnProfileResponse result = apiInstance.p2sVpnGatewaysGenerateVpnProfile(resourceGroupName, gatewayName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling P2SVpnGatewaysApi#p2sVpnGatewaysGenerateVpnProfile");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **gatewayName** | **String**| The name of the P2SVpnGateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**P2SVpnProfileParameters**](P2SVpnProfileParameters.md)| Parameters supplied to the generate P2SVpnGateway VPN client package operation. | |

### Return type

[**VpnProfileResponse**](VpnProfileResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | VPN profile package URL. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="p2sVpnGatewaysGetP2sVpnConnectionHealth"></a>
# **p2sVpnGatewaysGetP2sVpnConnectionHealth**
> P2SVpnGateway p2sVpnGatewaysGetP2sVpnConnectionHealth(resourceGroupName, gatewayName, apiVersion, subscriptionId)



Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.P2SVpnGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    P2SVpnGatewaysApi apiInstance = new P2SVpnGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String gatewayName = "gatewayName_example"; // String | The name of the P2SVpnGateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      P2SVpnGateway result = apiInstance.p2sVpnGatewaysGetP2sVpnConnectionHealth(resourceGroupName, gatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling P2SVpnGatewaysApi#p2sVpnGatewaysGetP2sVpnConnectionHealth");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **gatewayName** | **String**| The name of the P2SVpnGateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**P2SVpnGateway**](P2SVpnGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | P2S Vpn Gateway with P2S connection health details. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="p2sVpnGatewaysUpdateTags"></a>
# **p2sVpnGatewaysUpdateTags**
> P2SVpnGateway p2sVpnGatewaysUpdateTags(subscriptionId, resourceGroupName, gatewayName, apiVersion, p2SVpnGatewayParameters)



Updates virtual wan p2s vpn gateway tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.P2SVpnGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    P2SVpnGatewaysApi apiInstance = new P2SVpnGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the P2SVpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    P2sVpnGatewaysUpdateTagsRequest p2SVpnGatewayParameters = new P2sVpnGatewaysUpdateTagsRequest(); // P2sVpnGatewaysUpdateTagsRequest | Parameters supplied to update a virtual wan p2s vpn gateway tags.
    try {
      P2SVpnGateway result = apiInstance.p2sVpnGatewaysUpdateTags(subscriptionId, resourceGroupName, gatewayName, apiVersion, p2SVpnGatewayParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling P2SVpnGatewaysApi#p2sVpnGatewaysUpdateTags");
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
| **resourceGroupName** | **String**| The resource group name of the P2SVpnGateway. | |
| **gatewayName** | **String**| The name of the gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **p2SVpnGatewayParameters** | [**P2sVpnGatewaysUpdateTagsRequest**](P2sVpnGatewaysUpdateTagsRequest.md)| Parameters supplied to update a virtual wan p2s vpn gateway tags. | |

### Return type

[**P2SVpnGateway**](P2SVpnGateway.md)

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
| **0** | Error. |  -  |

