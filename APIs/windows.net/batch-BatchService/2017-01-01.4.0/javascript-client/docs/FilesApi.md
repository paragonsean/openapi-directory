# BatchService.FilesApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileDeleteFromComputeNode**](FilesApi.md#fileDeleteFromComputeNode) | **DELETE** /pools/{poolId}/nodes/{nodeId}/files/{filePath} | Deletes the specified task file from the compute node.
[**fileDeleteFromTask**](FilesApi.md#fileDeleteFromTask) | **DELETE** /jobs/{jobId}/tasks/{taskId}/files/{filePath} | Deletes the specified task file from the compute node where the task ran.
[**fileGetFromComputeNode**](FilesApi.md#fileGetFromComputeNode) | **GET** /pools/{poolId}/nodes/{nodeId}/files/{filePath} | 
[**fileGetFromTask**](FilesApi.md#fileGetFromTask) | **GET** /jobs/{jobId}/tasks/{taskId}/files/{filePath} | 
[**fileGetPropertiesFromComputeNode**](FilesApi.md#fileGetPropertiesFromComputeNode) | **HEAD** /pools/{poolId}/nodes/{nodeId}/files/{filePath} | 
[**fileGetPropertiesFromTask**](FilesApi.md#fileGetPropertiesFromTask) | **HEAD** /jobs/{jobId}/tasks/{taskId}/files/{filePath} | 
[**fileListFromComputeNode**](FilesApi.md#fileListFromComputeNode) | **GET** /pools/{poolId}/nodes/{nodeId}/files | Lists all of the files in task directories on the specified compute node.
[**fileListFromTask**](FilesApi.md#fileListFromTask) | **GET** /jobs/{jobId}/tasks/{taskId}/files | Lists the files in a task&#39;s directory on its compute node.



## fileDeleteFromComputeNode

> fileDeleteFromComputeNode(poolId, nodeId, filePath, apiVersion, opts)

Deletes the specified task file from the compute node.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node from which you want to delete the file.
let filePath = "filePath_example"; // String | The path to the file that you want to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'recursive': true, // Boolean | Whether to delete children of a directory. If the filePath parameter represents a directory instead of a file, you can set recursive to true to delete the directory and all of the files and subdirectories in it. If recursive is false then the directory must be empty or deletion will fail.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.fileDeleteFromComputeNode(poolId, nodeId, filePath, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node from which you want to delete the file. | 
 **filePath** | **String**| The path to the file that you want to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **recursive** | **Boolean**| Whether to delete children of a directory. If the filePath parameter represents a directory instead of a file, you can set recursive to true to delete the directory and all of the files and subdirectories in it. If recursive is false then the directory must be empty or deletion will fail. | [optional] 
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


## fileDeleteFromTask

> fileDeleteFromTask(jobId, taskId, filePath, apiVersion, opts)

Deletes the specified task file from the compute node where the task ran.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let jobId = "jobId_example"; // String | The ID of the job that contains the task.
let taskId = "taskId_example"; // String | The ID of the task whose file you want to delete.
let filePath = "filePath_example"; // String | The path to the task file that you want to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'recursive': true, // Boolean | Whether to delete children of a directory. If the filePath parameter represents a directory instead of a file, you can set recursive to true to delete the directory and all of the files and subdirectories in it. If recursive is false then the directory must be empty or deletion will fail.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.fileDeleteFromTask(jobId, taskId, filePath, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job that contains the task. | 
 **taskId** | **String**| The ID of the task whose file you want to delete. | 
 **filePath** | **String**| The path to the task file that you want to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **recursive** | **Boolean**| Whether to delete children of a directory. If the filePath parameter represents a directory instead of a file, you can set recursive to true to delete the directory and all of the files and subdirectories in it. If recursive is false then the directory must be empty or deletion will fail. | [optional] 
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


## fileGetFromComputeNode

> File fileGetFromComputeNode(poolId, nodeId, filePath, apiVersion, opts)



Returns the content of the specified compute node file.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node that contains the file.
let filePath = "filePath_example"; // String | The path to the compute node file that you want to get the content of.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ocpRange': "ocpRange_example", // String | The byte range to be retrieved. The default is to retrieve the entire file. The format is bytes=startRange-endRange.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.fileGetFromComputeNode(poolId, nodeId, filePath, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node that contains the file. | 
 **filePath** | **String**| The path to the compute node file that you want to get the content of. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ocpRange** | **String**| The byte range to be retrieved. The default is to retrieve the entire file. The format is bytes&#x3D;startRange-endRange. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileGetFromTask

> File fileGetFromTask(jobId, taskId, filePath, apiVersion, opts)



Returns the content of the specified task file.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let jobId = "jobId_example"; // String | The ID of the job that contains the task.
let taskId = "taskId_example"; // String | The ID of the task whose file you want to retrieve.
let filePath = "filePath_example"; // String | The path to the task file that you want to get the content of.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ocpRange': "ocpRange_example", // String | The byte range to be retrieved. The default is to retrieve the entire file. The format is bytes=startRange-endRange.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.fileGetFromTask(jobId, taskId, filePath, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job that contains the task. | 
 **taskId** | **String**| The ID of the task whose file you want to retrieve. | 
 **filePath** | **String**| The path to the task file that you want to get the content of. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ocpRange** | **String**| The byte range to be retrieved. The default is to retrieve the entire file. The format is bytes&#x3D;startRange-endRange. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileGetPropertiesFromComputeNode

> fileGetPropertiesFromComputeNode(poolId, nodeId, filePath, apiVersion, opts)



Gets the properties of the specified compute node file.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node that contains the file.
let filePath = "filePath_example"; // String | The path to the compute node file that you want to get the properties of.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.fileGetPropertiesFromComputeNode(poolId, nodeId, filePath, apiVersion, opts, (error, data, response) => {
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node that contains the file. | 
 **filePath** | **String**| The path to the compute node file that you want to get the properties of. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileGetPropertiesFromTask

> fileGetPropertiesFromTask(jobId, taskId, filePath, apiVersion, opts)



Gets the properties of the specified task file.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.FilesApi();
let jobId = "jobId_example"; // String | The ID of the job that contains the task.
let taskId = "taskId_example"; // String | The ID of the task whose file you want to get the properties of.
let filePath = "filePath_example"; // String | The path to the task file that you want to get the properties of.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
  'ifModifiedSince': "ifModifiedSince_example", // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
};
apiInstance.fileGetPropertiesFromTask(jobId, taskId, filePath, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job that contains the task. | 
 **taskId** | **String**| The ID of the task whose file you want to get the properties of. | 
 **filePath** | **String**| The path to the task file that you want to get the properties of. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 
 **ifModifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. | [optional] 
 **ifUnmodifiedSince** | **String**| A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. | [optional] 

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
let poolId = "poolId_example"; // String | The ID of the pool that contains the compute node.
let nodeId = "nodeId_example"; // String | The ID of the compute node whose files you want to list.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause.
  'recursive': true, // Boolean | Whether to list children of a directory.
  'maxresults': 1000, // Number | The maximum number of items to return in the response. A maximum of 1000 files can be returned.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
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
 **poolId** | **String**| The ID of the pool that contains the compute node. | 
 **nodeId** | **String**| The ID of the compute node whose files you want to list. | 
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause. | [optional] 
 **recursive** | **Boolean**| Whether to list children of a directory. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. A maximum of 1000 files can be returned. | [optional] [default to 1000]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

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
let jobId = "jobId_example"; // String | The ID of the job that contains the task.
let taskId = "taskId_example"; // String | The ID of the task whose files you want to list.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause.
  'recursive': true, // Boolean | Whether to list children of a directory. This parameter can be used in combination with the filter parameter to list specific type of files.
  'maxresults': 1000, // Number | The maximum number of items to return in the response. A maximum of 1000 files can be returned.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
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
 **jobId** | **String**| The ID of the job that contains the task. | 
 **taskId** | **String**| The ID of the task whose files you want to list. | 
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause. | [optional] 
 **recursive** | **Boolean**| Whether to list children of a directory. This parameter can be used in combination with the filter parameter to list specific type of files. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. A maximum of 1000 files can be returned. | [optional] [default to 1000]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

[**NodeFileListResult**](NodeFileListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

