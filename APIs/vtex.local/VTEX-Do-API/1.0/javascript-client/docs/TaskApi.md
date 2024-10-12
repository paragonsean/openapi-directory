# VtexDoApi.TaskApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addComment**](TaskApi.md#addComment) | **POST** /tasks/{taskId}/comments | Add Comment on a Task
[**editTask**](TaskApi.md#editTask) | **PUT** /tasks/{taskId} | Update Task
[**getTask**](TaskApi.md#getTask) | **GET** /tasks/{taskId} | Retrieve Task
[**listtasksbyassignee**](TaskApi.md#listtasksbyassignee) | **GET** /tasks | List tasks
[**newTask**](TaskApi.md#newTask) | **POST** /tasks | Create Task



## addComment

> Object addComment(accept, contentType, taskId, addCommentRequest)

Add Comment on a Task

Adds a comment to a given task, filtering by &#x60;taskId&#x60;.

### Example

```javascript
import VtexDoApi from 'vtex_do_api';
let defaultClient = VtexDoApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new VtexDoApi.TaskApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Type of the content being sent.
let taskId = "123456abc"; // String | Task ID.
let addCommentRequest = {"text":"write your comment here"}; // AddCommentRequest | 
apiInstance.addComment(accept, contentType, taskId, addCommentRequest, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Type of the content being sent. | 
 **taskId** | **String**| Task ID. | 
 **addCommentRequest** | [**AddCommentRequest**](AddCommentRequest.md)|  | 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## editTask

> Object editTask(accept, contentType, taskId, editTaskRequest)

Update Task

Updates a given task&#39;s status, for example, filtering by &#x60;taskId&#x60;.

### Example

```javascript
import VtexDoApi from 'vtex_do_api';
let defaultClient = VtexDoApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new VtexDoApi.TaskApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Type of the content being sent.
let taskId = "123456abc"; // String | Task ID.
let editTaskRequest = {"status":"InProgress"}; // EditTaskRequest | 
apiInstance.editTask(accept, contentType, taskId, editTaskRequest, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Type of the content being sent. | 
 **taskId** | **String**| Task ID. | 
 **editTaskRequest** | [**EditTaskRequest**](EditTaskRequest.md)|  | 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTask

> Object getTask(accept, contentType, taskId)

Retrieve Task

Retrieves a given task, filtering by &#x60;taskId&#x60;.

### Example

```javascript
import VtexDoApi from 'vtex_do_api';
let defaultClient = VtexDoApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new VtexDoApi.TaskApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Type of the content being sent.
let taskId = "123456abc"; // String | Task ID.
apiInstance.getTask(accept, contentType, taskId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Type of the content being sent. | 
 **taskId** | **String**| Task ID. | 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listtasksbyassignee

> Object listtasksbyassignee(accept, contentType, opts)

List tasks

This endpoint allows you to filter tasks. You can choose between the following filtering options:     - **Assignees:** using &#x60;assignee.email&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?assignee.email&#x3D;{{person@email.com}}&amp;status&#x3D;{{open}}&#x60;.     - **Targets:** using &#x60;targetId&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?target.id&#x3D;{{name}}&amp;status&#x3D;{{open}}&#x60;.     - **Paged tasks:** using &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?page&#x3D;{{1}}&amp;perPage&#x3D;{{10}}&amp;status&#x3D;;{{-Closed}}&#x60;.     - **Context:** using &#x60;context&#x60;, &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;. Example: &#x60;https://{{accountName}}.{{environment}}.com.br/api/do/tasks?context&#x3D;{{context}}&amp;page&#x3D;{{1}}&amp;perPage&#x3D;{{10}}&amp;status&#x3D;{{-Closed}}&#x60;.

### Example

```javascript
import VtexDoApi from 'vtex_do_api';
let defaultClient = VtexDoApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new VtexDoApi.TaskApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Type of the content being sent.
let opts = {
  'assigneeEmail': "{{assigneeEmail}}", // String | If you wish to list tasks by assignee, insert the desired assignee's email and status.
  'targetId': "{{targetId}}", // String | If you wish to list tasks by target, insert the desired `targetId` and `status`.
  'context': "{{context}}", // String | If you wish to list tasks by context, insert the desired context, `page`, `perPage` and `status`.
  'page': "{{page}}", // String | If you wish to list tasks by context, also insert the desired `page`.
  'perPage': "{{desired number per page}}", // String | If you wish to list tasks by context, also insert the desired `perPage` value.
  'status': "open" // String | If you wish to list tasks by context, also insert the desired `status`.
};
apiInstance.listtasksbyassignee(accept, contentType, opts, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Type of the content being sent. | 
 **assigneeEmail** | **String**| If you wish to list tasks by assignee, insert the desired assignee&#39;s email and status. | [optional] 
 **targetId** | **String**| If you wish to list tasks by target, insert the desired &#x60;targetId&#x60; and &#x60;status&#x60;. | [optional] 
 **context** | **String**| If you wish to list tasks by context, insert the desired context, &#x60;page&#x60;, &#x60;perPage&#x60; and &#x60;status&#x60;. | [optional] 
 **page** | **String**| If you wish to list tasks by context, also insert the desired &#x60;page&#x60;. | [optional] 
 **perPage** | **String**| If you wish to list tasks by context, also insert the desired &#x60;perPage&#x60; value. | [optional] 
 **status** | **String**| If you wish to list tasks by context, also insert the desired &#x60;status&#x60;. | [optional] 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## newTask

> Object newTask(contentType, accept, newTaskRequest)

Create Task

Creates a new task in VTEX DO.

### Example

```javascript
import VtexDoApi from 'vtex_do_api';
let defaultClient = VtexDoApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new VtexDoApi.TaskApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let newTaskRequest = {"assignee":{"email":"frederico.santos@vtex.com.br","id":null,"name":null},"context":"Marketplace","description":"Ajudar na doc API para lancar no postman","domain":"oms","dueDate":"2016-03-01","followers":[{"email":"alan.dantas@vtex.com.br","id":null,"name":null}],"name":"pricing","parentTaskId":null,"priority":"Critical","surrogateKey":"505224-0","target":[{"id":"633730670642-01","type":"order","url":"https://recorrenciaqa.vtexcommercebeta.com.br/admin/checkout/orders/633730670642-01"}]}; // NewTaskRequest | 
apiInstance.newTask(contentType, accept, newTaskRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **newTaskRequest** | [**NewTaskRequest**](NewTaskRequest.md)|  | 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

