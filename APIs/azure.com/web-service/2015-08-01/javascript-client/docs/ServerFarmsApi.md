# WebSiteManagementClient.ServerFarmsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serverFarmsCreateOrUpdateServerFarm**](ServerFarmsApi.md#serverFarmsCreateOrUpdateServerFarm) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Creates or updates an App Service Plan
[**serverFarmsCreateOrUpdateVnetRoute**](ServerFarmsApi.md#serverFarmsCreateOrUpdateVnetRoute) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Creates a new route or updates an existing route for a vnet in an app service plan.
[**serverFarmsDeleteServerFarm**](ServerFarmsApi.md#serverFarmsDeleteServerFarm) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Deletes a App Service Plan
[**serverFarmsDeleteVnetRoute**](ServerFarmsApi.md#serverFarmsDeleteVnetRoute) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Deletes an existing route for a vnet in an app service plan.
[**serverFarmsGetRouteForVnet**](ServerFarmsApi.md#serverFarmsGetRouteForVnet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Gets a specific route associated with a vnet, in an app service plan
[**serverFarmsGetRoutesForVnet**](ServerFarmsApi.md#serverFarmsGetRoutesForVnet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes | Gets a list of all routes associated with a vnet, in an app service plan
[**serverFarmsGetServerFarm**](ServerFarmsApi.md#serverFarmsGetServerFarm) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Gets specified App Service Plan in a resource group
[**serverFarmsGetServerFarmMetricDefintions**](ServerFarmsApi.md#serverFarmsGetServerFarmMetricDefintions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/metricdefinitions | List of metrics that can be queried for an App Service Plan
[**serverFarmsGetServerFarmMetrics**](ServerFarmsApi.md#serverFarmsGetServerFarmMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/metrics | Queries for App Service Plan metrics
[**serverFarmsGetServerFarmOperation**](ServerFarmsApi.md#serverFarmsGetServerFarmOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/operationresults/{operationId} | Gets a server farm operation
[**serverFarmsGetServerFarmSites**](ServerFarmsApi.md#serverFarmsGetServerFarmSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/sites | Gets list of Apps associated with an App Service Plan
[**serverFarmsGetServerFarmVnetGateway**](ServerFarmsApi.md#serverFarmsGetServerFarmVnetGateway) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Gets the vnet gateway.
[**serverFarmsGetServerFarms**](ServerFarmsApi.md#serverFarmsGetServerFarms) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms | Gets collection of App Service Plans in a resource group for a given subscription.
[**serverFarmsGetVnetFromServerFarm**](ServerFarmsApi.md#serverFarmsGetVnetFromServerFarm) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName} | Gets a vnet associated with an App Service Plan
[**serverFarmsGetVnetsForServerFarm**](ServerFarmsApi.md#serverFarmsGetVnetsForServerFarm) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections | Gets list of VNets associated with App Service Plan
[**serverFarmsRebootWorkerForServerFarm**](ServerFarmsApi.md#serverFarmsRebootWorkerForServerFarm) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/workers/{workerName}/reboot | Submit a reboot request for a worker machine in the specified server farm
[**serverFarmsRestartSitesForServerFarm**](ServerFarmsApi.md#serverFarmsRestartSitesForServerFarm) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/restartSites | Restarts web apps in a specified App Service Plan
[**serverFarmsUpdateServerFarmVnetGateway**](ServerFarmsApi.md#serverFarmsUpdateServerFarmVnetGateway) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Updates the vnet gateway
[**serverFarmsUpdateVnetRoute**](ServerFarmsApi.md#serverFarmsUpdateVnetRoute) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Creates a new route or updates an existing route for a vnet in an app service plan.



## serverFarmsCreateOrUpdateServerFarm

> ServerFarmWithRichSku serverFarmsCreateOrUpdateServerFarm(resourceGroupName, name, subscriptionId, apiVersion, serverFarmEnvelope, opts)

Creates or updates an App Service Plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let serverFarmEnvelope = new WebSiteManagementClient.ServerFarmWithRichSku(); // ServerFarmWithRichSku | Details of App Service Plan
let opts = {
  'allowPendingState': true // Boolean | OBSOLETE: If true, allow pending state for App Service Plan
};
apiInstance.serverFarmsCreateOrUpdateServerFarm(resourceGroupName, name, subscriptionId, apiVersion, serverFarmEnvelope, opts, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **serverFarmEnvelope** | [**ServerFarmWithRichSku**](ServerFarmWithRichSku.md)| Details of App Service Plan | 
 **allowPendingState** | **Boolean**| OBSOLETE: If true, allow pending state for App Service Plan | [optional] 

### Return type

[**ServerFarmWithRichSku**](ServerFarmWithRichSku.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsCreateOrUpdateVnetRoute

> VnetRoute serverFarmsCreateOrUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route)

Creates a new route or updates an existing route for a vnet in an app service plan.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let vnetName = "vnetName_example"; // String | Name of virtual network
let routeName = "routeName_example"; // String | Name of the virtual network route
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let route = new WebSiteManagementClient.VnetRoute(); // VnetRoute | The route object
apiInstance.serverFarmsCreateOrUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **vnetName** | **String**| Name of virtual network | 
 **routeName** | **String**| Name of the virtual network route | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **route** | [**VnetRoute**](VnetRoute.md)| The route object | 

### Return type

[**VnetRoute**](VnetRoute.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsDeleteServerFarm

> Object serverFarmsDeleteServerFarm(resourceGroupName, name, subscriptionId, apiVersion)

Deletes a App Service Plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsDeleteServerFarm(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsDeleteVnetRoute

> Object serverFarmsDeleteVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion)

Deletes an existing route for a vnet in an app service plan.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let vnetName = "vnetName_example"; // String | Name of virtual network
let routeName = "routeName_example"; // String | Name of the virtual network route
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsDeleteVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **vnetName** | **String**| Name of virtual network | 
 **routeName** | **String**| Name of the virtual network route | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsGetRouteForVnet

> [VnetRoute] serverFarmsGetRouteForVnet(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion)

Gets a specific route associated with a vnet, in an app service plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let vnetName = "vnetName_example"; // String | Name of virtual network
let routeName = "routeName_example"; // String | Name of the virtual network route
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetRouteForVnet(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **vnetName** | **String**| Name of virtual network | 
 **routeName** | **String**| Name of the virtual network route | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[VnetRoute]**](VnetRoute.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsGetRoutesForVnet

> [VnetRoute] serverFarmsGetRoutesForVnet(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Gets a list of all routes associated with a vnet, in an app service plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let vnetName = "vnetName_example"; // String | Name of virtual network
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetRoutesForVnet(resourceGroupName, name, vnetName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **vnetName** | **String**| Name of virtual network | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[VnetRoute]**](VnetRoute.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsGetServerFarm

> ServerFarmWithRichSku serverFarmsGetServerFarm(resourceGroupName, name, subscriptionId, apiVersion)

Gets specified App Service Plan in a resource group

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetServerFarm(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ServerFarmWithRichSku**](ServerFarmWithRichSku.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsGetServerFarmMetricDefintions

> MetricDefinitionCollection serverFarmsGetServerFarmMetricDefintions(resourceGroupName, name, subscriptionId, apiVersion)

List of metrics that can be queried for an App Service Plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetServerFarmMetricDefintions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## serverFarmsGetServerFarmMetrics

> ResourceMetricCollection serverFarmsGetServerFarmMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts)

Queries for App Service Plan metrics

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | If true, metrics are broken down per App Service Plan instance
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.serverFarmsGetServerFarmMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| If true, metrics are broken down per App Service Plan instance | [optional] 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**ResourceMetricCollection**](ResourceMetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## serverFarmsGetServerFarmOperation

> ServerFarmWithRichSku serverFarmsGetServerFarmOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Gets a server farm operation

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of server farm
let operationId = "operationId_example"; // String | Id of Server farm operation\"&gt;
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetServerFarmOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of server farm | 
 **operationId** | **String**| Id of Server farm operation\&quot;&amp;gt; | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ServerFarmWithRichSku**](ServerFarmWithRichSku.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsGetServerFarmSites

> SiteCollection serverFarmsGetServerFarmSites(resourceGroupName, name, subscriptionId, apiVersion, opts)

Gets list of Apps associated with an App Service Plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'skipToken': "skipToken_example", // String | Skip to of web apps in a list. If specified, the resulting list will contain web apps starting from (including) the skipToken. Else, the resulting list contains web apps from the start of the list
  'filter': "filter_example", // String | Supported filter: $filter=state eq running. Returns only web apps that are currently running
  'top': "top_example" // String | List page size. If specified, results are paged.
};
apiInstance.serverFarmsGetServerFarmSites(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **skipToken** | **String**| Skip to of web apps in a list. If specified, the resulting list will contain web apps starting from (including) the skipToken. Else, the resulting list contains web apps from the start of the list | [optional] 
 **filter** | **String**| Supported filter: $filter&#x3D;state eq running. Returns only web apps that are currently running | [optional] 
 **top** | **String**| List page size. If specified, results are paged. | [optional] 

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## serverFarmsGetServerFarmVnetGateway

> VnetGateway serverFarmsGetServerFarmVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion)

Gets the vnet gateway.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of the App Service Plan
let vnetName = "vnetName_example"; // String | Name of the virtual network
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Only the 'primary' gateway is supported.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetServerFarmVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service Plan | 
 **vnetName** | **String**| Name of the virtual network | 
 **gatewayName** | **String**| Name of the gateway. Only the &#39;primary&#39; gateway is supported. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsGetServerFarms

> ServerFarmCollection serverFarmsGetServerFarms(resourceGroupName, subscriptionId, apiVersion)

Gets collection of App Service Plans in a resource group for a given subscription.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetServerFarms(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## serverFarmsGetVnetFromServerFarm

> VnetInfo serverFarmsGetVnetFromServerFarm(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Gets a vnet associated with an App Service Plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let vnetName = "vnetName_example"; // String | Name of virtual network
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetVnetFromServerFarm(resourceGroupName, name, vnetName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **vnetName** | **String**| Name of virtual network | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**VnetInfo**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsGetVnetsForServerFarm

> [VnetInfo] serverFarmsGetVnetsForServerFarm(resourceGroupName, name, subscriptionId, apiVersion)

Gets list of VNets associated with App Service Plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsGetVnetsForServerFarm(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[VnetInfo]**](VnetInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsRebootWorkerForServerFarm

> Object serverFarmsRebootWorkerForServerFarm(resourceGroupName, name, workerName, subscriptionId, apiVersion)

Submit a reboot request for a worker machine in the specified server farm

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of server farm
let workerName = "workerName_example"; // String | Name of worker machine, typically starts with RD
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.serverFarmsRebootWorkerForServerFarm(resourceGroupName, name, workerName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of server farm | 
 **workerName** | **String**| Name of worker machine, typically starts with RD | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsRestartSitesForServerFarm

> Object serverFarmsRestartSitesForServerFarm(resourceGroupName, name, subscriptionId, apiVersion, opts)

Restarts web apps in a specified App Service Plan

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'softRestart': true // Boolean | Soft restart applies the configuration settings and restarts the apps if necessary. Hard restart always restarts and reprovisions the apps
};
apiInstance.serverFarmsRestartSitesForServerFarm(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **softRestart** | **Boolean**| Soft restart applies the configuration settings and restarts the apps if necessary. Hard restart always restarts and reprovisions the apps | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsUpdateServerFarmVnetGateway

> VnetGateway serverFarmsUpdateServerFarmVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Updates the vnet gateway

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let name = "name_example"; // String | The name of the App Service Plan
let vnetName = "vnetName_example"; // String | The name of the virtual network
let gatewayName = "gatewayName_example"; // String | The name of the gateway. Only 'primary' is supported.
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebSiteManagementClient.VnetGateway(); // VnetGateway | The gateway entity.
apiInstance.serverFarmsUpdateServerFarmVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group | 
 **name** | **String**| The name of the App Service Plan | 
 **vnetName** | **String**| The name of the virtual network | 
 **gatewayName** | **String**| The name of the gateway. Only &#39;primary&#39; is supported. | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**VnetGateway**](VnetGateway.md)| The gateway entity. | 

### Return type

[**VnetGateway**](VnetGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## serverFarmsUpdateVnetRoute

> VnetRoute serverFarmsUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route)

Creates a new route or updates an existing route for a vnet in an app service plan.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ServerFarmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of App Service Plan
let vnetName = "vnetName_example"; // String | Name of virtual network
let routeName = "routeName_example"; // String | Name of the virtual network route
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let route = new WebSiteManagementClient.VnetRoute(); // VnetRoute | The route object
apiInstance.serverFarmsUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **vnetName** | **String**| Name of virtual network | 
 **routeName** | **String**| Name of the virtual network route | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **route** | [**VnetRoute**](VnetRoute.md)| The route object | 

### Return type

[**VnetRoute**](VnetRoute.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

