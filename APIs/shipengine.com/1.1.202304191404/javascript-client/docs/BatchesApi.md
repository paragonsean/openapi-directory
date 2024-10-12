# ShipEngineApi.BatchesApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addToBatch**](BatchesApi.md#addToBatch) | **POST** /v1/batches/{batch_id}/add | Add to a Batch
[**createBatch**](BatchesApi.md#createBatch) | **POST** /v1/batches | Create A Batch
[**deleteBatch**](BatchesApi.md#deleteBatch) | **DELETE** /v1/batches/{batch_id} | Delete Batch By Id
[**getBatchByExternalId**](BatchesApi.md#getBatchByExternalId) | **GET** /v1/batches/external_batch_id/{external_batch_id} | Get Batch By External ID
[**getBatchById**](BatchesApi.md#getBatchById) | **GET** /v1/batches/{batch_id} | Get Batch By ID
[**listBatchErrors**](BatchesApi.md#listBatchErrors) | **GET** /v1/batches/{batch_id}/errors | Get Batch Errors
[**listBatches**](BatchesApi.md#listBatches) | **GET** /v1/batches | List Batches
[**processBatch**](BatchesApi.md#processBatch) | **POST** /v1/batches/{batch_id}/process/labels | Process Batch ID Labels
[**removeFromBatch**](BatchesApi.md#removeFromBatch) | **POST** /v1/batches/{batch_id}/remove | Remove From Batch
[**updateBatch**](BatchesApi.md#updateBatch) | **PUT** /v1/batches/{batch_id} | Update Batch By Id



## addToBatch

> String addToBatch(batchId, addToBatchRequestBody)

Add to a Batch

Add a Shipment or Rate to a Batch

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let batchId = "batchId_example"; // String | Batch ID
let addToBatchRequestBody = new ShipEngineApi.AddToBatchRequestBody(); // AddToBatchRequestBody | 
apiInstance.addToBatch(batchId, addToBatchRequestBody, (error, data, response) => {
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
 **batchId** | **String**| Batch ID | 
 **addToBatchRequestBody** | [**AddToBatchRequestBody**](AddToBatchRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain


## createBatch

> CreateBatchResponseBody createBatch(createBatchRequestBody)

Create A Batch

Create a Batch

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let createBatchRequestBody = new ShipEngineApi.CreateBatchRequestBody(); // CreateBatchRequestBody | 
apiInstance.createBatch(createBatchRequestBody, (error, data, response) => {
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
 **createBatchRequestBody** | [**CreateBatchRequestBody**](CreateBatchRequestBody.md)|  | 

### Return type

[**CreateBatchResponseBody**](CreateBatchResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBatch

> String deleteBatch(batchId)

Delete Batch By Id

Delete Batch By Id

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let batchId = "batchId_example"; // String | Batch ID
apiInstance.deleteBatch(batchId, (error, data, response) => {
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
 **batchId** | **String**| Batch ID | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## getBatchByExternalId

> GetBatchByExternalIdResponseBody getBatchByExternalId(externalBatchId)

Get Batch By External ID

Get Batch By External ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let externalBatchId = "13553d7f-3c87-4771-bae1-c49bacef11cb"; // String | 
apiInstance.getBatchByExternalId(externalBatchId, (error, data, response) => {
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
 **externalBatchId** | **String**|  | 

### Return type

[**GetBatchByExternalIdResponseBody**](GetBatchByExternalIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatchById

> GetBatchByIdResponseBody getBatchById(batchId)

Get Batch By ID

Get Batch By ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let batchId = "batchId_example"; // String | Batch ID
apiInstance.getBatchById(batchId, (error, data, response) => {
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
 **batchId** | **String**| Batch ID | 

### Return type

[**GetBatchByIdResponseBody**](GetBatchByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBatchErrors

> ListBatchErrorsResponseBody listBatchErrors(batchId, opts)

Get Batch Errors

Error handling in batches are handled differently than in a single synchronous request. You must retrieve the status of your batch by [getting a batch](https://www.shipengine.com/docs/reference/get-batch-by-id/) and getting an overview of the statuses or you can list errors directly here below to get detailed information about the errors. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let batchId = "batchId_example"; // String | Batch ID
let opts = {
  'page': 2, // Number | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
  'pagesize': 56 // Number | 
};
apiInstance.listBatchErrors(batchId, opts, (error, data, response) => {
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
 **batchId** | **String**| Batch ID | 
 **page** | **Number**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1]
 **pagesize** | **Number**|  | [optional] 

### Return type

[**ListBatchErrorsResponseBody**](ListBatchErrorsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBatches

> ListBatchesResponseBody listBatches(opts)

List Batches

List Batches associated with your Shipengine account

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let opts = {
  'status': new ShipEngineApi.BatchStatus(), // BatchStatus | 
  'page': 2, // Number | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
  'pageSize': 50, // Number | The number of results to return per response.
  'sortDir': new ShipEngineApi.SortDir(), // SortDir | Controls the sort order of the query.
  'batchNumber': "batchNumber_example", // String | Batch Number
  'sortBy': new ShipEngineApi.BatchesSortBy() // BatchesSortBy | 
};
apiInstance.listBatches(opts, (error, data, response) => {
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
 **status** | [**BatchStatus**](.md)|  | [optional] 
 **page** | **Number**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per response. | [optional] [default to 25]
 **sortDir** | [**SortDir**](.md)| Controls the sort order of the query. | [optional] 
 **batchNumber** | **String**| Batch Number | [optional] 
 **sortBy** | [**BatchesSortBy**](.md)|  | [optional] 

### Return type

[**ListBatchesResponseBody**](ListBatchesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## processBatch

> String processBatch(batchId, processBatchRequestBody)

Process Batch ID Labels

Process Batch ID Labels

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let batchId = "batchId_example"; // String | Batch ID
let processBatchRequestBody = new ShipEngineApi.ProcessBatchRequestBody(); // ProcessBatchRequestBody | 
apiInstance.processBatch(batchId, processBatchRequestBody, (error, data, response) => {
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
 **batchId** | **String**| Batch ID | 
 **processBatchRequestBody** | [**ProcessBatchRequestBody**](ProcessBatchRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain


## removeFromBatch

> String removeFromBatch(batchId, removeFromBatchRequestBody)

Remove From Batch

Remove a shipment or rate from a batch

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let batchId = "batchId_example"; // String | Batch ID
let removeFromBatchRequestBody = new ShipEngineApi.RemoveFromBatchRequestBody(); // RemoveFromBatchRequestBody | 
apiInstance.removeFromBatch(batchId, removeFromBatchRequestBody, (error, data, response) => {
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
 **batchId** | **String**| Batch ID | 
 **removeFromBatchRequestBody** | [**RemoveFromBatchRequestBody**](RemoveFromBatchRequestBody.md)|  | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain


## updateBatch

> String updateBatch(batchId)

Update Batch By Id

Update Batch By Id

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.BatchesApi();
let batchId = "batchId_example"; // String | Batch ID
apiInstance.updateBatch(batchId, (error, data, response) => {
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
 **batchId** | **String**| Batch ID | 

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

