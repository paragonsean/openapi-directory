# WebSiteManagementClient.HostingEnvironmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hostingEnvironmentsCreateOrUpdateHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsCreateOrUpdateHostingEnvironment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Create or update a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsCreateOrUpdateMultiRolePool**](HostingEnvironmentsApi.md#hostingEnvironmentsCreateOrUpdateMultiRolePool) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Create or update a multiRole pool.
[**hostingEnvironmentsCreateOrUpdateWorkerPool**](HostingEnvironmentsApi.md#hostingEnvironmentsCreateOrUpdateWorkerPool) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Create or update a worker pool.
[**hostingEnvironmentsDeleteHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsDeleteHostingEnvironment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Delete a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Get properties of hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentCapacities**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentCapacities) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/compute | Get used, available, and total worker capacity for hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentDiagnostics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentDiagnostics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics | Get diagnostic information for hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics/{diagnosticsName} | Get diagnostic information for hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/metricdefinitions | Get global metric definitions of hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/metrics | Get global metrics of hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metricdefinitions | Get metric definitions for a multiRole pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metrics | Get metrics for a multiRole pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/usages | Get usages for a multiRole pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentOperation**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/operations/{operationId} | Get status of an operation on a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentOperations**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentOperations) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/operations | List all currently running operations on the hostingEnvironment (App Service Environment)
[**hostingEnvironmentsGetHostingEnvironmentServerFarms**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentServerFarms) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/serverfarms | Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentSites**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/sites | Get all sites on the hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentUsages**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/usages | Get global usages of hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentVips**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentVips) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/virtualip | Get IP addresses assigned to the hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentWebHostingPlans**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentWebHostingPlans) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/webhostingplans | Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/metricdefinitions | Get metric definitions for a worker pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/metrics | Get metrics for a worker pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/usages | Get usages for a worker pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetHostingEnvironments**](HostingEnvironmentsApi.md#hostingEnvironmentsGetHostingEnvironments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments | Get all hostingEnvironments (App Service Environments) in a resource group.
[**hostingEnvironmentsGetMultiRolePool**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Get properties of a multiRole pool.
[**hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metricdefinitions | Get metric definitions for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetMultiRolePoolInstanceMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePoolInstanceMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metrics | Get metrics for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetMultiRolePoolSkus**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePoolSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/skus | Get available skus for scaling a multiRole pool.
[**hostingEnvironmentsGetMultiRolePools**](HostingEnvironmentsApi.md#hostingEnvironmentsGetMultiRolePools) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools | Get all multi role pools
[**hostingEnvironmentsGetWorkerPool**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Get properties of a worker pool.
[**hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/instances/{instance}/metricdefinitions | Get metric definitions for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetWorkerPoolInstanceMetrics**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPoolInstanceMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/instances/{instance}/metrics | Get metrics for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsGetWorkerPoolSkus**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPoolSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/skus | Get available skus for scaling a worker pool.
[**hostingEnvironmentsGetWorkerPools**](HostingEnvironmentsApi.md#hostingEnvironmentsGetWorkerPools) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools | Get all worker pools
[**hostingEnvironmentsRebootHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsRebootHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/reboot | Reboots all machines in a hostingEnvironment (App Service Environment).
[**hostingEnvironmentsResumeHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsResumeHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/resume | Resumes the hostingEnvironment.
[**hostingEnvironmentsSuspendHostingEnvironment**](HostingEnvironmentsApi.md#hostingEnvironmentsSuspendHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/suspend | Suspends the hostingEnvironment.



## hostingEnvironmentsCreateOrUpdateHostingEnvironment

> HostingEnvironment hostingEnvironmentsCreateOrUpdateHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope)

Create or update a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let hostingEnvironmentEnvelope = new WebSiteManagementClient.HostingEnvironment(); // HostingEnvironment | Properties of hostingEnvironment (App Service Environment)
apiInstance.hostingEnvironmentsCreateOrUpdateHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **hostingEnvironmentEnvelope** | [**HostingEnvironment**](HostingEnvironment.md)| Properties of hostingEnvironment (App Service Environment) | 

### Return type

[**HostingEnvironment**](HostingEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsCreateOrUpdateMultiRolePool

> WorkerPool hostingEnvironmentsCreateOrUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope)

Create or update a multiRole pool.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let multiRolePoolEnvelope = new WebSiteManagementClient.WorkerPool(); // WorkerPool | Properties of multiRole pool
apiInstance.hostingEnvironmentsCreateOrUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **multiRolePoolEnvelope** | [**WorkerPool**](WorkerPool.md)| Properties of multiRole pool | 

### Return type

[**WorkerPool**](WorkerPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsCreateOrUpdateWorkerPool

> WorkerPool hostingEnvironmentsCreateOrUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope)

Create or update a worker pool.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let workerPoolEnvelope = new WebSiteManagementClient.WorkerPool(); // WorkerPool | Properties of worker pool
apiInstance.hostingEnvironmentsCreateOrUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **workerPoolName** | **String**| Name of worker pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **workerPoolEnvelope** | [**WorkerPool**](WorkerPool.md)| Properties of worker pool | 

### Return type

[**WorkerPool**](WorkerPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsDeleteHostingEnvironment

> Object hostingEnvironmentsDeleteHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, opts)

Delete a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'forceDelete': true // Boolean | Delete even if the hostingEnvironment (App Service Environment) contains resources
};
apiInstance.hostingEnvironmentsDeleteHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **forceDelete** | **Boolean**| Delete even if the hostingEnvironment (App Service Environment) contains resources | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetHostingEnvironment

> HostingEnvironment hostingEnvironmentsGetHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Get properties of hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostingEnvironment**](HostingEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetHostingEnvironmentCapacities

> StampCapacityCollection hostingEnvironmentsGetHostingEnvironmentCapacities(resourceGroupName, name, subscriptionId, apiVersion)

Get used, available, and total worker capacity for hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentCapacities(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StampCapacityCollection**](StampCapacityCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentDiagnostics

> [HostingEnvironmentDiagnostics] hostingEnvironmentsGetHostingEnvironmentDiagnostics(resourceGroupName, name, subscriptionId, apiVersion)

Get diagnostic information for hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentDiagnostics(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[HostingEnvironmentDiagnostics]**](HostingEnvironmentDiagnostics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem

> HostingEnvironmentDiagnostics hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem(resourceGroupName, name, diagnosticsName, subscriptionId, apiVersion)

Get diagnostic information for hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let diagnosticsName = "diagnosticsName_example"; // String | Name of the diagnostics
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentDiagnosticsItem(resourceGroupName, name, diagnosticsName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **diagnosticsName** | **String**| Name of the diagnostics | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostingEnvironmentDiagnostics**](HostingEnvironmentDiagnostics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetHostingEnvironmentMetricDefinitions

> MetricDefinition hostingEnvironmentsGetHostingEnvironmentMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Get global metric definitions of hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MetricDefinition**](MetricDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetHostingEnvironmentMetrics

> ResourceMetricCollection hostingEnvironmentsGetHostingEnvironmentMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get global metrics of hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | Include instance details
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.hostingEnvironmentsGetHostingEnvironmentMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Include instance details | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions

> MetricDefinitionCollection hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Get metric definitions for a multiRole pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentMultiRoleMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics

> ResourceMetricCollection hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get metrics for a multiRole pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': "startTime_example", // String | Beginning time of metrics query
  'endTime': "endTime_example", // String | End time of metrics query
  'timeGrain': "timeGrain_example", // String | Time granularity of metrics query
  'details': true, // Boolean | Include instance details
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.hostingEnvironmentsGetHostingEnvironmentMultiRoleMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **String**| Beginning time of metrics query | [optional] 
 **endTime** | **String**| End time of metrics query | [optional] 
 **timeGrain** | **String**| Time granularity of metrics query | [optional] 
 **details** | **Boolean**| Include instance details | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages

> UsageCollection hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages(resourceGroupName, name, subscriptionId, apiVersion)

Get usages for a multiRole pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentMultiRoleUsages(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**UsageCollection**](UsageCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentOperation

> Object hostingEnvironmentsGetHostingEnvironmentOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Get status of an operation on a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let operationId = "operationId_example"; // String | operation identifier GUID
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **operationId** | **String**| operation identifier GUID | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetHostingEnvironmentOperations

> Object hostingEnvironmentsGetHostingEnvironmentOperations(resourceGroupName, name, subscriptionId, apiVersion)

List all currently running operations on the hostingEnvironment (App Service Environment)

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentOperations(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetHostingEnvironmentServerFarms

> ServerFarmCollection hostingEnvironmentsGetHostingEnvironmentServerFarms(resourceGroupName, name, subscriptionId, apiVersion)

Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentServerFarms(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentSites

> SiteCollection hostingEnvironmentsGetHostingEnvironmentSites(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get all sites on the hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'propertiesToInclude': "propertiesToInclude_example" // String | Comma separated list of site properties to include
};
apiInstance.hostingEnvironmentsGetHostingEnvironmentSites(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **propertiesToInclude** | **String**| Comma separated list of site properties to include | [optional] 

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentUsages

> CsmUsageQuotaCollection hostingEnvironmentsGetHostingEnvironmentUsages(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get global usages of hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.hostingEnvironmentsGetHostingEnvironmentUsages(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**CsmUsageQuotaCollection**](CsmUsageQuotaCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentVips

> AddressResponse hostingEnvironmentsGetHostingEnvironmentVips(resourceGroupName, name, subscriptionId, apiVersion)

Get IP addresses assigned to the hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentVips(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetHostingEnvironmentWebHostingPlans

> ServerFarmCollection hostingEnvironmentsGetHostingEnvironmentWebHostingPlans(resourceGroupName, name, subscriptionId, apiVersion)

Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentWebHostingPlans(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions

> MetricDefinitionCollection hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get metric definitions for a worker pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentWebWorkerMetricDefinitions(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **workerPoolName** | **String**| Name of worker pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics

> ResourceMetricCollection hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, opts)

Get metrics for a worker pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | Include instance details
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.hostingEnvironmentsGetHostingEnvironmentWebWorkerMetrics(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **workerPoolName** | **String**| Name of worker pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Include instance details | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages

> UsageCollection hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get usages for a worker pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironmentWebWorkerUsages(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **workerPoolName** | **String**| Name of worker pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**UsageCollection**](UsageCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetHostingEnvironments

> HostingEnvironmentCollection hostingEnvironmentsGetHostingEnvironments(resourceGroupName, subscriptionId, apiVersion)

Get all hostingEnvironments (App Service Environments) in a resource group.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetHostingEnvironments(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostingEnvironmentCollection**](HostingEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetMultiRolePool

> WorkerPool hostingEnvironmentsGetMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion)

Get properties of a multiRole pool.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WorkerPool**](WorkerPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions

> Object hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions(resourceGroupName, name, instance, subscriptionId, apiVersion)

Get metric definitions for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let instance = "instance_example"; // String | Name of instance in the multiRole pool&gt;
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetMultiRolePoolInstanceMetricDefinitions(resourceGroupName, name, instance, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **instance** | **String**| Name of instance in the multiRole pool&amp;gt; | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetMultiRolePoolInstanceMetrics

> Object hostingEnvironmentsGetMultiRolePoolInstanceMetrics(resourceGroupName, name, instance, subscriptionId, apiVersion, opts)

Get metrics for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let instance = "instance_example"; // String | Name of instance in the multiRole pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true // Boolean | Include instance details
};
apiInstance.hostingEnvironmentsGetMultiRolePoolInstanceMetrics(resourceGroupName, name, instance, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **instance** | **String**| Name of instance in the multiRole pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Include instance details | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetMultiRolePoolSkus

> SkuInfoCollection hostingEnvironmentsGetMultiRolePoolSkus(resourceGroupName, name, subscriptionId, apiVersion)

Get available skus for scaling a multiRole pool.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetMultiRolePoolSkus(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SkuInfoCollection**](SkuInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetMultiRolePools

> WorkerPoolCollection hostingEnvironmentsGetMultiRolePools(resourceGroupName, name, subscriptionId, apiVersion)

Get all multi role pools

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetMultiRolePools(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WorkerPoolCollection**](WorkerPoolCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetWorkerPool

> WorkerPool hostingEnvironmentsGetWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get properties of a worker pool.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **workerPoolName** | **String**| Name of worker pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WorkerPool**](WorkerPool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions

> Object hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion)

Get metric definitions for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let instance = "instance_example"; // String | Name of instance in the worker pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetWorkerPoolInstanceMetricDefinitions(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **workerPoolName** | **String**| Name of worker pool | 
 **instance** | **String**| Name of instance in the worker pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetWorkerPoolInstanceMetrics

> Object hostingEnvironmentsGetWorkerPoolInstanceMetrics(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, opts)

Get metrics for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let instance = "instance_example"; // String | Name of instance in the worker pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | Include instance details
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.hostingEnvironmentsGetWorkerPoolInstanceMetrics(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **workerPoolName** | **String**| Name of worker pool | 
 **instance** | **String**| Name of instance in the worker pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Include instance details | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsGetWorkerPoolSkus

> SkuInfoCollection hostingEnvironmentsGetWorkerPoolSkus(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get available skus for scaling a worker pool.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetWorkerPoolSkus(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **workerPoolName** | **String**| Name of worker pool | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SkuInfoCollection**](SkuInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsGetWorkerPools

> WorkerPoolCollection hostingEnvironmentsGetWorkerPools(resourceGroupName, name, subscriptionId, apiVersion)

Get all worker pools

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsGetWorkerPools(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WorkerPoolCollection**](WorkerPoolCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsRebootHostingEnvironment

> Object hostingEnvironmentsRebootHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Reboots all machines in a hostingEnvironment (App Service Environment).

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsRebootHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## hostingEnvironmentsResumeHostingEnvironment

> SiteCollection hostingEnvironmentsResumeHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Resumes the hostingEnvironment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsResumeHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## hostingEnvironmentsSuspendHostingEnvironment

> SiteCollection hostingEnvironmentsSuspendHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Suspends the hostingEnvironment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.HostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of hostingEnvironment (App Service Environment)
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.hostingEnvironmentsSuspendHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of hostingEnvironment (App Service Environment) | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

