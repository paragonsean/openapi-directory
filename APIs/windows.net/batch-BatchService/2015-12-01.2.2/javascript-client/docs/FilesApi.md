# BatchService.FilesApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileDeleteFromComputeNode**](FilesApi.md#fileDeleteFromComputeNode) | **DELETE** /pools/{poolId}/nodes/{nodeId}/files/{fileName} | 
[**fileDeleteFromTask**](FilesApi.md#fileDeleteFromTask) | **DELETE** /jobs/{jobId}/tasks/{taskId}/files/{fileName} | 
[**fileGetFromComputeNode**](FilesApi.md#fileGetFromComputeNode) | **GET** /pools/{poolId}/nodes/{nodeId}/files/{fileName} | 
[**fileGetFromTask**](FilesApi.md#fileGetFromTask) | **GET** /jobs/{jobId}/tasks/{taskId}/files/{fileName} | 
[**fileGetNodeFilePropertiesFromComputeNode**](FilesApi.md#fileGetNodeFilePropertiesFromComputeNode) | **HEAD** /pools/{poolId}/nodes/{nodeId}/files/{fileName} | 
[**fileGetNodeFilePropertiesFromTask**](FilesApi.md#fileGetNodeFilePropertiesFromTask) | **HEAD** /jobs/{jobId}/tasks/{taskId}/files/{fileName} | 
[**fileListFromComputeNode**](FilesApi.md#fileListFromComputeNode) | **GET** /pools/{poolId}/nodes/{nodeId}/files | 
[**fileListFromTask**](FilesApi.md#fileListFromTask) | **GET** /jobs/{jobId}/tasks/{taskId}/files | 



## fileDeleteFromComputeNode

> fileDeleteFromComputeNode(poolId, nodeId, fileName, apiVersion, opts)



Deletes the specified task file from the compute node.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let poolId = "poolId_example"; // String | The id of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The id of the compute node from which you want to delete the file.
let fileName = "fileName_example"; // String | The path to the file that you want to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'recursive': true, // Boolean | Sets whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail.
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.fileDeleteFromComputeNode(poolId, nodeId, fileName, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The id of the pool that contains the compute node. | 
 **nodeId** | **String**| The id of the compute node from which you want to delete the file. | 
 **fileName** | **String**| The path to the file that you want to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **recursive** | **Boolean**| Sets whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail. | [optional] 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileDeleteFromTask

> fileDeleteFromTask(jobId, taskId, fileName, apiVersion, opts)



Deletes the specified task file from the compute node where the task ran.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let jobId = "jobId_example"; // String | The id of the job that contains the task.
let taskId = "taskId_example"; // String | The id of the task whose file you want to delete.
let fileName = "fileName_example"; // String | The path to the task file that you want to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'recursive': true, // Boolean | Sets whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail.
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.fileDeleteFromTask(jobId, taskId, fileName, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The id of the job that contains the task. | 
 **taskId** | **String**| The id of the task whose file you want to delete. | 
 **fileName** | **String**| The path to the task file that you want to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **recursive** | **Boolean**| Sets whether to delete children of a directory. If the fileName parameter represents a directory instead of a file, you can set Recursive to true to delete the directory and all of the files and subdirectories in it. If Recursive is false then the directory must be empty or deletion will fail. | [optional] 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileGetFromComputeNode

> File fileGetFromComputeNode(poolId, nodeId, fileName, apiVersion, opts)



Gets the content of the specified task file.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let poolId = "poolId_example"; // String | The id of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The id of the compute node that contains the file.
let fileName = "fileName_example"; // String | The path to the task file that you want to get the content of.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ocpRange': "ocpRange_example", // String | Specifies the byte range to be retrieved. The default is to retrieve the entire file.  The format is startRange-endRange.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.fileGetFromComputeNode(poolId, nodeId, fileName, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The id of the pool that contains the compute node. | 
 **nodeId** | **String**| The id of the compute node that contains the file. | 
 **fileName** | **String**| The path to the task file that you want to get the content of. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ocpRange** | **String**| Specifies the byte range to be retrieved. The default is to retrieve the entire file.  The format is startRange-endRange. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileGetFromTask

> File fileGetFromTask(jobId, taskId, fileName, apiVersion, opts)



Gets the content of the specified task file.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let jobId = "jobId_example"; // String | The id of the job that contains the task.
let taskId = "taskId_example"; // String | The id of the task whose file you want to retrieve.
let fileName = "fileName_example"; // String | The path to the task file that you want to get the content of.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ocpRange': "ocpRange_example", // String | Specifies the byte range to be retrieved. The default is to retrieve the entire file.  The format is startRange-endRange.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.fileGetFromTask(jobId, taskId, fileName, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The id of the job that contains the task. | 
 **taskId** | **String**| The id of the task whose file you want to retrieve. | 
 **fileName** | **String**| The path to the task file that you want to get the content of. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ocpRange** | **String**| Specifies the byte range to be retrieved. The default is to retrieve the entire file.  The format is startRange-endRange. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileGetNodeFilePropertiesFromComputeNode

> fileGetNodeFilePropertiesFromComputeNode(poolId, nodeId, fileName, apiVersion, opts)



Gets the properties of the specified compute node file.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let poolId = "poolId_example"; // String | The id of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The id of the compute node that contains the file.
let fileName = "fileName_example"; // String | The path to the compute node file that you want to get the properties of.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.fileGetNodeFilePropertiesFromComputeNode(poolId, nodeId, fileName, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The id of the pool that contains the compute node. | 
 **nodeId** | **String**| The id of the compute node that contains the file. | 
 **fileName** | **String**| The path to the compute node file that you want to get the properties of. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileGetNodeFilePropertiesFromTask

> fileGetNodeFilePropertiesFromTask(jobId, taskId, fileName, apiVersion, opts)



Gets the properties of the specified task file.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let jobId = "jobId_example"; // String | The id of the job that contains the task.
let taskId = "taskId_example"; // String | The id of the task whose file you want to get the properties of.
let fileName = "fileName_example"; // String | The path to the task file that you want to get the properties of.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.fileGetNodeFilePropertiesFromTask(jobId, taskId, fileName, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The id of the job that contains the task. | 
 **taskId** | **String**| The id of the task whose file you want to get the properties of. | 
 **fileName** | **String**| The path to the task file that you want to get the properties of. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileListFromComputeNode

> NodeFileListResult fileListFromComputeNode(poolId, nodeId, apiVersion, opts)



Lists all of the files in task directories on the specified compute node.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let poolId = "poolId_example"; // String | The id of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The id of the compute node whose files you want to list.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | Sets an OData $filter clause.
  'recursive': true, // Boolean | Sets whether to list children of a directory.
  'maxresults': 56, // Number | Sets the maximum number of items to return in the response.
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.fileListFromComputeNode(poolId, nodeId, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The id of the pool that contains the compute node. | 
 **nodeId** | **String**| The id of the compute node whose files you want to list. | 
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| Sets an OData $filter clause. | [optional] 
 **recursive** | **Boolean**| Sets whether to list children of a directory. | [optional] 
 **maxresults** | **Number**| Sets the maximum number of items to return in the response. | [optional] 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**NodeFileListResult**](NodeFileListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileListFromTask

> NodeFileListResult fileListFromTask(jobId, taskId, apiVersion, opts)



Lists the files in a task&#39;s directory on its compute node.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let jobId = "jobId_example"; // String | The id of the job that contains the task.
let taskId = "taskId_example"; // String | The id of the task whose files you want to list.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | Sets an OData $filter clause.
  'recursive': true, // Boolean | Sets whether to list children of a directory.
  'maxresults': 56, // Number | Sets the maximum number of items to return in the response.
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.fileListFromTask(jobId, taskId, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The id of the job that contains the task. | 
 **taskId** | **String**| The id of the task whose files you want to list. | 
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| Sets an OData $filter clause. | [optional] 
 **recursive** | **Boolean**| Sets whether to list children of a directory. | [optional] 
 **maxresults** | **Number**| Sets the maximum number of items to return in the response. | [optional] 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**NodeFileListResult**](NodeFileListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

