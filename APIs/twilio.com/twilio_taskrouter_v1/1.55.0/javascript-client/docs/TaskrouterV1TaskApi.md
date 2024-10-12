# TwilioTaskrouter.TaskrouterV1TaskApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTask**](TaskrouterV1TaskApi.md#createTask) | **POST** /v1/Workspaces/{WorkspaceSid}/Tasks | 
[**deleteTask**](TaskrouterV1TaskApi.md#deleteTask) | **DELETE** /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid} | 
[**fetchTask**](TaskrouterV1TaskApi.md#fetchTask) | **GET** /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid} | 
[**listTask**](TaskrouterV1TaskApi.md#listTask) | **GET** /v1/Workspaces/{WorkspaceSid}/Tasks | 
[**updateTask**](TaskrouterV1TaskApi.md#updateTask) | **POST** /v1/Workspaces/{WorkspaceSid}/Tasks/{Sid} | 



## createTask

> TaskrouterV1WorkspaceTask createTask(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Task belongs to.
let opts = {
  'attributes': "attributes_example", // String | A URL-encoded JSON string with the attributes of the new task. This value is passed to the Workflow's `assignment_callback_url` when the Task is assigned to a Worker. For example: `{ \\\"task_type\\\": \\\"call\\\", \\\"twilio_call_sid\\\": \\\"CAxxx\\\", \\\"customer_ticket_number\\\": \\\"12345\\\" }`.
  'priority': 56, // Number | The priority to assign the new task and override the default. When supplied, the new Task will have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647).
  'taskChannel': "taskChannel_example", // String | When MultiTasking is enabled, specify the TaskChannel by passing either its `unique_name` or `sid`. Default value is `default`.
  'timeout': 56, // Number | The amount of time in seconds the new task can live before being assigned. Can be up to a maximum of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the `task.canceled` event will fire with description `Task TTL Exceeded`.
  'virtualStartTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The virtual start time to assign the new task and override the default. When supplied, the new task will have this virtual start time. When not supplied, the new task will have the virtual start time equal to `date_created`. Value can't be in the future.
  'workflowSid': "workflowSid_example" // String | The SID of the Workflow that you would like to handle routing for the new Task. If there is only one Workflow defined for the Workspace that you are posting the new task to, this parameter is optional.
};
apiInstance.createTask(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace that the new Task belongs to. | 
 **attributes** | **String**| A URL-encoded JSON string with the attributes of the new task. This value is passed to the Workflow&#39;s &#x60;assignment_callback_url&#x60; when the Task is assigned to a Worker. For example: &#x60;{ \\\&quot;task_type\\\&quot;: \\\&quot;call\\\&quot;, \\\&quot;twilio_call_sid\\\&quot;: \\\&quot;CAxxx\\\&quot;, \\\&quot;customer_ticket_number\\\&quot;: \\\&quot;12345\\\&quot; }&#x60;. | [optional] 
 **priority** | **Number**| The priority to assign the new task and override the default. When supplied, the new Task will have this priority unless it matches a Workflow Target with a Priority set. When not supplied, the new Task will have the priority of the matching Workflow Target. Value can be 0 to 2^31^ (2,147,483,647). | [optional] 
 **taskChannel** | **String**| When MultiTasking is enabled, specify the TaskChannel by passing either its &#x60;unique_name&#x60; or &#x60;sid&#x60;. Default value is &#x60;default&#x60;. | [optional] 
 **timeout** | **Number**| The amount of time in seconds the new task can live before being assigned. Can be up to a maximum of 2 weeks (1,209,600 seconds). The default value is 24 hours (86,400 seconds). On timeout, the &#x60;task.canceled&#x60; event will fire with description &#x60;Task TTL Exceeded&#x60;. | [optional] 
 **virtualStartTime** | **Date**| The virtual start time to assign the new task and override the default. When supplied, the new task will have this virtual start time. When not supplied, the new task will have the virtual start time equal to &#x60;date_created&#x60;. Value can&#39;t be in the future. | [optional] 
 **workflowSid** | **String**| The SID of the Workflow that you would like to handle routing for the new Task. If there is only one Workflow defined for the Workspace that you are posting the new task to, this parameter is optional. | [optional] 

### Return type

[**TaskrouterV1WorkspaceTask**](TaskrouterV1WorkspaceTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteTask

> deleteTask(workspaceSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task to delete.
let sid = "sid_example"; // String | The SID of the Task resource to delete.
let opts = {
  'ifMatch': "ifMatch_example" // String | If provided, deletes this Task if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
};
apiInstance.deleteTask(workspaceSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Task to delete. | 
 **sid** | **String**| The SID of the Task resource to delete. | 
 **ifMatch** | **String**| If provided, deletes this Task if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchTask

> TaskrouterV1WorkspaceTask fetchTask(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task to fetch.
let sid = "sid_example"; // String | The SID of the Task resource to fetch.
apiInstance.fetchTask(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Task to fetch. | 
 **sid** | **String**| The SID of the Task resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceTask**](TaskrouterV1WorkspaceTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTask

> ListTaskResponse listTask(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Tasks to read.
let opts = {
  'priority': 56, // Number | The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the specified priority.
  'assignmentStatus': ["null"], // [String] | The `assignment_status` of the Tasks you want to read. Can be: `pending`, `reserved`, `assigned`, `canceled`, `wrapping`, or `completed`. Returns all Tasks in the Workspace with the specified `assignment_status`.
  'workflowSid': "workflowSid_example", // String | The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this SID.
  'workflowName': "workflowName_example", // String | The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this friendly name.
  'taskQueueSid': "taskQueueSid_example", // String | The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this SID.
  'taskQueueName': "taskQueueName_example", // String | The `friendly_name` of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this friendly name.
  'evaluateTaskAttributes': "evaluateTaskAttributes_example", // String | The attributes of the Tasks to read. Returns the Tasks that match the attributes specified in this parameter.
  'ordering': "ordering_example", // String | How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated. This value is specified as: `Attribute:Order`, where `Attribute` can be either `DateCreated`, `Priority`, or `VirtualStartTime` and `Order` can be either `asc` or `desc`. For example, `Priority:desc` returns Tasks ordered in descending order of their Priority. Pairings of sort orders can be specified in a comma-separated list such as `Priority:desc,DateCreated:asc`, which returns the Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not allowed is DateCreated and VirtualStartTime.
  'hasAddons': true, // Boolean | Whether to read Tasks with Add-ons. If `true`, returns only Tasks with Add-ons. If `false`, returns only Tasks without Add-ons.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTask(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Tasks to read. | 
 **priority** | **Number**| The priority value of the Tasks to read. Returns the list of all Tasks in the Workspace with the specified priority. | [optional] 
 **assignmentStatus** | [**[String]**](String.md)| The &#x60;assignment_status&#x60; of the Tasks you want to read. Can be: &#x60;pending&#x60;, &#x60;reserved&#x60;, &#x60;assigned&#x60;, &#x60;canceled&#x60;, &#x60;wrapping&#x60;, or &#x60;completed&#x60;. Returns all Tasks in the Workspace with the specified &#x60;assignment_status&#x60;. | [optional] 
 **workflowSid** | **String**| The SID of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this SID. | [optional] 
 **workflowName** | **String**| The friendly name of the Workflow with the Tasks to read. Returns the Tasks controlled by the Workflow identified by this friendly name. | [optional] 
 **taskQueueSid** | **String**| The SID of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this SID. | [optional] 
 **taskQueueName** | **String**| The &#x60;friendly_name&#x60; of the TaskQueue with the Tasks to read. Returns the Tasks waiting in the TaskQueue identified by this friendly name. | [optional] 
 **evaluateTaskAttributes** | **String**| The attributes of the Tasks to read. Returns the Tasks that match the attributes specified in this parameter. | [optional] 
 **ordering** | **String**| How to order the returned Task resources. By default, Tasks are sorted by ascending DateCreated. This value is specified as: &#x60;Attribute:Order&#x60;, where &#x60;Attribute&#x60; can be either &#x60;DateCreated&#x60;, &#x60;Priority&#x60;, or &#x60;VirtualStartTime&#x60; and &#x60;Order&#x60; can be either &#x60;asc&#x60; or &#x60;desc&#x60;. For example, &#x60;Priority:desc&#x60; returns Tasks ordered in descending order of their Priority. Pairings of sort orders can be specified in a comma-separated list such as &#x60;Priority:desc,DateCreated:asc&#x60;, which returns the Tasks in descending Priority order and ascending DateCreated Order. The only ordering pairing not allowed is DateCreated and VirtualStartTime. | [optional] 
 **hasAddons** | **Boolean**| Whether to read Tasks with Add-ons. If &#x60;true&#x60;, returns only Tasks with Add-ons. If &#x60;false&#x60;, returns only Tasks without Add-ons. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTaskResponse**](ListTaskResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTask

> TaskrouterV1WorkspaceTask updateTask(workspaceSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1TaskApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task to update.
let sid = "sid_example"; // String | The SID of the Task resource to update.
let opts = {
  'ifMatch': "ifMatch_example", // String | If provided, applies this mutation if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
  'assignmentStatus': "assignmentStatus_example", // TaskEnumStatus | 
  'attributes': "attributes_example", // String | The JSON string that describes the custom attributes of the task.
  'priority': 56, // Number | The Task's new priority value. When supplied, the Task takes on the specified priority unless it matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647).
  'reason': "reason_example", // String | The reason that the Task was canceled or completed. This parameter is required only if the Task is canceled or completed. Setting this value queues the task for deletion and logs the reason.
  'taskChannel': "taskChannel_example", // String | When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
  'virtualStartTime': new Date("2013-10-20T19:20:30+01:00") // Date | The task's new virtual start time value. When supplied, the Task takes on the specified virtual start time. Value can't be in the future.
};
apiInstance.updateTask(workspaceSid, sid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Task to update. | 
 **sid** | **String**| The SID of the Task resource to update. | 
 **ifMatch** | **String**| If provided, applies this mutation if (and only if) the [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) header of the Task matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] 
 **assignmentStatus** | **TaskEnumStatus**|  | [optional] 
 **attributes** | **String**| The JSON string that describes the custom attributes of the task. | [optional] 
 **priority** | **Number**| The Task&#39;s new priority value. When supplied, the Task takes on the specified priority unless it matches a Workflow Target with a Priority set. Value can be 0 to 2^31^ (2,147,483,647). | [optional] 
 **reason** | **String**| The reason that the Task was canceled or completed. This parameter is required only if the Task is canceled or completed. Setting this value queues the task for deletion and logs the reason. | [optional] 
 **taskChannel** | **String**| When MultiTasking is enabled, specify the TaskChannel with the task to update. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] 
 **virtualStartTime** | **Date**| The task&#39;s new virtual start time value. When supplied, the Task takes on the specified virtual start time. Value can&#39;t be in the future. | [optional] 

### Return type

[**TaskrouterV1WorkspaceTask**](TaskrouterV1WorkspaceTask.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

