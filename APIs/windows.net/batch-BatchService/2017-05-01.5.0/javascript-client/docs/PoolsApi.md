# BatchService.PoolsApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**poolAdd**](PoolsApi.md#poolAdd) | **POST** /pools | Adds a pool to the specified account.
[**poolDelete**](PoolsApi.md#poolDelete) | **DELETE** /pools/{poolId} | Deletes a pool from the specified account.
[**poolDisableAutoScale**](PoolsApi.md#poolDisableAutoScale) | **POST** /pools/{poolId}/disableautoscale | Disables automatic scaling for a pool.
[**poolEnableAutoScale**](PoolsApi.md#poolEnableAutoScale) | **POST** /pools/{poolId}/enableautoscale | Enables automatic scaling for a pool.
[**poolEvaluateAutoScale**](PoolsApi.md#poolEvaluateAutoScale) | **POST** /pools/{poolId}/evaluateautoscale | Gets the result of evaluating an automatic scaling formula on the pool.
[**poolExists**](PoolsApi.md#poolExists) | **HEAD** /pools/{poolId} | 
[**poolGet**](PoolsApi.md#poolGet) | **GET** /pools/{poolId} | 
[**poolGetAllLifetimeStatistics**](PoolsApi.md#poolGetAllLifetimeStatistics) | **GET** /lifetimepoolstats | Gets lifetime summary statistics for all of the pools in the specified account.
[**poolList**](PoolsApi.md#poolList) | **GET** /pools | Lists all of the pools in the specified account.
[**poolListUsageMetrics**](PoolsApi.md#poolListUsageMetrics) | **GET** /poolusagemetrics | Lists the usage metrics, aggregated by pool across individual time intervals, for the specified account.
[**poolPatch**](PoolsApi.md#poolPatch) | **PATCH** /pools/{poolId} | Updates the properties of the specified pool.
[**poolResize**](PoolsApi.md#poolResize) | **POST** /pools/{poolId}/resize | Changes the number of compute nodes that are assigned to a pool.
[**poolStopResize**](PoolsApi.md#poolStopResize) | **POST** /pools/{poolId}/stopresize | Stops an ongoing resize operation on the pool.
[**poolUpdateProperties**](PoolsApi.md#poolUpdateProperties) | **POST** /pools/{poolId}/updateproperties | Updates the properties of the specified pool.
[**poolUpgradeOS**](PoolsApi.md#poolUpgradeOS) | **POST** /pools/{poolId}/upgradeos | Upgrades the operating system of the specified pool.



## poolAdd

> poolAdd(apiVersion, pool, opts)

Adds a pool to the specified account.

When naming pools, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let pool = new BatchService.PoolAddParameter(); // PoolAddParameter | The pool to be added.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.poolAdd(apiVersion, pool, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **pool** | [**PoolAddParameter**](PoolAddParameter.md)| The pool to be added. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## poolDelete

> poolDelete(poolId, apiVersion, opts)

Deletes a pool from the specified account.

When you request that a pool be deleted, the following actions occur: the pool state is set to deleting; any ongoing resize operation on the pool are stopped; the Batch service starts resizing the pool to zero nodes; any tasks running on existing nodes are terminated and requeued (as if a resize pool operation had been requested with the default requeue option); finally, the pool is removed from the system. Because running tasks are requeued, the user can rerun these tasks by updating their job to target a different pool. The tasks can then run on the new pool. If you want to override the requeue behavior, then you should call resize pool explicitly to shrink the pool to zero size before deleting the pool. If you call an Update, Patch or Delete API on a pool in the deleting state, it will fail with HTTP status code 409 with error code PoolBeingDeleted.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifMatch': "ifMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.poolDelete(poolId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] 
 **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolDisableAutoScale

> poolDisableAutoScale(poolId, apiVersion, opts)

Disables automatic scaling for a pool.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool on which to disable automatic scaling.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.poolDisableAutoScale(poolId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool on which to disable automatic scaling. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolEnableAutoScale

> poolEnableAutoScale(poolId, apiVersion, poolEnableAutoScaleParameter, opts)

Enables automatic scaling for a pool.

You cannot enable automatic scaling on a pool if a resize operation is in progress on the pool. If automatic scaling of the pool is currently disabled, you must specify a valid autoscale formula as part of the request. If automatic scaling of the pool is already enabled, you may specify a new autoscale formula and/or a new evaluation interval. You cannot call this API for the same pool more than once every 30 seconds.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool on which to enable automatic scaling.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let poolEnableAutoScaleParameter = new BatchService.PoolEnableAutoScaleParameter(); // PoolEnableAutoScaleParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifMatch': "ifMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.poolEnableAutoScale(poolId, apiVersion, poolEnableAutoScaleParameter, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool on which to enable automatic scaling. | 
 **apiVersion** | **String**| Client API Version. | 
 **poolEnableAutoScaleParameter** | [**PoolEnableAutoScaleParameter**](PoolEnableAutoScaleParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] 
 **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## poolEvaluateAutoScale

> AutoScaleRun poolEvaluateAutoScale(poolId, apiVersion, poolEvaluateAutoScaleParameter, opts)

Gets the result of evaluating an automatic scaling formula on the pool.

This API is primarily for validating an autoscale formula, as it simply returns the result without applying the formula to the pool.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool on which to evaluate the automatic scaling formula.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let poolEvaluateAutoScaleParameter = new BatchService.PoolEvaluateAutoScaleParameter(); // PoolEvaluateAutoScaleParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.poolEvaluateAutoScale(poolId, apiVersion, poolEvaluateAutoScaleParameter, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool on which to evaluate the automatic scaling formula. | 
 **apiVersion** | **String**| Client API Version. | 
 **poolEvaluateAutoScaleParameter** | [**PoolEvaluateAutoScaleParameter**](PoolEvaluateAutoScaleParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

[**AutoScaleRun**](AutoScaleRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## poolExists

> poolExists(poolId, apiVersion, opts)



Gets basic properties of a pool.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool to get.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifMatch': "ifMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.poolExists(poolId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool to get. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] 
 **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolGet

> CloudPool poolGet(poolId, apiVersion, opts)



Gets information about the specified pool.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool to get.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'select': "select_example", // String | An OData $select clause.
  'expand': "expand_example", // String | An OData $expand clause.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifMatch': "ifMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.poolGet(poolId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool to get. | 
 **apiVersion** | **String**| Client API Version. | 
 **select** | **String**| An OData $select clause. | [optional] 
 **expand** | **String**| An OData $expand clause. | [optional] 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] 
 **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

[**CloudPool**](CloudPool.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolGetAllLifetimeStatistics

> PoolStatistics poolGetAllLifetimeStatistics(apiVersion, opts)

Gets lifetime summary statistics for all of the pools in the specified account.

Statistics are aggregated across all pools that have ever existed in the account, from account creation to the last update time of the statistics.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.poolGetAllLifetimeStatistics(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

[**PoolStatistics**](PoolStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolList

> CloudPoolListResult poolList(apiVersion, opts)

Lists all of the pools in the specified account.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause.
  'select': "select_example", // String | An OData $select clause.
  'expand': "expand_example", // String | An OData $expand clause.
  'maxresults': 1000, // Number | The maximum number of items to return in the response. A maximum of 1000 pools can be returned.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.poolList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause. | [optional] 
 **select** | **String**| An OData $select clause. | [optional] 
 **expand** | **String**| An OData $expand clause. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. A maximum of 1000 pools can be returned. | [optional] [default to 1000]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

[**CloudPoolListResult**](CloudPoolListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolListUsageMetrics

> PoolListUsageMetricsResult poolListUsageMetrics(apiVersion, opts)

Lists the usage metrics, aggregated by pool across individual time intervals, for the specified account.

If you do not specify a $filter clause including a poolId, the response includes all pools that existed in the account in the time range of the returned aggregation intervals.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'starttime': new Date("2013-10-20T19:20:30+01:00"), // Date | The earliest time from which to include metrics. This must be at least two and a half hours before the current time. If not specified this defaults to the start time of the last aggregation interval currently available.
  'endtime': new Date("2013-10-20T19:20:30+01:00"), // Date | The latest time from which to include metrics. This must be at least two hours before the current time. If not specified this defaults to the end time of the last aggregation interval currently available.
  'filter': "filter_example", // String | An OData $filter clause. If this is not specified the response includes all pools that existed in the account in the time range of the returned aggregation intervals.
  'maxresults': 1000, // Number | The maximum number of items to return in the response. A maximum of 1000 results will be returned.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.poolListUsageMetrics(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **starttime** | **Date**| The earliest time from which to include metrics. This must be at least two and a half hours before the current time. If not specified this defaults to the start time of the last aggregation interval currently available. | [optional] 
 **endtime** | **Date**| The latest time from which to include metrics. This must be at least two hours before the current time. If not specified this defaults to the end time of the last aggregation interval currently available. | [optional] 
 **filter** | **String**| An OData $filter clause. If this is not specified the response includes all pools that existed in the account in the time range of the returned aggregation intervals. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. A maximum of 1000 results will be returned. | [optional] [default to 1000]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

[**PoolListUsageMetricsResult**](PoolListUsageMetricsResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolPatch

> poolPatch(poolId, apiVersion, poolPatchParameter, opts)

Updates the properties of the specified pool.

This only replaces the pool properties specified in the request. For example, if the pool has a start task associated with it, and a request does not specify a start task element, then the pool keeps the existing start task.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool to update.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let poolPatchParameter = new BatchService.PoolPatchParameter(); // PoolPatchParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifMatch': "ifMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.poolPatch(poolId, apiVersion, poolPatchParameter, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool to update. | 
 **apiVersion** | **String**| Client API Version. | 
 **poolPatchParameter** | [**PoolPatchParameter**](PoolPatchParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] 
 **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## poolResize

> poolResize(poolId, apiVersion, poolResizeParameter, opts)

Changes the number of compute nodes that are assigned to a pool.

You can only resize a pool when its allocation state is steady. If the pool is already resizing, the request fails with status code 409. When you resize a pool, the pool&#39;s allocation state changes from steady to resizing. You cannot resize pools which are configured for automatic scaling. If you try to do this, the Batch service returns an error 409. If you resize a pool downwards, the Batch service chooses which nodes to remove. To remove specific nodes, use the pool remove nodes API instead.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool to resize.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let poolResizeParameter = new BatchService.PoolResizeParameter(); // PoolResizeParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifMatch': "ifMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.poolResize(poolId, apiVersion, poolResizeParameter, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool to resize. | 
 **apiVersion** | **String**| Client API Version. | 
 **poolResizeParameter** | [**PoolResizeParameter**](PoolResizeParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] 
 **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## poolStopResize

> poolStopResize(poolId, apiVersion, opts)

Stops an ongoing resize operation on the pool.

This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool whose resizing you want to stop.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifMatch': "ifMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.poolStopResize(poolId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool whose resizing you want to stop. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] 
 **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## poolUpdateProperties

> poolUpdateProperties(poolId, apiVersion, poolUpdatePropertiesParameter, opts)

Updates the properties of the specified pool.

This fully replaces all the updatable properties of the pool. For example, if the pool has a start task associated with it and if start task is not specified with this request, then the Batch service will remove the existing start task.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool to update.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let poolUpdatePropertiesParameter = new BatchService.PoolUpdatePropertiesParameter(); // PoolUpdatePropertiesParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.poolUpdateProperties(poolId, apiVersion, poolUpdatePropertiesParameter, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool to update. | 
 **apiVersion** | **String**| Client API Version. | 
 **poolUpdatePropertiesParameter** | [**PoolUpdatePropertiesParameter**](PoolUpdatePropertiesParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## poolUpgradeOS

> poolUpgradeOS(poolId, apiVersion, poolUpgradeOSParameter, opts)

Upgrades the operating system of the specified pool.

During an upgrade, the Batch service upgrades each compute node in the pool. When a compute node is chosen for upgrade, any tasks running on that node are removed from the node and returned to the queue to be rerun later (or on a different compute node). The node will be unavailable until the upgrade is complete. This operation results in temporarily reduced pool capacity as nodes are taken out of service to be upgraded. Although the Batch service tries to avoid upgrading all compute nodes at the same time, it does not guarantee to do this (particularly on small pools); therefore, the pool may be temporarily unavailable to run tasks. When this operation runs, the pool state changes to upgrading. When all compute nodes have finished upgrading, the pool state returns to active.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.PoolsApi();
let poolId = "poolId_example"; // String | The ID of the pool to upgrade.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let poolUpgradeOSParameter = new BatchService.PoolUpgradeOSParameter(); // PoolUpgradeOSParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifMatch': "ifMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.poolUpgradeOS(poolId, apiVersion, poolUpgradeOSParameter, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool to upgrade. | 
 **apiVersion** | **String**| Client API Version. | 
 **poolUpgradeOSParameter** | [**PoolUpgradeOSParameter**](PoolUpgradeOSParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client. | [optional] 
 **ifNoneMatch** | **String**| An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json

