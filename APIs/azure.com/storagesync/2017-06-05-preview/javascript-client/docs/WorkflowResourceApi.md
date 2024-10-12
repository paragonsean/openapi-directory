# MicrosoftStorageSync.WorkflowResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowsAbort**](WorkflowResourceApi.md#workflowsAbort) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/workflows/{workflowId}/abort | 
[**workflowsGet**](WorkflowResourceApi.md#workflowsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/workflows/{workflowId} | 



## workflowsAbort

> workflowsAbort(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, workflowId)



Abort the given workflow.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.WorkflowResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let workflowId = "workflowId_example"; // String | workflow Id
apiInstance.workflowsAbort(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, workflowId, (error, data, response) => {
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
 **workflowId** | **String**| workflow Id | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workflowsGet

> Workflow workflowsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, workflowId)



Get Workflows resource

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.WorkflowResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let workflowId = "workflowId_example"; // String | workflow Id
apiInstance.workflowsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, workflowId, (error, data, response) => {
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
 **workflowId** | **String**| workflow Id | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

