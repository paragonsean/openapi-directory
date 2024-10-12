# NooshApiApplication.TaskApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCustomTaskTypesOfWg**](TaskApi.md#getCustomTaskTypesOfWg) | **GET** /v1/workgroups/{workgroup_id}/customTaskTypes | Get custom task types of workgroup level
[**getDefaultTaskStatusList**](TaskApi.md#getDefaultTaskStatusList) | **GET** /v1/workgroups/{workgroup_id}/defaultTaskStatus | Get default task status list
[**getTaskListOfProject**](TaskApi.md#getTaskListOfProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/tasks | Get task list of project level
[**getTaskListOfWorkgroup**](TaskApi.md#getTaskListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/tasks | Get task list of workgroup level
[**getTaskOfProject**](TaskApi.md#getTaskOfProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/tasks/{task_id} | Get a sepcific task of project level
[**getTaskOfWorkgroup**](TaskApi.md#getTaskOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/tasks/{task_id} | Get a sepcific task of workgroup level
[**getTaskTypesOfWorkgroup**](TaskApi.md#getTaskTypesOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/taskTypes | Get task types of workgroup level
[**getWgTaskStatusListOfWorkgroup**](TaskApi.md#getWgTaskStatusListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/customTaskStatus | Get custom task status of workgroup level
[**postTaskForProject**](TaskApi.md#postTaskForProject) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/tasks | Create a new task
[**taskPriorityList**](TaskApi.md#taskPriorityList) | **GET** /v1/workgroups/{workgroup_id}/defaultTaskPriority | Get default task priority list



## getCustomTaskTypesOfWg

> TaskTypeListVO getCustomTaskTypesOfWg(workgroupId)

Get custom task types of workgroup level

Get custom task types of workgroup level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getCustomTaskTypesOfWg(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**TaskTypeListVO**](TaskTypeListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getDefaultTaskStatusList

> TaskStatusListVO getDefaultTaskStatusList(workgroupId)

Get default task status list

Get default task status list

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getDefaultTaskStatusList(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**TaskStatusListVO**](TaskStatusListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTaskListOfProject

> TaskListVO getTaskListOfProject(workgroupId, projectId)

Get task list of project level

Get task list of project level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getTaskListOfProject(workgroupId, projectId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**TaskListVO**](TaskListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTaskListOfWorkgroup

> TaskWorkgroupLevelListVO getTaskListOfWorkgroup(workgroupId)

Get task list of workgroup level

Get task list of workgroup level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getTaskListOfWorkgroup(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**TaskWorkgroupLevelListVO**](TaskWorkgroupLevelListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTaskOfProject

> TaskExpandVO getTaskOfProject(workgroupId, projectId, taskId)

Get a sepcific task of project level

Get a sepcific task of project level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let taskId = "taskId_example"; // String | 
apiInstance.getTaskOfProject(workgroupId, projectId, taskId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **taskId** | **String**|  | 

### Return type

[**TaskExpandVO**](TaskExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTaskOfWorkgroup

> TaskExpandWorkgroupLevelVO getTaskOfWorkgroup(workgroupId, taskId)

Get a sepcific task of workgroup level

Get a sepcific task of workgroup level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
let taskId = "taskId_example"; // String | 
apiInstance.getTaskOfWorkgroup(workgroupId, taskId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **taskId** | **String**|  | 

### Return type

[**TaskExpandWorkgroupLevelVO**](TaskExpandWorkgroupLevelVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTaskTypesOfWorkgroup

> TaskTypeListVO getTaskTypesOfWorkgroup(workgroupId)

Get task types of workgroup level

Get task types of workgroup level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getTaskTypesOfWorkgroup(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**TaskTypeListVO**](TaskTypeListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getWgTaskStatusListOfWorkgroup

> WgTaskStatusListVO getWgTaskStatusListOfWorkgroup(workgroupId)

Get custom task status of workgroup level

Get custom task status of workgroup level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getWgTaskStatusListOfWorkgroup(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**WgTaskStatusListVO**](WgTaskStatusListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postTaskForProject

> TaskCreatedVO postTaskForProject(workgroupId, projectId, opts)

Create a new task

Create a new task

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'taskPersistVO': new NooshApiApplication.TaskPersistVO() // TaskPersistVO | 
};
apiInstance.postTaskForProject(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **taskPersistVO** | [**TaskPersistVO**](TaskPersistVO.md)|  | [optional] 

### Return type

[**TaskCreatedVO**](TaskCreatedVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## taskPriorityList

> TaskPriorityListVO taskPriorityList(workgroupId)

Get default task priority list

Get default task priority list

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TaskApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.taskPriorityList(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**TaskPriorityListVO**](TaskPriorityListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

