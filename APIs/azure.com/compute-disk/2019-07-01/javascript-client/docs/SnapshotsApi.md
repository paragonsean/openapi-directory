# DiskResourceProviderClient.SnapshotsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapshotsCreateOrUpdate**](SnapshotsApi.md#snapshotsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName} | 
[**snapshotsDelete**](SnapshotsApi.md#snapshotsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName} | 
[**snapshotsGet**](SnapshotsApi.md#snapshotsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName} | 
[**snapshotsGrantAccess**](SnapshotsApi.md#snapshotsGrantAccess) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName}/beginGetAccess | 
[**snapshotsList**](SnapshotsApi.md#snapshotsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/snapshots | 
[**snapshotsListByResourceGroup**](SnapshotsApi.md#snapshotsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots | 
[**snapshotsRevokeAccess**](SnapshotsApi.md#snapshotsRevokeAccess) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName}/endGetAccess | 
[**snapshotsUpdate**](SnapshotsApi.md#snapshotsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/snapshots/{snapshotName} | 



## snapshotsCreateOrUpdate

> Snapshot snapshotsCreateOrUpdate(subscriptionId, resourceGroupName, snapshotName, apiVersion, snapshot)



Creates or updates a snapshot.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let snapshotName = "snapshotName_example"; // String | The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let snapshot = new DiskResourceProviderClient.Snapshot(); // Snapshot | Snapshot object supplied in the body of the Put disk operation.
apiInstance.snapshotsCreateOrUpdate(subscriptionId, resourceGroupName, snapshotName, apiVersion, snapshot, (error, data, response) => {
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
 **snapshotName** | **String**| The name of the snapshot that is being created. The name can&#39;t be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **snapshot** | [**Snapshot**](Snapshot.md)| Snapshot object supplied in the body of the Put disk operation. | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## snapshotsDelete

> snapshotsDelete(subscriptionId, resourceGroupName, snapshotName, apiVersion)



Deletes a snapshot.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let snapshotName = "snapshotName_example"; // String | The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.snapshotsDelete(subscriptionId, resourceGroupName, snapshotName, apiVersion, (error, data, response) => {
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
 **snapshotName** | **String**| The name of the snapshot that is being created. The name can&#39;t be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## snapshotsGet

> Snapshot snapshotsGet(subscriptionId, resourceGroupName, snapshotName, apiVersion)



Gets information about a snapshot.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let snapshotName = "snapshotName_example"; // String | The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.snapshotsGet(subscriptionId, resourceGroupName, snapshotName, apiVersion, (error, data, response) => {
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
 **snapshotName** | **String**| The name of the snapshot that is being created. The name can&#39;t be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## snapshotsGrantAccess

> AccessUri snapshotsGrantAccess(subscriptionId, resourceGroupName, snapshotName, apiVersion, grantAccessData)



Grants access to a snapshot.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let snapshotName = "snapshotName_example"; // String | The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let grantAccessData = new DiskResourceProviderClient.GrantAccessData(); // GrantAccessData | Access data object supplied in the body of the get snapshot access operation.
apiInstance.snapshotsGrantAccess(subscriptionId, resourceGroupName, snapshotName, apiVersion, grantAccessData, (error, data, response) => {
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
 **snapshotName** | **String**| The name of the snapshot that is being created. The name can&#39;t be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **grantAccessData** | [**GrantAccessData**](GrantAccessData.md)| Access data object supplied in the body of the get snapshot access operation. | 

### Return type

[**AccessUri**](AccessUri.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## snapshotsList

> SnapshotList snapshotsList(subscriptionId, apiVersion)



Lists snapshots under a subscription.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.snapshotsList(subscriptionId, apiVersion, (error, data, response) => {
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

[**SnapshotList**](SnapshotList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## snapshotsListByResourceGroup

> SnapshotList snapshotsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists snapshots under a resource group.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.snapshotsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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

[**SnapshotList**](SnapshotList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## snapshotsRevokeAccess

> snapshotsRevokeAccess(subscriptionId, resourceGroupName, snapshotName, apiVersion)



Revokes access to a snapshot.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let snapshotName = "snapshotName_example"; // String | The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.snapshotsRevokeAccess(subscriptionId, resourceGroupName, snapshotName, apiVersion, (error, data, response) => {
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
 **snapshotName** | **String**| The name of the snapshot that is being created. The name can&#39;t be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## snapshotsUpdate

> Snapshot snapshotsUpdate(subscriptionId, resourceGroupName, snapshotName, apiVersion, snapshot)



Updates (patches) a snapshot.

### Example

```javascript
import DiskResourceProviderClient from 'disk_resource_provider_client';
let defaultClient = DiskResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiskResourceProviderClient.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let snapshotName = "snapshotName_example"; // String | The name of the snapshot that is being created. The name can't be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let snapshot = new DiskResourceProviderClient.SnapshotUpdate(); // SnapshotUpdate | Snapshot object supplied in the body of the Patch snapshot operation.
apiInstance.snapshotsUpdate(subscriptionId, resourceGroupName, snapshotName, apiVersion, snapshot, (error, data, response) => {
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
 **snapshotName** | **String**| The name of the snapshot that is being created. The name can&#39;t be changed after the snapshot is created. Supported characters for the name are a-z, A-Z, 0-9 and _. The max name length is 80 characters. | 
 **apiVersion** | **String**| Client Api Version. | 
 **snapshot** | [**SnapshotUpdate**](SnapshotUpdate.md)| Snapshot object supplied in the body of the Patch snapshot operation. | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

