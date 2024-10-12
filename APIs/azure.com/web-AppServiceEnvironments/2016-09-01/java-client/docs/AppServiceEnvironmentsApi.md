# AppServiceEnvironmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appServiceEnvironmentsCreateOrUpdate**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Create or update an App Service Environment. |
| [**appServiceEnvironmentsCreateOrUpdateMultiRolePool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsCreateOrUpdateMultiRolePool) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Create or update a multi-role pool. |
| [**appServiceEnvironmentsCreateOrUpdateWorkerPool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsCreateOrUpdateWorkerPool) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Create or update a worker pool. |
| [**appServiceEnvironmentsDelete**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Delete an App Service Environment. |
| [**appServiceEnvironmentsGet**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Get the properties of an App Service Environment. |
| [**appServiceEnvironmentsGetDiagnosticsItem**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGetDiagnosticsItem) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics/{diagnosticsName} | Get a diagnostics item for an App Service Environment. |
| [**appServiceEnvironmentsGetMultiRolePool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGetMultiRolePool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Get properties of a multi-role pool. |
| [**appServiceEnvironmentsGetWorkerPool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGetWorkerPool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Get properties of a worker pool. |
| [**appServiceEnvironmentsList**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/hostingEnvironments | Get all App Service Environments for a subscription. |
| [**appServiceEnvironmentsListAppServicePlans**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListAppServicePlans) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/serverfarms | Get all App Service plans in an App Service Environment. |
| [**appServiceEnvironmentsListByResourceGroup**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments | Get all App Service Environments in a resource group. |
| [**appServiceEnvironmentsListCapacities**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListCapacities) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/compute | Get the used, available, and total worker capacity an App Service Environment. |
| [**appServiceEnvironmentsListDiagnostics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListDiagnostics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics | Get diagnostic information for an App Service Environment. |
| [**appServiceEnvironmentsListMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/metricdefinitions | Get global metric definitions of an App Service Environment. |
| [**appServiceEnvironmentsListMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/metrics | Get global metrics of an App Service Environment. |
| [**appServiceEnvironmentsListMultiRoleMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRoleMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metricdefinitions | Get metric definitions for a multi-role pool of an App Service Environment. |
| [**appServiceEnvironmentsListMultiRoleMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRoleMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metrics | Get metrics for a multi-role pool of an App Service Environment. |
| [**appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metricdefinitions | Get metric definitions for a specific instance of a multi-role pool of an App Service Environment. |
| [**appServiceEnvironmentsListMultiRolePoolInstanceMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRolePoolInstanceMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metrics | Get metrics for a specific instance of a multi-role pool of an App Service Environment. |
| [**appServiceEnvironmentsListMultiRolePoolSkus**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRolePoolSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/skus | Get available SKUs for scaling a multi-role pool. |
| [**appServiceEnvironmentsListMultiRolePools**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRolePools) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools | Get all multi-role pools. |
| [**appServiceEnvironmentsListMultiRoleUsages**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRoleUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/usages | Get usage metrics for a multi-role pool of an App Service Environment. |
| [**appServiceEnvironmentsListOperations**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListOperations) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/operations | List all currently running operations on the App Service Environment. |
| [**appServiceEnvironmentsListUsages**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/usages | Get global usage metrics of an App Service Environment. |
| [**appServiceEnvironmentsListVips**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListVips) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/virtualip | Get IP addresses assigned to an App Service Environment. |
| [**appServiceEnvironmentsListWebApps**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWebApps) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/sites | Get all apps in an App Service Environment. |
| [**appServiceEnvironmentsListWebWorkerMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWebWorkerMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/metricdefinitions | Get metric definitions for a worker pool of an App Service Environment. |
| [**appServiceEnvironmentsListWebWorkerMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWebWorkerMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/metrics | Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment). |
| [**appServiceEnvironmentsListWebWorkerUsages**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWebWorkerUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/usages | Get usage metrics for a worker pool of an App Service Environment. |
| [**appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/instances/{instance}/metricdefinitions | Get metric definitions for a specific instance of a worker pool of an App Service Environment. |
| [**appServiceEnvironmentsListWorkerPoolInstanceMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWorkerPoolInstanceMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/instances/{instance}/metrics | Get metrics for a specific instance of a worker pool of an App Service Environment. |
| [**appServiceEnvironmentsListWorkerPoolSkus**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWorkerPoolSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/skus | Get available SKUs for scaling a worker pool. |
| [**appServiceEnvironmentsListWorkerPools**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWorkerPools) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools | Get all worker pools of an App Service Environment. |
| [**appServiceEnvironmentsReboot**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsReboot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/reboot | Reboot all machines in an App Service Environment. |
| [**appServiceEnvironmentsResume**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/resume | Resume an App Service Environment. |
| [**appServiceEnvironmentsSuspend**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsSuspend) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/suspend | Suspend an App Service Environment. |
| [**appServiceEnvironmentsUpdate**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Create or update an App Service Environment. |
| [**appServiceEnvironmentsUpdateMultiRolePool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsUpdateMultiRolePool) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Create or update a multi-role pool. |
| [**appServiceEnvironmentsUpdateWorkerPool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsUpdateWorkerPool) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Create or update a worker pool. |


<a id="appServiceEnvironmentsCreateOrUpdate"></a>
# **appServiceEnvironmentsCreateOrUpdate**
> AppServiceEnvironmentResource appServiceEnvironmentsCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope)

Create or update an App Service Environment.

Create or update an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServiceEnvironmentResource hostingEnvironmentEnvelope = new AppServiceEnvironmentResource(); // AppServiceEnvironmentResource | Configuration details of the App Service Environment.
    try {
      AppServiceEnvironmentResource result = apiInstance.appServiceEnvironmentsCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsCreateOrUpdate");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **hostingEnvironmentEnvelope** | [**AppServiceEnvironmentResource**](AppServiceEnvironmentResource.md)| Configuration details of the App Service Environment. | |

### Return type

[**AppServiceEnvironmentResource**](AppServiceEnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Operation is in progress. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **409** | Conflict. |  -  |

<a id="appServiceEnvironmentsCreateOrUpdateMultiRolePool"></a>
# **appServiceEnvironmentsCreateOrUpdateMultiRolePool**
> WorkerPoolResource appServiceEnvironmentsCreateOrUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope)

Create or update a multi-role pool.

Create or update a multi-role pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    WorkerPoolResource multiRolePoolEnvelope = new WorkerPoolResource(); // WorkerPoolResource | Properties of the multi-role pool.
    try {
      WorkerPoolResource result = apiInstance.appServiceEnvironmentsCreateOrUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsCreateOrUpdateMultiRolePool");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **multiRolePoolEnvelope** | [**WorkerPoolResource**](WorkerPoolResource.md)| Properties of the multi-role pool. | |

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

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
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **409** | Conflict. |  -  |

<a id="appServiceEnvironmentsCreateOrUpdateWorkerPool"></a>
# **appServiceEnvironmentsCreateOrUpdateWorkerPool**
> WorkerPoolResource appServiceEnvironmentsCreateOrUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope)

Create or update a worker pool.

Create or update a worker pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    WorkerPoolResource workerPoolEnvelope = new WorkerPoolResource(); // WorkerPoolResource | Properties of the worker pool.
    try {
      WorkerPoolResource result = apiInstance.appServiceEnvironmentsCreateOrUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsCreateOrUpdateWorkerPool");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of the worker pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **workerPoolEnvelope** | [**WorkerPoolResource**](WorkerPoolResource.md)| Properties of the worker pool. | |

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

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
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **409** | Conflict. |  -  |

<a id="appServiceEnvironmentsDelete"></a>
# **appServiceEnvironmentsDelete**
> appServiceEnvironmentsDelete(resourceGroupName, name, subscriptionId, apiVersion, forceDelete)

Delete an App Service Environment.

Delete an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean forceDelete = true; // Boolean | Specify <code>true</code> to force the deletion even if the App Service Environment contains resources. The default is <code>false</code>.
    try {
      apiInstance.appServiceEnvironmentsDelete(resourceGroupName, name, subscriptionId, apiVersion, forceDelete);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsDelete");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **forceDelete** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to force the deletion even if the App Service Environment contains resources. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] |

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
| **202** | Operation is in progress. |  -  |
| **204** | App Service Environment does not exist |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **409** | Conflict. |  -  |

<a id="appServiceEnvironmentsGet"></a>
# **appServiceEnvironmentsGet**
> AppServiceEnvironmentResource appServiceEnvironmentsGet(resourceGroupName, name, subscriptionId, apiVersion)

Get the properties of an App Service Environment.

Get the properties of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentResource result = apiInstance.appServiceEnvironmentsGet(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsGet");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceEnvironmentResource**](AppServiceEnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsGetDiagnosticsItem"></a>
# **appServiceEnvironmentsGetDiagnosticsItem**
> HostingEnvironmentDiagnostics appServiceEnvironmentsGetDiagnosticsItem(resourceGroupName, name, diagnosticsName, subscriptionId, apiVersion)

Get a diagnostics item for an App Service Environment.

Get a diagnostics item for an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String diagnosticsName = "diagnosticsName_example"; // String | Name of the diagnostics item.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostingEnvironmentDiagnostics result = apiInstance.appServiceEnvironmentsGetDiagnosticsItem(resourceGroupName, name, diagnosticsName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsGetDiagnosticsItem");
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
| **name** | **String**| Name of the App Service Environment. | |
| **diagnosticsName** | **String**| Name of the diagnostics item. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HostingEnvironmentDiagnostics**](HostingEnvironmentDiagnostics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsGetMultiRolePool"></a>
# **appServiceEnvironmentsGetMultiRolePool**
> WorkerPoolResource appServiceEnvironmentsGetMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion)

Get properties of a multi-role pool.

Get properties of a multi-role pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      WorkerPoolResource result = apiInstance.appServiceEnvironmentsGetMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsGetMultiRolePool");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsGetWorkerPool"></a>
# **appServiceEnvironmentsGetWorkerPool**
> WorkerPoolResource appServiceEnvironmentsGetWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get properties of a worker pool.

Get properties of a worker pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      WorkerPoolResource result = apiInstance.appServiceEnvironmentsGetWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsGetWorkerPool");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of the worker pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsList"></a>
# **appServiceEnvironmentsList**
> AppServiceEnvironmentCollection appServiceEnvironmentsList(subscriptionId, apiVersion)

Get all App Service Environments for a subscription.

Get all App Service Environments for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentCollection result = apiInstance.appServiceEnvironmentsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsList");
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

### Return type

[**AppServiceEnvironmentCollection**](AppServiceEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListAppServicePlans"></a>
# **appServiceEnvironmentsListAppServicePlans**
> AppServiceEnvironmentsListAppServicePlans200Response appServiceEnvironmentsListAppServicePlans(resourceGroupName, name, subscriptionId, apiVersion)

Get all App Service plans in an App Service Environment.

Get all App Service plans in an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentsListAppServicePlans200Response result = apiInstance.appServiceEnvironmentsListAppServicePlans(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListAppServicePlans");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceEnvironmentsListAppServicePlans200Response**](AppServiceEnvironmentsListAppServicePlans200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListByResourceGroup"></a>
# **appServiceEnvironmentsListByResourceGroup**
> AppServiceEnvironmentCollection appServiceEnvironmentsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Get all App Service Environments in a resource group.

Get all App Service Environments in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentCollection result = apiInstance.appServiceEnvironmentsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListByResourceGroup");
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

[**AppServiceEnvironmentCollection**](AppServiceEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListCapacities"></a>
# **appServiceEnvironmentsListCapacities**
> StampCapacityCollection appServiceEnvironmentsListCapacities(resourceGroupName, name, subscriptionId, apiVersion)

Get the used, available, and total worker capacity an App Service Environment.

Get the used, available, and total worker capacity an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      StampCapacityCollection result = apiInstance.appServiceEnvironmentsListCapacities(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListCapacities");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**StampCapacityCollection**](StampCapacityCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListDiagnostics"></a>
# **appServiceEnvironmentsListDiagnostics**
> List&lt;HostingEnvironmentDiagnostics&gt; appServiceEnvironmentsListDiagnostics(resourceGroupName, name, subscriptionId, apiVersion)

Get diagnostic information for an App Service Environment.

Get diagnostic information for an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<HostingEnvironmentDiagnostics> result = apiInstance.appServiceEnvironmentsListDiagnostics(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListDiagnostics");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;HostingEnvironmentDiagnostics&gt;**](HostingEnvironmentDiagnostics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMetricDefinitions"></a>
# **appServiceEnvironmentsListMetricDefinitions**
> MetricDefinition appServiceEnvironmentsListMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Get global metric definitions of an App Service Environment.

Get global metric definitions of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      MetricDefinition result = apiInstance.appServiceEnvironmentsListMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMetricDefinitions");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**MetricDefinition**](MetricDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMetrics"></a>
# **appServiceEnvironmentsListMetrics**
> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListMetrics(resourceGroupName, name, subscriptionId, apiVersion, details, $filter)

Get global metrics of an App Service Environment.

Get global metrics of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      AppServiceEnvironmentsListMetrics200Response result = apiInstance.appServiceEnvironmentsListMetrics(resourceGroupName, name, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMetrics");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMultiRoleMetricDefinitions"></a>
# **appServiceEnvironmentsListMultiRoleMetricDefinitions**
> AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response appServiceEnvironmentsListMultiRoleMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Get metric definitions for a multi-role pool of an App Service Environment.

Get metric definitions for a multi-role pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response result = apiInstance.appServiceEnvironmentsListMultiRoleMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMultiRoleMetricDefinitions");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMultiRoleMetrics"></a>
# **appServiceEnvironmentsListMultiRoleMetrics**
> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListMultiRoleMetrics(resourceGroupName, name, subscriptionId, apiVersion, startTime, endTime, timeGrain, details, $filter)

Get metrics for a multi-role pool of an App Service Environment.

Get metrics for a multi-role pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String startTime = "startTime_example"; // String | Beginning time of the metrics query.
    String endTime = "endTime_example"; // String | End time of the metrics query.
    String timeGrain = "timeGrain_example"; // String | Time granularity of the metrics query.
    Boolean details = true; // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      AppServiceEnvironmentsListMetrics200Response result = apiInstance.appServiceEnvironmentsListMultiRoleMetrics(resourceGroupName, name, subscriptionId, apiVersion, startTime, endTime, timeGrain, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMultiRoleMetrics");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **String**| Beginning time of the metrics query. | [optional] |
| **endTime** | **String**| End time of the metrics query. | [optional] |
| **timeGrain** | **String**| Time granularity of the metrics query. | [optional] |
| **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions"></a>
# **appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions**
> AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions(resourceGroupName, name, instance, subscriptionId, apiVersion)

Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.

Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String instance = "instance_example"; // String | Name of the instance in the multi-role pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response result = apiInstance.appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions(resourceGroupName, name, instance, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions");
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
| **name** | **String**| Name of the App Service Environment. | |
| **instance** | **String**| Name of the instance in the multi-role pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMultiRolePoolInstanceMetrics"></a>
# **appServiceEnvironmentsListMultiRolePoolInstanceMetrics**
> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListMultiRolePoolInstanceMetrics(resourceGroupName, name, instance, subscriptionId, apiVersion, details)

Get metrics for a specific instance of a multi-role pool of an App Service Environment.

Get metrics for a specific instance of a multi-role pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String instance = "instance_example"; // String | Name of the instance in the multi-role pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
    try {
      AppServiceEnvironmentsListMetrics200Response result = apiInstance.appServiceEnvironmentsListMultiRolePoolInstanceMetrics(resourceGroupName, name, instance, subscriptionId, apiVersion, details);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMultiRolePoolInstanceMetrics");
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
| **name** | **String**| Name of the App Service Environment. | |
| **instance** | **String**| Name of the instance in the multi-role pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] |

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMultiRolePoolSkus"></a>
# **appServiceEnvironmentsListMultiRolePoolSkus**
> SkuInfoCollection appServiceEnvironmentsListMultiRolePoolSkus(resourceGroupName, name, subscriptionId, apiVersion)

Get available SKUs for scaling a multi-role pool.

Get available SKUs for scaling a multi-role pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SkuInfoCollection result = apiInstance.appServiceEnvironmentsListMultiRolePoolSkus(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMultiRolePoolSkus");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SkuInfoCollection**](SkuInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMultiRolePools"></a>
# **appServiceEnvironmentsListMultiRolePools**
> WorkerPoolCollection appServiceEnvironmentsListMultiRolePools(resourceGroupName, name, subscriptionId, apiVersion)

Get all multi-role pools.

Get all multi-role pools.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      WorkerPoolCollection result = apiInstance.appServiceEnvironmentsListMultiRolePools(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMultiRolePools");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**WorkerPoolCollection**](WorkerPoolCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListMultiRoleUsages"></a>
# **appServiceEnvironmentsListMultiRoleUsages**
> UsageCollection appServiceEnvironmentsListMultiRoleUsages(resourceGroupName, name, subscriptionId, apiVersion)

Get usage metrics for a multi-role pool of an App Service Environment.

Get usage metrics for a multi-role pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      UsageCollection result = apiInstance.appServiceEnvironmentsListMultiRoleUsages(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListMultiRoleUsages");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**UsageCollection**](UsageCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListOperations"></a>
# **appServiceEnvironmentsListOperations**
> List&lt;AppServiceEnvironmentsListOperations200ResponseInner&gt; appServiceEnvironmentsListOperations(resourceGroupName, name, subscriptionId, apiVersion)

List all currently running operations on the App Service Environment.

List all currently running operations on the App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<AppServiceEnvironmentsListOperations200ResponseInner> result = apiInstance.appServiceEnvironmentsListOperations(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListOperations");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;AppServiceEnvironmentsListOperations200ResponseInner&gt;**](AppServiceEnvironmentsListOperations200ResponseInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListUsages"></a>
# **appServiceEnvironmentsListUsages**
> AppServiceEnvironmentsListUsages200Response appServiceEnvironmentsListUsages(resourceGroupName, name, subscriptionId, apiVersion, $filter)

Get global usage metrics of an App Service Environment.

Get global usage metrics of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      AppServiceEnvironmentsListUsages200Response result = apiInstance.appServiceEnvironmentsListUsages(resourceGroupName, name, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListUsages");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**AppServiceEnvironmentsListUsages200Response**](AppServiceEnvironmentsListUsages200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListVips"></a>
# **appServiceEnvironmentsListVips**
> AddressResponse appServiceEnvironmentsListVips(resourceGroupName, name, subscriptionId, apiVersion)

Get IP addresses assigned to an App Service Environment.

Get IP addresses assigned to an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AddressResponse result = apiInstance.appServiceEnvironmentsListVips(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListVips");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListWebApps"></a>
# **appServiceEnvironmentsListWebApps**
> AppServiceEnvironmentsResume200Response appServiceEnvironmentsListWebApps(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude)

Get all apps in an App Service Environment.

Get all apps in an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String propertiesToInclude = "propertiesToInclude_example"; // String | Comma separated list of app properties to include.
    try {
      AppServiceEnvironmentsResume200Response result = apiInstance.appServiceEnvironmentsListWebApps(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListWebApps");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **propertiesToInclude** | **String**| Comma separated list of app properties to include. | [optional] |

### Return type

[**AppServiceEnvironmentsResume200Response**](AppServiceEnvironmentsResume200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListWebWorkerMetricDefinitions"></a>
# **appServiceEnvironmentsListWebWorkerMetricDefinitions**
> AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response appServiceEnvironmentsListWebWorkerMetricDefinitions(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get metric definitions for a worker pool of an App Service Environment.

Get metric definitions for a worker pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response result = apiInstance.appServiceEnvironmentsListWebWorkerMetricDefinitions(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListWebWorkerMetricDefinitions");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of the worker pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListWebWorkerMetrics"></a>
# **appServiceEnvironmentsListWebWorkerMetrics**
> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListWebWorkerMetrics(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, details, $filter)

Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment).

Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      AppServiceEnvironmentsListMetrics200Response result = apiInstance.appServiceEnvironmentsListWebWorkerMetrics(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListWebWorkerMetrics");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of worker pool | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListWebWorkerUsages"></a>
# **appServiceEnvironmentsListWebWorkerUsages**
> UsageCollection appServiceEnvironmentsListWebWorkerUsages(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get usage metrics for a worker pool of an App Service Environment.

Get usage metrics for a worker pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      UsageCollection result = apiInstance.appServiceEnvironmentsListWebWorkerUsages(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListWebWorkerUsages");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of the worker pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**UsageCollection**](UsageCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions"></a>
# **appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions**
> AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion)

Get metric definitions for a specific instance of a worker pool of an App Service Environment.

Get metric definitions for a specific instance of a worker pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
    String instance = "instance_example"; // String | Name of the instance in the worker pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response result = apiInstance.appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of the worker pool. | |
| **instance** | **String**| Name of the instance in the worker pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListWorkerPoolInstanceMetrics"></a>
# **appServiceEnvironmentsListWorkerPoolInstanceMetrics**
> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListWorkerPoolInstanceMetrics(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, details, $filter)

Get metrics for a specific instance of a worker pool of an App Service Environment.

Get metrics for a specific instance of a worker pool of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
    String instance = "instance_example"; // String | Name of the instance in the worker pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      AppServiceEnvironmentsListMetrics200Response result = apiInstance.appServiceEnvironmentsListWorkerPoolInstanceMetrics(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListWorkerPoolInstanceMetrics");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of the worker pool. | |
| **instance** | **String**| Name of the instance in the worker pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListWorkerPoolSkus"></a>
# **appServiceEnvironmentsListWorkerPoolSkus**
> SkuInfoCollection appServiceEnvironmentsListWorkerPoolSkus(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get available SKUs for scaling a worker pool.

Get available SKUs for scaling a worker pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SkuInfoCollection result = apiInstance.appServiceEnvironmentsListWorkerPoolSkus(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListWorkerPoolSkus");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of the worker pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SkuInfoCollection**](SkuInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsListWorkerPools"></a>
# **appServiceEnvironmentsListWorkerPools**
> WorkerPoolCollection appServiceEnvironmentsListWorkerPools(resourceGroupName, name, subscriptionId, apiVersion)

Get all worker pools of an App Service Environment.

Get all worker pools of an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      WorkerPoolCollection result = apiInstance.appServiceEnvironmentsListWorkerPools(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsListWorkerPools");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**WorkerPoolCollection**](WorkerPoolCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="appServiceEnvironmentsReboot"></a>
# **appServiceEnvironmentsReboot**
> appServiceEnvironmentsReboot(resourceGroupName, name, subscriptionId, apiVersion)

Reboot all machines in an App Service Environment.

Reboot all machines in an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.appServiceEnvironmentsReboot(resourceGroupName, name, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsReboot");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

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
| **202** | Asynchronous operation in progress. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **409** | Conflict. |  -  |

<a id="appServiceEnvironmentsResume"></a>
# **appServiceEnvironmentsResume**
> AppServiceEnvironmentsResume200Response appServiceEnvironmentsResume(resourceGroupName, name, subscriptionId, apiVersion)

Resume an App Service Environment.

Resume an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentsResume200Response result = apiInstance.appServiceEnvironmentsResume(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsResume");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceEnvironmentsResume200Response**](AppServiceEnvironmentsResume200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Operation is in progress. |  -  |

<a id="appServiceEnvironmentsSuspend"></a>
# **appServiceEnvironmentsSuspend**
> AppServiceEnvironmentsResume200Response appServiceEnvironmentsSuspend(resourceGroupName, name, subscriptionId, apiVersion)

Suspend an App Service Environment.

Suspend an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AppServiceEnvironmentsResume200Response result = apiInstance.appServiceEnvironmentsSuspend(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsSuspend");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AppServiceEnvironmentsResume200Response**](AppServiceEnvironmentsResume200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Operation is in progress. |  -  |

<a id="appServiceEnvironmentsUpdate"></a>
# **appServiceEnvironmentsUpdate**
> AppServiceEnvironmentResource appServiceEnvironmentsUpdate(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope)

Create or update an App Service Environment.

Create or update an App Service Environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    AppServiceEnvironmentPatchResource hostingEnvironmentEnvelope = new AppServiceEnvironmentPatchResource(); // AppServiceEnvironmentPatchResource | Configuration details of the App Service Environment.
    try {
      AppServiceEnvironmentResource result = apiInstance.appServiceEnvironmentsUpdate(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsUpdate");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **hostingEnvironmentEnvelope** | [**AppServiceEnvironmentPatchResource**](AppServiceEnvironmentPatchResource.md)| Configuration details of the App Service Environment. | |

### Return type

[**AppServiceEnvironmentResource**](AppServiceEnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Operation is in progress. |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **409** | Conflict. |  -  |

<a id="appServiceEnvironmentsUpdateMultiRolePool"></a>
# **appServiceEnvironmentsUpdateMultiRolePool**
> WorkerPoolResource appServiceEnvironmentsUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope)

Create or update a multi-role pool.

Create or update a multi-role pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    WorkerPoolResource multiRolePoolEnvelope = new WorkerPoolResource(); // WorkerPoolResource | Properties of the multi-role pool.
    try {
      WorkerPoolResource result = apiInstance.appServiceEnvironmentsUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsUpdateMultiRolePool");
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
| **name** | **String**| Name of the App Service Environment. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **multiRolePoolEnvelope** | [**WorkerPoolResource**](WorkerPoolResource.md)| Properties of the multi-role pool. | |

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

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
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **409** | Conflict. |  -  |

<a id="appServiceEnvironmentsUpdateWorkerPool"></a>
# **appServiceEnvironmentsUpdateWorkerPool**
> WorkerPoolResource appServiceEnvironmentsUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope)

Create or update a worker pool.

Create or update a worker pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppServiceEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AppServiceEnvironmentsApi apiInstance = new AppServiceEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the App Service Environment.
    String workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    WorkerPoolResource workerPoolEnvelope = new WorkerPoolResource(); // WorkerPoolResource | Properties of the worker pool.
    try {
      WorkerPoolResource result = apiInstance.appServiceEnvironmentsUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppServiceEnvironmentsApi#appServiceEnvironmentsUpdateWorkerPool");
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
| **name** | **String**| Name of the App Service Environment. | |
| **workerPoolName** | **String**| Name of the worker pool. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **workerPoolEnvelope** | [**WorkerPoolResource**](WorkerPoolResource.md)| Properties of the worker pool. | |

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

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
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **409** | Conflict. |  -  |

