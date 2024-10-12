# MicrosoftNetApp.SnapshotsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapshotsCreate**](SnapshotsApi.md#snapshotsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots/{snapshotName} | Create a snapshot
[**snapshotsDelete**](SnapshotsApi.md#snapshotsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots/{snapshotName} | Delete a snapshot
[**snapshotsGet**](SnapshotsApi.md#snapshotsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots/{snapshotName} | Describe a snapshot
[**snapshotsList**](SnapshotsApi.md#snapshotsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots | Describe all snapshots
[**snapshotsUpdate**](SnapshotsApi.md#snapshotsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots/{snapshotName} | Update a snapshot



## snapshotsCreate

> Snapshot snapshotsCreate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, body)

Create a snapshot

Create the specified snapshot within the given volume

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let snapshotName = "snapshotName_example"; // String | The name of the mount target
let apiVersion = "'2019-06-01'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.Snapshot(); // Snapshot | Snapshot object supplied in the body of the operation.
apiInstance.snapshotsCreate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, body, (error, data, response) => {
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
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **snapshotName** | **String**| The name of the mount target | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-06-01&#39;]
 **body** | [**Snapshot**](Snapshot.md)| Snapshot object supplied in the body of the operation. | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## snapshotsDelete

> snapshotsDelete(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion)

Delete a snapshot

Delete snapshot

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let snapshotName = "snapshotName_example"; // String | The name of the mount target
let apiVersion = "'2019-06-01'"; // String | Version of the API to be used with the client request.
apiInstance.snapshotsDelete(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, (error, data, response) => {
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
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **snapshotName** | **String**| The name of the mount target | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-06-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## snapshotsGet

> Snapshot snapshotsGet(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion)

Describe a snapshot

Get details of the specified snapshot

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let snapshotName = "snapshotName_example"; // String | The name of the mount target
let apiVersion = "'2019-06-01'"; // String | Version of the API to be used with the client request.
apiInstance.snapshotsGet(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, (error, data, response) => {
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
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **snapshotName** | **String**| The name of the mount target | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-06-01&#39;]

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## snapshotsList

> SnapshotsList snapshotsList(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Describe all snapshots

List all snapshots associated with the volume

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-06-01'"; // String | Version of the API to be used with the client request.
apiInstance.snapshotsList(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, (error, data, response) => {
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
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-06-01&#39;]

### Return type

[**SnapshotsList**](SnapshotsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## snapshotsUpdate

> Snapshot snapshotsUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, body)

Update a snapshot

Patch a snapshot

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.SnapshotsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let snapshotName = "snapshotName_example"; // String | The name of the mount target
let apiVersion = "'2019-06-01'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.SnapshotPatch(); // SnapshotPatch | Snapshot object supplied in the body of the operation.
apiInstance.snapshotsUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, body, (error, data, response) => {
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
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **snapshotName** | **String**| The name of the mount target | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-06-01&#39;]
 **body** | [**SnapshotPatch**](SnapshotPatch.md)| Snapshot object supplied in the body of the operation. | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

