# DataBoxEdgeManagementClient.StorageAccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageAccountsCreateOrUpdate**](StorageAccountsApi.md#storageAccountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccounts/{storageAccountName} | Creates a new StorageAccount or updates an existing StorageAccount on the device.
[**storageAccountsDelete**](StorageAccountsApi.md#storageAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccounts/{storageAccountName} | 
[**storageAccountsGet**](StorageAccountsApi.md#storageAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccounts/{storageAccountName} | Gets a StorageAccount by name.
[**storageAccountsListByDataBoxEdgeDevice**](StorageAccountsApi.md#storageAccountsListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/storageAccounts | Lists all the storage accounts in a Data Box Edge/Data Box Gateway device.



## storageAccountsCreateOrUpdate

> StorageAccount storageAccountsCreateOrUpdate(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion, storageAccount)

Creates a new StorageAccount or updates an existing StorageAccount on the device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.StorageAccountsApi();
let deviceName = "deviceName_example"; // String | The device name.
let storageAccountName = "storageAccountName_example"; // String | The StorageAccount name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let storageAccount = new DataBoxEdgeManagementClient.StorageAccount(); // StorageAccount | The StorageAccount properties.
apiInstance.storageAccountsCreateOrUpdate(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion, storageAccount, (error, data, response) => {
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
 **storageAccountName** | **String**| The StorageAccount name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **storageAccount** | [**StorageAccount**](StorageAccount.md)| The StorageAccount properties. | 

### Return type

[**StorageAccount**](StorageAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageAccountsDelete

> storageAccountsDelete(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion)



Deletes the StorageAccount on the Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.StorageAccountsApi();
let deviceName = "deviceName_example"; // String | The device name.
let storageAccountName = "storageAccountName_example"; // String | The StorageAccount name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.storageAccountsDelete(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **storageAccountName** | **String**| The StorageAccount name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageAccountsGet

> StorageAccount storageAccountsGet(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion)

Gets a StorageAccount by name.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.StorageAccountsApi();
let deviceName = "deviceName_example"; // String | The device name.
let storageAccountName = "storageAccountName_example"; // String | The storage account name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.storageAccountsGet(deviceName, storageAccountName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **storageAccountName** | **String**| The storage account name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**StorageAccount**](StorageAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageAccountsListByDataBoxEdgeDevice

> StorageAccountList storageAccountsListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion)

Lists all the storage accounts in a Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.StorageAccountsApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.storageAccountsListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**StorageAccountList**](StorageAccountList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

