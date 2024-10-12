# DiskResourceProviderClient.DisksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disksCreateOrUpdate**](DisksApi.md#disksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName} | 
[**disksDelete**](DisksApi.md#disksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName} | 
[**disksGet**](DisksApi.md#disksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName} | 
[**disksGrantAccess**](DisksApi.md#disksGrantAccess) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName}/beginGetAccess | 
[**disksList**](DisksApi.md#disksList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/disks | 
[**disksListByResourceGroup**](DisksApi.md#disksListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks | 
[**disksRevokeAccess**](DisksApi.md#disksRevokeAccess) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName}/endGetAccess | 
[**disksUpdate**](DisksApi.md#disksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/disks/{diskName} | 



## disksCreateOrUpdate

> Disk disksCreateOrUpdate(subscriptionId, resourceGroupName, diskName, apiVersion, disk)



Creates or updates a disk.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';

let apiInstance = new DiskResourceProviderClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskName = "diskName_example"; // String | The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let disk = new DiskResourceProviderClient.Disk(); // Disk | Disk object supplied in the body of the Put disk operation.
apiInstance.disksCreateOrUpdate(subscriptionId, resourceGroupName, diskName, apiVersion, disk, (error, data, response) => {
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
 **diskName** | **String**| The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **disk** | [**Disk**](Disk.md)| Disk object supplied in the body of the Put disk operation. | 

### Return type

[**Disk**](Disk.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disksDelete

> OperationStatusResponse disksDelete(subscriptionId, resourceGroupName, diskName, apiVersion)



Deletes a disk.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';

let apiInstance = new DiskResourceProviderClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskName = "diskName_example"; // String | The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.disksDelete(subscriptionId, resourceGroupName, diskName, apiVersion, (error, data, response) => {
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
 **diskName** | **String**| The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disksGet

> Disk disksGet(subscriptionId, resourceGroupName, diskName, apiVersion)



Gets information about a disk.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';

let apiInstance = new DiskResourceProviderClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskName = "diskName_example"; // String | The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.disksGet(subscriptionId, resourceGroupName, diskName, apiVersion, (error, data, response) => {
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
 **diskName** | **String**| The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Disk**](Disk.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disksGrantAccess

> AccessUri disksGrantAccess(subscriptionId, resourceGroupName, diskName, apiVersion, grantAccessData)



Grants access to a disk.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';

let apiInstance = new DiskResourceProviderClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskName = "diskName_example"; // String | The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let grantAccessData = new DiskResourceProviderClient.GrantAccessData(); // GrantAccessData | Access data object supplied in the body of the get disk access operation.
apiInstance.disksGrantAccess(subscriptionId, resourceGroupName, diskName, apiVersion, grantAccessData, (error, data, response) => {
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
 **diskName** | **String**| The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **grantAccessData** | [**GrantAccessData**](GrantAccessData.md)| Access data object supplied in the body of the get disk access operation. | 

### Return type

[**AccessUri**](AccessUri.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disksList

> DiskList disksList(subscriptionId, apiVersion)



Lists all the disks under a subscription.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';

let apiInstance = new DiskResourceProviderClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.disksList(subscriptionId, apiVersion, (error, data, response) => {
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

[**DiskList**](DiskList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disksListByResourceGroup

> DiskList disksListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all the disks under a resource group.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';

let apiInstance = new DiskResourceProviderClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.disksListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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

[**DiskList**](DiskList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disksRevokeAccess

> OperationStatusResponse disksRevokeAccess(subscriptionId, resourceGroupName, diskName, apiVersion)



Revokes access to a disk.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';

let apiInstance = new DiskResourceProviderClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskName = "diskName_example"; // String | The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.disksRevokeAccess(subscriptionId, resourceGroupName, diskName, apiVersion, (error, data, response) => {
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
 **diskName** | **String**| The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disksUpdate

> Disk disksUpdate(subscriptionId, resourceGroupName, diskName, apiVersion, disk)



Updates (patches) a disk.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';

let apiInstance = new DiskResourceProviderClient.DisksApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let diskName = "diskName_example"; // String | The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let disk = new DiskResourceProviderClient.DiskUpdate(); // DiskUpdate | Disk object supplied in the body of the Patch disk operation.
apiInstance.disksUpdate(subscriptionId, resourceGroupName, diskName, apiVersion, disk, (error, data, response) => {
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
 **diskName** | **String**| The name of the managed disk that is being created. The name can&#39;t be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The maximum name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **disk** | [**DiskUpdate**](DiskUpdate.md)| Disk object supplied in the body of the Patch disk operation. | 

### Return type

[**Disk**](Disk.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

