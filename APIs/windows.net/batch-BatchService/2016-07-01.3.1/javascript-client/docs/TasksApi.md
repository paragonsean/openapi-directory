# BatchService.TasksApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taskAdd**](TasksApi.md#taskAdd) | **POST** /jobs/{jobId}/tasks | Adds a task to the specified job.
[**taskAddCollection**](TasksApi.md#taskAddCollection) | **POST** /jobs/{jobId}/addtaskcollection | Adds a collection of tasks to the specified job.
[**taskDelete**](TasksApi.md#taskDelete) | **DELETE** /jobs/{jobId}/tasks/{taskId} | Deletes a task from the specified job.
[**taskGet**](TasksApi.md#taskGet) | **GET** /jobs/{jobId}/tasks/{taskId} | Gets information about the specified task.
[**taskList**](TasksApi.md#taskList) | **GET** /jobs/{jobId}/tasks | Lists all of the tasks that are associated with the specified job.
[**taskListSubtasks**](TasksApi.md#taskListSubtasks) | **GET** /jobs/{jobId}/tasks/{taskId}/subtasksinfo | Lists all of the subtasks that are associated with the specified multi-instance task.
[**taskReactivate**](TasksApi.md#taskReactivate) | **POST** /jobs/{jobId}/tasks/{taskId}/reactivate | Reactivates the specified task.
[**taskTerminate**](TasksApi.md#taskTerminate) | **POST** /jobs/{jobId}/tasks/{taskId}/terminate | Terminates the specified task.
[**taskUpdate**](TasksApi.md#taskUpdate) | **PUT** /jobs/{jobId}/tasks/{taskId} | 



## taskAdd

> taskAdd(jobId, apiVersion, task, opts)

Adds a task to the specified job.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job to which the task is to be added.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let task = new BatchService.TaskAddParameter(); // TaskAddParameter | The task to be added.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.taskAdd(jobId, apiVersion, task, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job to which the task is to be added. | 
 **apiVersion** | **String**| Client API Version. | 
 **task** | [**TaskAddParameter**](TaskAddParameter.md)| The task to be added. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## taskAddCollection

> TaskAddCollectionResult taskAddCollection(jobId, apiVersion, taskCollection, opts)

Adds a collection of tasks to the specified job.

Note that each task must have a unique ID. The Batch service may not return the results for each task in the same order the tasks were submitted in this request. If the server times out or the connection is closed during the request, the request may have been partially or fully processed, or not at all. In such cases, the user should re-issue the request. Note that it is up to the user to correctly handle failures when re-issuing a request. For example, you should use the same task ids during a retry so that if the prior operation succeeded, the retry will not create extra tasks unexpectedly.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job to which the task collection is to be added.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let taskCollection = new BatchService.TaskAddCollectionParameter(); // TaskAddCollectionParameter | The tasks to be added.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.taskAddCollection(jobId, apiVersion, taskCollection, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job to which the task collection is to be added. | 
 **apiVersion** | **String**| Client API Version. | 
 **taskCollection** | [**TaskAddCollectionParameter**](TaskAddCollectionParameter.md)| The tasks to be added. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**TaskAddCollectionResult**](TaskAddCollectionResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## taskDelete

> taskDelete(jobId, taskId, apiVersion, opts)

Deletes a task from the specified job.

When a task is deleted, all of the files in its directory on the compute node where it ran are also deleted (regardless of the retention time). For multi-instance tasks, the delete task operation applies synchronously to the primary task; subtasks and their files are then deleted asynchronously in the background.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job from which to delete the task.
let taskId = "taskId_example"; // String | The ID of the task to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.taskDelete(jobId, taskId, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job from which to delete the task. | 
 **taskId** | **String**| The ID of the task to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskGet

> CloudTask taskGet(jobId, taskId, apiVersion, opts)

Gets information about the specified task.

For multi-instance tasks, information such as affinityId, executionInfo and nodeInfo refer to the primary task. Use the list subtasks API to retrieve information about subtasks.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job that contains the task.
let taskId = "taskId_example"; // String | The ID of the task to get information about.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'select': "select_example", // String | An OData $select clause.
  'expand': "expand_example", // String | An OData $expand clause.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.taskGet(jobId, taskId, apiVersion, opts, (error, data, response) => {
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
 **taskId** | **String**| The ID of the task to get information about. | 
 **apiVersion** | **String**| Client API Version. | 
 **select** | **String**| An OData $select clause. | [optional] 
 **expand** | **String**| An OData $expand clause. | [optional] 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

[**CloudTask**](CloudTask.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskList

> CloudTaskListResult taskList(jobId, apiVersion, opts)

Lists all of the tasks that are associated with the specified job.

For multi-instance tasks, information such as affinityId, executionInfo and nodeInfo refer to the primary task. Use the list subtasks API to retrieve information about subtasks.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause.
  'select': "select_example", // String | An OData $select clause.
  'expand': "expand_example", // String | An OData $expand clause.
  'maxresults': 1000, // Number | The maximum number of items to return in the response. A maximum of 1000 tasks can be returned.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.taskList(jobId, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job. | 
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause. | [optional] 
 **select** | **String**| An OData $select clause. | [optional] 
 **expand** | **String**| An OData $expand clause. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. A maximum of 1000 tasks can be returned. | [optional] [default to 1000]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**CloudTaskListResult**](CloudTaskListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskListSubtasks

> CloudTaskListSubtasksResult taskListSubtasks(jobId, taskId, apiVersion, opts)

Lists all of the subtasks that are associated with the specified multi-instance task.

If the task is not a multi-instance task then this returns an empty collection.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job.
let taskId = "taskId_example"; // String | The ID of the task.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'select': "select_example", // String | An OData $select clause.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.taskListSubtasks(jobId, taskId, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job. | 
 **taskId** | **String**| The ID of the task. | 
 **apiVersion** | **String**| Client API Version. | 
 **select** | **String**| An OData $select clause. | [optional] 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**CloudTaskListSubtasksResult**](CloudTaskListSubtasksResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskReactivate

> taskReactivate(jobId, taskId, apiVersion, opts)

Reactivates the specified task.

Reactivation makes a task eligible to be retried again up to its maximum retry count. The task&#39;s state is changed to active. As the task is no longer in the completed state, any previous exit code or scheduling error is no longer available after reactivation. This will fail for tasks that are not completed or that previously completed successfully (with an exit code of 0). Additionally, this will fail if the job has completed (or is terminating or deleting).

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job containing the task.
let taskId = "taskId_example"; // String | The ID of the task to reactivate.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.taskReactivate(jobId, taskId, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job containing the task. | 
 **taskId** | **String**| The ID of the task to reactivate. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskTerminate

> taskTerminate(jobId, taskId, apiVersion, opts)

Terminates the specified task.

When the task has been terminated, it moves to the completed state. For multi-instance tasks, the terminate task operation applies synchronously to the primary task; subtasks are then terminated asynchronously in the background.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job containing the task.
let taskId = "taskId_example"; // String | The ID of the task to terminate.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.taskTerminate(jobId, taskId, apiVersion, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job containing the task. | 
 **taskId** | **String**| The ID of the task to terminate. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskUpdate

> taskUpdate(jobId, taskId, apiVersion, taskUpdateParameter, opts)



Updates the properties of the specified task.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The ID of the job containing the task.
let taskId = "taskId_example"; // String | The ID of the task to update.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let taskUpdateParameter = new BatchService.TaskUpdateParameter(); // TaskUpdateParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example", // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
  'ifMatch': "ifMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag is an exact match as specified.
  'ifNoneMatch': "ifNoneMatch_example", // String | An ETag is specified. Specify this header to perform the operation only if the resource's ETag does not match the specified ETag.
  'ifModifiedSince': "ifModifiedSince_example", // String | Specify this header to perform the operation only if the resource has been modified since the specified date/time.
  'ifUnmodifiedSince': "ifUnmodifiedSince_example" // String | Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
};
apiInstance.taskUpdate(jobId, taskId, apiVersion, taskUpdateParameter, opts, (error, data, response) => {
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
 **jobId** | **String**| The ID of the job containing the task. | 
 **taskId** | **String**| The ID of the task to update. | 
 **apiVersion** | **String**| Client API Version. | 
 **taskUpdateParameter** | [**TaskUpdateParameter**](TaskUpdateParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 
 **ifMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified. | [optional] 
 **ifNoneMatch** | **String**| An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag. | [optional] 
 **ifModifiedSince** | **String**| Specify this header to perform the operation only if the resource has been modified since the specified date/time. | [optional] 
 **ifUnmodifiedSince** | **String**| Specify this header to perform the operation only if the resource has not been modified since the specified date/time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json

