# HostingEnvironmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hostingEnvironmentsCreateOrUpdateHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsCreateOrUpdateHostingEnvironment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Create or update a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsCreateOrUpdateMultiRolePool**](HostingEnvironmentsApi.md#hostingEnvironmentsCreateOrUpdateMultiRolePool) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Create or update a multiRole pool. |
| [**hostingEnvironmentsCreateOrUpdateWorkerPool**](HostingEnvironmentsApi.md#hostingEnvironmentsCreateOrUpdateWorkerPool) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Create or update a worker pool. |
| [**hostingEnvironmentsDeleteHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsDeleteHostingEnvironment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Delete a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Get properties of hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentCapacities**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentCapacities) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/compute | Get used, available, and total worker capacity for hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentDiagnostics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentDiagnostics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics | Get diagnostic information for hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics/{diagnosticsName} | Get diagnostic information for hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/metricdefinitions | Get global metric definitions of hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/metrics | Get global metrics of hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metricdefinitions | Get metric definitions for a multiRole pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metrics | Get metrics for a multiRole pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/usages | Get usages for a multiRole pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentOperation**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/operations/{operationId} | Get status of an operation on a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentOperations**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentOperations) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/operations | List all currently running operations on the hostingEnvironment (App Service Environment) |
| [**hostingEnvironmentsGetHostingEnvironmentServerFarms**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentServerFarms) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/serverfarms | Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentSites**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/sites | Get all sites on the hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentUsages**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/usages | Get global usages of hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentVips**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentVips) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/virtualip | Get IP addresses assigned to the hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentWebHostingPlans**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentWebHostingPlans) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/webhostingplans | Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/metricdefinitions | Get metric definitions for a worker pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/metrics | Get metrics for a worker pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/usages | Get usages for a worker pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetHostingEnvironments**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments | Get all hostingEnvironments (App Service Environments) in a resource group. |
| [**hostingEnvironmentsGetMultiRolePool**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Get properties of a multiRole pool. |
| [**hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metricdefinitions | Get metric definitions for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetMultiRolePoolInstanceMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePoolInstanceMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metrics | Get metrics for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetMultiRolePoolSkus**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePoolSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/skus | Get available skus for scaling a multiRole pool. |
| [**hostingEnvironmentsGetMultiRolePools**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePools) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools | Get all multi role pools |
| [**hostingEnvironmentsGetWorkerPool**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Get properties of a worker pool. |
| [**hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/instances/{instance}/metricdefinitions | Get metric definitions for a specific instance of a worker pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetWorkerPoolInstanceMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPoolInstanceMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/instances/{instance}/metrics | Get metrics for a specific instance of a worker pool of a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsGetWorkerPoolSkus**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPoolSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/skus | Get available skus for scaling a worker pool. |
| [**hostingEnvironmentsGetWorkerPools**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPools) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools | Get all worker pools |
| [**hostingEnvironmentsRebootHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsRebootHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/reboot | Reboots all machines in a hostingEnvironment (App Service Environment). |
| [**hostingEnvironmentsResumeHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsResumeHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/resume | Resumes the hostingEnvironment. |
| [**hostingEnvironmentsSuspendHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsSuspendHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/suspend | Suspends the hostingEnvironment. |


<a id="hostingEnvironmentsCreateOrUpdateHostingEnvironment"></a>
# **hostingEnvironmentsCreateOrUpdateHostingEnvironment**
> HostingEnvironment hostingEnvironmentsCreateOrUpdateHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope)

Create or update a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    HostingEnvironment hostingEnvironmentEnvelope = new HostingEnvironment(); // HostingEnvironment | Properties of hostingEnvironment (App Service Environment)
    try {
      HostingEnvironment result = apiInstance.hostingEnvironmentsCreateOrUpdateHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsCreateOrUpdateHostingEnvironment");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **hostingEnvironmentEnvelope** | [**HostingEnvironment**](HostingEnvironment.md)| Properties of hostingEnvironment (App Service Environment) | |

### Return type

[**HostingEnvironment**](HostingEnvironment.md)

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
| **400** | Bad request |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |

<a id="hostingEnvironmentsCreateOrUpdateMultiRolePool"></a>
# **hostingEnvironmentsCreateOrUpdateMultiRolePool**
> WorkerPool hostingEnvironmentsCreateOrUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope)

Create or update a multiRole pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    WorkerPool multiRolePoolEnvelope = new WorkerPool(); // WorkerPool | Properties of multiRole pool
    try {
      WorkerPool result = apiInstance.hostingEnvironmentsCreateOrUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsCreateOrUpdateMultiRolePool");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **multiRolePoolEnvelope** | [**WorkerPool**](WorkerPool.md)| Properties of multiRole pool | |

### Return type

[**WorkerPool**](WorkerPool.md)

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
| **400** | Bad request |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |

<a id="hostingEnvironmentsCreateOrUpdateWorkerPool"></a>
# **hostingEnvironmentsCreateOrUpdateWorkerPool**
> WorkerPool hostingEnvironmentsCreateOrUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope)

Create or update a worker pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    WorkerPool workerPoolEnvelope = new WorkerPool(); // WorkerPool | Properties of worker pool
    try {
      WorkerPool result = apiInstance.hostingEnvironmentsCreateOrUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsCreateOrUpdateWorkerPool");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **workerPoolName** | **String**| Name of worker pool | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **workerPoolEnvelope** | [**WorkerPool**](WorkerPool.md)| Properties of worker pool | |

### Return type

[**WorkerPool**](WorkerPool.md)

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
| **400** | Bad request |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |

<a id="hostingEnvironmentsDeleteHostingEnvironment"></a>
# **hostingEnvironmentsDeleteHostingEnvironment**
> Object hostingEnvironmentsDeleteHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, forceDelete)

Delete a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean forceDelete = true; // Boolean | Delete even if the hostingEnvironment (App Service Environment) contains resources
    try {
      Object result = apiInstance.hostingEnvironmentsDeleteHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, forceDelete);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsDeleteHostingEnvironment");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **forceDelete** | **Boolean**| Delete even if the hostingEnvironment (App Service Environment) contains resources | [optional] |

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
| **202** | Operation is in progress |  -  |
| **400** | Bad request |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |

<a id="hostingEnvironmentsGetHostingEnvironment"></a>
# **hostingEnvironmentsGetHostingEnvironment**
> HostingEnvironment hostingEnvironmentsGetHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Get properties of hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostingEnvironment result = apiInstance.hostingEnvironmentsGetHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironment");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HostingEnvironment**](HostingEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentCapacities"></a>
# **hostingEnvironmentsGetHostingEnvironmentCapacities**
> StampCapacityCollection hostingEnvironmentsGetHostingEnvironmentCapacities(resourceGroupName, name, subscriptionId, apiVersion)

Get used, available, and total worker capacity for hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      StampCapacityCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentCapacities(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentCapacities");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**StampCapacityCollection**](StampCapacityCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentDiagnostics"></a>
# **hostingEnvironmentsGetHostingEnvironmentDiagnostics**
> List&lt;HostingEnvironmentDiagnostics&gt; hostingEnvironmentsGetHostingEnvironmentDiagnostics(resourceGroupName, name, subscriptionId, apiVersion)

Get diagnostic information for hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      List<HostingEnvironmentDiagnostics> result = apiInstance.hostingEnvironmentsGetHostingEnvironmentDiagnostics(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentDiagnostics");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**List&lt;HostingEnvironmentDiagnostics&gt;**](HostingEnvironmentDiagnostics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem"></a>
# **hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem**
> HostingEnvironmentDiagnostics hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem(resourceGroupName, name, diagnosticsName, subscriptionId, apiVersion)

Get diagnostic information for hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String diagnosticsName = "diagnosticsName_example"; // String | Name of the diagnostics
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostingEnvironmentDiagnostics result = apiInstance.hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem(resourceGroupName, name, diagnosticsName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **diagnosticsName** | **String**| Name of the diagnostics | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HostingEnvironmentDiagnostics**](HostingEnvironmentDiagnostics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentMetricDefinitions"></a>
# **hostingEnvironmentsGetHostingEnvironmentMetricDefinitions**
> MetricDefinition hostingEnvironmentsGetHostingEnvironmentMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Get global metric definitions of hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      MetricDefinition result = apiInstance.hostingEnvironmentsGetHostingEnvironmentMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentMetricDefinitions");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**MetricDefinition**](MetricDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentMetrics"></a>
# **hostingEnvironmentsGetHostingEnvironmentMetrics**
> ResourceMetricCollection hostingEnvironmentsGetHostingEnvironmentMetrics(resourceGroupName, name, subscriptionId, apiVersion, details, $filter)

Get global metrics of hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | Include instance details
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      ResourceMetricCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentMetrics(resourceGroupName, name, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentMetrics");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| Include instance details | [optional] |
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

<a id="hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions"></a>
# **hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions**
> MetricDefinitionCollection hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Get metric definitions for a multiRole pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      MetricDefinitionCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
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

<a id="hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics"></a>
# **hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics**
> ResourceMetricCollection hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics(resourceGroupName, name, subscriptionId, apiVersion, startTime, endTime, timeGrain, details, $filter)

Get metrics for a multiRole pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String startTime = "startTime_example"; // String | Beginning time of metrics query
    String endTime = "endTime_example"; // String | End time of metrics query
    String timeGrain = "timeGrain_example"; // String | Time granularity of metrics query
    Boolean details = true; // Boolean | Include instance details
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      ResourceMetricCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics(resourceGroupName, name, subscriptionId, apiVersion, startTime, endTime, timeGrain, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **String**| Beginning time of metrics query | [optional] |
| **endTime** | **String**| End time of metrics query | [optional] |
| **timeGrain** | **String**| Time granularity of metrics query | [optional] |
| **details** | **Boolean**| Include instance details | [optional] |
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

<a id="hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages"></a>
# **hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages**
> UsageCollection hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages(resourceGroupName, name, subscriptionId, apiVersion)

Get usages for a multiRole pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      UsageCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**UsageCollection**](UsageCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentOperation"></a>
# **hostingEnvironmentsGetHostingEnvironmentOperation**
> Object hostingEnvironmentsGetHostingEnvironmentOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Get status of an operation on a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String operationId = "operationId_example"; // String | operation identifier GUID
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.hostingEnvironmentsGetHostingEnvironmentOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentOperation");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **operationId** | **String**| operation identifier GUID | |
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
| **200** | Operation completed successfully |  -  |
| **202** | Asynchronous operation in progress |  -  |
| **404** | Not found |  -  |
| **500** | Operation failed |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentOperations"></a>
# **hostingEnvironmentsGetHostingEnvironmentOperations**
> Object hostingEnvironmentsGetHostingEnvironmentOperations(resourceGroupName, name, subscriptionId, apiVersion)

List all currently running operations on the hostingEnvironment (App Service Environment)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.hostingEnvironmentsGetHostingEnvironmentOperations(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentOperations");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
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

<a id="hostingEnvironmentsGetHostingEnvironmentServerFarms"></a>
# **hostingEnvironmentsGetHostingEnvironmentServerFarms**
> ServerFarmCollection hostingEnvironmentsGetHostingEnvironmentServerFarms(resourceGroupName, name, subscriptionId, apiVersion)

Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ServerFarmCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentServerFarms(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentServerFarms");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
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

<a id="hostingEnvironmentsGetHostingEnvironmentSites"></a>
# **hostingEnvironmentsGetHostingEnvironmentSites**
> SiteCollection hostingEnvironmentsGetHostingEnvironmentSites(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude)

Get all sites on the hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String propertiesToInclude = "propertiesToInclude_example"; // String | Comma separated list of site properties to include
    try {
      SiteCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentSites(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentSites");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **propertiesToInclude** | **String**| Comma separated list of site properties to include | [optional] |

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

<a id="hostingEnvironmentsGetHostingEnvironmentUsages"></a>
# **hostingEnvironmentsGetHostingEnvironmentUsages**
> CsmUsageQuotaCollection hostingEnvironmentsGetHostingEnvironmentUsages(resourceGroupName, name, subscriptionId, apiVersion, $filter)

Get global usages of hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      CsmUsageQuotaCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentUsages(resourceGroupName, name, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentUsages");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

### Return type

[**CsmUsageQuotaCollection**](CsmUsageQuotaCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentVips"></a>
# **hostingEnvironmentsGetHostingEnvironmentVips**
> AddressResponse hostingEnvironmentsGetHostingEnvironmentVips(resourceGroupName, name, subscriptionId, apiVersion)

Get IP addresses assigned to the hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AddressResponse result = apiInstance.hostingEnvironmentsGetHostingEnvironmentVips(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentVips");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironmentWebHostingPlans"></a>
# **hostingEnvironmentsGetHostingEnvironmentWebHostingPlans**
> ServerFarmCollection hostingEnvironmentsGetHostingEnvironmentWebHostingPlans(resourceGroupName, name, subscriptionId, apiVersion)

Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ServerFarmCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentWebHostingPlans(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentWebHostingPlans");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
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

<a id="hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions"></a>
# **hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions**
> MetricDefinitionCollection hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get metric definitions for a worker pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      MetricDefinitionCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **workerPoolName** | **String**| Name of worker pool | |
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

<a id="hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics"></a>
# **hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics**
> ResourceMetricCollection hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, details, $filter)

Get metrics for a worker pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | Include instance details
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      ResourceMetricCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **workerPoolName** | **String**| Name of worker pool | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| Include instance details | [optional] |
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

<a id="hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages"></a>
# **hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages**
> UsageCollection hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get usages for a worker pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      UsageCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **workerPoolName** | **String**| Name of worker pool | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**UsageCollection**](UsageCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetHostingEnvironments"></a>
# **hostingEnvironmentsGetHostingEnvironments**
> HostingEnvironmentCollection hostingEnvironmentsGetHostingEnvironments(resourceGroupName, subscriptionId, apiVersion)

Get all hostingEnvironments (App Service Environments) in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostingEnvironmentCollection result = apiInstance.hostingEnvironmentsGetHostingEnvironments(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetHostingEnvironments");
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

[**HostingEnvironmentCollection**](HostingEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetMultiRolePool"></a>
# **hostingEnvironmentsGetMultiRolePool**
> WorkerPool hostingEnvironmentsGetMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion)

Get properties of a multiRole pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      WorkerPool result = apiInstance.hostingEnvironmentsGetMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetMultiRolePool");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**WorkerPool**](WorkerPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions"></a>
# **hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions**
> Object hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions(resourceGroupName, name, instance, subscriptionId, apiVersion)

Get metric definitions for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String instance = "instance_example"; // String | Name of instance in the multiRole pool&gt;
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions(resourceGroupName, name, instance, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **instance** | **String**| Name of instance in the multiRole pool&amp;gt; | |
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

<a id="hostingEnvironmentsGetMultiRolePoolInstanceMetrics"></a>
# **hostingEnvironmentsGetMultiRolePoolInstanceMetrics**
> Object hostingEnvironmentsGetMultiRolePoolInstanceMetrics(resourceGroupName, name, instance, subscriptionId, apiVersion, details)

Get metrics for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String instance = "instance_example"; // String | Name of instance in the multiRole pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | Include instance details
    try {
      Object result = apiInstance.hostingEnvironmentsGetMultiRolePoolInstanceMetrics(resourceGroupName, name, instance, subscriptionId, apiVersion, details);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetMultiRolePoolInstanceMetrics");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **instance** | **String**| Name of instance in the multiRole pool | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| Include instance details | [optional] |

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

<a id="hostingEnvironmentsGetMultiRolePoolSkus"></a>
# **hostingEnvironmentsGetMultiRolePoolSkus**
> SkuInfoCollection hostingEnvironmentsGetMultiRolePoolSkus(resourceGroupName, name, subscriptionId, apiVersion)

Get available skus for scaling a multiRole pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SkuInfoCollection result = apiInstance.hostingEnvironmentsGetMultiRolePoolSkus(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetMultiRolePoolSkus");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SkuInfoCollection**](SkuInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetMultiRolePools"></a>
# **hostingEnvironmentsGetMultiRolePools**
> WorkerPoolCollection hostingEnvironmentsGetMultiRolePools(resourceGroupName, name, subscriptionId, apiVersion)

Get all multi role pools

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      WorkerPoolCollection result = apiInstance.hostingEnvironmentsGetMultiRolePools(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetMultiRolePools");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**WorkerPoolCollection**](WorkerPoolCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetWorkerPool"></a>
# **hostingEnvironmentsGetWorkerPool**
> WorkerPool hostingEnvironmentsGetWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get properties of a worker pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      WorkerPool result = apiInstance.hostingEnvironmentsGetWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetWorkerPool");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **workerPoolName** | **String**| Name of worker pool | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**WorkerPool**](WorkerPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions"></a>
# **hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions**
> Object hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion)

Get metric definitions for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String instance = "instance_example"; // String | Name of instance in the worker pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **workerPoolName** | **String**| Name of worker pool | |
| **instance** | **String**| Name of instance in the worker pool | |
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

<a id="hostingEnvironmentsGetWorkerPoolInstanceMetrics"></a>
# **hostingEnvironmentsGetWorkerPoolInstanceMetrics**
> Object hostingEnvironmentsGetWorkerPoolInstanceMetrics(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, details, $filter)

Get metrics for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String instance = "instance_example"; // String | Name of instance in the worker pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean details = true; // Boolean | Include instance details
    String $filter = "$filter_example"; // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
    try {
      Object result = apiInstance.hostingEnvironmentsGetWorkerPoolInstanceMetrics(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, details, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetWorkerPoolInstanceMetrics");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **workerPoolName** | **String**| Name of worker pool | |
| **instance** | **String**| Name of instance in the worker pool | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **details** | **Boolean**| Include instance details | [optional] |
| **$filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] |

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

<a id="hostingEnvironmentsGetWorkerPoolSkus"></a>
# **hostingEnvironmentsGetWorkerPoolSkus**
> SkuInfoCollection hostingEnvironmentsGetWorkerPoolSkus(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get available skus for scaling a worker pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String workerPoolName = "workerPoolName_example"; // String | Name of worker pool
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SkuInfoCollection result = apiInstance.hostingEnvironmentsGetWorkerPoolSkus(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetWorkerPoolSkus");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **workerPoolName** | **String**| Name of worker pool | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SkuInfoCollection**](SkuInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsGetWorkerPools"></a>
# **hostingEnvironmentsGetWorkerPools**
> WorkerPoolCollection hostingEnvironmentsGetWorkerPools(resourceGroupName, name, subscriptionId, apiVersion)

Get all worker pools

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      WorkerPoolCollection result = apiInstance.hostingEnvironmentsGetWorkerPools(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsGetWorkerPools");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**WorkerPoolCollection**](WorkerPoolCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hostingEnvironmentsRebootHostingEnvironment"></a>
# **hostingEnvironmentsRebootHostingEnvironment**
> Object hostingEnvironmentsRebootHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Reboots all machines in a hostingEnvironment (App Service Environment).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.hostingEnvironmentsRebootHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsRebootHostingEnvironment");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
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
| **202** | Asynchronous operation in progress |  -  |
| **400** | Bad request |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |

<a id="hostingEnvironmentsResumeHostingEnvironment"></a>
# **hostingEnvironmentsResumeHostingEnvironment**
> SiteCollection hostingEnvironmentsResumeHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Resumes the hostingEnvironment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteCollection result = apiInstance.hostingEnvironmentsResumeHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsResumeHostingEnvironment");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

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
| **202** | Operation is in progress |  -  |

<a id="hostingEnvironmentsSuspendHostingEnvironment"></a>
# **hostingEnvironmentsSuspendHostingEnvironment**
> SiteCollection hostingEnvironmentsSuspendHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Suspends the hostingEnvironment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HostingEnvironmentsApi apiInstance = new HostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SiteCollection result = apiInstance.hostingEnvironmentsSuspendHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingEnvironmentsApi#hostingEnvironmentsSuspendHostingEnvironment");
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
| **name** | **String**| Name of hostingEnvironment (App Service Environment) | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

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
| **202** | Operation is in progress |  -  |

