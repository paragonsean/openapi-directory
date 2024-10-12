# VirtualNetworkGatewaysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualNetworkGatewaysCreateOrUpdate**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} |  |
| [**virtualNetworkGatewaysDelete**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} |  |
| [**virtualNetworkGatewaysGeneratevpnclientpackage**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGeneratevpnclientpackage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/generatevpnclientpackage |  |
| [**virtualNetworkGatewaysGet**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} |  |
| [**virtualNetworkGatewaysGetAdvertisedRoutes**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetAdvertisedRoutes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getAdvertisedRoutes |  |
| [**virtualNetworkGatewaysGetBgpPeerStatus**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetBgpPeerStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getBgpPeerStatus |  |
| [**virtualNetworkGatewaysGetLearnedRoutes**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetLearnedRoutes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getLearnedRoutes |  |
| [**virtualNetworkGatewaysList**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways |  |
| [**virtualNetworkGatewaysReset**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysReset) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/reset |  |


<a id="virtualNetworkGatewaysCreateOrUpdate"></a>
# **virtualNetworkGatewaysCreateOrUpdate**
> VirtualNetworkGateway virtualNetworkGatewaysCreateOrUpdate(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Creates or updates a virtual network gateway in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualNetworkGateway parameters = new VirtualNetworkGateway(); // VirtualNetworkGateway | Parameters supplied to create or update virtual network gateway operation.
    try {
      VirtualNetworkGateway result = apiInstance.virtualNetworkGatewaysCreateOrUpdate(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysCreateOrUpdate");
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
| **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md)| Parameters supplied to create or update virtual network gateway operation. | |

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting VirtualNetworkGateway resource. |  -  |
| **201** | Create successful. The operation returns the resulting VirtualNetworkGateway resource. |  -  |

<a id="virtualNetworkGatewaysDelete"></a>
# **virtualNetworkGatewaysDelete**
> virtualNetworkGatewaysDelete(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Deletes the specified virtual network gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.virtualNetworkGatewaysDelete(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysDelete");
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
| **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Delete successful. |  -  |

<a id="virtualNetworkGatewaysGeneratevpnclientpackage"></a>
# **virtualNetworkGatewaysGeneratevpnclientpackage**
> String virtualNetworkGatewaysGeneratevpnclientpackage(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Generates VPN client package for P2S client of the virtual network gateway in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VpnClientParameters parameters = new VpnClientParameters(); // VpnClientParameters | Parameters supplied to the generate virtual network gateway VPN client package operation.
    try {
      String result = apiInstance.virtualNetworkGatewaysGeneratevpnclientpackage(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGeneratevpnclientpackage");
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
| **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VpnClientParameters**](VpnClientParameters.md)| Parameters supplied to the generate virtual network gateway VPN client package operation. | |

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | VPN client package URL. |  -  |

<a id="virtualNetworkGatewaysGet"></a>
# **virtualNetworkGatewaysGet**
> VirtualNetworkGateway virtualNetworkGatewaysGet(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets the specified virtual network gateway by resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualNetworkGateway result = apiInstance.virtualNetworkGatewaysGet(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGet");
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
| **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a VirtualNetworkGateway resource. |  -  |

<a id="virtualNetworkGatewaysGetAdvertisedRoutes"></a>
# **virtualNetworkGatewaysGetAdvertisedRoutes**
> GatewayRouteListResult virtualNetworkGatewaysGetAdvertisedRoutes(resourceGroupName, virtualNetworkGatewayName, peer, apiVersion, subscriptionId)



This operation retrieves a list of routes the virtual network gateway is advertising to the specified peer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
    String peer = "peer_example"; // String | The IP address of the peer
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      GatewayRouteListResult result = apiInstance.virtualNetworkGatewaysGetAdvertisedRoutes(resourceGroupName, virtualNetworkGatewayName, peer, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGetAdvertisedRoutes");
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
| **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | |
| **peer** | **String**| The IP address of the peer | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**GatewayRouteListResult**](GatewayRouteListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of learned BGP routes |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysGetBgpPeerStatus"></a>
# **virtualNetworkGatewaysGetBgpPeerStatus**
> BgpPeerStatusListResult virtualNetworkGatewaysGetBgpPeerStatus(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, peer)



The GetBgpPeerStatus operation retrieves the status of all BGP peers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String peer = "peer_example"; // String | The IP address of the peer to retrieve the status of.
    try {
      BgpPeerStatusListResult result = apiInstance.virtualNetworkGatewaysGetBgpPeerStatus(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, peer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGetBgpPeerStatus");
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
| **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **peer** | **String**| The IP address of the peer to retrieve the status of. | [optional] |

### Return type

[**BgpPeerStatusListResult**](BgpPeerStatusListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of BGP peer statuses |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysGetLearnedRoutes"></a>
# **virtualNetworkGatewaysGetLearnedRoutes**
> GatewayRouteListResult virtualNetworkGatewaysGetLearnedRoutes(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



This operation retrieves a list of routes the virtual network gateway has learned, including routes learned from BGP peers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      GatewayRouteListResult result = apiInstance.virtualNetworkGatewaysGetLearnedRoutes(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGetLearnedRoutes");
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
| **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**GatewayRouteListResult**](GatewayRouteListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of advertised BGP routes |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysList"></a>
# **virtualNetworkGatewaysList**
> VirtualNetworkGatewayListResult virtualNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId)



Gets all virtual network gateways by resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualNetworkGatewayListResult result = apiInstance.virtualNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysList");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualNetworkGatewayListResult**](VirtualNetworkGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of VirtualNetworkGateway resources. |  -  |

<a id="virtualNetworkGatewaysReset"></a>
# **virtualNetworkGatewaysReset**
> VirtualNetworkGateway virtualNetworkGatewaysReset(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, gatewayVip)



Resets the primary of the virtual network gateway in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewaysApi apiInstance = new VirtualNetworkGatewaysApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String gatewayVip = "gatewayVip_example"; // String | Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway.
    try {
      VirtualNetworkGateway result = apiInstance.virtualNetworkGatewaysReset(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, gatewayVip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysReset");
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
| **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **gatewayVip** | **String**| Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway. | [optional] |

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation reset the primary of the virtual network gateway. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

