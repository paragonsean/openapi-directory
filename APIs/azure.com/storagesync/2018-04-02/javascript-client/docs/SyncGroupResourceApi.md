# MicrosoftStorageSync.SyncGroupResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**syncGroupsCreate**](SyncGroupResourceApi.md#syncGroupsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName} | 
[**syncGroupsDelete**](SyncGroupResourceApi.md#syncGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName} | 
[**syncGroupsGet**](SyncGroupResourceApi.md#syncGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName} | 
[**syncGroupsListByStorageSyncService**](SyncGroupResourceApi.md#syncGroupsListByStorageSyncService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups | 



## syncGroupsCreate

> SyncGroup syncGroupsCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, parameters)



Create a new SyncGroup.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.SyncGroupResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let parameters = new MicrosoftStorageSync.SyncGroupCreateParameters(); // SyncGroupCreateParameters | Sync Group Body
apiInstance.syncGroupsCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **syncGroupName** | **String**| Name of Sync Group resource. | 
 **parameters** | [**SyncGroupCreateParameters**](SyncGroupCreateParameters.md)| Sync Group Body | 

### Return type

[**SyncGroup**](SyncGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## syncGroupsDelete

> syncGroupsDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName)



Delete a given SyncGroup.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.SyncGroupResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
apiInstance.syncGroupsDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **syncGroupName** | **String**| Name of Sync Group resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## syncGroupsGet

> SyncGroup syncGroupsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName)



Get a given SyncGroup.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.SyncGroupResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
apiInstance.syncGroupsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **syncGroupName** | **String**| Name of Sync Group resource. | 

### Return type

[**SyncGroup**](SyncGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## syncGroupsListByStorageSyncService

> SyncGroupArray syncGroupsListByStorageSyncService(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName)



Get a SyncGroup List.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.SyncGroupResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
apiInstance.syncGroupsListByStorageSyncService(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 

### Return type

[**SyncGroupArray**](SyncGroupArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

