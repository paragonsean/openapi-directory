# MicrosoftStorageSync.BackupRestoreApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudEndpointsPostBackup_1**](BackupRestoreApi.md#cloudEndpointsPostBackup_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/postbackup | 
[**cloudEndpointsPostRestore_1**](BackupRestoreApi.md#cloudEndpointsPostRestore_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/postrestore | 
[**cloudEndpointsPreBackup_1**](BackupRestoreApi.md#cloudEndpointsPreBackup_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/prebackup | 
[**cloudEndpointsPreRestore_1**](BackupRestoreApi.md#cloudEndpointsPreRestore_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/prerestore | 
[**cloudEndpointsRestoreHeatbeat_1**](BackupRestoreApi.md#cloudEndpointsRestoreHeatbeat_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/restoreheartbeat | 



## cloudEndpointsPostBackup_1

> PostBackupResponse cloudEndpointsPostBackup_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Post Backup a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.BackupRestoreApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.BackupRequest(); // BackupRequest | Body of Backup request.
apiInstance.cloudEndpointsPostBackup_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **syncGroupName** | **String**| Name of Sync Group resource. | 
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**BackupRequest**](BackupRequest.md)| Body of Backup request. | 

### Return type

[**PostBackupResponse**](PostBackupResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsPostRestore_1

> cloudEndpointsPostRestore_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Post Restore a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.BackupRestoreApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.PostRestoreRequest(); // PostRestoreRequest | Body of Cloud Endpoint object.
apiInstance.cloudEndpointsPostRestore_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **syncGroupName** | **String**| Name of Sync Group resource. | 
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**PostRestoreRequest**](PostRestoreRequest.md)| Body of Cloud Endpoint object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsPreBackup_1

> cloudEndpointsPreBackup_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Pre Backup a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.BackupRestoreApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.BackupRequest(); // BackupRequest | Body of Backup request.
apiInstance.cloudEndpointsPreBackup_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **syncGroupName** | **String**| Name of Sync Group resource. | 
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**BackupRequest**](BackupRequest.md)| Body of Backup request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsPreRestore_1

> cloudEndpointsPreRestore_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Pre Restore a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.BackupRestoreApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.PreRestoreRequest(); // PreRestoreRequest | Body of Cloud Endpoint object.
apiInstance.cloudEndpointsPreRestore_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **syncGroupName** | **String**| Name of Sync Group resource. | 
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**PreRestoreRequest**](PreRestoreRequest.md)| Body of Cloud Endpoint object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsRestoreHeatbeat_1

> cloudEndpointsRestoreHeatbeat_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName)



Restore Heartbeat a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.BackupRestoreApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
apiInstance.cloudEndpointsRestoreHeatbeat_1(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **syncGroupName** | **String**| Name of Sync Group resource. | 
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

