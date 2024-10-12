# VirtualNetworkGatewaysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualNetworkGatewaysCreateOrUpdate**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} |  |
| [**virtualNetworkGatewaysDelete**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} |  |
| [**virtualNetworkGatewaysGenerateVpnProfile**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGenerateVpnProfile) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/generatevpnprofile |  |
| [**virtualNetworkGatewaysGeneratevpnclientpackage**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGeneratevpnclientpackage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/generatevpnclientpackage |  |
| [**virtualNetworkGatewaysGet**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} |  |
| [**virtualNetworkGatewaysGetAdvertisedRoutes**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetAdvertisedRoutes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getAdvertisedRoutes |  |
| [**virtualNetworkGatewaysGetBgpPeerStatus**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetBgpPeerStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getBgpPeerStatus |  |
| [**virtualNetworkGatewaysGetLearnedRoutes**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetLearnedRoutes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getLearnedRoutes |  |
| [**virtualNetworkGatewaysGetVpnProfilePackageUrl**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetVpnProfilePackageUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getvpnprofilepackageurl |  |
| [**virtualNetworkGatewaysGetVpnclientConnectionHealth**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetVpnclientConnectionHealth) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getVpnClientConnectionHealth |  |
| [**virtualNetworkGatewaysGetVpnclientIpsecParameters**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGetVpnclientIpsecParameters) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/getvpnclientipsecparameters |  |
| [**virtualNetworkGatewaysList**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways |  |
| [**virtualNetworkGatewaysListConnections**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysListConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/connections |  |
| [**virtualNetworkGatewaysReset**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysReset) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/reset |  |
| [**virtualNetworkGatewaysResetVpnClientSharedKey**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysResetVpnClientSharedKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/resetvpnclientsharedkey |  |
| [**virtualNetworkGatewaysSetVpnclientIpsecParameters**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysSetVpnclientIpsecParameters) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/setvpnclientipsecparameters |  |
| [**virtualNetworkGatewaysSupportedVpnDevices**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysSupportedVpnDevices) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/supportedvpndevices |  |
| [**virtualNetworkGatewaysUpdateTags**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} |  |
| [**virtualNetworkGatewaysVpnDeviceConfigurationScript**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysVpnDeviceConfigurationScript) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/vpndeviceconfigurationscript |  |


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

 - **Content-Type**: application/json
 - **Accept**: application/json

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

<a id="virtualNetworkGatewaysGenerateVpnProfile"></a>
# **virtualNetworkGatewaysGenerateVpnProfile**
> String virtualNetworkGatewaysGenerateVpnProfile(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Generates VPN profile for P2S client of the virtual network gateway in the specified resource group. Used for IKEV2 and radius based authentication.

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
      String result = apiInstance.virtualNetworkGatewaysGenerateVpnProfile(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGenerateVpnProfile");
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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | VPN profile package URL. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

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

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | VPN client package URL. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

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
 - **Accept**: application/json

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
    String peer = "peer_example"; // String | The IP address of the peer.
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
| **peer** | **String**| The IP address of the peer. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**GatewayRouteListResult**](GatewayRouteListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of learned BGP routes. |  -  |
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of BGP peer statuses. |  -  |
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of advertised BGP routes. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysGetVpnProfilePackageUrl"></a>
# **virtualNetworkGatewaysGetVpnProfilePackageUrl**
> String virtualNetworkGatewaysGetVpnProfilePackageUrl(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets pre-generated VPN profile for P2S client of the virtual network gateway in the specified resource group. The profile needs to be generated first using generateVpnProfile.

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
      String result = apiInstance.virtualNetworkGatewaysGetVpnProfilePackageUrl(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGetVpnProfilePackageUrl");
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

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | VPN profile package URL. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysGetVpnclientConnectionHealth"></a>
# **virtualNetworkGatewaysGetVpnclientConnectionHealth**
> VpnClientConnectionHealthDetailListResult virtualNetworkGatewaysGetVpnclientConnectionHealth(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Get VPN client connection health detail per P2S client connection of the virtual network gateway in the specified resource group.

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
      VpnClientConnectionHealthDetailListResult result = apiInstance.virtualNetworkGatewaysGetVpnclientConnectionHealth(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGetVpnclientConnectionHealth");
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

[**VpnClientConnectionHealthDetailListResult**](VpnClientConnectionHealthDetailListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of VPN client connection health details. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysGetVpnclientIpsecParameters"></a>
# **virtualNetworkGatewaysGetVpnclientIpsecParameters**
> VpnClientIPsecParameters virtualNetworkGatewaysGetVpnclientIpsecParameters(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



The Get VpnclientIpsecParameters operation retrieves information about the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.

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
    String virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The virtual network gateway name.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VpnClientIPsecParameters result = apiInstance.virtualNetworkGatewaysGetVpnclientIpsecParameters(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysGetVpnclientIpsecParameters");
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
| **virtualNetworkGatewayName** | **String**| The virtual network gateway name. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VpnClientIPsecParameters**](VpnClientIPsecParameters.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the set vpnclient ipsec parameters for P2S client of VirtualNetworkGateway resource. |  -  |

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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of VirtualNetworkGateway resources. |  -  |

<a id="virtualNetworkGatewaysListConnections"></a>
# **virtualNetworkGatewaysListConnections**
> VirtualNetworkGatewayListConnectionsResult virtualNetworkGatewaysListConnections(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets all the connections in a virtual network gateway.

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
      VirtualNetworkGatewayListConnectionsResult result = apiInstance.virtualNetworkGatewaysListConnections(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysListConnections");
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

[**VirtualNetworkGatewayListConnectionsResult**](VirtualNetworkGatewayListConnectionsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of VirtualNetworkGatewayConnection resource. |  -  |

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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation reset the primary of the virtual network gateway. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysResetVpnClientSharedKey"></a>
# **virtualNetworkGatewaysResetVpnClientSharedKey**
> virtualNetworkGatewaysResetVpnClientSharedKey(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Resets the VPN client shared key of the virtual network gateway in the specified resource group.

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
      apiInstance.virtualNetworkGatewaysResetVpnClientSharedKey(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysResetVpnClientSharedKey");
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
| **200** | Request successful. The operation reset the vpn client shared key of the virtual network gateway. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysSetVpnclientIpsecParameters"></a>
# **virtualNetworkGatewaysSetVpnclientIpsecParameters**
> VpnClientIPsecParameters virtualNetworkGatewaysSetVpnclientIpsecParameters(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, vpnclientIpsecParams)



The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider.

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
    VpnClientIPsecParameters vpnclientIpsecParams = new VpnClientIPsecParameters(); // VpnClientIPsecParameters | Parameters supplied to the Begin Set vpnclient ipsec parameters of Virtual Network Gateway P2S client operation through Network resource provider.
    try {
      VpnClientIPsecParameters result = apiInstance.virtualNetworkGatewaysSetVpnclientIpsecParameters(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, vpnclientIpsecParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysSetVpnclientIpsecParameters");
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
| **vpnclientIpsecParams** | [**VpnClientIPsecParameters**](VpnClientIPsecParameters.md)| Parameters supplied to the Begin Set vpnclient ipsec parameters of Virtual Network Gateway P2S client operation through Network resource provider. | |

### Return type

[**VpnClientIPsecParameters**](VpnClientIPsecParameters.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation sets the specified vpnclient ipsec parameters for P2S client of the virtual network gateway. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysSupportedVpnDevices"></a>
# **virtualNetworkGatewaysSupportedVpnDevices**
> String virtualNetworkGatewaysSupportedVpnDevices(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets a xml format representation for supported vpn devices.

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
      String result = apiInstance.virtualNetworkGatewaysSupportedVpnDevices(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysSupportedVpnDevices");
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

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Xml format representation for supported vpn devices. |  -  |

<a id="virtualNetworkGatewaysUpdateTags"></a>
# **virtualNetworkGatewaysUpdateTags**
> VirtualNetworkGateway virtualNetworkGatewaysUpdateTags(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Updates a virtual network gateway tags.

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
    VirtualNetworkGatewayConnectionsUpdateTagsRequest parameters = new VirtualNetworkGatewayConnectionsUpdateTagsRequest(); // VirtualNetworkGatewayConnectionsUpdateTagsRequest | Parameters supplied to update virtual network gateway tags.
    try {
      VirtualNetworkGateway result = apiInstance.virtualNetworkGatewaysUpdateTags(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysUpdateTags");
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
| **parameters** | [**VirtualNetworkGatewayConnectionsUpdateTagsRequest**](VirtualNetworkGatewayConnectionsUpdateTagsRequest.md)| Parameters supplied to update virtual network gateway tags. | |

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting VirtualNetworkGateway resource. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |

<a id="virtualNetworkGatewaysVpnDeviceConfigurationScript"></a>
# **virtualNetworkGatewaysVpnDeviceConfigurationScript**
> String virtualNetworkGatewaysVpnDeviceConfigurationScript(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



Gets a xml format representation for vpn device configuration script.

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
    String virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection for which the configuration script is generated.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VpnDeviceScriptParameters parameters = new VpnDeviceScriptParameters(); // VpnDeviceScriptParameters | Parameters supplied to the generate vpn device script operation.
    try {
      String result = apiInstance.virtualNetworkGatewaysVpnDeviceConfigurationScript(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewaysApi#virtualNetworkGatewaysVpnDeviceConfigurationScript");
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
| **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection for which the configuration script is generated. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VpnDeviceScriptParameters**](VpnDeviceScriptParameters.md)| Parameters supplied to the generate vpn device script operation. | |

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Xml format representation for vpn device configuration script. |  -  |

