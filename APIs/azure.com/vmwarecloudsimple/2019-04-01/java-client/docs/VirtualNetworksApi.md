# VirtualNetworksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualNetworksGet**](VirtualNetworksApi.md#virtualNetworksGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/virtualNetworks/{virtualNetworkName} | Implements virtual network GET method |
| [**virtualNetworksList**](VirtualNetworksApi.md#virtualNetworksList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/virtualNetworks | Implements list available virtual networks within a subscription method |


<a id="virtualNetworksGet"></a>
# **virtualNetworksGet**
> VirtualNetwork virtualNetworksGet(subscriptionId, regionId, pcName, virtualNetworkName, apiVersion)

Implements virtual network GET method

Return virtual network by its name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworksApi apiInstance = new VirtualNetworksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String pcName = "pcName_example"; // String | The private cloud name
    String virtualNetworkName = "virtualNetworkName_example"; // String | virtual network id (vsphereId)
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      VirtualNetwork result = apiInstance.virtualNetworksGet(subscriptionId, regionId, pcName, virtualNetworkName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworksApi#virtualNetworksGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **pcName** | **String**| The private cloud name | |
| **virtualNetworkName** | **String**| virtual network id (vsphereId) | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

<a id="virtualNetworksList"></a>
# **virtualNetworksList**
> VirtualNetworkListResponse virtualNetworksList(subscriptionId, regionId, pcName, apiVersion, resourcePoolName)

Implements list available virtual networks within a subscription method

Return list of virtual networks in location for private cloud

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworksApi apiInstance = new VirtualNetworksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String regionId = "regionId_example"; // String | The region Id (westus, eastus)
    String pcName = "pcName_example"; // String | The private cloud name
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String resourcePoolName = "resourcePoolName_example"; // String | Resource pool used to derive vSphere cluster which contains virtual networks
    try {
      VirtualNetworkListResponse result = apiInstance.virtualNetworksList(subscriptionId, regionId, pcName, apiVersion, resourcePoolName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworksApi#virtualNetworksList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **regionId** | **String**| The region Id (westus, eastus) | |
| **pcName** | **String**| The private cloud name | |
| **apiVersion** | **String**| Client API version. | |
| **resourcePoolName** | **String**| Resource pool used to derive vSphere cluster which contains virtual networks | |

### Return type

[**VirtualNetworkListResponse**](VirtualNetworkListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | General Error |  -  |

