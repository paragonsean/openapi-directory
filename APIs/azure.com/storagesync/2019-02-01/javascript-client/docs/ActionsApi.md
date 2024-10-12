# MicrosoftStorageSync.ActionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudEndpointsPostBackup_0**](ActionsApi.md#cloudEndpointsPostBackup_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/postbackup | 
[**cloudEndpointsPostRestore_0**](ActionsApi.md#cloudEndpointsPostRestore_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/postrestore | 
[**cloudEndpointsPreBackup_0**](ActionsApi.md#cloudEndpointsPreBackup_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/prebackup | 
[**cloudEndpointsPreRestore_0**](ActionsApi.md#cloudEndpointsPreRestore_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/prerestore | 
[**cloudEndpointsRestoreheartbeat_0**](ActionsApi.md#cloudEndpointsRestoreheartbeat_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/restoreheartbeat | 
[**registeredServersTriggerRollover_0**](ActionsApi.md#registeredServersTriggerRollover_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId}/triggerRollover | 
[**serverEndpointsRecallAction_0**](ActionsApi.md#serverEndpointsRecallAction_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/serverEndpoints/{serverEndpointName}/recallAction | 
[**workflowsAbort_0**](ActionsApi.md#workflowsAbort_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/workflows/{workflowId}/abort | 



## cloudEndpointsPostBackup_0

> PostBackupResponse cloudEndpointsPostBackup_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Post Backup a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.ActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.BackupRequest(); // BackupRequest | Body of Backup request.
apiInstance.cloudEndpointsPostBackup_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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


## cloudEndpointsPostRestore_0

> cloudEndpointsPostRestore_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Post Restore a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.ActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.PostRestoreRequest(); // PostRestoreRequest | Body of Cloud Endpoint object.
apiInstance.cloudEndpointsPostRestore_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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


## cloudEndpointsPreBackup_0

> cloudEndpointsPreBackup_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Pre Backup a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.ActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.BackupRequest(); // BackupRequest | Body of Backup request.
apiInstance.cloudEndpointsPreBackup_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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


## cloudEndpointsPreRestore_0

> cloudEndpointsPreRestore_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Pre Restore a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.ActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
let parameters = new MicrosoftStorageSync.PreRestoreRequest(); // PreRestoreRequest | Body of Cloud Endpoint object.
apiInstance.cloudEndpointsPreRestore_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters, (error, data, response) => {
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


## cloudEndpointsRestoreheartbeat_0

> cloudEndpointsRestoreheartbeat_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName)



Restore Heartbeat a given CloudEndpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.ActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
apiInstance.cloudEndpointsRestoreheartbeat_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, (error, data, response) => {
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


## registeredServersTriggerRollover_0

> registeredServersTriggerRollover_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, serverId, parameters)



Triggers Server certificate rollover.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.ActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let serverId = "serverId_example"; // String | Server Id
let parameters = new MicrosoftStorageSync.TriggerRolloverRequest(); // TriggerRolloverRequest | Body of Trigger Rollover request.
apiInstance.registeredServersTriggerRollover_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, serverId, parameters, (error, data, response) => {
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
 **serverId** | **String**| Server Id | 
 **parameters** | [**TriggerRolloverRequest**](TriggerRolloverRequest.md)| Body of Trigger Rollover request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serverEndpointsRecallAction_0

> serverEndpointsRecallAction_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, serverEndpointName, parameters)



Recall a server endpoint.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.ActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
let serverEndpointName = "serverEndpointName_example"; // String | Name of Server Endpoint object.
let parameters = new MicrosoftStorageSync.RecallActionParameters(); // RecallActionParameters | Body of Recall Action object.
apiInstance.serverEndpointsRecallAction_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, serverEndpointName, parameters, (error, data, response) => {
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
 **serverEndpointName** | **String**| Name of Server Endpoint object. | 
 **parameters** | [**RecallActionParameters**](RecallActionParameters.md)| Body of Recall Action object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workflowsAbort_0

> workflowsAbort_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, workflowId)



Abort the given workflow.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.ActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let workflowId = "workflowId_example"; // String | workflow Id
apiInstance.workflowsAbort_0(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, workflowId, (error, data, response) => {
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
 **workflowId** | **String**| workflow Id | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

