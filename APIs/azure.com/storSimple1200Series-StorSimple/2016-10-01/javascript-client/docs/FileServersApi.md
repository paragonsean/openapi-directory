# StorSimpleManagementClient.FileServersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileServersBackupNow**](FileServersApi.md#fileServersBackupNow) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName}/backup | 
[**fileServersCreateOrUpdate**](FileServersApi.md#fileServersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName} | 
[**fileServersDelete**](FileServersApi.md#fileServersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName} | 
[**fileServersGet**](FileServersApi.md#fileServersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName} | 
[**fileServersListByDevice**](FileServersApi.md#fileServersListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers | 
[**fileServersListByManager**](FileServersApi.md#fileServersListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/fileservers | 
[**fileServersListMetricDefinition**](FileServersApi.md#fileServersListMetricDefinition) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName}/metricsDefinitions | 
[**fileServersListMetrics**](FileServersApi.md#fileServersListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/fileservers/{fileServerName}/metrics | 



## fileServersBackupNow

> fileServersBackupNow(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Backup the file server now.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.FileServersApi();
let deviceName = "deviceName_example"; // String | The device name.
let fileServerName = "fileServerName_example"; // String | The file server name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.fileServersBackupNow(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **fileServerName** | **String**| The file server name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileServersCreateOrUpdate

> FileServer fileServersCreateOrUpdate(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, fileServer)



Creates or updates the file server.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.FileServersApi();
let deviceName = "deviceName_example"; // String | The device name.
let fileServerName = "fileServerName_example"; // String | The file server name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let fileServer = new StorSimpleManagementClient.FileServer(); // FileServer | The file server.
apiInstance.fileServersCreateOrUpdate(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, fileServer, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **fileServerName** | **String**| The file server name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **fileServer** | [**FileServer**](FileServer.md)| The file server. | 

### Return type

[**FileServer**](FileServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fileServersDelete

> fileServersDelete(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the file server.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.FileServersApi();
let deviceName = "deviceName_example"; // String | The device name.
let fileServerName = "fileServerName_example"; // String | The file server name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.fileServersDelete(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **fileServerName** | **String**| The file server name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileServersGet

> FileServer fileServersGet(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified file server name.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.FileServersApi();
let deviceName = "deviceName_example"; // String | The device name.
let fileServerName = "fileServerName_example"; // String | The file server name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.fileServersGet(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **fileServerName** | **String**| The file server name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**FileServer**](FileServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileServersListByDevice

> FileServerList fileServersListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the file servers in a device.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.FileServersApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.fileServersListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**FileServerList**](FileServerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileServersListByManager

> FileServerList fileServersListByManager(subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the file servers in a manager.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.FileServersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.fileServersListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**FileServerList**](FileServerList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileServersListMetricDefinition

> MetricDefinitionList fileServersListMetricDefinition(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves metric definitions of all metrics aggregated at the file server.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.FileServersApi();
let deviceName = "deviceName_example"; // String | The name of the device.
let fileServerName = "fileServerName_example"; // String | The name of the file server.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.fileServersListMetricDefinition(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The name of the device. | 
 **fileServerName** | **String**| The name of the file server. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**MetricDefinitionList**](MetricDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileServersListMetrics

> MetricList fileServersListMetrics(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, opts)



Gets the file server metrics.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.FileServersApi();
let deviceName = "deviceName_example"; // String | The name of the device.
let fileServerName = "fileServerName_example"; // String | The name of the file server name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.fileServersListMetrics(deviceName, fileServerName, subscriptionId, resourceGroupName, managerName, apiVersion, opts, (error, data, response) => {
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
 **deviceName** | **String**| The name of the device. | 
 **fileServerName** | **String**| The name of the file server name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**MetricList**](MetricList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

