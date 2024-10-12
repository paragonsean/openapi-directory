# TwilioTaskrouter.TaskrouterV1TaskQueueApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTaskQueue**](TaskrouterV1TaskQueueApi.md#createTaskQueue) | **POST** /v1/Workspaces/{WorkspaceSid}/TaskQueues | 
[**deleteTaskQueue**](TaskrouterV1TaskQueueApi.md#deleteTaskQueue) | **DELETE** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid} | 
[**fetchTaskQueue**](TaskrouterV1TaskQueueApi.md#fetchTaskQueue) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid} | 
[**listTaskQueue**](TaskrouterV1TaskQueueApi.md#listTaskQueue) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues | 
[**updateTaskQueue**](TaskrouterV1TaskQueueApi.md#updateTaskQueue) | **POST** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{Sid} | 



## createTaskQueue

> TaskrouterV1WorkspaceTaskQueue createTaskQueue(workspaceSid, friendlyName, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskQueueApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new TaskQueue belongs to.
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
let opts = {
  'assignmentActivitySid': "assignmentActivitySid_example", // String | The SID of the Activity to assign Workers when a task is assigned to them.
  'maxReservedWorkers': 56, // Number | The maximum number of Workers to reserve for the assignment of a Task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1.
  'reservationActivitySid': "reservationActivitySid_example", // String | The SID of the Activity to assign Workers when a task is reserved for them.
  'targetWorkers': "targetWorkers_example", // String | A string that describes the Worker selection criteria for any Tasks that enter the TaskQueue. For example, `'\\\"language\\\" == \\\"spanish\\\"'`. The default value is `1==1`. If this value is empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more information about Worker selection, see [Describing Worker selection criteria](https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers).
  'taskOrder': "taskOrder_example" // TaskQueueEnumTaskOrder | 
};
apiInstance.createTaskQueue(workspaceSid, friendlyName, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace that the new TaskQueue belongs to. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the TaskQueue. For example &#x60;Support-Tier 1&#x60;, &#x60;Sales&#x60;, or &#x60;Escalation&#x60;. | 
 **assignmentActivitySid** | **String**| The SID of the Activity to assign Workers when a task is assigned to them. | [optional] 
 **maxReservedWorkers** | **Number**| The maximum number of Workers to reserve for the assignment of a Task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1. | [optional] 
 **reservationActivitySid** | **String**| The SID of the Activity to assign Workers when a task is reserved for them. | [optional] 
 **targetWorkers** | **String**| A string that describes the Worker selection criteria for any Tasks that enter the TaskQueue. For example, &#x60;&#39;\\\&quot;language\\\&quot; &#x3D;&#x3D; \\\&quot;spanish\\\&quot;&#39;&#x60;. The default value is &#x60;1&#x3D;&#x3D;1&#x60;. If this value is empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more information about Worker selection, see [Describing Worker selection criteria](https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers). | [optional] 
 **taskOrder** | **TaskQueueEnumTaskOrder**|  | [optional] 

### Return type

[**TaskrouterV1WorkspaceTaskQueue**](TaskrouterV1WorkspaceTaskQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteTaskQueue

> deleteTaskQueue(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskQueueApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to delete.
let sid = "sid_example"; // String | The SID of the TaskQueue resource to delete.
apiInstance.deleteTaskQueue(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to delete. | 
 **sid** | **String**| The SID of the TaskQueue resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchTaskQueue

> TaskrouterV1WorkspaceTaskQueue fetchTaskQueue(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskQueueApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to fetch.
let sid = "sid_example"; // String | The SID of the TaskQueue resource to fetch.
apiInstance.fetchTaskQueue(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to fetch. | 
 **sid** | **String**| The SID of the TaskQueue resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceTaskQueue**](TaskrouterV1WorkspaceTaskQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTaskQueue

> ListTaskQueueResponse listTaskQueue(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskQueueApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to read.
let opts = {
  'friendlyName': "friendlyName_example", // String | The `friendly_name` of the TaskQueue resources to read.
  'evaluateWorkerAttributes': "evaluateWorkerAttributes_example", // String | The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
  'workerSid': "workerSid_example", // String | The SID of the Worker with the TaskQueue resources to read.
  'ordering': "ordering_example", // String | Sorting parameter for TaskQueues
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTaskQueue(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to read. | 
 **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the TaskQueue resources to read. | [optional] 
 **evaluateWorkerAttributes** | **String**| The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter. | [optional] 
 **workerSid** | **String**| The SID of the Worker with the TaskQueue resources to read. | [optional] 
 **ordering** | **String**| Sorting parameter for TaskQueues | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTaskQueueResponse**](ListTaskQueueResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTaskQueue

> TaskrouterV1WorkspaceTaskQueue updateTaskQueue(workspaceSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskQueueApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to update.
let sid = "sid_example"; // String | The SID of the TaskQueue resource to update.
let opts = {
  'assignmentActivitySid': "assignmentActivitySid_example", // String | The SID of the Activity to assign Workers when a task is assigned for them.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
  'maxReservedWorkers': 56, // Number | The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50.
  'reservationActivitySid': "reservationActivitySid_example", // String | The SID of the Activity to assign Workers when a task is reserved for them.
  'targetWorkers': "targetWorkers_example", // String | A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example '\\\"language\\\" == \\\"spanish\\\"' If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below.
  'taskOrder': "taskOrder_example" // TaskQueueEnumTaskOrder | 
};
apiInstance.updateTaskQueue(workspaceSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to update. | 
 **sid** | **String**| The SID of the TaskQueue resource to update. | 
 **assignmentActivitySid** | **String**| The SID of the Activity to assign Workers when a task is assigned for them. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the TaskQueue. For example &#x60;Support-Tier 1&#x60;, &#x60;Sales&#x60;, or &#x60;Escalation&#x60;. | [optional] 
 **maxReservedWorkers** | **Number**| The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50. | [optional] 
 **reservationActivitySid** | **String**| The SID of the Activity to assign Workers when a task is reserved for them. | [optional] 
 **targetWorkers** | **String**| A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example &#39;\\\&quot;language\\\&quot; &#x3D;&#x3D; \\\&quot;spanish\\\&quot;&#39; If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below. | [optional] 
 **taskOrder** | **TaskQueueEnumTaskOrder**|  | [optional] 

### Return type

[**TaskrouterV1WorkspaceTaskQueue**](TaskrouterV1WorkspaceTaskQueue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

