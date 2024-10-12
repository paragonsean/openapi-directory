# SvixApi.BackgroundTasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBackgroundTaskApiV1BackgroundTaskTaskIdGet**](BackgroundTasksApi.md#getBackgroundTaskApiV1BackgroundTaskTaskIdGet) | **GET** /api/v1/background-task/{task_id}/ | Get Background Task
[**listBackgroundTasksApiV1BackgroundTaskGet**](BackgroundTasksApi.md#listBackgroundTasksApiV1BackgroundTaskGet) | **GET** /api/v1/background-task/ | List Background Tasks



## getBackgroundTaskApiV1BackgroundTaskTaskIdGet

> BackgroundTaskOut getBackgroundTaskApiV1BackgroundTaskTaskIdGet(taskId, opts)

Get Background Task

Get a background task by ID.

### Example

```javascript
import SvixApi from 'svix_api';

let apiInstance = new SvixApi.BackgroundTasksApi();
let taskId = "qtask_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getBackgroundTaskApiV1BackgroundTaskTaskIdGet(taskId, opts, (error, data, response) => {
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
 **taskId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**BackgroundTaskOut**](BackgroundTaskOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBackgroundTasksApiV1BackgroundTaskGet

> ListResponseBackgroundTaskOut listBackgroundTasksApiV1BackgroundTaskGet(opts)

List Background Tasks

List background tasks executed in the past 90 days.

### Example

```javascript
import SvixApi from 'svix_api';

let apiInstance = new SvixApi.BackgroundTasksApi();
let opts = {
  'iterator': "qtask_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'order': new SvixApi.Ordering(), // Ordering | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listBackgroundTasksApiV1BackgroundTaskGet(opts, (error, data, response) => {
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
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **order** | [**Ordering**](.md)|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseBackgroundTaskOut**](ListResponseBackgroundTaskOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

