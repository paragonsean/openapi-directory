# VirtualWansApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualHubsUpdateTags**](VirtualWansApi.md#virtualHubsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName} |  |
| [**virtualWansUpdateTags**](VirtualWansApi.md#virtualWansUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{VirtualWANName} |  |


<a id="virtualHubsUpdateTags"></a>
# **virtualHubsUpdateTags**
> VirtualHub virtualHubsUpdateTags(subscriptionId, resourceGroupName, virtualHubName, apiVersion, virtualHubParameters)



Updates VirtualHub tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualWansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualWansApi apiInstance = new VirtualWansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualHub.
    String virtualHubName = "virtualHubName_example"; // String | The name of the VirtualHub.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    P2sVpnGatewaysUpdateTagsRequest virtualHubParameters = new P2sVpnGatewaysUpdateTagsRequest(); // P2sVpnGatewaysUpdateTagsRequest | Parameters supplied to update VirtualHub tags.
    try {
      VirtualHub result = apiInstance.virtualHubsUpdateTags(subscriptionId, resourceGroupName, virtualHubName, apiVersion, virtualHubParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualWansApi#virtualHubsUpdateTags");
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
| **resourceGroupName** | **String**| The resource group name of the VirtualHub. | |
| **virtualHubName** | **String**| The name of the VirtualHub. | |
| **apiVersion** | **String**| Client API version. | |
| **virtualHubParameters** | [**P2sVpnGatewaysUpdateTagsRequest**](P2sVpnGatewaysUpdateTagsRequest.md)| Parameters supplied to update VirtualHub tags. | |

### Return type

[**VirtualHub**](VirtualHub.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the VirtualHub updated. |  -  |
| **201** | Request received successfully. Returns the details of the VirtualHub updated. |  -  |
| **0** | Error |  -  |

<a id="virtualWansUpdateTags"></a>
# **virtualWansUpdateTags**
> VirtualWAN virtualWansUpdateTags(subscriptionId, resourceGroupName, virtualWANName, apiVersion, waNParameters)



Updates a VirtualWAN tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualWansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualWansApi apiInstance = new VirtualWansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualWan.
    String virtualWANName = "virtualWANName_example"; // String | The name of the VirtualWAN being updated.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    P2sVpnGatewaysUpdateTagsRequest waNParameters = new P2sVpnGatewaysUpdateTagsRequest(); // P2sVpnGatewaysUpdateTagsRequest | Parameters supplied to Update VirtualWAN tags.
    try {
      VirtualWAN result = apiInstance.virtualWansUpdateTags(subscriptionId, resourceGroupName, virtualWANName, apiVersion, waNParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualWansApi#virtualWansUpdateTags");
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
| **resourceGroupName** | **String**| The resource group name of the VirtualWan. | |
| **virtualWANName** | **String**| The name of the VirtualWAN being updated. | |
| **apiVersion** | **String**| Client API version. | |
| **waNParameters** | [**P2sVpnGatewaysUpdateTagsRequest**](P2sVpnGatewaysUpdateTagsRequest.md)| Parameters supplied to Update VirtualWAN tags. | |

### Return type

[**VirtualWAN**](VirtualWAN.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the VirtualWAN updated. |  -  |
| **201** | Request received successfully. Returns the details of the VirtualWAN updated. |  -  |
| **0** | Error |  -  |

