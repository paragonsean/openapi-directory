# BatchService.TasksApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taskAdd**](TasksApi.md#taskAdd) | **POST** /jobs/{jobId}/tasks | 
[**taskDelete**](TasksApi.md#taskDelete) | **DELETE** /jobs/{jobId}/tasks/{taskId} | 
[**taskGet**](TasksApi.md#taskGet) | **GET** /jobs/{jobId}/tasks/{taskId} | 
[**taskList**](TasksApi.md#taskList) | **GET** /jobs/{jobId}/tasks | 
[**taskListSubtasks**](TasksApi.md#taskListSubtasks) | **GET** /jobs/{jobId}/tasks/{taskId}/subtasksinfo | 
[**taskTerminate**](TasksApi.md#taskTerminate) | **POST** /jobs/{jobId}/tasks/{taskId}/terminate | 
[**taskUpdate**](TasksApi.md#taskUpdate) | **PUT** /jobs/{jobId}/tasks/{taskId} | 



## taskAdd

> taskAdd(jobId, apiVersion, taskAddParameter, opts)



Adds a task to the specified job.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The id of the job to which the task is to be added.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let taskAddParameter = new BatchService.TaskAddParameter(); // TaskAddParameter | Specifies the task to be added.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
};
apiInstance.taskAdd(jobId, apiVersion, taskAddParameter, opts, (error, data, response) => {
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
 **jobId** | **String**| The id of the job to which the task is to be added. | 
 **apiVersion** | **String**| Client API Version. | 
 **taskAddParameter** | [**TaskAddParameter**](TaskAddParameter.md)| Specifies the task to be added. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; odata=minimalmetadata
- **Accept**: application/json


## taskDelete

> taskDelete(jobId, taskId, apiVersion, opts)



Deletes a task from the specified job.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The id of the job from which to delete the task.
let taskId = "taskId_example"; // String | The id of the task to delete.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
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
 **jobId** | **String**| The id of the job from which to delete the task. | 
 **taskId** | **String**| The id of the task to delete. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
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

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The id of the job that contains the task.
let taskId = "taskId_example"; // String | The id of the task to get information about.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'select': "select_example", // String | Sets an OData $select clause.
  'expand': "expand_example", // String | Sets an OData $expand clause.
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
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
 **jobId** | **String**| The id of the job that contains the task. | 
 **taskId** | **String**| The id of the task to get information about. | 
 **apiVersion** | **String**| Client API Version. | 
 **select** | **String**| Sets an OData $select clause. | [optional] 
 **expand** | **String**| Sets an OData $expand clause. | [optional] 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
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

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The id of the job.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | Sets an OData $filter clause.
  'select': "select_example", // String | Sets an OData $select clause.
  'expand': "expand_example", // String | Sets an OData $expand clause.
  'maxresults': 56, // Number | Sets the maximum number of items to return in the response.
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
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
 **jobId** | **String**| The id of the job. | 
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| Sets an OData $filter clause. | [optional] 
 **select** | **String**| Sets an OData $select clause. | [optional] 
 **expand** | **String**| Sets an OData $expand clause. | [optional] 
 **maxresults** | **Number**| Sets the maximum number of items to return in the response. | [optional] 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
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

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The id of the job.
let taskId = "taskId_example"; // String | The id of the task.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'select': "select_example", // String | Sets an OData $select clause.
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
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
 **jobId** | **String**| The id of the job. | 
 **taskId** | **String**| The id of the task. | 
 **apiVersion** | **String**| Client API Version. | 
 **select** | **String**| Sets an OData $select clause. | [optional] 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
 **ocpDate** | **String**| The time the request was issued. If not specified, this header will be automatically populated with the current system clock time. | [optional] 

### Return type

[**CloudTaskListSubtasksResult**](CloudTaskListSubtasksResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskTerminate

> taskTerminate(jobId, taskId, apiVersion, opts)



Terminates the specified task.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.TasksApi();
let jobId = "jobId_example"; // String | The id of the job containing the task.
let taskId = "taskId_example"; // String | The id of the task to terminate.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
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
 **jobId** | **String**| The id of the job containing the task. | 
 **taskId** | **String**| The id of the task to terminate. | 
 **apiVersion** | **String**| Client API Version. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
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
let jobId = "jobId_example"; // String | The id of the job containing the task.
let taskId = "taskId_example"; // String | The id of the task to update.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let taskUpdateParameter = new BatchService.TaskUpdateParameter(); // TaskUpdateParameter | The parameters for the request.
let opts = {
  'timeout': 30, // Number | Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': true, // Boolean | Specifies if the server should return the client-request-id identifier in the response.
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
 **jobId** | **String**| The id of the job containing the task. | 
 **taskId** | **String**| The id of the task to update. | 
 **apiVersion** | **String**| Client API Version. | 
 **taskUpdateParameter** | [**TaskUpdateParameter**](TaskUpdateParameter.md)| The parameters for the request. | 
 **timeout** | **Number**| Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Specifies if the server should return the client-request-id identifier in the response. | [optional] 
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

