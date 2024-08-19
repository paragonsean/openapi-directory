# BatchManagement.PoolApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poolCreate**](PoolApi.md#poolCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName} | 
[**poolDelete**](PoolApi.md#poolDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName} | 
[**poolDisableAutoScale**](PoolApi.md#poolDisableAutoScale) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName}/disableAutoScale | 
[**poolGet**](PoolApi.md#poolGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName} | 
[**poolListByBatchAccount**](PoolApi.md#poolListByBatchAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools | 
[**poolStopResize**](PoolApi.md#poolStopResize) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName}/stopResize | Stops an ongoing resize operation on the pool.
[**poolUpdate**](PoolApi.md#poolUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/pools/{poolName} | 



## poolCreate

> Pool poolCreate(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, parameters, opts)



Creates a new pool inside the specified account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.PoolApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.Pool(); // Pool | Additional parameters for pool creation.
let opts = {
  'ifMatch': "ifMatch_example", // String | The entity state (ETag) version of the pool to update. A value of \"*\" can be used to apply the operation only if the pool already exists. If omitted, this operation will always be applied.
  'ifNoneMatch': "ifNoneMatch_example" // String | Set to '*' to allow a new pool to be created, but to prevent updating an existing pool. Other values will be ignored.
};
apiInstance.poolCreate(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **poolName** | **String**| The pool name. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**Pool**](Pool.md)| Additional parameters for pool creation. | 
 **ifMatch** | **String**| The entity state (ETag) version of the pool to update. A value of \&quot;*\&quot; can be used to apply the operation only if the pool already exists. If omitted, this operation will always be applied. | [optional] 
 **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new pool to be created, but to prevent updating an existing pool. Other values will be ignored. | [optional] 

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## poolDelete

> poolDelete(resourceGroupName, accountName, poolName, apiVersion, subscriptionId)



Deletes the specified pool.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.PoolApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.poolDelete(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **poolName** | **String**| The pool name. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolDisableAutoScale

> Pool poolDisableAutoScale(resourceGroupName, accountName, poolName, apiVersion, subscriptionId)



Disables automatic scaling for a pool.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.PoolApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.poolDisableAutoScale(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **poolName** | **String**| The pool name. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolGet

> Pool poolGet(resourceGroupName, accountName, poolName, apiVersion, subscriptionId)



Gets information about the specified pool.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.PoolApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.poolGet(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **poolName** | **String**| The pool name. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolListByBatchAccount

> ListPoolsResult poolListByBatchAccount(resourceGroupName, accountName, apiVersion, subscriptionId, opts)



Lists all of the pools in the specified account.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.PoolApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let opts = {
  'maxresults': 56, // Number | The maximum number of items to return in the response.
  'select': "select_example", // String | Comma separated list of properties that should be returned. e.g. \"properties/provisioningState\". Only top level properties under properties/ are valid for selection.
  'filter': "filter_example" // String | OData filter expression. Valid properties for filtering are:   name  properties/allocationState  properties/allocationStateTransitionTime  properties/creationTime  properties/provisioningState  properties/provisioningStateTransitionTime  properties/lastModified  properties/vmSize  properties/interNodeCommunication  properties/scaleSettings/autoScale  properties/scaleSettings/fixedScale
};
apiInstance.poolListByBatchAccount(resourceGroupName, accountName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **maxresults** | **Number**| The maximum number of items to return in the response. | [optional] 
 **select** | **String**| Comma separated list of properties that should be returned. e.g. \&quot;properties/provisioningState\&quot;. Only top level properties under properties/ are valid for selection. | [optional] 
 **filter** | **String**| OData filter expression. Valid properties for filtering are:   name  properties/allocationState  properties/allocationStateTransitionTime  properties/creationTime  properties/provisioningState  properties/provisioningStateTransitionTime  properties/lastModified  properties/vmSize  properties/interNodeCommunication  properties/scaleSettings/autoScale  properties/scaleSettings/fixedScale | [optional] 

### Return type

[**ListPoolsResult**](ListPoolsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolStopResize

> Pool poolStopResize(resourceGroupName, accountName, poolName, apiVersion, subscriptionId)

Stops an ongoing resize operation on the pool.

This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. After stopping, the pool stabilizes at the number of nodes it was at when the stop operation was done. During the stop operation, the pool allocation state changes first to stopping and then to steady. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.PoolApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.poolStopResize(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **poolName** | **String**| The pool name. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolUpdate

> Pool poolUpdate(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, parameters, opts)



Updates the properties of an existing pool.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.PoolApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the Batch account.
let accountName = "accountName_example"; // String | The name of the Batch account.
let poolName = "poolName_example"; // String | The pool name. This must be unique within the account.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
let parameters = new BatchManagement.Pool(); // Pool | Pool properties that should be updated. Properties that are supplied will be updated, any property not supplied will be unchanged.
let opts = {
  'ifMatch': "ifMatch_example" // String | The entity state (ETag) version of the pool to update. This value can be omitted or set to \"*\" to apply the operation unconditionally.
};
apiInstance.poolUpdate(resourceGroupName, accountName, poolName, apiVersion, subscriptionId, parameters, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the Batch account. | 
 **accountName** | **String**| The name of the Batch account. | 
 **poolName** | **String**| The pool name. This must be unique within the account. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 
 **parameters** | [**Pool**](Pool.md)| Pool properties that should be updated. Properties that are supplied will be updated, any property not supplied will be unchanged. | 
 **ifMatch** | **String**| The entity state (ETag) version of the pool to update. This value can be omitted or set to \&quot;*\&quot; to apply the operation unconditionally. | [optional] 

### Return type

[**Pool**](Pool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

