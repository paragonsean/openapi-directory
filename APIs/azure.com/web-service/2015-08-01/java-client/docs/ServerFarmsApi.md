# ServerFarmsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverFarmsCreateOrUpdateServerFarm**](ServerFarmsApi.md#serverFarmsCreateOrUpdateServerFarm) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Creates or updates an App Service Plan |
| [**serverFarmsCreateOrUpdateVnetRoute**](ServerFarmsApi.md#serverFarmsCreateOrUpdateVnetRoute) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Creates a new route or updates an existing route for a vnet in an app service plan. |
| [**serverFarmsDeleteServerFarm**](ServerFarmsApi.md#serverFarmsDeleteServerFarm) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Deletes a App Service Plan |
| [**serverFarmsDeleteVnetRoute**](ServerFarmsApi.md#serverFarmsDeleteVnetRoute) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Deletes an existing route for a vnet in an app service plan. |
| [**serverFarmsGetRouteForVnet**](ServerFarmsApi.md#serverFarmsGetRouteForVnet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Gets a specific route associated with a vnet, in an app service plan |
| [**serverFarmsGetRoutesForVnet**](ServerFarmsApi.md#serverFarmsGetRoutesForVnet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes | Gets a list of all routes associated with a vnet, in an app service plan |
| [**serverFarmsGetServerFarm**](ServerFarmsApi.md#serverFarmsGetServerFarm) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Gets specified App Service Plan in a resource group |
| [**serverFarmsGetServerFarmMetricDefintions**](ServerFarmsApi.md#serverFarmsGetServerFarmMetricDefintions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/metricdefinitions | List of metrics that can be queried for an App Service Plan |
| [**serverFarmsGetServerFarmMetrics**](ServerFarmsApi.md#serverFarmsGetServerFarmMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/metrics | Queries for App Service Plan metrics |
| [**serverFarmsGetServerFarmOperation**](ServerFarmsApi.md#serverFarmsGetServerFarmOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/operationresults/{operationId} | Gets a server farm operation |
| [**serverFarmsGetServerFarmSites**](ServerFarmsApi.md#serverFarmsGetServerFarmSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/sites | Gets list of Apps associated with an App Service Plan |
| [**serverFarmsGetServerFarmVnetGateway**](ServerFarmsApi.md#serverFarmsGetServerFarmVnetGateway) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Gets the vnet gateway. |
| [**serverFarmsGetServerFarms**](ServerFarmsApi.md#serverFarmsGetServerFarms) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms | Gets collection of App Service Plans in a resource group for a given subscription. |
| [**serverFarmsGetVnetFromServerFarm**](ServerFarmsApi.md#serverFarmsGetVnetFromServerFarm) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName} | Gets a vnet associated with an App Service Plan |
| [**serverFarmsGetVnetsForServerFarm**](ServerFarmsApi.md#serverFarmsGetVnetsForServerFarm) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections | Gets list of VNets associated with App Service Plan |
| [**serverFarmsRebootWorkerForServerFarm**](ServerFarmsApi.md#serverFarmsRebootWorkerForServerFarm) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/workers/{workerName}/reboot | Submit a reboot request for a worker machine in the specified server farm |
| [**serverFarmsRestartSitesForServerFarm**](ServerFarmsApi.md#serverFarmsRestartSitesForServerFarm) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/restartSites | Restarts web apps in a specified App Service Plan |
| [**serverFarmsUpdateServerFarmVnetGateway**](ServerFarmsApi.md#serverFarmsUpdateServerFarmVnetGateway) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the vnet gateway |
| [**serverFarmsUpdateVnetRoute**](ServerFarmsApi.md#serverFarmsUpdateVnetRoute) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Creates a new route or updates an existing route for a vnet in an app service plan. |


<a id="serverFarmsCreateOrUpdateServerFarm"></a>
# **serverFarmsCreateOrUpdateServerFarm**
> ServerFarmWithRichSku serverFarmsCreateOrUpdateServerFarm(resourceGroupName, name, subscriptionId, apiVersion, serverFarmEnvelope, allowPendingState)

Creates or updates an App Service Plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    ServerFarmWithRichSku serverFarmEnvelope = new ServerFarmWithRichSku(); // ServerFarmWithRichSku | Details of App Service Plan
    Boolean allowPendingState = true; // Boolean | OBSOLETE: If true, allow pending state for App Service Plan
    try {
      ServerFarmWithRichSku result = apiInstance.serverFarmsCreateOrUpdateServerFarm(resourceGroupName, name, subscriptionId, apiVersion, serverFarmEnvelope, allowPendingState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsCreateOrUpdateServerFarm");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **serverFarmEnvelope** | [**ServerFarmWithRichSku**](ServerFarmWithRichSku.md)| Details of App Service Plan | |
| **allowPendingState** | **Boolean**| OBSOLETE: If true, allow pending state for App Service Plan | [optional] |

### Return type

[**ServerFarmWithRichSku**](ServerFarmWithRichSku.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Operation is in progress |  -  |

<a id="serverFarmsCreateOrUpdateVnetRoute"></a>
# **serverFarmsCreateOrUpdateVnetRoute**
> VnetRoute serverFarmsCreateOrUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route)

Creates a new route or updates an existing route for a vnet in an app service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String vnetName = "vnetName_example"; // String | Name of virtual network
    String routeName = "routeName_example"; // String | Name of the virtual network route
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetRoute route = new VnetRoute(); // VnetRoute | The route object
    try {
      VnetRoute result = apiInstance.serverFarmsCreateOrUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsCreateOrUpdateVnetRoute");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **vnetName** | **String**| Name of virtual network | |
| **routeName** | **String**| Name of the virtual network route | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **route** | [**VnetRoute**](VnetRoute.md)| The route object | |

### Return type

[**VnetRoute**](VnetRoute.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid request. Ensure that required parameters are given, and that addresses and address spaces are valid |  -  |
| **404** | Route not found. This will only occur when using the PATCH verb. |  -  |

<a id="serverFarmsDeleteServerFarm"></a>
# **serverFarmsDeleteServerFarm**
> Object serverFarmsDeleteServerFarm(resourceGroupName, name, subscriptionId, apiVersion)

Deletes a App Service Plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.serverFarmsDeleteServerFarm(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsDeleteServerFarm");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsDeleteVnetRoute"></a>
# **serverFarmsDeleteVnetRoute**
> Object serverFarmsDeleteVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion)

Deletes an existing route for a vnet in an app service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String vnetName = "vnetName_example"; // String | Name of virtual network
    String routeName = "routeName_example"; // String | Name of the virtual network route
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.serverFarmsDeleteVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsDeleteVnetRoute");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **vnetName** | **String**| Name of virtual network | |
| **routeName** | **String**| Name of the virtual network route | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Specified route does not exist. |  -  |

<a id="serverFarmsGetRouteForVnet"></a>
# **serverFarmsGetRouteForVnet**
> List&lt;VnetRoute&gt; serverFarmsGetRouteForVnet(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion)

Gets a specific route associated with a vnet, in an app service plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String vnetName = "vnetName_example"; // String | Name of virtual network
    String routeName = "routeName_example"; // String | Name of the virtual network route
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<VnetRoute> result = apiInstance.serverFarmsGetRouteForVnet(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetRouteForVnet");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **vnetName** | **String**| Name of virtual network | |
| **routeName** | **String**| Name of the virtual network route | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;VnetRoute&gt;**](VnetRoute.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Specified route does not exist |  -  |

<a id="serverFarmsGetRoutesForVnet"></a>
# **serverFarmsGetRoutesForVnet**
> List&lt;VnetRoute&gt; serverFarmsGetRoutesForVnet(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Gets a list of all routes associated with a vnet, in an app service plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String vnetName = "vnetName_example"; // String | Name of virtual network
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<VnetRoute> result = apiInstance.serverFarmsGetRoutesForVnet(resourceGroupName, name, vnetName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetRoutesForVnet");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **vnetName** | **String**| Name of virtual network | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;VnetRoute&gt;**](VnetRoute.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsGetServerFarm"></a>
# **serverFarmsGetServerFarm**
> ServerFarmWithRichSku serverFarmsGetServerFarm(resourceGroupName, name, subscriptionId, apiVersion)

Gets specified App Service Plan in a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ServerFarmWithRichSku result = apiInstance.serverFarmsGetServerFarm(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetServerFarm");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ServerFarmWithRichSku**](ServerFarmWithRichSku.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsGetServerFarmMetricDefintions"></a>
# **serverFarmsGetServerFarmMetricDefintions**
> MetricDefinitionCollection serverFarmsGetServerFarmMetricDefintions(resourceGroupName, name, subscriptionId, apiVersion)

List of metrics that can be queried for an App Service Plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      MetricDefinitionCollection result = apiInstance.serverFarmsGetServerFarmMetricDefintions(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetServerFarmMetricDefintions");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsGetServerFarmMetrics"></a>
# **serverFarmsGetServerFarmMetrics**
> ResourceMetricCollection serverFarmsGetServerFarmMetrics(resourceGroupName, name, subscriptionId, apiVersion, details, $filter)

Queries for App Service Plan metrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | If true, metrics are broken down per App Service Plan instance
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      ResourceMetricCollection result = apiInstance.serverFarmsGetServerFarmMetrics(resourceGroupName, name, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetServerFarmMetrics");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| If true, metrics are broken down per App Service Plan instance | [optional] |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsGetServerFarmOperation"></a>
# **serverFarmsGetServerFarmOperation**
> ServerFarmWithRichSku serverFarmsGetServerFarmOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Gets a server farm operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of server farm
    String operationId = "operationId_example"; // String | Id of Server farm operation\"&gt;
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ServerFarmWithRichSku result = apiInstance.serverFarmsGetServerFarmOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetServerFarmOperation");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of server farm | |
| **operationId** | **String**| Id of Server farm operation\&quot;&amp;gt; | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ServerFarmWithRichSku**](ServerFarmWithRichSku.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsGetServerFarmSites"></a>
# **serverFarmsGetServerFarmSites**
> SiteCollection serverFarmsGetServerFarmSites(resourceGroupName, name, subscriptionId, apiVersion, $skipToken, $filter, $top)

Gets list of Apps associated with an App Service Plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String $skipToken = "$skipToken_example"; // String | Skip to of web apps in a list. If specified, the resulting list will contain web apps starting from (including) the skipToken. Else, the resulting list contains web apps from the start of the list
    String $filter = "$filter_example"; // String | Supported filter: $filter=state eq running. Returns only web apps that are currently running
    String $top = "$top_example"; // String | List page size. If specified, results are paged.
    try {
      SiteCollection result = apiInstance.serverFarmsGetServerFarmSites(resourceGroupName, name, subscriptionId, apiVersion, $skipToken, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetServerFarmSites");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **$skipToken** | **String**| Skip to of web apps in a list. If specified, the resulting list will contain web apps starting from (including) the skipToken. Else, the resulting list contains web apps from the start of the list | [optional] |
| **$filter** | **String**| Supported filter: $filter&#x3D;state eq running. Returns only web apps that are currently running | [optional] |
| **$top** | **String**| List page size. If specified, results are paged. | [optional] |

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsGetServerFarmVnetGateway"></a>
# **serverFarmsGetServerFarmVnetGateway**
> VnetGateway serverFarmsGetServerFarmVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion)

Gets the vnet gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of the App Service Plan
    String vnetName = "vnetName_example"; // String | Name of the virtual network
    String gatewayName = "gatewayName_example"; // String | Name of the gateway. Only the 'primary' gateway is supported.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      VnetGateway result = apiInstance.serverFarmsGetServerFarmVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetServerFarmVnetGateway");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of the App Service Plan | |
| **vnetName** | **String**| Name of the virtual network | |
| **gatewayName** | **String**| Name of the gateway. Only the &#39;primary&#39; gateway is supported. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsGetServerFarms"></a>
# **serverFarmsGetServerFarms**
> ServerFarmCollection serverFarmsGetServerFarms(resourceGroupName, subscriptionId, apiVersion)

Gets collection of App Service Plans in a resource group for a given subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ServerFarmCollection result = apiInstance.serverFarmsGetServerFarms(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetServerFarms");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsGetVnetFromServerFarm"></a>
# **serverFarmsGetVnetFromServerFarm**
> VnetInfo serverFarmsGetVnetFromServerFarm(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Gets a vnet associated with an App Service Plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String vnetName = "vnetName_example"; // String | Name of virtual network
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      VnetInfo result = apiInstance.serverFarmsGetVnetFromServerFarm(resourceGroupName, name, vnetName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetVnetFromServerFarm");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **vnetName** | **String**| Name of virtual network | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Virtual network could not be found |  -  |

<a id="serverFarmsGetVnetsForServerFarm"></a>
# **serverFarmsGetVnetsForServerFarm**
> List&lt;VnetInfo&gt; serverFarmsGetVnetsForServerFarm(resourceGroupName, name, subscriptionId, apiVersion)

Gets list of VNets associated with App Service Plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<VnetInfo> result = apiInstance.serverFarmsGetVnetsForServerFarm(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsGetVnetsForServerFarm");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;VnetInfo&gt;**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsRebootWorkerForServerFarm"></a>
# **serverFarmsRebootWorkerForServerFarm**
> Object serverFarmsRebootWorkerForServerFarm(resourceGroupName, name, workerName, subscriptionId, apiVersion)

Submit a reboot request for a worker machine in the specified server farm

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of server farm
    String workerName = "workerName_example"; // String | Name of worker machine, typically starts with RD
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.serverFarmsRebootWorkerForServerFarm(resourceGroupName, name, workerName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsRebootWorkerForServerFarm");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of server farm | |
| **workerName** | **String**| Name of worker machine, typically starts with RD | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsRestartSitesForServerFarm"></a>
# **serverFarmsRestartSitesForServerFarm**
> Object serverFarmsRestartSitesForServerFarm(resourceGroupName, name, subscriptionId, apiVersion, softRestart)

Restarts web apps in a specified App Service Plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean softRestart = true; // Boolean | Soft restart applies the configuration settings and restarts the apps if necessary. Hard restart always restarts and reprovisions the apps
    try {
      Object result = apiInstance.serverFarmsRestartSitesForServerFarm(resourceGroupName, name, subscriptionId, apiVersion, softRestart);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsRestartSitesForServerFarm");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **softRestart** | **Boolean**| Soft restart applies the configuration settings and restarts the apps if necessary. Hard restart always restarts and reprovisions the apps | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsUpdateServerFarmVnetGateway"></a>
# **serverFarmsUpdateServerFarmVnetGateway**
> VnetGateway serverFarmsUpdateServerFarmVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Updates the vnet gateway

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String name = "name_example"; // String | The name of the App Service Plan
    String vnetName = "vnetName_example"; // String | The name of the virtual network
    String gatewayName = "gatewayName_example"; // String | The name of the gateway. Only 'primary' is supported.
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetGateway connectionEnvelope = new VnetGateway(); // VnetGateway | The gateway entity.
    try {
      VnetGateway result = apiInstance.serverFarmsUpdateServerFarmVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsUpdateServerFarmVnetGateway");
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
| **resourceGroupName** | **String**| The resource group | |
| **name** | **String**| The name of the App Service Plan | |
| **vnetName** | **String**| The name of the virtual network | |
| **gatewayName** | **String**| The name of the gateway. Only &#39;primary&#39; is supported. | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The gateway entity. | |

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverFarmsUpdateVnetRoute"></a>
# **serverFarmsUpdateVnetRoute**
> VnetRoute serverFarmsUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route)

Creates a new route or updates an existing route for a vnet in an app service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerFarmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerFarmsApi apiInstance = new ServerFarmsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of App Service Plan
    String vnetName = "vnetName_example"; // String | Name of virtual network
    String routeName = "routeName_example"; // String | Name of the virtual network route
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetRoute route = new VnetRoute(); // VnetRoute | The route object
    try {
      VnetRoute result = apiInstance.serverFarmsUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerFarmsApi#serverFarmsUpdateVnetRoute");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of App Service Plan | |
| **vnetName** | **String**| Name of virtual network | |
| **routeName** | **String**| Name of the virtual network route | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **route** | [**VnetRoute**](VnetRoute.md)| The route object | |

### Return type

[**VnetRoute**](VnetRoute.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid request. Ensure that required parameters are given, and that addresses and address spaces are valid |  -  |
| **404** | Route not found. This will only occur when using the PATCH verb. |  -  |

