# InfluxOssApiService.TasksApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteTasksID**](TasksApi.md#deleteTasksID) | **DELETE** /tasks/{taskID} | Delete a task
[**deleteTasksIDLabelsID**](TasksApi.md#deleteTasksIDLabelsID) | **DELETE** /tasks/{taskID}/labels/{labelID} | Delete a label from a task
[**deleteTasksIDMembersID**](TasksApi.md#deleteTasksIDMembersID) | **DELETE** /tasks/{taskID}/members/{userID} | Remove a member from a task
[**deleteTasksIDOwnersID**](TasksApi.md#deleteTasksIDOwnersID) | **DELETE** /tasks/{taskID}/owners/{userID} | Remove an owner from a task
[**deleteTasksIDRunsID**](TasksApi.md#deleteTasksIDRunsID) | **DELETE** /tasks/{taskID}/runs/{runID} | Cancel a running task
[**getTasks**](TasksApi.md#getTasks) | **GET** /tasks | List all tasks
[**getTasksID**](TasksApi.md#getTasksID) | **GET** /tasks/{taskID} | Retrieve a task
[**getTasksIDLabels**](TasksApi.md#getTasksIDLabels) | **GET** /tasks/{taskID}/labels | List all labels for a task
[**getTasksIDLogs**](TasksApi.md#getTasksIDLogs) | **GET** /tasks/{taskID}/logs | Retrieve all logs for a task
[**getTasksIDMembers**](TasksApi.md#getTasksIDMembers) | **GET** /tasks/{taskID}/members | List all task members
[**getTasksIDOwners**](TasksApi.md#getTasksIDOwners) | **GET** /tasks/{taskID}/owners | List all owners of a task
[**getTasksIDRuns**](TasksApi.md#getTasksIDRuns) | **GET** /tasks/{taskID}/runs | List runs for a task
[**getTasksIDRunsID**](TasksApi.md#getTasksIDRunsID) | **GET** /tasks/{taskID}/runs/{runID} | Retrieve a single run for a task
[**getTasksIDRunsIDLogs**](TasksApi.md#getTasksIDRunsIDLogs) | **GET** /tasks/{taskID}/runs/{runID}/logs | Retrieve all logs for a run
[**patchTasksID**](TasksApi.md#patchTasksID) | **PATCH** /tasks/{taskID} | Update a task
[**postTasks**](TasksApi.md#postTasks) | **POST** /tasks | Create a new task
[**postTasksIDLabels**](TasksApi.md#postTasksIDLabels) | **POST** /tasks/{taskID}/labels | Add a label to a task
[**postTasksIDMembers**](TasksApi.md#postTasksIDMembers) | **POST** /tasks/{taskID}/members | Add a member to a task
[**postTasksIDOwners**](TasksApi.md#postTasksIDOwners) | **POST** /tasks/{taskID}/owners | Add an owner to a task
[**postTasksIDRuns**](TasksApi.md#postTasksIDRuns) | **POST** /tasks/{taskID}/runs | Manually start a task run, overriding the current schedule
[**postTasksIDRunsIDRetry**](TasksApi.md#postTasksIDRunsIDRetry) | **POST** /tasks/{taskID}/runs/{runID}/retry | Retry a task run



## deleteTasksID

> deleteTasksID(taskID, opts)

Delete a task

Deletes a task and all associated records

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The ID of the task to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTasksID(taskID, opts, (error, data, response) => {
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
 **taskID** | **String**| The ID of the task to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTasksIDLabelsID

> deleteTasksIDLabelsID(taskID, labelID, opts)

Delete a label from a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let labelID = "labelID_example"; // String | The label ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTasksIDLabelsID(taskID, labelID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **labelID** | **String**| The label ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTasksIDMembersID

> deleteTasksIDMembersID(userID, taskID, opts)

Remove a member from a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let userID = "userID_example"; // String | The ID of the member to remove.
let taskID = "taskID_example"; // String | The task ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTasksIDMembersID(userID, taskID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the member to remove. | 
 **taskID** | **String**| The task ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTasksIDOwnersID

> deleteTasksIDOwnersID(userID, taskID, opts)

Remove an owner from a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let userID = "userID_example"; // String | The ID of the owner to remove.
let taskID = "taskID_example"; // String | The task ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTasksIDOwnersID(userID, taskID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the owner to remove. | 
 **taskID** | **String**| The task ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTasksIDRunsID

> deleteTasksIDRunsID(taskID, runID, opts)

Cancel a running task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let runID = "runID_example"; // String | The run ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTasksIDRunsID(taskID, runID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **runID** | **String**| The run ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasks

> Tasks getTasks(opts)

List all tasks

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'name': "name_example", // String | Returns task with a specific name.
  'after': "after_example", // String | Return tasks after a specified ID.
  'user': "user_example", // String | Filter tasks to a specific user ID.
  'org': "org_example", // String | Filter tasks to a specific organization name.
  'orgID': "orgID_example", // String | Filter tasks to a specific organization ID.
  'status': "status_example", // String | Filter tasks by a status--\"inactive\" or \"active\".
  'limit': 100 // Number | The number of tasks to return
};
apiInstance.getTasks(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **name** | **String**| Returns task with a specific name. | [optional] 
 **after** | **String**| Return tasks after a specified ID. | [optional] 
 **user** | **String**| Filter tasks to a specific user ID. | [optional] 
 **org** | **String**| Filter tasks to a specific organization name. | [optional] 
 **orgID** | **String**| Filter tasks to a specific organization ID. | [optional] 
 **status** | **String**| Filter tasks by a status--\&quot;inactive\&quot; or \&quot;active\&quot;. | [optional] 
 **limit** | **Number**| The number of tasks to return | [optional] [default to 100]

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasksID

> Task getTasksID(taskID, opts)

Retrieve a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTasksID(taskID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasksIDLabels

> LabelsResponse getTasksIDLabels(taskID, opts)

List all labels for a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTasksIDLabels(taskID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasksIDLogs

> Logs getTasksIDLogs(taskID, opts)

Retrieve all logs for a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTasksIDLogs(taskID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Logs**](Logs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasksIDMembers

> ResourceMembers getTasksIDMembers(taskID, opts)

List all task members

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTasksIDMembers(taskID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasksIDOwners

> ResourceOwners getTasksIDOwners(taskID, opts)

List all owners of a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTasksIDOwners(taskID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasksIDRuns

> Runs getTasksIDRuns(taskID, opts)

List runs for a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The ID of the task to get runs for.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'after': "after_example", // String | Returns runs after a specific ID.
  'limit': 100, // Number | The number of runs to return
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter runs to those scheduled after this time, RFC3339
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter runs to those scheduled before this time, RFC3339
};
apiInstance.getTasksIDRuns(taskID, opts, (error, data, response) => {
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
 **taskID** | **String**| The ID of the task to get runs for. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **after** | **String**| Returns runs after a specific ID. | [optional] 
 **limit** | **Number**| The number of runs to return | [optional] [default to 100]
 **afterTime** | **Date**| Filter runs to those scheduled after this time, RFC3339 | [optional] 
 **beforeTime** | **Date**| Filter runs to those scheduled before this time, RFC3339 | [optional] 

### Return type

[**Runs**](Runs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasksIDRunsID

> Run getTasksIDRunsID(taskID, runID, opts)

Retrieve a single run for a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let runID = "runID_example"; // String | The run ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTasksIDRunsID(taskID, runID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **runID** | **String**| The run ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasksIDRunsIDLogs

> Logs getTasksIDRunsIDLogs(taskID, runID, opts)

Retrieve all logs for a run

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | ID of task to get logs for.
let runID = "runID_example"; // String | ID of run to get logs for.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTasksIDRunsIDLogs(taskID, runID, opts, (error, data, response) => {
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
 **taskID** | **String**| ID of task to get logs for. | 
 **runID** | **String**| ID of run to get logs for. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Logs**](Logs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchTasksID

> Task patchTasksID(taskID, taskUpdateRequest, opts)

Update a task

Update a task. This will cancel all queued runs.

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let taskUpdateRequest = new InfluxOssApiService.TaskUpdateRequest(); // TaskUpdateRequest | Task update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchTasksID(taskID, taskUpdateRequest, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **taskUpdateRequest** | [**TaskUpdateRequest**](TaskUpdateRequest.md)| Task update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTasks

> Task postTasks(taskCreateRequest, opts)

Create a new task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskCreateRequest = new InfluxOssApiService.TaskCreateRequest(); // TaskCreateRequest | Task to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postTasks(taskCreateRequest, opts, (error, data, response) => {
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
 **taskCreateRequest** | [**TaskCreateRequest**](TaskCreateRequest.md)| Task to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTasksIDLabels

> LabelResponse postTasksIDLabels(taskID, labelMapping, opts)

Add a label to a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postTasksIDLabels(taskID, labelMapping, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTasksIDMembers

> ResourceMember postTasksIDMembers(taskID, addResourceMemberRequestBody, opts)

Add a member to a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postTasksIDMembers(taskID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTasksIDOwners

> ResourceOwner postTasksIDOwners(taskID, addResourceMemberRequestBody, opts)

Add an owner to a task

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postTasksIDOwners(taskID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTasksIDRuns

> Run postTasksIDRuns(taskID, opts)

Manually start a task run, overriding the current schedule

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | 
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'runManually': new InfluxOssApiService.RunManually() // RunManually | 
};
apiInstance.postTasksIDRuns(taskID, opts, (error, data, response) => {
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
 **taskID** | **String**|  | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **runManually** | [**RunManually**](RunManually.md)|  | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTasksIDRunsIDRetry

> Run postTasksIDRunsIDRetry(taskID, runID, opts)

Retry a task run

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TasksApi();
let taskID = "taskID_example"; // String | The task ID.
let runID = "runID_example"; // String | The run ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'body': {key: null} // Object | 
};
apiInstance.postTasksIDRunsIDRetry(taskID, runID, opts, (error, data, response) => {
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
 **taskID** | **String**| The task ID. | 
 **runID** | **String**| The run ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**Run**](Run.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: application/json

