# StorSimpleManagementClient.BackupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupsClone**](BackupsApi.md#backupsClone) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backups/{backupName}/elements/{elementName}/clone | 
[**backupsDelete**](BackupsApi.md#backupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backups/{backupName} | 
[**backupsListByDevice**](BackupsApi.md#backupsListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backups | 
[**backupsListByManager**](BackupsApi.md#backupsListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/backups | 



## backupsClone

> backupsClone(deviceName, backupName, elementName, subscriptionId, resourceGroupName, managerName, apiVersion, cloneRequest)



Clones the given backup element to a new disk or share with given details.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.BackupsApi();
let deviceName = "deviceName_example"; // String | The device name.
let backupName = "backupName_example"; // String | The backup name.
let elementName = "elementName_example"; // String | The backup element name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let cloneRequest = new StorSimpleManagementClient.CloneRequest(); // CloneRequest | The clone request.
apiInstance.backupsClone(deviceName, backupName, elementName, subscriptionId, resourceGroupName, managerName, apiVersion, cloneRequest, (error, data, response) => {
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
 **backupName** | **String**| The backup name. | 
 **elementName** | **String**| The backup element name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **cloneRequest** | [**CloneRequest**](CloneRequest.md)| The clone request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## backupsDelete

> backupsDelete(deviceName, backupName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the backup.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.BackupsApi();
let deviceName = "deviceName_example"; // String | The device name.
let backupName = "backupName_example"; // String | The backup name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.backupsDelete(deviceName, backupName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **backupName** | **String**| The backup name. | 
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


## backupsListByDevice

> BackupList backupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, opts)



Retrieves all the backups in a device. Can be used to get the backups for failover also.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.BackupsApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let opts = {
  'forFailover': true, // Boolean | Set to true if you need backups which can be used for failover.
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.backupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, opts, (error, data, response) => {
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
 **forFailover** | **Boolean**| Set to true if you need backups which can be used for failover. | [optional] 
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**BackupList**](BackupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupsListByManager

> BackupList backupsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, opts)



Retrieves all the backups in a manager.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.BackupsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let opts = {
  'filter': "filter_example" // String | OData Filter options
};
apiInstance.backupsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| OData Filter options | [optional] 

### Return type

[**BackupList**](BackupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

