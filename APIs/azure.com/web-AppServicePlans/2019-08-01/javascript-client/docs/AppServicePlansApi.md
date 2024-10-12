# AppServicePlansApiClient.AppServicePlansApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appServicePlansCreateOrUpdate**](AppServicePlansApi.md#appServicePlansCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Creates or updates an App Service Plan.
[**appServicePlansCreateOrUpdateVnetRoute**](AppServicePlansApi.md#appServicePlansCreateOrUpdateVnetRoute) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Create or update a Virtual Network route in an App Service plan.
[**appServicePlansDelete**](AppServicePlansApi.md#appServicePlansDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Delete an App Service plan.
[**appServicePlansDeleteHybridConnection**](AppServicePlansApi.md#appServicePlansDeleteHybridConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Delete a Hybrid Connection in use in an App Service plan.
[**appServicePlansDeleteVnetRoute**](AppServicePlansApi.md#appServicePlansDeleteVnetRoute) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Delete a Virtual Network route in an App Service plan.
[**appServicePlansGet**](AppServicePlansApi.md#appServicePlansGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Get an App Service plan.
[**appServicePlansGetHybridConnection**](AppServicePlansApi.md#appServicePlansGetHybridConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Retrieve a Hybrid Connection in use in an App Service plan.
[**appServicePlansGetHybridConnectionPlanLimit**](AppServicePlansApi.md#appServicePlansGetHybridConnectionPlanLimit) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionPlanLimits/limit | Get the maximum number of Hybrid Connections allowed in an App Service plan.
[**appServicePlansGetRouteForVnet**](AppServicePlansApi.md#appServicePlansGetRouteForVnet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Get a Virtual Network route in an App Service plan.
[**appServicePlansGetServerFarmSkus**](AppServicePlansApi.md#appServicePlansGetServerFarmSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/skus | Gets all selectable SKUs for a given App Service Plan
[**appServicePlansGetVnetFromServerFarm**](AppServicePlansApi.md#appServicePlansGetVnetFromServerFarm) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName} | Get a Virtual Network associated with an App Service plan.
[**appServicePlansGetVnetGateway**](AppServicePlansApi.md#appServicePlansGetVnetGateway) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Get a Virtual Network gateway.
[**appServicePlansList**](AppServicePlansApi.md#appServicePlansList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/serverfarms | Get all App Service plans for a subscription.
[**appServicePlansListByResourceGroup**](AppServicePlansApi.md#appServicePlansListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms | Get all App Service plans in a resource group.
[**appServicePlansListCapabilities**](AppServicePlansApi.md#appServicePlansListCapabilities) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/capabilities | List all capabilities of an App Service plan.
[**appServicePlansListHybridConnectionKeys**](AppServicePlansApi.md#appServicePlansListHybridConnectionKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName}/listKeys | Get the send key name and value of a Hybrid Connection.
[**appServicePlansListHybridConnections**](AppServicePlansApi.md#appServicePlansListHybridConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionRelays | Retrieve all Hybrid Connections in use in an App Service plan.
[**appServicePlansListRoutesForVnet**](AppServicePlansApi.md#appServicePlansListRoutesForVnet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes | Get all routes that are associated with a Virtual Network in an App Service plan.
[**appServicePlansListUsages**](AppServicePlansApi.md#appServicePlansListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/usages | Gets server farm usage information
[**appServicePlansListVnets**](AppServicePlansApi.md#appServicePlansListVnets) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections | Get all Virtual Networks associated with an App Service plan.
[**appServicePlansListWebApps**](AppServicePlansApi.md#appServicePlansListWebApps) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/sites | Get all apps associated with an App Service plan.
[**appServicePlansListWebAppsByHybridConnection**](AppServicePlansApi.md#appServicePlansListWebAppsByHybridConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName}/sites | Get all apps that use a Hybrid Connection in an App Service Plan.
[**appServicePlansRebootWorker**](AppServicePlansApi.md#appServicePlansRebootWorker) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/workers/{workerName}/reboot | Reboot a worker machine in an App Service plan.
[**appServicePlansRestartWebApps**](AppServicePlansApi.md#appServicePlansRestartWebApps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/restartSites | Restart all apps in an App Service plan.
[**appServicePlansUpdate**](AppServicePlansApi.md#appServicePlansUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name} | Creates or updates an App Service Plan.
[**appServicePlansUpdateVnetGateway**](AppServicePlansApi.md#appServicePlansUpdateVnetGateway) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Update a Virtual Network gateway.
[**appServicePlansUpdateVnetRoute**](AppServicePlansApi.md#appServicePlansUpdateVnetRoute) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/serverfarms/{name}/virtualNetworkConnections/{vnetName}/routes/{routeName} | Create or update a Virtual Network route in an App Service plan.



## appServicePlansCreateOrUpdate

> AppServicePlansGet200Response appServicePlansCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, appServicePlan)

Creates or updates an App Service Plan.

Description for Creates or updates an App Service Plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let appServicePlan = new AppServicePlansApiClient.AppServicePlansGet200Response(); // AppServicePlansGet200Response | Details of the App Service plan.
apiInstance.appServicePlansCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, appServicePlan, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **appServicePlan** | [**AppServicePlansGet200Response**](AppServicePlansGet200Response.md)| Details of the App Service plan. | 

### Return type

[**AppServicePlansGet200Response**](AppServicePlansGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServicePlansCreateOrUpdateVnetRoute

> AppServicePlansCreateOrUpdateVnetRouteRequest appServicePlansCreateOrUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route)

Create or update a Virtual Network route in an App Service plan.

Description for Create or update a Virtual Network route in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let routeName = "routeName_example"; // String | Name of the Virtual Network route.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let route = new AppServicePlansApiClient.AppServicePlansCreateOrUpdateVnetRouteRequest(); // AppServicePlansCreateOrUpdateVnetRouteRequest | Definition of the Virtual Network route.
apiInstance.appServicePlansCreateOrUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **routeName** | **String**| Name of the Virtual Network route. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **route** | [**AppServicePlansCreateOrUpdateVnetRouteRequest**](AppServicePlansCreateOrUpdateVnetRouteRequest.md)| Definition of the Virtual Network route. | 

### Return type

[**AppServicePlansCreateOrUpdateVnetRouteRequest**](AppServicePlansCreateOrUpdateVnetRouteRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServicePlansDelete

> appServicePlansDelete(resourceGroupName, name, subscriptionId, apiVersion)

Delete an App Service plan.

Description for Delete an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansDelete(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansDeleteHybridConnection

> appServicePlansDeleteHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Delete a Hybrid Connection in use in an App Service plan.

Description for Delete a Hybrid Connection in use in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let namespaceName = "namespaceName_example"; // String | Name of the Service Bus namespace.
let relayName = "relayName_example"; // String | Name of the Service Bus relay.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansDeleteHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **namespaceName** | **String**| Name of the Service Bus namespace. | 
 **relayName** | **String**| Name of the Service Bus relay. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansDeleteVnetRoute

> appServicePlansDeleteVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion)

Delete a Virtual Network route in an App Service plan.

Description for Delete a Virtual Network route in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let routeName = "routeName_example"; // String | Name of the Virtual Network route.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansDeleteVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **routeName** | **String**| Name of the Virtual Network route. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansGet

> AppServicePlansGet200Response appServicePlansGet(resourceGroupName, name, subscriptionId, apiVersion)

Get an App Service plan.

Description for Get an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansGet(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServicePlansGet200Response**](AppServicePlansGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansGetHybridConnection

> AppServicePlansGetHybridConnection200Response appServicePlansGetHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Retrieve a Hybrid Connection in use in an App Service plan.

Description for Retrieve a Hybrid Connection in use in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let namespaceName = "namespaceName_example"; // String | Name of the Service Bus namespace.
let relayName = "relayName_example"; // String | Name of the Service Bus relay.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansGetHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **namespaceName** | **String**| Name of the Service Bus namespace. | 
 **relayName** | **String**| Name of the Service Bus relay. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServicePlansGetHybridConnection200Response**](AppServicePlansGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansGetHybridConnectionPlanLimit

> HybridConnectionLimits appServicePlansGetHybridConnectionPlanLimit(resourceGroupName, name, subscriptionId, apiVersion)

Get the maximum number of Hybrid Connections allowed in an App Service plan.

Description for Get the maximum number of Hybrid Connections allowed in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansGetHybridConnectionPlanLimit(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HybridConnectionLimits**](HybridConnectionLimits.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansGetRouteForVnet

> [AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner] appServicePlansGetRouteForVnet(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion)

Get a Virtual Network route in an App Service plan.

Description for Get a Virtual Network route in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let routeName = "routeName_example"; // String | Name of the Virtual Network route.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansGetRouteForVnet(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **routeName** | **String**| Name of the Virtual Network route. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner]**](AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansGetServerFarmSkus

> Object appServicePlansGetServerFarmSkus(resourceGroupName, name, subscriptionId, apiVersion)

Gets all selectable SKUs for a given App Service Plan

Description for Gets all selectable SKUs for a given App Service Plan

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansGetServerFarmSkus(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansGetVnetFromServerFarm

> AppServicePlansGetVnetFromServerFarm200Response appServicePlansGetVnetFromServerFarm(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Get a Virtual Network associated with an App Service plan.

Description for Get a Virtual Network associated with an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansGetVnetFromServerFarm(resourceGroupName, name, vnetName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServicePlansGetVnetFromServerFarm200Response**](AppServicePlansGetVnetFromServerFarm200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansGetVnetGateway

> AppServicePlansGetVnetGateway200Response appServicePlansGetVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion)

Get a Virtual Network gateway.

Description for Get a Virtual Network gateway.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Only the 'primary' gateway is supported.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansGetVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **gatewayName** | **String**| Name of the gateway. Only the &#39;primary&#39; gateway is supported. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AppServicePlansGetVnetGateway200Response**](AppServicePlansGetVnetGateway200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansList

> AppServicePlansList200Response appServicePlansList(subscriptionId, apiVersion, opts)

Get all App Service plans for a subscription.

Description for Get all App Service plans for a subscription.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'detailed': true // Boolean | Specify <code>true</code> to return all App Service plan properties. The default is <code>false</code>, which returns a subset of the properties.  Retrieval of all properties may increase the API latency.
};
apiInstance.appServicePlansList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **detailed** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to return all App Service plan properties. The default is &lt;code&gt;false&lt;/code&gt;, which returns a subset of the properties.  Retrieval of all properties may increase the API latency. | [optional] 

### Return type

[**AppServicePlansList200Response**](AppServicePlansList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListByResourceGroup

> AppServicePlansList200Response appServicePlansListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)

Get all App Service plans in a resource group.

Description for Get all App Service plans in a resource group.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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

[**AppServicePlansList200Response**](AppServicePlansList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListCapabilities

> [AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner] appServicePlansListCapabilities(resourceGroupName, name, subscriptionId, apiVersion)

List all capabilities of an App Service plan.

Description for List all capabilities of an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansListCapabilities(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner]**](AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListHybridConnectionKeys

> HybridConnectionKey appServicePlansListHybridConnectionKeys(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Get the send key name and value of a Hybrid Connection.

Description for Get the send key name and value of a Hybrid Connection.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let namespaceName = "namespaceName_example"; // String | The name of the Service Bus namespace.
let relayName = "relayName_example"; // String | The name of the Service Bus relay.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansListHybridConnectionKeys(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **namespaceName** | **String**| The name of the Service Bus namespace. | 
 **relayName** | **String**| The name of the Service Bus relay. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HybridConnectionKey**](HybridConnectionKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListHybridConnections

> HybridConnectionCollection appServicePlansListHybridConnections(resourceGroupName, name, subscriptionId, apiVersion)

Retrieve all Hybrid Connections in use in an App Service plan.

Description for Retrieve all Hybrid Connections in use in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansListHybridConnections(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HybridConnectionCollection**](HybridConnectionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListRoutesForVnet

> [AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner] appServicePlansListRoutesForVnet(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Get all routes that are associated with a Virtual Network in an App Service plan.

Description for Get all routes that are associated with a Virtual Network in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansListRoutesForVnet(resourceGroupName, name, vnetName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner]**](AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListUsages

> AppServicePlansListUsages200Response appServicePlansListUsages(resourceGroupName, name, subscriptionId, apiVersion, opts)

Gets server farm usage information

Description for Gets server farm usage information

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of App Service Plan
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2').
};
apiInstance.appServicePlansListUsages(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| Name of App Service Plan | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;). | [optional] 

### Return type

[**AppServicePlansListUsages200Response**](AppServicePlansListUsages200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListVnets

> [AppServicePlansListVnets200ResponseInner] appServicePlansListVnets(resourceGroupName, name, subscriptionId, apiVersion)

Get all Virtual Networks associated with an App Service plan.

Description for Get all Virtual Networks associated with an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansListVnets(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[AppServicePlansListVnets200ResponseInner]**](AppServicePlansListVnets200ResponseInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListWebApps

> AppServicePlansListWebApps200Response appServicePlansListWebApps(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get all apps associated with an App Service plan.

Description for Get all apps associated with an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'skipToken': "skipToken_example", // String | Skip to a web app in the list of webapps associated with app service plan. If specified, the resulting list will contain web apps starting from (including) the skipToken. Otherwise, the resulting list contains web apps from the start of the list
  'filter': "filter_example", // String | Supported filter: $filter=state eq running. Returns only web apps that are currently running
  'top': "top_example" // String | List page size. If specified, results are paged.
};
apiInstance.appServicePlansListWebApps(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **skipToken** | **String**| Skip to a web app in the list of webapps associated with app service plan. If specified, the resulting list will contain web apps starting from (including) the skipToken. Otherwise, the resulting list contains web apps from the start of the list | [optional] 
 **filter** | **String**| Supported filter: $filter&#x3D;state eq running. Returns only web apps that are currently running | [optional] 
 **top** | **String**| List page size. If specified, results are paged. | [optional] 

### Return type

[**AppServicePlansListWebApps200Response**](AppServicePlansListWebApps200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansListWebAppsByHybridConnection

> ResourceCollection appServicePlansListWebAppsByHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Get all apps that use a Hybrid Connection in an App Service Plan.

Description for Get all apps that use a Hybrid Connection in an App Service Plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let namespaceName = "namespaceName_example"; // String | Name of the Hybrid Connection namespace.
let relayName = "relayName_example"; // String | Name of the Hybrid Connection relay.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansListWebAppsByHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **namespaceName** | **String**| Name of the Hybrid Connection namespace. | 
 **relayName** | **String**| Name of the Hybrid Connection relay. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ResourceCollection**](ResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansRebootWorker

> appServicePlansRebootWorker(resourceGroupName, name, workerName, subscriptionId, apiVersion)

Reboot a worker machine in an App Service plan.

Description for Reboot a worker machine in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let workerName = "workerName_example"; // String | Name of worker machine, which typically starts with RD.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.appServicePlansRebootWorker(resourceGroupName, name, workerName, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **workerName** | **String**| Name of worker machine, which typically starts with RD. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansRestartWebApps

> appServicePlansRestartWebApps(resourceGroupName, name, subscriptionId, apiVersion, opts)

Restart all apps in an App Service plan.

Description for Restart all apps in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'softRestart': true // Boolean | Specify <code>true</code> to perform a soft restart, applies the configuration settings and restarts the apps if necessary. The default is <code>false</code>, which always restarts and reprovisions the apps
};
apiInstance.appServicePlansRestartWebApps(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **softRestart** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to perform a soft restart, applies the configuration settings and restarts the apps if necessary. The default is &lt;code&gt;false&lt;/code&gt;, which always restarts and reprovisions the apps | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appServicePlansUpdate

> AppServicePlansGet200Response appServicePlansUpdate(resourceGroupName, name, subscriptionId, apiVersion, appServicePlan)

Creates or updates an App Service Plan.

Description for Creates or updates an App Service Plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let appServicePlan = new AppServicePlansApiClient.AppServicePlanPatchResource(); // AppServicePlanPatchResource | Details of the App Service plan.
apiInstance.appServicePlansUpdate(resourceGroupName, name, subscriptionId, apiVersion, appServicePlan, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **appServicePlan** | [**AppServicePlanPatchResource**](AppServicePlanPatchResource.md)| Details of the App Service plan. | 

### Return type

[**AppServicePlansGet200Response**](AppServicePlansGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServicePlansUpdateVnetGateway

> AppServicePlansGetVnetGateway200Response appServicePlansUpdateVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Update a Virtual Network gateway.

Description for Update a Virtual Network gateway.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Only the 'primary' gateway is supported.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new AppServicePlansApiClient.AppServicePlansGetVnetGateway200Response(); // AppServicePlansGetVnetGateway200Response | Definition of the gateway.
apiInstance.appServicePlansUpdateVnetGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **gatewayName** | **String**| Name of the gateway. Only the &#39;primary&#39; gateway is supported. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**AppServicePlansGetVnetGateway200Response**](AppServicePlansGetVnetGateway200Response.md)| Definition of the gateway. | 

### Return type

[**AppServicePlansGetVnetGateway200Response**](AppServicePlansGetVnetGateway200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appServicePlansUpdateVnetRoute

> AppServicePlansCreateOrUpdateVnetRouteRequest appServicePlansUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route)

Create or update a Virtual Network route in an App Service plan.

Description for Create or update a Virtual Network route in an App Service plan.

### Example

```javascript
import AppServicePlansApiClient from 'app_service_plans_api_client';
let defaultClient = AppServicePlansApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppServicePlansApiClient.AppServicePlansApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the App Service plan.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let routeName = "routeName_example"; // String | Name of the Virtual Network route.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let route = new AppServicePlansApiClient.AppServicePlansCreateOrUpdateVnetRouteRequest(); // AppServicePlansCreateOrUpdateVnetRouteRequest | Definition of the Virtual Network route.
apiInstance.appServicePlansUpdateVnetRoute(resourceGroupName, name, vnetName, routeName, subscriptionId, apiVersion, route, (error, data, response) => {
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
 **name** | **String**| Name of the App Service plan. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **routeName** | **String**| Name of the Virtual Network route. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **route** | [**AppServicePlansCreateOrUpdateVnetRouteRequest**](AppServicePlansCreateOrUpdateVnetRouteRequest.md)| Definition of the Virtual Network route. | 

### Return type

[**AppServicePlansCreateOrUpdateVnetRouteRequest**](AppServicePlansCreateOrUpdateVnetRouteRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

