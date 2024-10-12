# DiskResourceProviderClient.DiskEncryptionSetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diskEncryptionSetsCreateOrUpdate**](DiskEncryptionSetsApi.md#diskEncryptionSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName} | 
[**diskEncryptionSetsDelete**](DiskEncryptionSetsApi.md#diskEncryptionSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName} | 
[**diskEncryptionSetsGet**](DiskEncryptionSetsApi.md#diskEncryptionSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName} | 
[**diskEncryptionSetsList**](DiskEncryptionSetsApi.md#diskEncryptionSetsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/diskEncryptionSets | 
[**diskEncryptionSetsListByResourceGroup**](DiskEncryptionSetsApi.md#diskEncryptionSetsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets | 
[**diskEncryptionSetsUpdate**](DiskEncryptionSetsApi.md#diskEncryptionSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/diskEncryptionSets/{diskEncryptionSetName} | 



## diskEncryptionSetsCreateOrUpdate

> DiskEncryptionSet diskEncryptionSetsCreateOrUpdate(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, diskEncryptionSet)



Creates or updates a disk encryption set

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.DiskEncryptionSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskEncryptionSetName = "diskEncryptionSetName_example"; // String | The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let diskEncryptionSet = new DiskResourceProviderClient.DiskEncryptionSet(); // DiskEncryptionSet | disk encryption set object supplied in the body of the Put disk encryption set operation.
apiInstance.diskEncryptionSetsCreateOrUpdate(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, diskEncryptionSet, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **diskEncryptionSetName** | **String**| The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **diskEncryptionSet** | [**DiskEncryptionSet**](DiskEncryptionSet.md)| disk encryption set object supplied in the body of the Put disk encryption set operation. | 

### Return type

[**DiskEncryptionSet**](DiskEncryptionSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## diskEncryptionSetsDelete

> diskEncryptionSetsDelete(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion)



Deletes a disk encryption set.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.DiskEncryptionSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskEncryptionSetName = "diskEncryptionSetName_example"; // String | The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.diskEncryptionSetsDelete(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **diskEncryptionSetName** | **String**| The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diskEncryptionSetsGet

> DiskEncryptionSet diskEncryptionSetsGet(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion)



Gets information about a disk encryption set.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.DiskEncryptionSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskEncryptionSetName = "diskEncryptionSetName_example"; // String | The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.diskEncryptionSetsGet(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **diskEncryptionSetName** | **String**| The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DiskEncryptionSet**](DiskEncryptionSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diskEncryptionSetsList

> DiskEncryptionSetList diskEncryptionSetsList(subscriptionId, apiVersion)



Lists all the disk encryption sets under a subscription.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.DiskEncryptionSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.diskEncryptionSetsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DiskEncryptionSetList**](DiskEncryptionSetList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diskEncryptionSetsListByResourceGroup

> DiskEncryptionSetList diskEncryptionSetsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the disk encryption sets under a resource group.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.DiskEncryptionSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.diskEncryptionSetsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DiskEncryptionSetList**](DiskEncryptionSetList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diskEncryptionSetsUpdate

> DiskEncryptionSet diskEncryptionSetsUpdate(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, diskEncryptionSet)



Updates (patches) a disk encryption set.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.DiskEncryptionSetsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskEncryptionSetName = "diskEncryptionSetName_example"; // String | The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let diskEncryptionSet = new DiskResourceProviderClient.DiskEncryptionSetUpdate(); // DiskEncryptionSetUpdate | disk encryption set object supplied in the body of the Patch disk encryption set operation.
apiInstance.diskEncryptionSetsUpdate(subscriptionId, resourceGroupName, diskEncryptionSetName, apiVersion, diskEncryptionSet, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **diskEncryptionSetName** | **String**| The name of the disk encryption set that is being created. The name can&#39;t be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **diskEncryptionSet** | [**DiskEncryptionSetUpdate**](DiskEncryptionSetUpdate.md)| disk encryption set object supplied in the body of the Patch disk encryption set operation. | 

### Return type

[**DiskEncryptionSet**](DiskEncryptionSet.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

