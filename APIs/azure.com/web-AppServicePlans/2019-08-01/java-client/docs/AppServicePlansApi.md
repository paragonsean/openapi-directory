# AppServicePlansApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appServicePlansCreateOrUpdate**](AppServicePlansApi.md#appServicePlansCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Creates or updates an App Service Plan. |
| [**appServicePlansCreateOrUpdateVnetRoute**](AppServicePlansApi.md#appServicePlansCreateOrUpdateVnetRoute) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Create or update a Virtual Network route in an App Service plan. |
| [**appServicePlansDelete**](AppServicePlansApi.md#appServicePlansDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Delete an App Service plan. |
| [**appServicePlansDeleteHybridConnection**](AppServicePlansApi.md#appServicePlansDeleteHybridConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Delete a Hybrid Connection in use in an App Service plan. |
| [**appServicePlansDeleteVnetRoute**](AppServicePlansApi.md#appServicePlansDeleteVnetRoute) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Delete a Virtual Network route in an App Service plan. |
| [**appServicePlansGet**](AppServicePlansApi.md#appServicePlansGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Get an App Service plan. |
| [**appServicePlansGetHybridConnection**](AppServicePlansApi.md#appServicePlansGetHybridConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Retrieve a Hybrid Connection in use in an App Service plan. |
| [**appServicePlansGetHybridConnectionPlanLimit**](AppServicePlansApi.md#appServicePlansGetHybridConnectionPlanLimit) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionPlanLimits/limit | Get the maximum number of Hybrid Connections allowed in an App Service plan. |
| [**appServicePlansGetRouteForVnet**](AppServicePlansApi.md#appServicePlansGetRouteForVnet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Get a Virtual Network route in an App Service plan. |
| [**appServicePlansGetServerFarmSkus**](AppServicePlansApi.md#appServicePlansGetServerFarmSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/skus | Gets all selectable SKUs for a given App Service Plan |
| [**appServicePlansGetVnetFromServerFarm**](AppServicePlansApi.md#appServicePlansGetVnetFromServerFarm) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName} | Get a Virtual Network associated with an App Service plan. |
| [**appServicePlansGetVnetGateway**](AppServicePlansApi.md#appServicePlansGetVnetGateway) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Get a Virtual Network gateway. |
| [**appServicePlansList**](AppServicePlansApi.md#appServicePlansList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/serverfarms | Get all App Service plans for a subscription. |
| [**appServicePlansListByResourceGroup**](AppServicePlansApi.md#appServicePlansListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms | Get all App Service plans in a resource group. |
| [**appServicePlansListCapabilities**](AppServicePlansApi.md#appServicePlansListCapabilities) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/capabilities | List all capabilities of an App Service plan. |
| [**appServicePlansListHybridConnectionKeys**](AppServicePlansApi.md#appServicePlansListHybridConnectionKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName}/listKeys | Get the send key name and value of a Hybrid Connection. |
| [**appServicePlansListHybridConnections**](AppServicePlansApi.md#appServicePlansListHybridConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionRelays | Retrieve all Hybrid Connections in use in an App Service plan. |
| [**appServicePlansListRoutesForVnet**](AppServicePlansApi.md#appServicePlansListRoutesForVnet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes | Get all routes that are associated with a Virtual Network in an App Service plan. |
| [**appServicePlansListUsages**](AppServicePlansApi.md#appServicePlansListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/usages | Gets server farm usage information |
| [**appServicePlansListVnets**](AppServicePlansApi.md#appServicePlansListVnets) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections | Get all Virtual Networks associated with an App Service plan. |
| [**appServicePlansListWebApps**](AppServicePlansApi.md#appServicePlansListWebApps) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/sites | Get all apps associated with an App Service plan. |
| [**appServicePlansListWebAppsByHybridConnection**](AppServicePlansApi.md#appServicePlansListWebAppsByHybridConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName}/sites | Get all apps that use a Hybrid Connection in an App Service Plan. |
| [**appServicePlansRebootWorker**](AppServicePlansApi.md#appServicePlansRebootWorker) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/workers/{workerName}/reboot | Reboot a worker machine in an App Service plan. |
| [**appServicePlansRestartWebApps**](AppServicePlansApi.md#appServicePlansRestartWebApps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/restartSites | Restart all apps in an App Service plan. |
| [**appServicePlansUpdate**](AppServicePlansApi.md#appServicePlansUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Creates or updates an App Service Plan. |
| [**appServicePlansUpdateVnetGateway**](AppServicePlansApi.md#appServicePlansUpdateVnetGateway) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Update a Virtual Network gateway. |
| [**appServicePlansUpdateVnetRoute**](AppServicePlansApi.md#appServicePlansUpdateVnetRoute) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Create or update a Virtual Network route in an App Service plan. |


<a id="appServicePlansCreateOrUpdate"></a>
# **appServicePlansCreateOrUpdate**
> AppServicePlansGet200Response appServicePlansCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, appServicePlan)

Creates or updates an App Service Plan.

Description for Creates or updates an App Service Plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServicePlansGet200Response appServicePlan = new AppServicePlansGet200Response(); // AppServicePlansGet200Response | Details of the App Service plan.
    try {
      AppServicePlansGet200Response result = apiInstance.appServicePlansCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, appServicePlan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansCreateOrUpdate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **appServicePlan** | [**AppServicePlansGet200Response**](AppServicePlansGet200Response.md)| Details of the App Service plan. | |

### Return type

[**AppServicePlansGet200Response**](AppServicePlansGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Operation is in progress. |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansCreateOrUpdateVnetRoute"></a>
# **appServicePlansCreateOrUpdateVnetRoute**
> AppServicePlansCreateOrUpdateVnetRouteRequest appServicePlansCreateOrUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route)

Create or update a Virtual Network route in an App Service plan.

Description for Create or update a Virtual Network route in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String vnetName = "vnetName_example"; // String | Name of the Virtual Network.
    String routeName = "routeName_example"; // String | Name of the Virtual Network route.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServicePlansCreateOrUpdateVnetRouteRequest route = new AppServicePlansCreateOrUpdateVnetRouteRequest(); // AppServicePlansCreateOrUpdateVnetRouteRequest | Definition of the Virtual Network route.
    try {
      AppServicePlansCreateOrUpdateVnetRouteRequest result = apiInstance.appServicePlansCreateOrUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansCreateOrUpdateVnetRoute");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **vnetName** | **String**| Name of the Virtual Network. | |
| **routeName** | **String**| Name of the Virtual Network route. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **route** | [**AppServicePlansCreateOrUpdateVnetRouteRequest**](AppServicePlansCreateOrUpdateVnetRouteRequest.md)| Definition of the Virtual Network route. | |

### Return type

[**AppServicePlansCreateOrUpdateVnetRouteRequest**](AppServicePlansCreateOrUpdateVnetRouteRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **400** | Invalid request. Ensure that required parameters are given, and that addresses and address spaces are valid. |  -  |
| **404** | Route not found. |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansDelete"></a>
# **appServicePlansDelete**
> appServicePlansDelete(resourceGroupName, name, subscriptionId, apiVersion)

Delete an App Service plan.

Description for Delete an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServicePlansDelete(resourceGroupName, name, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansDelete");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

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
| **200** | OK. |  -  |
| **204** | OK. |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansDeleteHybridConnection"></a>
# **appServicePlansDeleteHybridConnection**
> appServicePlansDeleteHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Delete a Hybrid Connection in use in an App Service plan.

Description for Delete a Hybrid Connection in use in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String namespaceName = "namespaceName_example"; // String | Name of the Service Bus namespace.
    String relayName = "relayName_example"; // String | Name of the Service Bus relay.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServicePlansDeleteHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansDeleteHybridConnection");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **namespaceName** | **String**| Name of the Service Bus namespace. | |
| **relayName** | **String**| Name of the Service Bus relay. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

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
| **200** | Successfully deleted hybrid connection |  -  |
| **204** | Hybrid connection does not exist |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansDeleteVnetRoute"></a>
# **appServicePlansDeleteVnetRoute**
> appServicePlansDeleteVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion)

Delete a Virtual Network route in an App Service plan.

Description for Delete a Virtual Network route in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String vnetName = "vnetName_example"; // String | Name of the Virtual Network.
    String routeName = "routeName_example"; // String | Name of the Virtual Network route.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServicePlansDeleteVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansDeleteVnetRoute");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **vnetName** | **String**| Name of the Virtual Network. | |
| **routeName** | **String**| Name of the Virtual Network route. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

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
| **200** | Successfully deleted Virtual Network route. |  -  |
| **404** | Specified Virtual Network route does not exist. |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansGet"></a>
# **appServicePlansGet**
> AppServicePlansGet200Response appServicePlansGet(resourceGroupName, name, subscriptionId, apiVersion)

Get an App Service plan.

Description for Get an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServicePlansGet200Response result = apiInstance.appServicePlansGet(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansGet");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServicePlansGet200Response**](AppServicePlansGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **404** | Not found. |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansGetHybridConnection"></a>
# **appServicePlansGetHybridConnection**
> AppServicePlansGetHybridConnection200Response appServicePlansGetHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Retrieve a Hybrid Connection in use in an App Service plan.

Description for Retrieve a Hybrid Connection in use in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String namespaceName = "namespaceName_example"; // String | Name of the Service Bus namespace.
    String relayName = "relayName_example"; // String | Name of the Service Bus relay.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServicePlansGetHybridConnection200Response result = apiInstance.appServicePlansGetHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansGetHybridConnection");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **namespaceName** | **String**| Name of the Service Bus namespace. | |
| **relayName** | **String**| Name of the Service Bus relay. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServicePlansGetHybridConnection200Response**](AppServicePlansGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansGetHybridConnectionPlanLimit"></a>
# **appServicePlansGetHybridConnectionPlanLimit**
> HybridConnectionLimits appServicePlansGetHybridConnectionPlanLimit(resourceGroupName, name, subscriptionId, apiVersion)

Get the maximum number of Hybrid Connections allowed in an App Service plan.

Description for Get the maximum number of Hybrid Connections allowed in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HybridConnectionLimits result = apiInstance.appServicePlansGetHybridConnectionPlanLimit(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansGetHybridConnectionPlanLimit");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HybridConnectionLimits**](HybridConnectionLimits.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansGetRouteForVnet"></a>
# **appServicePlansGetRouteForVnet**
> List&lt;AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner&gt; appServicePlansGetRouteForVnet(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion)

Get a Virtual Network route in an App Service plan.

Description for Get a Virtual Network route in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String vnetName = "vnetName_example"; // String | Name of the Virtual Network.
    String routeName = "routeName_example"; // String | Name of the Virtual Network route.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner> result = apiInstance.appServicePlansGetRouteForVnet(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansGetRouteForVnet");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **vnetName** | **String**| Name of the Virtual Network. | |
| **routeName** | **String**| Name of the Virtual Network route. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner&gt;**](AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **404** | Specified route does not exist. |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansGetServerFarmSkus"></a>
# **appServicePlansGetServerFarmSkus**
> Object appServicePlansGetServerFarmSkus(resourceGroupName, name, subscriptionId, apiVersion)

Gets all selectable SKUs for a given App Service Plan

Description for Gets all selectable SKUs for a given App Service Plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.appServicePlansGetServerFarmSkus(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansGetServerFarmSkus");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansGetVnetFromServerFarm"></a>
# **appServicePlansGetVnetFromServerFarm**
> AppServicePlansGetVnetFromServerFarm200Response appServicePlansGetVnetFromServerFarm(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Get a Virtual Network associated with an App Service plan.

Description for Get a Virtual Network associated with an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String vnetName = "vnetName_example"; // String | Name of the Virtual Network.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServicePlansGetVnetFromServerFarm200Response result = apiInstance.appServicePlansGetVnetFromServerFarm(resourceGroupName, name, vnetName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansGetVnetFromServerFarm");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **vnetName** | **String**| Name of the Virtual Network. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServicePlansGetVnetFromServerFarm200Response**](AppServicePlansGetVnetFromServerFarm200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **404** | Virtual network could not be found. |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansGetVnetGateway"></a>
# **appServicePlansGetVnetGateway**
> AppServicePlansGetVnetGateway200Response appServicePlansGetVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion)

Get a Virtual Network gateway.

Description for Get a Virtual Network gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String vnetName = "vnetName_example"; // String | Name of the Virtual Network.
    String gatewayName = "gatewayName_example"; // String | Name of the gateway. Only the 'primary' gateway is supported.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServicePlansGetVnetGateway200Response result = apiInstance.appServicePlansGetVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansGetVnetGateway");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **vnetName** | **String**| Name of the Virtual Network. | |
| **gatewayName** | **String**| Name of the gateway. Only the &#39;primary&#39; gateway is supported. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServicePlansGetVnetGateway200Response**](AppServicePlansGetVnetGateway200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansList"></a>
# **appServicePlansList**
> AppServicePlansList200Response appServicePlansList(subscriptionId, apiVersion, detailed)

Get all App Service plans for a subscription.

Description for Get all App Service plans for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean detailed = true; // Boolean | Specify <code>true</code> to return all App Service plan properties. The default is <code>false</code>, which returns a subset of the properties.  Retrieval of all properties may increase the API latency.
    try {
      AppServicePlansList200Response result = apiInstance.appServicePlansList(subscriptionId, apiVersion, detailed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansList");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **detailed** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to return all App Service plan properties. The default is &lt;code&gt;false&lt;/code&gt;, which returns a subset of the properties.  Retrieval of all properties may increase the API latency. | [optional] |

### Return type

[**AppServicePlansList200Response**](AppServicePlansList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListByResourceGroup"></a>
# **appServicePlansListByResourceGroup**
> AppServicePlansList200Response appServicePlansListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Get all App Service plans in a resource group.

Description for Get all App Service plans in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServicePlansList200Response result = apiInstance.appServicePlansListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListByResourceGroup");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServicePlansList200Response**](AppServicePlansList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListCapabilities"></a>
# **appServicePlansListCapabilities**
> List&lt;AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner&gt; appServicePlansListCapabilities(resourceGroupName, name, subscriptionId, apiVersion)

List all capabilities of an App Service plan.

Description for List all capabilities of an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner> result = apiInstance.appServicePlansListCapabilities(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListCapabilities");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner&gt;**](AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListHybridConnectionKeys"></a>
# **appServicePlansListHybridConnectionKeys**
> HybridConnectionKey appServicePlansListHybridConnectionKeys(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Get the send key name and value of a Hybrid Connection.

Description for Get the send key name and value of a Hybrid Connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String namespaceName = "namespaceName_example"; // String | The name of the Service Bus namespace.
    String relayName = "relayName_example"; // String | The name of the Service Bus relay.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HybridConnectionKey result = apiInstance.appServicePlansListHybridConnectionKeys(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListHybridConnectionKeys");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **namespaceName** | **String**| The name of the Service Bus namespace. | |
| **relayName** | **String**| The name of the Service Bus relay. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HybridConnectionKey**](HybridConnectionKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListHybridConnections"></a>
# **appServicePlansListHybridConnections**
> HybridConnectionCollection appServicePlansListHybridConnections(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve all Hybrid Connections in use in an App Service plan.

Description for Retrieve all Hybrid Connections in use in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HybridConnectionCollection result = apiInstance.appServicePlansListHybridConnections(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListHybridConnections");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HybridConnectionCollection**](HybridConnectionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListRoutesForVnet"></a>
# **appServicePlansListRoutesForVnet**
> List&lt;AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner&gt; appServicePlansListRoutesForVnet(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Get all routes that are associated with a Virtual Network in an App Service plan.

Description for Get all routes that are associated with a Virtual Network in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String vnetName = "vnetName_example"; // String | Name of the Virtual Network.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner> result = apiInstance.appServicePlansListRoutesForVnet(resourceGroupName, name, vnetName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListRoutesForVnet");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **vnetName** | **String**| Name of the Virtual Network. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner&gt;**](AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListUsages"></a>
# **appServicePlansListUsages**
> AppServicePlansListUsages200Response appServicePlansListUsages(resourceGroupName, name, subscriptionId, apiVersion, $filter)

Gets server farm usage information

Description for Gets server farm usage information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of App Service Plan
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2').
    try {
      AppServicePlansListUsages200Response result = apiInstance.appServicePlansListUsages(resourceGroupName, name, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListUsages");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of App Service Plan | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;). | [optional] |

### Return type

[**AppServicePlansListUsages200Response**](AppServicePlansListUsages200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListVnets"></a>
# **appServicePlansListVnets**
> List&lt;AppServicePlansListVnets200ResponseInner&gt; appServicePlansListVnets(resourceGroupName, name, subscriptionId, apiVersion)

Get all Virtual Networks associated with an App Service plan.

Description for Get all Virtual Networks associated with an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<AppServicePlansListVnets200ResponseInner> result = apiInstance.appServicePlansListVnets(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListVnets");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;AppServicePlansListVnets200ResponseInner&gt;**](AppServicePlansListVnets200ResponseInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListWebApps"></a>
# **appServicePlansListWebApps**
> AppServicePlansListWebApps200Response appServicePlansListWebApps(resourceGroupName, name, subscriptionId, apiVersion, $skipToken, $filter, $top)

Get all apps associated with an App Service plan.

Description for Get all apps associated with an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String $skipToken = "$skipToken_example"; // String | Skip to a web app in the list of webapps associated with app service plan. If specified, the resulting list will contain web apps starting from (including) the skipToken. Otherwise, the resulting list contains web apps from the start of the list
    String $filter = "$filter_example"; // String | Supported filter: $filter=state eq running. Returns only web apps that are currently running
    String $top = "$top_example"; // String | List page size. If specified, results are paged.
    try {
      AppServicePlansListWebApps200Response result = apiInstance.appServicePlansListWebApps(resourceGroupName, name, subscriptionId, apiVersion, $skipToken, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListWebApps");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **$skipToken** | **String**| Skip to a web app in the list of webapps associated with app service plan. If specified, the resulting list will contain web apps starting from (including) the skipToken. Otherwise, the resulting list contains web apps from the start of the list | [optional] |
| **$filter** | **String**| Supported filter: $filter&#x3D;state eq running. Returns only web apps that are currently running | [optional] |
| **$top** | **String**| List page size. If specified, results are paged. | [optional] |

### Return type

[**AppServicePlansListWebApps200Response**](AppServicePlansListWebApps200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansListWebAppsByHybridConnection"></a>
# **appServicePlansListWebAppsByHybridConnection**
> ResourceCollection appServicePlansListWebAppsByHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Get all apps that use a Hybrid Connection in an App Service Plan.

Description for Get all apps that use a Hybrid Connection in an App Service Plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String namespaceName = "namespaceName_example"; // String | Name of the Hybrid Connection namespace.
    String relayName = "relayName_example"; // String | Name of the Hybrid Connection relay.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ResourceCollection result = apiInstance.appServicePlansListWebAppsByHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansListWebAppsByHybridConnection");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **namespaceName** | **String**| Name of the Hybrid Connection namespace. | |
| **relayName** | **String**| Name of the Hybrid Connection relay. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ResourceCollection**](ResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansRebootWorker"></a>
# **appServicePlansRebootWorker**
> appServicePlansRebootWorker(resourceGroupName, name, workerName, subscriptionId, apiVersion)

Reboot a worker machine in an App Service plan.

Description for Reboot a worker machine in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String workerName = "workerName_example"; // String | Name of worker machine, which typically starts with RD.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServicePlansRebootWorker(resourceGroupName, name, workerName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansRebootWorker");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **workerName** | **String**| Name of worker machine, which typically starts with RD. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

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
| **204** | No Content |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansRestartWebApps"></a>
# **appServicePlansRestartWebApps**
> appServicePlansRestartWebApps(resourceGroupName, name, subscriptionId, apiVersion, softRestart)

Restart all apps in an App Service plan.

Description for Restart all apps in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean softRestart = true; // Boolean | Specify <code>true</code> to perform a soft restart, applies the configuration settings and restarts the apps if necessary. The default is <code>false</code>, which always restarts and reprovisions the apps
    try {
      apiInstance.appServicePlansRestartWebApps(resourceGroupName, name, subscriptionId, apiVersion, softRestart);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansRestartWebApps");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **softRestart** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to perform a soft restart, applies the configuration settings and restarts the apps if necessary. The default is &lt;code&gt;false&lt;/code&gt;, which always restarts and reprovisions the apps | [optional] |

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
| **204** | No Content |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansUpdate"></a>
# **appServicePlansUpdate**
> AppServicePlansGet200Response appServicePlansUpdate(resourceGroupName, name, subscriptionId, apiVersion, appServicePlan)

Creates or updates an App Service Plan.

Description for Creates or updates an App Service Plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServicePlanPatchResource appServicePlan = new AppServicePlanPatchResource(); // AppServicePlanPatchResource | Details of the App Service plan.
    try {
      AppServicePlansGet200Response result = apiInstance.appServicePlansUpdate(resourceGroupName, name, subscriptionId, apiVersion, appServicePlan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansUpdate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **appServicePlan** | [**AppServicePlanPatchResource**](AppServicePlanPatchResource.md)| Details of the App Service plan. | |

### Return type

[**AppServicePlansGet200Response**](AppServicePlansGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Operation is in progress. |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansUpdateVnetGateway"></a>
# **appServicePlansUpdateVnetGateway**
> AppServicePlansGetVnetGateway200Response appServicePlansUpdateVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Update a Virtual Network gateway.

Description for Update a Virtual Network gateway.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String vnetName = "vnetName_example"; // String | Name of the Virtual Network.
    String gatewayName = "gatewayName_example"; // String | Name of the gateway. Only the 'primary' gateway is supported.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServicePlansGetVnetGateway200Response connectionEnvelope = new AppServicePlansGetVnetGateway200Response(); // AppServicePlansGetVnetGateway200Response | Definition of the gateway.
    try {
      AppServicePlansGetVnetGateway200Response result = apiInstance.appServicePlansUpdateVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansUpdateVnetGateway");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **vnetName** | **String**| Name of the Virtual Network. | |
| **gatewayName** | **String**| Name of the gateway. Only the &#39;primary&#39; gateway is supported. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **connectionEnvelope** | [**AppServicePlansGetVnetGateway200Response**](AppServicePlansGetVnetGateway200Response.md)| Definition of the gateway. | |

### Return type

[**AppServicePlansGetVnetGateway200Response**](AppServicePlansGetVnetGateway200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="appServicePlansUpdateVnetRoute"></a>
# **appServicePlansUpdateVnetRoute**
> AppServicePlansCreateOrUpdateVnetRouteRequest appServicePlansUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route)

Create or update a Virtual Network route in an App Service plan.

Description for Create or update a Virtual Network route in an App Service plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServicePlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServicePlansApi apiInstance = new AppServicePlansApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service plan.
    String vnetName = "vnetName_example"; // String | Name of the Virtual Network.
    String routeName = "routeName_example"; // String | Name of the Virtual Network route.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServicePlansCreateOrUpdateVnetRouteRequest route = new AppServicePlansCreateOrUpdateVnetRouteRequest(); // AppServicePlansCreateOrUpdateVnetRouteRequest | Definition of the Virtual Network route.
    try {
      AppServicePlansCreateOrUpdateVnetRouteRequest result = apiInstance.appServicePlansUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServicePlansApi#appServicePlansUpdateVnetRoute");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **name** | **String**| Name of the App Service plan. | |
| **vnetName** | **String**| Name of the Virtual Network. | |
| **routeName** | **String**| Name of the Virtual Network route. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **route** | [**AppServicePlansCreateOrUpdateVnetRouteRequest**](AppServicePlansCreateOrUpdateVnetRouteRequest.md)| Definition of the Virtual Network route. | |

### Return type

[**AppServicePlansCreateOrUpdateVnetRouteRequest**](AppServicePlansCreateOrUpdateVnetRouteRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **400** | Invalid request. Ensure that required parameters are given, and that addresses and address spaces are valid. |  -  |
| **404** | Route not found. |  -  |
| **0** | App Service error response. |  -  |

