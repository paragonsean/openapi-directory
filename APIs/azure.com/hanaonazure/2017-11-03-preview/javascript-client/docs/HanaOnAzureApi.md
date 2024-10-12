# HanaManagementClient.HanaOnAzureApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hanaInstancesCreate**](HanaOnAzureApi.md#hanaInstancesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName} | Creates a SAP HANA instance.
[**hanaInstancesDelete**](HanaOnAzureApi.md#hanaInstancesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName} | Deletes a SAP HANA instance.
[**hanaInstancesGet**](HanaOnAzureApi.md#hanaInstancesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName} | Gets properties of a SAP HANA instance.
[**hanaInstancesList**](HanaOnAzureApi.md#hanaInstancesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HanaOnAzure/hanaInstances | Gets a list of SAP HANA instances in the specified subscription.
[**hanaInstancesListByResourceGroup**](HanaOnAzureApi.md#hanaInstancesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances | Gets a list of SAP HANA instances in the specified subscription and the resource group.
[**hanaInstancesRestart**](HanaOnAzureApi.md#hanaInstancesRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName}/restart | 
[**hanaInstancesShutdown**](HanaOnAzureApi.md#hanaInstancesShutdown) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName}/shutdown | 
[**hanaInstancesStart**](HanaOnAzureApi.md#hanaInstancesStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName}/start | 
[**hanaInstancesUpdate**](HanaOnAzureApi.md#hanaInstancesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/hanaInstances/{hanaInstanceName} | Patches the Tags field of a SAP HANA instance.
[**operationsList**](HanaOnAzureApi.md#operationsList) | **GET** /providers/Microsoft.HanaOnAzure/operations | 
[**sapMonitorsCreate**](HanaOnAzureApi.md#sapMonitorsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName} | Creates a SAP monitor.
[**sapMonitorsDelete**](HanaOnAzureApi.md#sapMonitorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName} | Deletes a SAP monitor.
[**sapMonitorsGet**](HanaOnAzureApi.md#sapMonitorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName} | Gets properties of a SAP monitor.
[**sapMonitorsList**](HanaOnAzureApi.md#sapMonitorsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HanaOnAzure/sapMonitors | Gets a list of SAP monitors in the specified subscription.
[**sapMonitorsUpdate**](HanaOnAzureApi.md#sapMonitorsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HanaOnAzure/sapMonitors/{sapMonitorName} | Patches the Tags field of a SAP monitor.



## hanaInstancesCreate

> HanaInstance hanaInstancesCreate(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, hanaInstanceParameter)

Creates a SAP HANA instance.

Creates a SAP HANA instance for the specified subscription, resource group, and instance name.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
let hanaInstanceParameter = new HanaManagementClient.HanaInstance(); // HanaInstance | Request body representing a HanaInstance
apiInstance.hanaInstancesCreate(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, hanaInstanceParameter, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | 
 **hanaInstanceParameter** | [**HanaInstance**](HanaInstance.md)| Request body representing a HanaInstance | 

### Return type

[**HanaInstance**](HanaInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## hanaInstancesDelete

> hanaInstancesDelete(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)

Deletes a SAP HANA instance.

Deletes a SAP HANA instance with the specified subscription, resource group, and instance name.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
apiInstance.hanaInstancesDelete(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hanaInstancesGet

> HanaInstance hanaInstancesGet(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)

Gets properties of a SAP HANA instance.

Gets properties of a SAP HANA instance for the specified subscription, resource group, and instance name.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
apiInstance.hanaInstancesGet(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | 

### Return type

[**HanaInstance**](HanaInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hanaInstancesList

> HanaInstancesListResult hanaInstancesList(apiVersion, subscriptionId)

Gets a list of SAP HANA instances in the specified subscription.

Gets a list of SAP HANA instances in the specified subscription. The operations returns various properties of each SAP HANA on Azure instance.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.hanaInstancesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**HanaInstancesListResult**](HanaInstancesListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hanaInstancesListByResourceGroup

> HanaInstancesListResult hanaInstancesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Gets a list of SAP HANA instances in the specified subscription and the resource group.

Gets a list of SAP HANA instances in the specified subscription and the resource group. The operations returns various properties of each SAP HANA on Azure instance.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
apiInstance.hanaInstancesListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 

### Return type

[**HanaInstancesListResult**](HanaInstancesListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hanaInstancesRestart

> hanaInstancesRestart(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)



The operation to restart a SAP HANA instance.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
apiInstance.hanaInstancesRestart(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hanaInstancesShutdown

> hanaInstancesShutdown(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)



The operation to shutdown a SAP HANA instance.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
apiInstance.hanaInstancesShutdown(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hanaInstancesStart

> hanaInstancesStart(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName)



The operation to start a SAP HANA instance.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
apiInstance.hanaInstancesStart(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hanaInstancesUpdate

> HanaInstance hanaInstancesUpdate(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, tagsParameter)

Patches the Tags field of a SAP HANA instance.

Patches the Tags field of a SAP HANA instance for the specified subscription, resource group, and instance name.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let hanaInstanceName = "hanaInstanceName_example"; // String | Name of the SAP HANA on Azure instance.
let tagsParameter = new HanaManagementClient.Tags(); // Tags | Request body that only contains the new Tags field
apiInstance.hanaInstancesUpdate(apiVersion, subscriptionId, resourceGroupName, hanaInstanceName, tagsParameter, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **hanaInstanceName** | **String**| Name of the SAP HANA on Azure instance. | 
 **tagsParameter** | [**Tags**](Tags.md)| Request body that only contains the new Tags field | 

### Return type

[**HanaInstance**](HanaInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## operationsList

> OperationList operationsList(apiVersion)



Gets a list of SAP HANA management operations.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 

### Return type

[**OperationList**](OperationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sapMonitorsCreate

> SapMonitor sapMonitorsCreate(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, sapMonitorParameter)

Creates a SAP monitor.

Creates a SAP monitor for the specified subscription, resource group, and resource name.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let sapMonitorName = "sapMonitorName_example"; // String | Name of the SAP monitor resource.
let sapMonitorParameter = new HanaManagementClient.SapMonitor(); // SapMonitor | Request body representing a SAP Monitor
apiInstance.sapMonitorsCreate(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, sapMonitorParameter, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **sapMonitorName** | **String**| Name of the SAP monitor resource. | 
 **sapMonitorParameter** | [**SapMonitor**](SapMonitor.md)| Request body representing a SAP Monitor | 

### Return type

[**SapMonitor**](SapMonitor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sapMonitorsDelete

> sapMonitorsDelete(apiVersion, subscriptionId, resourceGroupName, sapMonitorName)

Deletes a SAP monitor.

Deletes a SAP monitor with the specified subscription, resource group, and monitor name.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let sapMonitorName = "sapMonitorName_example"; // String | Name of the SAP monitor resource.
apiInstance.sapMonitorsDelete(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **sapMonitorName** | **String**| Name of the SAP monitor resource. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sapMonitorsGet

> SapMonitor sapMonitorsGet(apiVersion, subscriptionId, resourceGroupName, sapMonitorName)

Gets properties of a SAP monitor.

Gets properties of a SAP monitor for the specified subscription, resource group, and resource name.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let sapMonitorName = "sapMonitorName_example"; // String | Name of the SAP monitor resource.
apiInstance.sapMonitorsGet(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **sapMonitorName** | **String**| Name of the SAP monitor resource. | 

### Return type

[**SapMonitor**](SapMonitor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sapMonitorsList

> SapMonitorListResult sapMonitorsList(apiVersion, subscriptionId)

Gets a list of SAP monitors in the specified subscription.

Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.sapMonitorsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SapMonitorListResult**](SapMonitorListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sapMonitorsUpdate

> SapMonitor sapMonitorsUpdate(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, tagsParameter)

Patches the Tags field of a SAP monitor.

Patches the Tags field of a SAP monitor for the specified subscription, resource group, and monitor name.

### Example

```javascript
import HanaManagementClient from 'hana_management_client';

let apiInstance = new HanaManagementClient.HanaOnAzureApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let sapMonitorName = "sapMonitorName_example"; // String | Name of the SAP monitor resource.
let tagsParameter = new HanaManagementClient.Tags(); // Tags | Request body that only contains the new Tags field
apiInstance.sapMonitorsUpdate(apiVersion, subscriptionId, resourceGroupName, sapMonitorName, tagsParameter, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **sapMonitorName** | **String**| Name of the SAP monitor resource. | 
 **tagsParameter** | [**Tags**](Tags.md)| Request body that only contains the new Tags field | 

### Return type

[**SapMonitor**](SapMonitor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

