# MicrosoftNetApp.VolumesReplicationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volumesAuthorizeReplication**](VolumesReplicationApi.md#volumesAuthorizeReplication) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/authorizeReplication | Authorize source volume replication
[**volumesBreakReplication**](VolumesReplicationApi.md#volumesBreakReplication) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/breakReplication | Break volume replication
[**volumesDeleteReplication**](VolumesReplicationApi.md#volumesDeleteReplication) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/deleteReplication | Delete volume replication
[**volumesReplicationStatus**](VolumesReplicationApi.md#volumesReplicationStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/replicationStatus | Get volume replication status
[**volumesResyncReplication**](VolumesReplicationApi.md#volumesResyncReplication) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/resyncReplication | Resync volume replication



## volumesAuthorizeReplication

> volumesAuthorizeReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body)

Authorize source volume replication

Authorize the replication connection on the source volume

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesReplicationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-11-01'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.AuthorizeRequest(); // AuthorizeRequest | Authorize request object supplied in the body of the operation.
apiInstance.volumesAuthorizeReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-11-01&#39;]
 **body** | [**AuthorizeRequest**](AuthorizeRequest.md)| Authorize request object supplied in the body of the operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## volumesBreakReplication

> volumesBreakReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Break volume replication

Break the replication connection on the destination volume

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesReplicationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-11-01'"; // String | Version of the API to be used with the client request.
apiInstance.volumesBreakReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-11-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## volumesDeleteReplication

> volumesDeleteReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Delete volume replication

Delete the replication connection on the destination volume, and send release to the source replication

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesReplicationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-11-01'"; // String | Version of the API to be used with the client request.
apiInstance.volumesDeleteReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-11-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## volumesReplicationStatus

> ReplicationStatus volumesReplicationStatus(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Get volume replication status

Get the status of the replication

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesReplicationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-11-01'"; // String | Version of the API to be used with the client request.
apiInstance.volumesReplicationStatus(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-11-01&#39;]

### Return type

[**ReplicationStatus**](ReplicationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## volumesResyncReplication

> volumesResyncReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Resync volume replication

Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from source to destination.

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesReplicationApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-11-01'"; // String | Version of the API to be used with the client request.
apiInstance.volumesResyncReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-11-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

