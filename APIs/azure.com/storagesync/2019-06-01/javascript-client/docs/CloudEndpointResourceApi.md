# MicrosoftStorageSync.CloudEndpointResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudEndpointsCreate**](CloudEndpointResourceApi.md#cloudEndpointsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName} | 
[**cloudEndpointsDelete**](CloudEndpointResourceApi.md#cloudEndpointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName} | 
[**cloudEndpointsGet**](CloudEndpointResourceApi.md#cloudEndpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName} | 
[**cloudEndpointsListBySyncGroup**](CloudEndpointResourceApi.md#cloudEndpointsListBySyncGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints | 
[**cloudEndpointsPostBackup**](CloudEndpointResourceApi.md#cloudEndpointsPostBackup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/postbackup | 
[**cloudEndpointsPostRestore**](CloudEndpointResourceApi.md#cloudEndpointsPostRestore) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/postrestore | 
[**cloudEndpointsPreBackup**](CloudEndpointResourceApi.md#cloudEndpointsPreBackup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/prebackup | 
[**cloudEndpointsPreRestore**](CloudEndpointResourceApi.md#cloudEndpointsPreRestore) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/prerestore | 
[**cloudEndpointsRestoreheartbeat**](CloudEndpointResourceApi.md#cloudEndpointsRestoreheartbeat) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/restoreheartbeat | 
[**cloudEndpointsTriggerChangeDetection**](CloudEndpointResourceApi.md#cloudEndpointsTriggerChangeDetection) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/triggerChangeDetection | 



## cloudEndpointsCreate

> CloudEndpoint cloudEndpointsCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Create a new CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.CloudEndpointCreateParameters(); // CloudEndpointCreateParameters | Body of Cloud Endpoint resource.
apiInstance.cloudEndpointsCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**CloudEndpointCreateParameters**](CloudEndpointCreateParameters.md)| Body of Cloud Endpoint resource. | 

### Return type

[**CloudEndpoint**](CloudEndpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsDelete

> cloudEndpointsDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName)



Delete a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
apiInstance.cloudEndpointsDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudEndpointsGet

> CloudEndpoint cloudEndpointsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName)



Get a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
apiInstance.cloudEndpointsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 

### Return type

[**CloudEndpoint**](CloudEndpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudEndpointsListBySyncGroup

> CloudEndpointArray cloudEndpointsListBySyncGroup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName)



Get a CloudEndpoint List.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
apiInstance.cloudEndpointsListBySyncGroup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, (error, data, response) => {
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

[**CloudEndpointArray**](CloudEndpointArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudEndpointsPostBackup

> PostBackupResponse cloudEndpointsPostBackup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Post Backup a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.BackupRequest(); // BackupRequest | Body of Backup request.
apiInstance.cloudEndpointsPostBackup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**BackupRequest**](BackupRequest.md)| Body of Backup request. | 

### Return type

[**PostBackupResponse**](PostBackupResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsPostRestore

> cloudEndpointsPostRestore(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Post Restore a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.PostRestoreRequest(); // PostRestoreRequest | Body of Cloud Endpoint object.
apiInstance.cloudEndpointsPostRestore(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**PostRestoreRequest**](PostRestoreRequest.md)| Body of Cloud Endpoint object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsPreBackup

> cloudEndpointsPreBackup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Pre Backup a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.BackupRequest(); // BackupRequest | Body of Backup request.
apiInstance.cloudEndpointsPreBackup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**BackupRequest**](BackupRequest.md)| Body of Backup request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsPreRestore

> cloudEndpointsPreRestore(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Pre Restore a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.PreRestoreRequest(); // PreRestoreRequest | Body of Cloud Endpoint object.
apiInstance.cloudEndpointsPreRestore(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**PreRestoreRequest**](PreRestoreRequest.md)| Body of Cloud Endpoint object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudEndpointsRestoreheartbeat

> cloudEndpointsRestoreheartbeat(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName)



Restore Heartbeat a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
apiInstance.cloudEndpointsRestoreheartbeat(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudEndpointsTriggerChangeDetection

> cloudEndpointsTriggerChangeDetection(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.CloudEndpointResourceApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.TriggerChangeDetectionParameters(); // TriggerChangeDetectionParameters | Trigger Change Detection Action parameters.
apiInstance.cloudEndpointsTriggerChangeDetection(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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
 **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | 
 **parameters** | [**TriggerChangeDetectionParameters**](TriggerChangeDetectionParameters.md)| Trigger Change Detection Action parameters. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

