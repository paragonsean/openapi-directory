# MicrosoftStorageSync.StorageSyncServicesResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageSyncServicesCreate**](StorageSyncServicesResourceApi.md#storageSyncServicesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName} | 
[**storageSyncServicesDelete**](StorageSyncServicesResourceApi.md#storageSyncServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName} | 
[**storageSyncServicesGet**](StorageSyncServicesResourceApi.md#storageSyncServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName} | 
[**storageSyncServicesListByResourceGroup**](StorageSyncServicesResourceApi.md#storageSyncServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices | 
[**storageSyncServicesListBySubscription**](StorageSyncServicesResourceApi.md#storageSyncServicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.StorageSync/storageSyncServices | 
[**storageSyncServicesUpdate**](StorageSyncServicesResourceApi.md#storageSyncServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName} | 



## storageSyncServicesCreate

> StorageSyncService storageSyncServicesCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, parameters)



Create a new StorageSyncService.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.StorageSyncServicesResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let parameters = new MicrosoftStorageSync.StorageSyncService(); // StorageSyncService | Storage Sync Service resource name.
apiInstance.storageSyncServicesCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, parameters, (error, data, response) => {
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
 **parameters** | [**StorageSyncService**](StorageSyncService.md)| Storage Sync Service resource name. | 

### Return type

[**StorageSyncService**](StorageSyncService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageSyncServicesDelete

> storageSyncServicesDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName)



Delete a given StorageSyncService.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.StorageSyncServicesResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
apiInstance.storageSyncServicesDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageSyncServicesGet

> StorageSyncService storageSyncServicesGet(subscriptionId, resourceGroupName, storageSyncServiceName, apiVersion)



Get a given StorageSyncService.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.StorageSyncServicesResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.storageSyncServicesGet(subscriptionId, resourceGroupName, storageSyncServiceName, apiVersion, (error, data, response) => {
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
 **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**StorageSyncService**](StorageSyncService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageSyncServicesListByResourceGroup

> StorageSyncServiceArray storageSyncServicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Get a StorageSyncService list by Resource group name.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.StorageSyncServicesResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.storageSyncServicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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

### Return type

[**StorageSyncServiceArray**](StorageSyncServiceArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageSyncServicesListBySubscription

> StorageSyncServiceArray storageSyncServicesListBySubscription(subscriptionId, apiVersion)



Get a StorageSyncService list by subscription.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.StorageSyncServicesResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.storageSyncServicesListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**StorageSyncServiceArray**](StorageSyncServiceArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageSyncServicesUpdate

> StorageSyncService storageSyncServicesUpdate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, opts)



Patch a given StorageSyncService.

### Example

```javascript
import MicrosoftStorageSync from 'microsoft_storage_sync';
let defaultClient = MicrosoftStorageSync.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftStorageSync.StorageSyncServicesResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
let opts = {
  'parameters': new MicrosoftStorageSync.StorageSyncService() // StorageSyncService | Storage Sync Service resource.
};
apiInstance.storageSyncServicesUpdate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, opts, (error, data, response) => {
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
 **parameters** | [**StorageSyncService**](StorageSyncService.md)| Storage Sync Service resource. | [optional] 

### Return type

[**StorageSyncService**](StorageSyncService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

