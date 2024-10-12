# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hubVirtualNetworkConnectionsGet**](DefaultApi.md#hubVirtualNetworkConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections/{connectionName} |  |
| [**hubVirtualNetworkConnectionsList**](DefaultApi.md#hubVirtualNetworkConnectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/hubVirtualNetworkConnections |  |
| [**p2sVpnGatewaysCreateOrUpdate**](DefaultApi.md#p2sVpnGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName} |  |
| [**p2sVpnGatewaysDelete**](DefaultApi.md#p2sVpnGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName} |  |
| [**p2sVpnGatewaysGet**](DefaultApi.md#p2sVpnGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName} |  |
| [**p2sVpnGatewaysList**](DefaultApi.md#p2sVpnGatewaysList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/p2svpnGateways |  |
| [**p2sVpnGatewaysListByResourceGroup**](DefaultApi.md#p2sVpnGatewaysListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways |  |
| [**p2sVpnServerConfigurationsCreateOrUpdate**](DefaultApi.md#p2sVpnServerConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWanName}/p2sVpnServerConfigurations/{p2SVpnServerConfigurationName} |  |
| [**p2sVpnServerConfigurationsDelete**](DefaultApi.md#p2sVpnServerConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWanName}/p2sVpnServerConfigurations/{p2SVpnServerConfigurationName} |  |
| [**p2sVpnServerConfigurationsGet**](DefaultApi.md#p2sVpnServerConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWanName}/p2sVpnServerConfigurations/{p2SVpnServerConfigurationName} |  |
| [**p2sVpnServerConfigurationsListByVirtualWan**](DefaultApi.md#p2sVpnServerConfigurationsListByVirtualWan) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWanName}/p2sVpnServerConfigurations |  |
| [**supportedSecurityProviders**](DefaultApi.md#supportedSecurityProviders) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWANName}/supportedSecurityProviders |  |
| [**virtualHubsCreateOrUpdate**](DefaultApi.md#virtualHubsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName} |  |
| [**virtualHubsDelete**](DefaultApi.md#virtualHubsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName} |  |
| [**virtualHubsGet**](DefaultApi.md#virtualHubsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName} |  |
| [**virtualHubsList**](DefaultApi.md#virtualHubsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/virtualHubs |  |
| [**virtualHubsListByResourceGroup**](DefaultApi.md#virtualHubsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs |  |
| [**virtualWansCreateOrUpdate**](DefaultApi.md#virtualWansCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{VirtualWANName} |  |
| [**virtualWansDelete**](DefaultApi.md#virtualWansDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{VirtualWANName} |  |
| [**virtualWansGet**](DefaultApi.md#virtualWansGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{VirtualWANName} |  |
| [**virtualWansList**](DefaultApi.md#virtualWansList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/virtualWans |  |
| [**virtualWansListByResourceGroup**](DefaultApi.md#virtualWansListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans |  |
| [**vpnConnectionsCreateOrUpdate**](DefaultApi.md#vpnConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName} |  |
| [**vpnConnectionsDelete**](DefaultApi.md#vpnConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName} |  |
| [**vpnConnectionsGet**](DefaultApi.md#vpnConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections/{connectionName} |  |
| [**vpnConnectionsListByVpnGateway**](DefaultApi.md#vpnConnectionsListByVpnGateway) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName}/vpnConnections |  |
| [**vpnGatewaysCreateOrUpdate**](DefaultApi.md#vpnGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName} |  |
| [**vpnGatewaysDelete**](DefaultApi.md#vpnGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName} |  |
| [**vpnGatewaysGet**](DefaultApi.md#vpnGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName} |  |
| [**vpnGatewaysList**](DefaultApi.md#vpnGatewaysList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/vpnGateways |  |
| [**vpnGatewaysListByResourceGroup**](DefaultApi.md#vpnGatewaysListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways |  |
| [**vpnSitesConfigurationDownload**](DefaultApi.md#vpnSitesConfigurationDownload) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWANName}/vpnConfiguration |  |
| [**vpnSitesCreateOrUpdate**](DefaultApi.md#vpnSitesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnSites/{vpnSiteName} |  |
| [**vpnSitesDelete**](DefaultApi.md#vpnSitesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnSites/{vpnSiteName} |  |
| [**vpnSitesGet**](DefaultApi.md#vpnSitesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnSites/{vpnSiteName} |  |
| [**vpnSitesList**](DefaultApi.md#vpnSitesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/vpnSites |  |
| [**vpnSitesListByResourceGroup**](DefaultApi.md#vpnSitesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnSites |  |


<a id="hubVirtualNetworkConnectionsGet"></a>
# **hubVirtualNetworkConnectionsGet**
> HubVirtualNetworkConnection hubVirtualNetworkConnectionsGet(subscriptionId, resourceGroupName, virtualHubName, connectionName, apiVersion)



Retrieves the details of a HubVirtualNetworkConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualHub.
    String virtualHubName = "virtualHubName_example"; // String | The name of the VirtualHub.
    String connectionName = "connectionName_example"; // String | The name of the vpn connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      HubVirtualNetworkConnection result = apiInstance.hubVirtualNetworkConnectionsGet(subscriptionId, resourceGroupName, virtualHubName, connectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hubVirtualNetworkConnectionsGet");
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
| **connectionName** | **String**| The name of the vpn connection. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**HubVirtualNetworkConnection**](HubVirtualNetworkConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the HubVirtualNetworkConnection retrieved. |  -  |
| **0** | Error. |  -  |

<a id="hubVirtualNetworkConnectionsList"></a>
# **hubVirtualNetworkConnectionsList**
> ListHubVirtualNetworkConnectionsResult hubVirtualNetworkConnectionsList(subscriptionId, resourceGroupName, virtualHubName, apiVersion)



Retrieves the details of all HubVirtualNetworkConnections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualHub.
    String virtualHubName = "virtualHubName_example"; // String | The name of the VirtualHub.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListHubVirtualNetworkConnectionsResult result = apiInstance.hubVirtualNetworkConnectionsList(subscriptionId, resourceGroupName, virtualHubName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hubVirtualNetworkConnectionsList");
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

### Return type

[**ListHubVirtualNetworkConnectionsResult**](ListHubVirtualNetworkConnectionsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the HubVirtualNetworkConnections for the VirtualHub. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnGatewaysCreateOrUpdate"></a>
# **p2sVpnGatewaysCreateOrUpdate**
> P2SVpnGateway p2sVpnGatewaysCreateOrUpdate(subscriptionId, resourceGroupName, gatewayName, apiVersion, p2SVpnGatewayParameters)



Creates a virtual wan p2s vpn gateway if it doesn&#39;t exist else updates the existing gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the P2SVpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    P2SVpnGateway p2SVpnGatewayParameters = new P2SVpnGateway(); // P2SVpnGateway | Parameters supplied to create or Update a virtual wan p2s vpn gateway.
    try {
      P2SVpnGateway result = apiInstance.p2sVpnGatewaysCreateOrUpdate(subscriptionId, resourceGroupName, gatewayName, apiVersion, p2SVpnGatewayParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnGatewaysCreateOrUpdate");
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
| **p2SVpnGatewayParameters** | [**P2SVpnGateway**](P2SVpnGateway.md)| Parameters supplied to create or Update a virtual wan p2s vpn gateway. | |

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
| **200** | Request successful. Returns the details of the virtual wan p2s vpn Gateway created or updated. |  -  |
| **201** | Request successful. Returns the details of the virtual wan p2s vpn gateway retrieved. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnGatewaysDelete"></a>
# **p2sVpnGatewaysDelete**
> p2sVpnGatewaysDelete(subscriptionId, resourceGroupName, gatewayName, apiVersion)



Deletes a virtual wan p2s vpn gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the P2SVpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.p2sVpnGatewaysDelete(subscriptionId, resourceGroupName, gatewayName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnGatewaysDelete");
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. P2SVpnGateway deleted. |  -  |
| **202** | Request received successfully. P2SVpnGateway deletion is in progress; follow the Location header to poll for final outcome. |  -  |
| **204** | No p2s vpn gateways exist by the name provided. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnGatewaysGet"></a>
# **p2sVpnGatewaysGet**
> P2SVpnGateway p2sVpnGatewaysGet(subscriptionId, resourceGroupName, gatewayName, apiVersion)



Retrieves the details of a virtual wan p2s vpn gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the P2SVpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      P2SVpnGateway result = apiInstance.p2sVpnGatewaysGet(subscriptionId, resourceGroupName, gatewayName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnGatewaysGet");
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
| **200** | Request successful. Returns the details of the virtual wan p2s vpn gateway retrieved. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnGatewaysList"></a>
# **p2sVpnGatewaysList**
> ListP2SVpnGatewaysResult p2sVpnGatewaysList(subscriptionId, apiVersion)



Lists all the P2SVpnGateways in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListP2SVpnGatewaysResult result = apiInstance.p2sVpnGatewaysList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnGatewaysList");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListP2SVpnGatewaysResult**](ListP2SVpnGatewaysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the P2SVpnGateways in the subscription. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnGatewaysListByResourceGroup"></a>
# **p2sVpnGatewaysListByResourceGroup**
> ListP2SVpnGatewaysResult p2sVpnGatewaysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the P2SVpnGateways in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the P2SVpnGateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListP2SVpnGatewaysResult result = apiInstance.p2sVpnGatewaysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnGatewaysListByResourceGroup");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListP2SVpnGatewaysResult**](ListP2SVpnGatewaysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the P2SVpnGateways in the resource group. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnServerConfigurationsCreateOrUpdate"></a>
# **p2sVpnServerConfigurationsCreateOrUpdate**
> P2SVpnServerConfiguration p2sVpnServerConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, virtualWanName, p2SVpnServerConfigurationName, apiVersion, p2SVpnServerConfigurationParameters)



Creates a P2SVpnServerConfiguration to associate with a VirtualWan if it doesn&#39;t exist else updates the existing P2SVpnServerConfiguration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualWan.
    String virtualWanName = "virtualWanName_example"; // String | The name of the VirtualWan.
    String p2SVpnServerConfigurationName = "p2SVpnServerConfigurationName_example"; // String | The name of the P2SVpnServerConfiguration.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    P2SVpnServerConfiguration p2SVpnServerConfigurationParameters = new P2SVpnServerConfiguration(); // P2SVpnServerConfiguration | Parameters supplied to create or Update a P2SVpnServerConfiguration.
    try {
      P2SVpnServerConfiguration result = apiInstance.p2sVpnServerConfigurationsCreateOrUpdate(subscriptionId, resourceGroupName, virtualWanName, p2SVpnServerConfigurationName, apiVersion, p2SVpnServerConfigurationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnServerConfigurationsCreateOrUpdate");
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
| **virtualWanName** | **String**| The name of the VirtualWan. | |
| **p2SVpnServerConfigurationName** | **String**| The name of the P2SVpnServerConfiguration. | |
| **apiVersion** | **String**| Client API version. | |
| **p2SVpnServerConfigurationParameters** | [**P2SVpnServerConfiguration**](P2SVpnServerConfiguration.md)| Parameters supplied to create or Update a P2SVpnServerConfiguration. | |

### Return type

[**P2SVpnServerConfiguration**](P2SVpnServerConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the P2SVpnServerConfiguration created or updated. |  -  |
| **201** | Request successful. Returns the details of the P2SVpnServerConfiguration created or updated. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnServerConfigurationsDelete"></a>
# **p2sVpnServerConfigurationsDelete**
> p2sVpnServerConfigurationsDelete(subscriptionId, resourceGroupName, virtualWanName, p2SVpnServerConfigurationName, apiVersion)



Deletes a P2SVpnServerConfiguration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the P2SVpnServerConfiguration.
    String virtualWanName = "virtualWanName_example"; // String | The name of the VirtualWan.
    String p2SVpnServerConfigurationName = "p2SVpnServerConfigurationName_example"; // String | The name of the P2SVpnServerConfiguration.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.p2sVpnServerConfigurationsDelete(subscriptionId, resourceGroupName, virtualWanName, p2SVpnServerConfigurationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnServerConfigurationsDelete");
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
| **resourceGroupName** | **String**| The resource group name of the P2SVpnServerConfiguration. | |
| **virtualWanName** | **String**| The name of the VirtualWan. | |
| **p2SVpnServerConfigurationName** | **String**| The name of the P2SVpnServerConfiguration. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. P2SVpnServerConfiguration deleted. |  -  |
| **202** | Request received successfully. P2SVpnServerConfiguration deletion is in progress; follow the Location header to poll for final outcome. |  -  |
| **204** | No P2SVpnServerConfigurations exist by the name provided. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnServerConfigurationsGet"></a>
# **p2sVpnServerConfigurationsGet**
> P2SVpnServerConfiguration p2sVpnServerConfigurationsGet(subscriptionId, resourceGroupName, virtualWanName, p2SVpnServerConfigurationName, apiVersion)



Retrieves the details of a P2SVpnServerConfiguration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the P2SVpnServerConfiguration.
    String virtualWanName = "virtualWanName_example"; // String | The name of the VirtualWan.
    String p2SVpnServerConfigurationName = "p2SVpnServerConfigurationName_example"; // String | The name of the P2SVpnServerConfiguration.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      P2SVpnServerConfiguration result = apiInstance.p2sVpnServerConfigurationsGet(subscriptionId, resourceGroupName, virtualWanName, p2SVpnServerConfigurationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnServerConfigurationsGet");
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
| **resourceGroupName** | **String**| The resource group name of the P2SVpnServerConfiguration. | |
| **virtualWanName** | **String**| The name of the VirtualWan. | |
| **p2SVpnServerConfigurationName** | **String**| The name of the P2SVpnServerConfiguration. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**P2SVpnServerConfiguration**](P2SVpnServerConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the P2SVpnServerConfiguration. |  -  |
| **0** | Error. |  -  |

<a id="p2sVpnServerConfigurationsListByVirtualWan"></a>
# **p2sVpnServerConfigurationsListByVirtualWan**
> ListP2SVpnServerConfigurationsResult p2sVpnServerConfigurationsListByVirtualWan(subscriptionId, resourceGroupName, virtualWanName, apiVersion)



Retrieves all P2SVpnServerConfigurations for a particular VirtualWan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualWan.
    String virtualWanName = "virtualWanName_example"; // String | The name of the VirtualWan.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListP2SVpnServerConfigurationsResult result = apiInstance.p2sVpnServerConfigurationsListByVirtualWan(subscriptionId, resourceGroupName, virtualWanName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#p2sVpnServerConfigurationsListByVirtualWan");
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
| **virtualWanName** | **String**| The name of the VirtualWan. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListP2SVpnServerConfigurationsResult**](ListP2SVpnServerConfigurationsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns all P2SVpnServerConfigurations for a VirtualWan. |  -  |
| **0** | Error. |  -  |

<a id="supportedSecurityProviders"></a>
# **supportedSecurityProviders**
> VirtualWanSecurityProviders supportedSecurityProviders(subscriptionId, resourceGroupName, virtualWANName, apiVersion)



Gives the supported security providers for the virtual wan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String virtualWANName = "virtualWANName_example"; // String | The name of the VirtualWAN for which supported security providers are needed.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      VirtualWanSecurityProviders result = apiInstance.supportedSecurityProviders(subscriptionId, resourceGroupName, virtualWANName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#supportedSecurityProviders");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **virtualWANName** | **String**| The name of the VirtualWAN for which supported security providers are needed. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**VirtualWanSecurityProviders**](VirtualWanSecurityProviders.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the object containing supported security providers. |  -  |
| **0** | Error. |  -  |

<a id="virtualHubsCreateOrUpdate"></a>
# **virtualHubsCreateOrUpdate**
> VirtualHub virtualHubsCreateOrUpdate(subscriptionId, resourceGroupName, virtualHubName, apiVersion, virtualHubParameters)



Creates a VirtualHub resource if it doesn&#39;t exist else updates the existing VirtualHub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualHub.
    String virtualHubName = "virtualHubName_example"; // String | The name of the VirtualHub.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    VirtualHub virtualHubParameters = new VirtualHub(); // VirtualHub | Parameters supplied to create or update VirtualHub.
    try {
      VirtualHub result = apiInstance.virtualHubsCreateOrUpdate(subscriptionId, resourceGroupName, virtualHubName, apiVersion, virtualHubParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualHubsCreateOrUpdate");
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
| **virtualHubParameters** | [**VirtualHub**](VirtualHub.md)| Parameters supplied to create or update VirtualHub. | |

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
| **200** | Request successful. Returns the details of the VirtualHub created or updated. |  -  |
| **201** | Request received successfully. Returns the details of the VirtualHub created or updated. |  -  |
| **0** | Error. |  -  |

<a id="virtualHubsDelete"></a>
# **virtualHubsDelete**
> virtualHubsDelete(subscriptionId, resourceGroupName, virtualHubName, apiVersion)



Deletes a VirtualHub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualHub.
    String virtualHubName = "virtualHubName_example"; // String | The name of the VirtualHub.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.virtualHubsDelete(subscriptionId, resourceGroupName, virtualHubName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualHubsDelete");
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. VirtualHub deleted. |  -  |
| **202** | Request received successfully. VirtualHub deletion is in progress; follow the Location header to poll for final outcome. |  -  |
| **204** | No VirtualHubs exist by the name provided. |  -  |
| **0** | Error. |  -  |

<a id="virtualHubsGet"></a>
# **virtualHubsGet**
> VirtualHub virtualHubsGet(subscriptionId, resourceGroupName, virtualHubName, apiVersion)



Retrieves the details of a VirtualHub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualHub.
    String virtualHubName = "virtualHubName_example"; // String | The name of the VirtualHub.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      VirtualHub result = apiInstance.virtualHubsGet(subscriptionId, resourceGroupName, virtualHubName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualHubsGet");
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

### Return type

[**VirtualHub**](VirtualHub.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the VirtualHub retrieved. |  -  |
| **0** | Error. |  -  |

<a id="virtualHubsList"></a>
# **virtualHubsList**
> ListVirtualHubsResult virtualHubsList(subscriptionId, apiVersion)



Lists all the VirtualHubs in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVirtualHubsResult result = apiInstance.virtualHubsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualHubsList");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListVirtualHubsResult**](ListVirtualHubsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the VirtualHubs in the subscription. |  -  |
| **0** | Error. |  -  |

<a id="virtualHubsListByResourceGroup"></a>
# **virtualHubsListByResourceGroup**
> ListVirtualHubsResult virtualHubsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the VirtualHubs in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualHub.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVirtualHubsResult result = apiInstance.virtualHubsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualHubsListByResourceGroup");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListVirtualHubsResult**](ListVirtualHubsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the VirtualHubs in the resource group. |  -  |
| **0** | Error. |  -  |

<a id="virtualWansCreateOrUpdate"></a>
# **virtualWansCreateOrUpdate**
> VirtualWAN virtualWansCreateOrUpdate(subscriptionId, resourceGroupName, virtualWANName, apiVersion, waNParameters)



Creates a VirtualWAN resource if it doesn&#39;t exist else updates the existing VirtualWAN.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualWan.
    String virtualWANName = "virtualWANName_example"; // String | The name of the VirtualWAN being created or updated.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    VirtualWAN waNParameters = new VirtualWAN(); // VirtualWAN | Parameters supplied to create or update VirtualWAN.
    try {
      VirtualWAN result = apiInstance.virtualWansCreateOrUpdate(subscriptionId, resourceGroupName, virtualWANName, apiVersion, waNParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualWansCreateOrUpdate");
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
| **virtualWANName** | **String**| The name of the VirtualWAN being created or updated. | |
| **apiVersion** | **String**| Client API version. | |
| **waNParameters** | [**VirtualWAN**](VirtualWAN.md)| Parameters supplied to create or update VirtualWAN. | |

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
| **200** | Request successful. Returns the details of the VirtualWAN created or updated. |  -  |
| **201** | Create successful. The operation returns the resulting VirtualWAN resource. |  -  |
| **0** | Error. |  -  |

<a id="virtualWansDelete"></a>
# **virtualWansDelete**
> virtualWansDelete(subscriptionId, resourceGroupName, virtualWANName, apiVersion)



Deletes a VirtualWAN.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualWan.
    String virtualWANName = "virtualWANName_example"; // String | The name of the VirtualWAN being deleted.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.virtualWansDelete(subscriptionId, resourceGroupName, virtualWANName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualWansDelete");
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
| **virtualWANName** | **String**| The name of the VirtualWAN being deleted. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. VirtualWAN deleted. |  -  |
| **202** | Request received successfully. VirtualWAN deletion is in progress; follow the Location header to poll for final outcome. |  -  |
| **204** | No VirtualWANs exist by the name provided. |  -  |
| **0** | Error. |  -  |

<a id="virtualWansGet"></a>
# **virtualWansGet**
> VirtualWAN virtualWansGet(resourceGroupName, virtualWANName, apiVersion, subscriptionId)



Retrieves the details of a VirtualWAN.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualWan.
    String virtualWANName = "virtualWANName_example"; // String | The name of the VirtualWAN being retrieved.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualWAN result = apiInstance.virtualWansGet(resourceGroupName, virtualWANName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualWansGet");
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
| **resourceGroupName** | **String**| The resource group name of the VirtualWan. | |
| **virtualWANName** | **String**| The name of the VirtualWAN being retrieved. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualWAN**](VirtualWAN.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the VirtualWAN retrieved. |  -  |
| **0** | Error. |  -  |

<a id="virtualWansList"></a>
# **virtualWansList**
> ListVirtualWANsResult virtualWansList(subscriptionId, apiVersion)



Lists all the VirtualWANs in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVirtualWANsResult result = apiInstance.virtualWansList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualWansList");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListVirtualWANsResult**](ListVirtualWANsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the VirtualWANs in the subscription. |  -  |
| **0** | Error. |  -  |

<a id="virtualWansListByResourceGroup"></a>
# **virtualWansListByResourceGroup**
> ListVirtualWANsResult virtualWansListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the VirtualWANs in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualWan.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVirtualWANsResult result = apiInstance.virtualWansListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#virtualWansListByResourceGroup");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListVirtualWANsResult**](ListVirtualWANsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the VirtualWANs in the resource group. |  -  |
| **0** | Error. |  -  |

<a id="vpnConnectionsCreateOrUpdate"></a>
# **vpnConnectionsCreateOrUpdate**
> VpnConnection vpnConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, gatewayName, connectionName, apiVersion, vpnConnectionParameters)



Creates a vpn connection to a scalable vpn gateway if it doesn&#39;t exist else updates the existing connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String connectionName = "connectionName_example"; // String | The name of the connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    VpnConnection vpnConnectionParameters = new VpnConnection(); // VpnConnection | Parameters supplied to create or Update a VPN Connection.
    try {
      VpnConnection result = apiInstance.vpnConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, gatewayName, connectionName, apiVersion, vpnConnectionParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnConnectionsCreateOrUpdate");
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
| **connectionName** | **String**| The name of the connection. | |
| **apiVersion** | **String**| Client API version. | |
| **vpnConnectionParameters** | [**VpnConnection**](VpnConnection.md)| Parameters supplied to create or Update a VPN Connection. | |

### Return type

[**VpnConnection**](VpnConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the vpn connection created or updated. |  -  |
| **201** | Request successful. Returns the details of the vpn connection created or updated. |  -  |
| **0** | Error. |  -  |

<a id="vpnConnectionsDelete"></a>
# **vpnConnectionsDelete**
> vpnConnectionsDelete(subscriptionId, resourceGroupName, gatewayName, connectionName, apiVersion)



Deletes a vpn connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String connectionName = "connectionName_example"; // String | The name of the connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.vpnConnectionsDelete(subscriptionId, resourceGroupName, gatewayName, connectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnConnectionsDelete");
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
| **connectionName** | **String**| The name of the connection. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Vpn Connection deleted. |  -  |
| **202** | Request received successfully. Vpn Connection deletion is in progress; follow the Location header to poll for final outcome. |  -  |
| **204** | No vpn connections exist by the name provided. |  -  |
| **0** | Error. |  -  |

<a id="vpnConnectionsGet"></a>
# **vpnConnectionsGet**
> VpnConnection vpnConnectionsGet(subscriptionId, resourceGroupName, gatewayName, connectionName, apiVersion)



Retrieves the details of a vpn connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String connectionName = "connectionName_example"; // String | The name of the vpn connection.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      VpnConnection result = apiInstance.vpnConnectionsGet(subscriptionId, resourceGroupName, gatewayName, connectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnConnectionsGet");
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
| **connectionName** | **String**| The name of the vpn connection. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**VpnConnection**](VpnConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the vpn connection. |  -  |
| **0** | Error. |  -  |

<a id="vpnConnectionsListByVpnGateway"></a>
# **vpnConnectionsListByVpnGateway**
> ListVpnConnectionsResult vpnConnectionsListByVpnGateway(subscriptionId, resourceGroupName, gatewayName, apiVersion)



Retrieves all vpn connections for a particular virtual wan vpn gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVpnConnectionsResult result = apiInstance.vpnConnectionsListByVpnGateway(subscriptionId, resourceGroupName, gatewayName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnConnectionsListByVpnGateway");
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

### Return type

[**ListVpnConnectionsResult**](ListVpnConnectionsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns all Vpn connections for a virtual wan vpn gateway. |  -  |
| **0** | Error. |  -  |

<a id="vpnGatewaysCreateOrUpdate"></a>
# **vpnGatewaysCreateOrUpdate**
> VpnGateway vpnGatewaysCreateOrUpdate(subscriptionId, resourceGroupName, gatewayName, apiVersion, vpnGatewayParameters)



Creates a virtual wan vpn gateway if it doesn&#39;t exist else updates the existing gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    VpnGateway vpnGatewayParameters = new VpnGateway(); // VpnGateway | Parameters supplied to create or Update a virtual wan vpn gateway.
    try {
      VpnGateway result = apiInstance.vpnGatewaysCreateOrUpdate(subscriptionId, resourceGroupName, gatewayName, apiVersion, vpnGatewayParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnGatewaysCreateOrUpdate");
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
| **vpnGatewayParameters** | [**VpnGateway**](VpnGateway.md)| Parameters supplied to create or Update a virtual wan vpn gateway. | |

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
| **200** | Request successful. Returns the details of the virtual wan vpn Gateway created or updated. |  -  |
| **201** | Request successful. Returns the details of the virtual wan vpn gateway retrieved. |  -  |
| **0** | Error. |  -  |

<a id="vpnGatewaysDelete"></a>
# **vpnGatewaysDelete**
> vpnGatewaysDelete(subscriptionId, resourceGroupName, gatewayName, apiVersion)



Deletes a virtual wan vpn gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.vpnGatewaysDelete(subscriptionId, resourceGroupName, gatewayName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnGatewaysDelete");
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Vpn Gateway deleted. |  -  |
| **202** | Request received successfully. Vpn Gateway deletion is in progress; follow the Location header to poll for final outcome. |  -  |
| **204** | No vpn gateways exist by the name provided. |  -  |
| **0** | Error. |  -  |

<a id="vpnGatewaysGet"></a>
# **vpnGatewaysGet**
> VpnGateway vpnGatewaysGet(subscriptionId, resourceGroupName, gatewayName, apiVersion)



Retrieves the details of a virtual wan vpn gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String gatewayName = "gatewayName_example"; // String | The name of the gateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      VpnGateway result = apiInstance.vpnGatewaysGet(subscriptionId, resourceGroupName, gatewayName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnGatewaysGet");
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

### Return type

[**VpnGateway**](VpnGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the virtual wan vpn gateway retrieved. |  -  |
| **0** | Error. |  -  |

<a id="vpnGatewaysList"></a>
# **vpnGatewaysList**
> ListVpnGatewaysResult vpnGatewaysList(subscriptionId, apiVersion)



Lists all the VpnGateways in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVpnGatewaysResult result = apiInstance.vpnGatewaysList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnGatewaysList");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListVpnGatewaysResult**](ListVpnGatewaysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the VpnGateways in the subscription. |  -  |
| **0** | Error. |  -  |

<a id="vpnGatewaysListByResourceGroup"></a>
# **vpnGatewaysListByResourceGroup**
> ListVpnGatewaysResult vpnGatewaysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the VpnGateways in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVpnGatewaysResult result = apiInstance.vpnGatewaysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnGatewaysListByResourceGroup");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListVpnGatewaysResult**](ListVpnGatewaysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the VpnGateways in the resource group. |  -  |
| **0** | Error. |  -  |

<a id="vpnSitesConfigurationDownload"></a>
# **vpnSitesConfigurationDownload**
> vpnSitesConfigurationDownload(subscriptionId, resourceGroupName, virtualWANName, apiVersion, request)



Gives the sas-url to download the configurations for vpn-sites in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String virtualWANName = "virtualWANName_example"; // String | The name of the VirtualWAN for which configuration of all vpn-sites is needed.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    GetVpnSitesConfigurationRequest request = new GetVpnSitesConfigurationRequest(); // GetVpnSitesConfigurationRequest | Parameters supplied to download vpn-sites configuration.
    try {
      apiInstance.vpnSitesConfigurationDownload(subscriptionId, resourceGroupName, virtualWANName, apiVersion, request);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnSitesConfigurationDownload");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **virtualWANName** | **String**| The name of the VirtualWAN for which configuration of all vpn-sites is needed. | |
| **apiVersion** | **String**| Client API version. | |
| **request** | [**GetVpnSitesConfigurationRequest**](GetVpnSitesConfigurationRequest.md)| Parameters supplied to download vpn-sites configuration. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Follow the location header for sas-url to output blob. |  -  |
| **202** | Accepted and the operation will complete asynchronously. Follow the location header for sas-url to output blob. |  -  |
| **0** | Error. |  -  |

<a id="vpnSitesCreateOrUpdate"></a>
# **vpnSitesCreateOrUpdate**
> VpnSite vpnSitesCreateOrUpdate(subscriptionId, resourceGroupName, vpnSiteName, apiVersion, vpnSiteParameters)



Creates a VpnSite resource if it doesn&#39;t exist else updates the existing VpnSite.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnSite.
    String vpnSiteName = "vpnSiteName_example"; // String | The name of the VpnSite being created or updated.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    VpnSite vpnSiteParameters = new VpnSite(); // VpnSite | Parameters supplied to create or update VpnSite.
    try {
      VpnSite result = apiInstance.vpnSitesCreateOrUpdate(subscriptionId, resourceGroupName, vpnSiteName, apiVersion, vpnSiteParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnSitesCreateOrUpdate");
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
| **vpnSiteName** | **String**| The name of the VpnSite being created or updated. | |
| **apiVersion** | **String**| Client API version. | |
| **vpnSiteParameters** | [**VpnSite**](VpnSite.md)| Parameters supplied to create or update VpnSite. | |

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
| **200** | Request successful. Returns the details of the VpnSite created or updated. |  -  |
| **201** | Request received successfully. Returns the details of the VpnSite created or updated. |  -  |
| **0** | Error. |  -  |

<a id="vpnSitesDelete"></a>
# **vpnSitesDelete**
> vpnSitesDelete(subscriptionId, resourceGroupName, vpnSiteName, apiVersion)



Deletes a VpnSite.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnSite.
    String vpnSiteName = "vpnSiteName_example"; // String | The name of the VpnSite being deleted.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.vpnSitesDelete(subscriptionId, resourceGroupName, vpnSiteName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnSitesDelete");
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
| **vpnSiteName** | **String**| The name of the VpnSite being deleted. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. VpnSite deleted. |  -  |
| **202** | Request received successfully. VpnSite deletion is in progress. |  -  |
| **204** | No VpnSites exist by the name provided. |  -  |
| **0** | Error. |  -  |

<a id="vpnSitesGet"></a>
# **vpnSitesGet**
> VpnSite vpnSitesGet(subscriptionId, resourceGroupName, vpnSiteName, apiVersion)



Retrieves the details of a VPN site.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnSite.
    String vpnSiteName = "vpnSiteName_example"; // String | The name of the VpnSite being retrieved.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      VpnSite result = apiInstance.vpnSitesGet(subscriptionId, resourceGroupName, vpnSiteName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnSitesGet");
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
| **vpnSiteName** | **String**| The name of the VpnSite being retrieved. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**VpnSite**](VpnSite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of the VpnSite retrieved. |  -  |
| **0** | Error. |  -  |

<a id="vpnSitesList"></a>
# **vpnSitesList**
> ListVpnSitesResult vpnSitesList(subscriptionId, apiVersion)



Lists all the VpnSites in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVpnSitesResult result = apiInstance.vpnSitesList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnSitesList");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListVpnSitesResult**](ListVpnSitesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the VpnSites in the subscription. |  -  |
| **0** | Error. |  -  |

<a id="vpnSitesListByResourceGroup"></a>
# **vpnSitesListByResourceGroup**
> ListVpnSitesResult vpnSitesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the vpnSites in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnSite.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ListVpnSitesResult result = apiInstance.vpnSitesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vpnSitesListByResourceGroup");
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
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ListVpnSitesResult**](ListVpnSitesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. Returns the details of all the vpnSites in the resource group. |  -  |
| **0** | Error. |  -  |

