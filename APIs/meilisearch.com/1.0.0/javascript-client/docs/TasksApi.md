# MeilisearchV11.TasksApi

All URIs are relative to *http://localhost:7700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelTasks**](TasksApi.md#cancelTasks) | **POST** /tasks/cancel | Cancel tasks
[**deleteTasks**](TasksApi.md#deleteTasks) | **DELETE** /tasks | Delete tasks
[**getAllTasks**](TasksApi.md#getAllTasks) | **GET** /tasks | Get all tasks
[**getOneTask**](TasksApi.md#getOneTask) | **GET** /tasks/0 | Get one task



## cancelTasks

> cancelTasks(opts)

Cancel tasks

Cancel tasks

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.TasksApi();
let opts = {
  'uids': "uids_example", // String | 
  'indexUids': "books", // String | 
  'types': "documentAdditionOrUpdate", // String | 
  'statuses': "failed", // String | 
  'beforeEnqueuedAt': "beforeEnqueuedAt_example", // String | 
  'afterEnqueuedAt': "afterEnqueuedAt_example", // String | 
  'beforeStartedAt': "beforeStartedAt_example", // String | 
  'afterStartedAt': "afterStartedAt_example", // String | 
  'beforeFinishedAt': "beforeFinishedAt_example", // String | 
  'afterFinishedAt': "afterFinishedAt_example", // String | 
  'canceledBy': "canceledBy_example", // String | 
  'limit': "2", // String | 
  'from': "10" // String | 
};
apiInstance.cancelTasks(opts, (error, data, response) => {
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
 **uids** | **String**|  | [optional] 
 **indexUids** | **String**|  | [optional] 
 **types** | **String**|  | [optional] 
 **statuses** | **String**|  | [optional] 
 **beforeEnqueuedAt** | **String**|  | [optional] 
 **afterEnqueuedAt** | **String**|  | [optional] 
 **beforeStartedAt** | **String**|  | [optional] 
 **afterStartedAt** | **String**|  | [optional] 
 **beforeFinishedAt** | **String**|  | [optional] 
 **afterFinishedAt** | **String**|  | [optional] 
 **canceledBy** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 
 **from** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteTasks

> deleteTasks(opts)

Delete tasks

Delete tasks

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.TasksApi();
let opts = {
  'uids': "uids_example", // String | 
  'indexUids': "books", // String | 
  'types': "documentAdditionOrUpdate", // String | 
  'statuses': "failed", // String | 
  'beforeEnqueuedAt': "beforeEnqueuedAt_example", // String | 
  'afterEnqueuedAt': "afterEnqueuedAt_example", // String | 
  'beforeStartedAt': "beforeStartedAt_example", // String | 
  'afterStartedAt': "afterStartedAt_example", // String | 
  'beforeFinishedAt': "beforeFinishedAt_example", // String | 
  'afterFinishedAt': "afterFinishedAt_example", // String | 
  'canceledBy': "canceledBy_example", // String | 
  'limit': "2", // String | 
  'from': "10" // String | 
};
apiInstance.deleteTasks(opts, (error, data, response) => {
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
 **uids** | **String**|  | [optional] 
 **indexUids** | **String**|  | [optional] 
 **types** | **String**|  | [optional] 
 **statuses** | **String**|  | [optional] 
 **beforeEnqueuedAt** | **String**|  | [optional] 
 **afterEnqueuedAt** | **String**|  | [optional] 
 **beforeStartedAt** | **String**|  | [optional] 
 **afterStartedAt** | **String**|  | [optional] 
 **beforeFinishedAt** | **String**|  | [optional] 
 **afterFinishedAt** | **String**|  | [optional] 
 **canceledBy** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 
 **from** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllTasks

> getAllTasks(opts)

Get all tasks

Get all tasks

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.TasksApi();
let opts = {
  'uids': "3", // String | 
  'indexUids': "books", // String | 
  'types': "documentAdditionOrUpdate", // String | 
  'statuses': "failed", // String | 
  'beforeEnqueuedAt': "beforeEnqueuedAt_example", // String | 
  'afterEnqueuedAt': "afterEnqueuedAt_example", // String | 
  'beforeStartedAt': "beforeStartedAt_example", // String | 
  'afterStartedAt': "afterStartedAt_example", // String | 
  'beforeFinishedAt': "beforeFinishedAt_example", // String | 
  'afterFinishedAt': "afterFinishedAt_example", // String | 
  'canceledBy': "canceledBy_example", // String | 
  'limit': "2", // String | 
  'from': "10" // String | 
};
apiInstance.getAllTasks(opts, (error, data, response) => {
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
 **uids** | **String**|  | [optional] 
 **indexUids** | **String**|  | [optional] 
 **types** | **String**|  | [optional] 
 **statuses** | **String**|  | [optional] 
 **beforeEnqueuedAt** | **String**|  | [optional] 
 **afterEnqueuedAt** | **String**|  | [optional] 
 **beforeStartedAt** | **String**|  | [optional] 
 **afterStartedAt** | **String**|  | [optional] 
 **beforeFinishedAt** | **String**|  | [optional] 
 **afterFinishedAt** | **String**|  | [optional] 
 **canceledBy** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 
 **from** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOneTask

> getOneTask()

Get one task

Get one task

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.TasksApi();
apiInstance.getOneTask((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

