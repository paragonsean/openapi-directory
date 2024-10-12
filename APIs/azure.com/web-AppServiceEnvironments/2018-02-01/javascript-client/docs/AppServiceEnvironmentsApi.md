# AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appServiceEnvironmentsChangeVnet**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsChangeVnet) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/changeVirtualNetwork | Move an App Service Environment to a different VNET.
[**appServiceEnvironmentsCreateOrUpdate**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Create or update an App Service Environment.
[**appServiceEnvironmentsCreateOrUpdateMultiRolePool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsCreateOrUpdateMultiRolePool) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Create or update a multi-role pool.
[**appServiceEnvironmentsCreateOrUpdateWorkerPool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsCreateOrUpdateWorkerPool) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Create or update a worker pool.
[**appServiceEnvironmentsDelete**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Delete an App Service Environment.
[**appServiceEnvironmentsGet**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Get the properties of an App Service Environment.
[**appServiceEnvironmentsGetDiagnosticsItem**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGetDiagnosticsItem) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics/{diagnosticsName} | Get a diagnostics item for an App Service Environment.
[**appServiceEnvironmentsGetInboundNetworkDependenciesEndpoints**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGetInboundNetworkDependenciesEndpoints) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/inboundNetworkDependenciesEndpoints | Get the network endpoints of all inbound dependencies of an App Service Environment.
[**appServiceEnvironmentsGetMultiRolePool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGetMultiRolePool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Get properties of a multi-role pool.
[**appServiceEnvironmentsGetOutboundNetworkDependenciesEndpoints**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGetOutboundNetworkDependenciesEndpoints) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/outboundNetworkDependenciesEndpoints | Get the network endpoints of all outbound dependencies of an App Service Environment.
[**appServiceEnvironmentsGetWorkerPool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsGetWorkerPool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Get properties of a worker pool.
[**appServiceEnvironmentsList**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/hostingEnvironments | Get all App Service Environments for a subscription.
[**appServiceEnvironmentsListAppServicePlans**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListAppServicePlans) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/serverfarms | Get all App Service plans in an App Service Environment.
[**appServiceEnvironmentsListByResourceGroup**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments | Get all App Service Environments in a resource group.
[**appServiceEnvironmentsListCapacities**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListCapacities) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/compute | Get the used, available, and total worker capacity an App Service Environment.
[**appServiceEnvironmentsListDiagnostics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListDiagnostics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/diagnostics | Get diagnostic information for an App Service Environment.
[**appServiceEnvironmentsListMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/metricdefinitions | Get global metric definitions of an App Service Environment.
[**appServiceEnvironmentsListMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/metrics | Get global metrics of an App Service Environment.
[**appServiceEnvironmentsListMultiRoleMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRoleMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metricdefinitions | Get metric definitions for a multi-role pool of an App Service Environment.
[**appServiceEnvironmentsListMultiRoleMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRoleMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/metrics | Get metrics for a multi-role pool of an App Service Environment.
[**appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metricdefinitions | Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.
[**appServiceEnvironmentsListMultiRolePoolInstanceMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRolePoolInstanceMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/instances/{instance}/metrics | Get metrics for a specific instance of a multi-role pool of an App Service Environment.
[**appServiceEnvironmentsListMultiRolePoolSkus**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRolePoolSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/skus | Get available SKUs for scaling a multi-role pool.
[**appServiceEnvironmentsListMultiRolePools**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRolePools) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools | Get all multi-role pools.
[**appServiceEnvironmentsListMultiRoleUsages**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListMultiRoleUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default/usages | Get usage metrics for a multi-role pool of an App Service Environment.
[**appServiceEnvironmentsListOperations**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListOperations) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/operations | List all currently running operations on the App Service Environment.
[**appServiceEnvironmentsListUsages**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/usages | Get global usage metrics of an App Service Environment.
[**appServiceEnvironmentsListVips**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListVips) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/capacities/virtualip | Get IP addresses assigned to an App Service Environment.
[**appServiceEnvironmentsListWebApps**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWebApps) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/sites | Get all apps in an App Service Environment.
[**appServiceEnvironmentsListWebWorkerMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWebWorkerMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/metricdefinitions | Get metric definitions for a worker pool of an App Service Environment.
[**appServiceEnvironmentsListWebWorkerMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWebWorkerMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/metrics | Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment).
[**appServiceEnvironmentsListWebWorkerUsages**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWebWorkerUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/usages | Get usage metrics for a worker pool of an App Service Environment.
[**appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/instances/{instance}/metricdefinitions | Get metric definitions for a specific instance of a worker pool of an App Service Environment.
[**appServiceEnvironmentsListWorkerPoolInstanceMetrics**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWorkerPoolInstanceMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/instances/{instance}/metrics | Get metrics for a specific instance of a worker pool of an App Service Environment.
[**appServiceEnvironmentsListWorkerPoolSkus**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWorkerPoolSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName}/skus | Get available SKUs for scaling a worker pool.
[**appServiceEnvironmentsListWorkerPools**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsListWorkerPools) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools | Get all worker pools of an App Service Environment.
[**appServiceEnvironmentsReboot**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsReboot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/reboot | Reboot all machines in an App Service Environment.
[**appServiceEnvironmentsResume**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/resume | Resume an App Service Environment.
[**appServiceEnvironmentsSuspend**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsSuspend) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/suspend | Suspend an App Service Environment.
[**appServiceEnvironmentsUpdate**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name} | Create or update an App Service Environment.
[**appServiceEnvironmentsUpdateMultiRolePool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsUpdateMultiRolePool) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/multiRolePools/default | Create or update a multi-role pool.
[**appServiceEnvironmentsUpdateWorkerPool**](AppServiceEnvironmentsApi.md#appServiceEnvironmentsUpdateWorkerPool) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/workerPools/{workerPoolName} | Create or update a worker pool.



## appServiceEnvironmentsChangeVnet

> AppServiceEnvironmentsChangeVnet200Response appServiceEnvironmentsChangeVnet(resourceGroupName, name, subscriptionId, apiVersion, vnetInfo)

Move an App Service Environment to a different VNET.

Move an App Service Environment to a different VNET.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let vnetInfo = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsChangeVnetRequest(); // AppServiceEnvironmentsChangeVnetRequest | Details for the new virtual network.
apiInstance.appServiceEnvironmentsChangeVnet(resourceGroupName, name, subscriptionId, apiVersion, vnetInfo, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **vnetInfo** | [**AppServiceEnvironmentsChangeVnetRequest**](AppServiceEnvironmentsChangeVnetRequest.md)| Details for the new virtual network. | 

### Return type

[**AppServiceEnvironmentsChangeVnet200Response**](AppServiceEnvironmentsChangeVnet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceEnvironmentsCreateOrUpdate

> AppServiceEnvironmentResource appServiceEnvironmentsCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope)

Create or update an App Service Environment.

Create or update an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let hostingEnvironmentEnvelope = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentResource(); // AppServiceEnvironmentResource | Configuration details of the App Service Environment.
apiInstance.appServiceEnvironmentsCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **hostingEnvironmentEnvelope** | [**AppServiceEnvironmentResource**](AppServiceEnvironmentResource.md)| Configuration details of the App Service Environment. | 

### Return type

[**AppServiceEnvironmentResource**](AppServiceEnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceEnvironmentsCreateOrUpdateMultiRolePool

> WorkerPoolResource appServiceEnvironmentsCreateOrUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope)

Create or update a multi-role pool.

Create or update a multi-role pool.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let multiRolePoolEnvelope = new AppServiceEnvironmentsApiClient.WorkerPoolResource(); // WorkerPoolResource | Properties of the multi-role pool.
apiInstance.appServiceEnvironmentsCreateOrUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **multiRolePoolEnvelope** | [**WorkerPoolResource**](WorkerPoolResource.md)| Properties of the multi-role pool. | 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceEnvironmentsCreateOrUpdateWorkerPool

> WorkerPoolResource appServiceEnvironmentsCreateOrUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope)

Create or update a worker pool.

Create or update a worker pool.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let workerPoolEnvelope = new AppServiceEnvironmentsApiClient.WorkerPoolResource(); // WorkerPoolResource | Properties of the worker pool.
apiInstance.appServiceEnvironmentsCreateOrUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of the worker pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **workerPoolEnvelope** | [**WorkerPoolResource**](WorkerPoolResource.md)| Properties of the worker pool. | 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceEnvironmentsDelete

> appServiceEnvironmentsDelete(resourceGroupName, name, subscriptionId, apiVersion, opts)

Delete an App Service Environment.

Delete an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'forceDelete': true // Boolean | Specify <code>true</code> to force the deletion even if the App Service Environment contains resources. The default is <code>false</code>.
};
apiInstance.appServiceEnvironmentsDelete(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **forceDelete** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to force the deletion even if the App Service Environment contains resources. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appServiceEnvironmentsGet

> AppServiceEnvironmentResource appServiceEnvironmentsGet(resourceGroupName, name, subscriptionId, apiVersion)

Get the properties of an App Service Environment.

Get the properties of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsGet(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentResource**](AppServiceEnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsGetDiagnosticsItem

> HostingEnvironmentDiagnostics appServiceEnvironmentsGetDiagnosticsItem(resourceGroupName, name, diagnosticsName, subscriptionId, apiVersion)

Get a diagnostics item for an App Service Environment.

Get a diagnostics item for an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let diagnosticsName = "diagnosticsName_example"; // String | Name of the diagnostics item.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsGetDiagnosticsItem(resourceGroupName, name, diagnosticsName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **diagnosticsName** | **String**| Name of the diagnostics item. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostingEnvironmentDiagnostics**](HostingEnvironmentDiagnostics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsGetInboundNetworkDependenciesEndpoints

> InboundEnvironmentEndpointCollection appServiceEnvironmentsGetInboundNetworkDependenciesEndpoints(resourceGroupName, name, subscriptionId, apiVersion)

Get the network endpoints of all inbound dependencies of an App Service Environment.

Get the network endpoints of all inbound dependencies of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsGetInboundNetworkDependenciesEndpoints(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**InboundEnvironmentEndpointCollection**](InboundEnvironmentEndpointCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsGetMultiRolePool

> WorkerPoolResource appServiceEnvironmentsGetMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion)

Get properties of a multi-role pool.

Get properties of a multi-role pool.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsGetMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsGetOutboundNetworkDependenciesEndpoints

> OutboundEnvironmentEndpointCollection appServiceEnvironmentsGetOutboundNetworkDependenciesEndpoints(resourceGroupName, name, subscriptionId, apiVersion)

Get the network endpoints of all outbound dependencies of an App Service Environment.

Get the network endpoints of all outbound dependencies of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsGetOutboundNetworkDependenciesEndpoints(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**OutboundEnvironmentEndpointCollection**](OutboundEnvironmentEndpointCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsGetWorkerPool

> WorkerPoolResource appServiceEnvironmentsGetWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get properties of a worker pool.

Get properties of a worker pool.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsGetWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of the worker pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsList

> AppServiceEnvironmentCollection appServiceEnvironmentsList(subscriptionId, apiVersion)

Get all App Service Environments for a subscription.

Get all App Service Environments for a subscription.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentCollection**](AppServiceEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListAppServicePlans

> AppServiceEnvironmentsListAppServicePlans200Response appServiceEnvironmentsListAppServicePlans(resourceGroupName, name, subscriptionId, apiVersion)

Get all App Service plans in an App Service Environment.

Get all App Service plans in an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListAppServicePlans(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentsListAppServicePlans200Response**](AppServiceEnvironmentsListAppServicePlans200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListByResourceGroup

> AppServiceEnvironmentCollection appServiceEnvironmentsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Get all App Service Environments in a resource group.

Get all App Service Environments in a resource group.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentCollection**](AppServiceEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListCapacities

> StampCapacityCollection appServiceEnvironmentsListCapacities(resourceGroupName, name, subscriptionId, apiVersion)

Get the used, available, and total worker capacity an App Service Environment.

Get the used, available, and total worker capacity an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListCapacities(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StampCapacityCollection**](StampCapacityCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListDiagnostics

> [HostingEnvironmentDiagnostics] appServiceEnvironmentsListDiagnostics(resourceGroupName, name, subscriptionId, apiVersion)

Get diagnostic information for an App Service Environment.

Get diagnostic information for an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListDiagnostics(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[HostingEnvironmentDiagnostics]**](HostingEnvironmentDiagnostics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMetricDefinitions

> MetricDefinition appServiceEnvironmentsListMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Get global metric definitions of an App Service Environment.

Get global metric definitions of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MetricDefinition**](MetricDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMetrics

> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get global metrics of an App Service Environment.

Get global metrics of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.appServiceEnvironmentsListMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMultiRoleMetricDefinitions

> AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response appServiceEnvironmentsListMultiRoleMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Get metric definitions for a multi-role pool of an App Service Environment.

Get metric definitions for a multi-role pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListMultiRoleMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMultiRoleMetrics

> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListMultiRoleMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get metrics for a multi-role pool of an App Service Environment.

Get metrics for a multi-role pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': "startTime_example", // String | Beginning time of the metrics query.
  'endTime': "endTime_example", // String | End time of the metrics query.
  'timeGrain': "timeGrain_example", // String | Time granularity of the metrics query.
  'details': true, // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.appServiceEnvironmentsListMultiRoleMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **String**| Beginning time of the metrics query. | [optional] 
 **endTime** | **String**| End time of the metrics query. | [optional] 
 **timeGrain** | **String**| Time granularity of the metrics query. | [optional] 
 **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions

> AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions(resourceGroupName, name, instance, subscriptionId, apiVersion)

Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.

Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let instance = "instance_example"; // String | Name of the instance in the multi-role pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions(resourceGroupName, name, instance, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **instance** | **String**| Name of the instance in the multi-role pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMultiRolePoolInstanceMetrics

> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListMultiRolePoolInstanceMetrics(resourceGroupName, name, instance, subscriptionId, apiVersion, opts)

Get metrics for a specific instance of a multi-role pool of an App Service Environment.

Get metrics for a specific instance of a multi-role pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let instance = "instance_example"; // String | Name of the instance in the multi-role pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
};
apiInstance.appServiceEnvironmentsListMultiRolePoolInstanceMetrics(resourceGroupName, name, instance, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **instance** | **String**| Name of the instance in the multi-role pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] 

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMultiRolePoolSkus

> SkuInfoCollection appServiceEnvironmentsListMultiRolePoolSkus(resourceGroupName, name, subscriptionId, apiVersion)

Get available SKUs for scaling a multi-role pool.

Get available SKUs for scaling a multi-role pool.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListMultiRolePoolSkus(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SkuInfoCollection**](SkuInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMultiRolePools

> WorkerPoolCollection appServiceEnvironmentsListMultiRolePools(resourceGroupName, name, subscriptionId, apiVersion)

Get all multi-role pools.

Get all multi-role pools.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListMultiRolePools(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WorkerPoolCollection**](WorkerPoolCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListMultiRoleUsages

> UsageCollection appServiceEnvironmentsListMultiRoleUsages(resourceGroupName, name, subscriptionId, apiVersion)

Get usage metrics for a multi-role pool of an App Service Environment.

Get usage metrics for a multi-role pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListMultiRoleUsages(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**UsageCollection**](UsageCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListOperations

> [AppServiceEnvironmentsListOperations200ResponseInner] appServiceEnvironmentsListOperations(resourceGroupName, name, subscriptionId, apiVersion)

List all currently running operations on the App Service Environment.

List all currently running operations on the App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListOperations(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[AppServiceEnvironmentsListOperations200ResponseInner]**](AppServiceEnvironmentsListOperations200ResponseInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListUsages

> AppServiceEnvironmentsListUsages200Response appServiceEnvironmentsListUsages(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get global usage metrics of an App Service Environment.

Get global usage metrics of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.appServiceEnvironmentsListUsages(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**AppServiceEnvironmentsListUsages200Response**](AppServiceEnvironmentsListUsages200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListVips

> AddressResponse appServiceEnvironmentsListVips(resourceGroupName, name, subscriptionId, apiVersion)

Get IP addresses assigned to an App Service Environment.

Get IP addresses assigned to an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListVips(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListWebApps

> AppServiceEnvironmentsChangeVnet200Response appServiceEnvironmentsListWebApps(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get all apps in an App Service Environment.

Get all apps in an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'propertiesToInclude': "propertiesToInclude_example" // String | Comma separated list of app properties to include.
};
apiInstance.appServiceEnvironmentsListWebApps(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **propertiesToInclude** | **String**| Comma separated list of app properties to include. | [optional] 

### Return type

[**AppServiceEnvironmentsChangeVnet200Response**](AppServiceEnvironmentsChangeVnet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListWebWorkerMetricDefinitions

> AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response appServiceEnvironmentsListWebWorkerMetricDefinitions(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get metric definitions for a worker pool of an App Service Environment.

Get metric definitions for a worker pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListWebWorkerMetricDefinitions(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of the worker pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListWebWorkerMetrics

> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListWebWorkerMetrics(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, opts)

Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment).

Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment).

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of worker pool
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.appServiceEnvironmentsListWebWorkerMetrics(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of worker pool | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListWebWorkerUsages

> UsageCollection appServiceEnvironmentsListWebWorkerUsages(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get usage metrics for a worker pool of an App Service Environment.

Get usage metrics for a worker pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListWebWorkerUsages(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of the worker pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**UsageCollection**](UsageCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions

> AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion)

Get metric definitions for a specific instance of a worker pool of an App Service Environment.

Get metric definitions for a specific instance of a worker pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
let instance = "instance_example"; // String | Name of the instance in the worker pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListWorkerPoolInstanceMetricDefinitions(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of the worker pool. | 
 **instance** | **String**| Name of the instance in the worker pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response**](AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListWorkerPoolInstanceMetrics

> AppServiceEnvironmentsListMetrics200Response appServiceEnvironmentsListWorkerPoolInstanceMetrics(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, opts)

Get metrics for a specific instance of a worker pool of an App Service Environment.

Get metrics for a specific instance of a worker pool of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
let instance = "instance_example"; // String | Name of the instance in the worker pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | Specify <code>true</code> to include instance details. The default is <code>false</code>.
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.appServiceEnvironmentsListWorkerPoolInstanceMetrics(resourceGroupName, name, workerPoolName, instance, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of the worker pool. | 
 **instance** | **String**| Name of the instance in the worker pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;. | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**AppServiceEnvironmentsListMetrics200Response**](AppServiceEnvironmentsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListWorkerPoolSkus

> SkuInfoCollection appServiceEnvironmentsListWorkerPoolSkus(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion)

Get available SKUs for scaling a worker pool.

Get available SKUs for scaling a worker pool.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListWorkerPoolSkus(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of the worker pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SkuInfoCollection**](SkuInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsListWorkerPools

> WorkerPoolCollection appServiceEnvironmentsListWorkerPools(resourceGroupName, name, subscriptionId, apiVersion)

Get all worker pools of an App Service Environment.

Get all worker pools of an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsListWorkerPools(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WorkerPoolCollection**](WorkerPoolCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsReboot

> appServiceEnvironmentsReboot(resourceGroupName, name, subscriptionId, apiVersion)

Reboot all machines in an App Service Environment.

Reboot all machines in an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsReboot(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appServiceEnvironmentsResume

> AppServiceEnvironmentsChangeVnet200Response appServiceEnvironmentsResume(resourceGroupName, name, subscriptionId, apiVersion)

Resume an App Service Environment.

Resume an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsResume(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentsChangeVnet200Response**](AppServiceEnvironmentsChangeVnet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsSuspend

> AppServiceEnvironmentsChangeVnet200Response appServiceEnvironmentsSuspend(resourceGroupName, name, subscriptionId, apiVersion)

Suspend an App Service Environment.

Suspend an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServiceEnvironmentsSuspend(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServiceEnvironmentsChangeVnet200Response**](AppServiceEnvironmentsChangeVnet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServiceEnvironmentsUpdate

> AppServiceEnvironmentResource appServiceEnvironmentsUpdate(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope)

Create or update an App Service Environment.

Create or update an App Service Environment.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let hostingEnvironmentEnvelope = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentPatchResource(); // AppServiceEnvironmentPatchResource | Configuration details of the App Service Environment.
apiInstance.appServiceEnvironmentsUpdate(resourceGroupName, name, subscriptionId, apiVersion, hostingEnvironmentEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **hostingEnvironmentEnvelope** | [**AppServiceEnvironmentPatchResource**](AppServiceEnvironmentPatchResource.md)| Configuration details of the App Service Environment. | 

### Return type

[**AppServiceEnvironmentResource**](AppServiceEnvironmentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceEnvironmentsUpdateMultiRolePool

> WorkerPoolResource appServiceEnvironmentsUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope)

Create or update a multi-role pool.

Create or update a multi-role pool.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let multiRolePoolEnvelope = new AppServiceEnvironmentsApiClient.WorkerPoolResource(); // WorkerPoolResource | Properties of the multi-role pool.
apiInstance.appServiceEnvironmentsUpdateMultiRolePool(resourceGroupName, name, subscriptionId, apiVersion, multiRolePoolEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **multiRolePoolEnvelope** | [**WorkerPoolResource**](WorkerPoolResource.md)| Properties of the multi-role pool. | 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServiceEnvironmentsUpdateWorkerPool

> WorkerPoolResource appServiceEnvironmentsUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope)

Create or update a worker pool.

Create or update a worker pool.

### Example

```javascript
import AppServiceEnvironmentsApiClient from 'app_service_environments_api_client';
let defaultClient = AppServiceEnvironmentsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServiceEnvironmentsApiClient.AppServiceEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service Environment.
let workerPoolName = "workerPoolName_example"; // String | Name of the worker pool.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let workerPoolEnvelope = new AppServiceEnvironmentsApiClient.WorkerPoolResource(); // WorkerPoolResource | Properties of the worker pool.
apiInstance.appServiceEnvironmentsUpdateWorkerPool(resourceGroupName, name, workerPoolName, subscriptionId, apiVersion, workerPoolEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the App Service Environment. | 
 **workerPoolName** | **String**| Name of the worker pool. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **workerPoolEnvelope** | [**WorkerPoolResource**](WorkerPoolResource.md)| Properties of the worker pool. | 

### Return type

[**WorkerPoolResource**](WorkerPoolResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

