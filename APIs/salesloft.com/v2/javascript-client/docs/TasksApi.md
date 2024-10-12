# SalesLoftPlatform.TasksApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2TasksIdJsonGet**](TasksApi.md#v2TasksIdJsonGet) | **GET** /v2/tasks/{id}.json | Fetch a task
[**v2TasksIdJsonPut**](TasksApi.md#v2TasksIdJsonPut) | **PUT** /v2/tasks/{id}.json | Update a Task
[**v2TasksJsonGet**](TasksApi.md#v2TasksJsonGet) | **GET** /v2/tasks.json | List tasks
[**v2TasksJsonPost**](TasksApi.md#v2TasksJsonPost) | **POST** /v2/tasks.json | Create a Task



## v2TasksIdJsonGet

> Step v2TasksIdJsonGet(id)

Fetch a task

Fetches a task, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.TasksApi();
let id = "id_example"; // String | Task ID
apiInstance.v2TasksIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Task ID | 

### Return type

[**Step**](Step.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2TasksIdJsonPut

> Task v2TasksIdJsonPut(id, opts)

Update a Task

Updates a task. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.TasksApi();
let id = "id_example"; // String | Task ID
let opts = {
  'currentState': "currentState_example", // String | Current state of the task, valid options are: completed
  'description': "description_example", // String | A description of the task recorded for person at completion time
  'dueDate': "dueDate_example", // String | Date of when the Task is due, ISO-8601 date format required
  'isLogged': true, // Boolean | A flag to indicate that the task should only be logged
  'remindAt': "remindAt_example", // String | Datetime of when the user will be reminded of the task, ISO-8601 datetime format required
  'subject': "subject_example" // String | Subject line of the task
};
apiInstance.v2TasksIdJsonPut(id, opts, (error, data, response) => {
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
 **id** | **String**| Task ID | 
 **currentState** | **String**| Current state of the task, valid options are: completed | [optional] 
 **description** | **String**| A description of the task recorded for person at completion time | [optional] 
 **dueDate** | **String**| Date of when the Task is due, ISO-8601 date format required | [optional] 
 **isLogged** | **Boolean**| A flag to indicate that the task should only be logged | [optional] 
 **remindAt** | **String**| Datetime of when the user will be reminded of the task, ISO-8601 datetime format required | [optional] 
 **subject** | **String**| Subject line of the task | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2TasksJsonGet

> [Task] v2TasksJsonGet(opts)

List tasks

Fetches multiple task records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.TasksApi();
let opts = {
  'ids': [null], // [Number] | IDs of tasks to fetch.
  'userId': [null], // [Number] | Filters tasks by the user to which they are assigned.
  'personId': [null], // [Number] | Filters tasks by the person to which they are associated.
  'accountId': [null], // [Number] | Filters tasks by the account to which they are associated.
  'currentState': ["null"], // [String] | Filters tasks by their current state. Valid current_states include: ['scheduled', 'completed'].
  'taskType': ["null"], // [String] | Filters tasks by their task type. Valid task_types include: ['call', 'email', 'general'].
  'timeIntervalFilter': "timeIntervalFilter_example", // String | Filters tasks by time interval. Valid time_intervals include: ['overdue', 'today', 'tomorrow', 'this_week', 'next_week'].
  'idempotencyKey': "idempotencyKey_example", // String | Filters tasks by idempotency key.
  'locale': ["null"], // [String] | Filters tasks by locale of the person to which they are associated.
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: due_date, due_at. Defaults to due_date
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to ASC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2TasksJsonGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| IDs of tasks to fetch. | [optional] 
 **userId** | [**[Number]**](Number.md)| Filters tasks by the user to which they are assigned. | [optional] 
 **personId** | [**[Number]**](Number.md)| Filters tasks by the person to which they are associated. | [optional] 
 **accountId** | [**[Number]**](Number.md)| Filters tasks by the account to which they are associated. | [optional] 
 **currentState** | [**[String]**](String.md)| Filters tasks by their current state. Valid current_states include: [&#39;scheduled&#39;, &#39;completed&#39;]. | [optional] 
 **taskType** | [**[String]**](String.md)| Filters tasks by their task type. Valid task_types include: [&#39;call&#39;, &#39;email&#39;, &#39;general&#39;]. | [optional] 
 **timeIntervalFilter** | **String**| Filters tasks by time interval. Valid time_intervals include: [&#39;overdue&#39;, &#39;today&#39;, &#39;tomorrow&#39;, &#39;this_week&#39;, &#39;next_week&#39;]. | [optional] 
 **idempotencyKey** | **String**| Filters tasks by idempotency key. | [optional] 
 **locale** | [**[String]**](String.md)| Filters tasks by locale of the person to which they are associated. | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: due_date, due_at. Defaults to due_date | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to ASC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2TasksJsonPost

> Task v2TasksJsonPost(currentState, dueDate, personId, subject, taskType, userId, opts)

Create a Task

Creates a task. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.TasksApi();
let currentState = "currentState_example"; // String | Current state of the task, valid options are: scheduled
let dueDate = "dueDate_example"; // String | Date of when the Task is due, ISO-8601 date format required
let personId = "personId_example"; // String | ID of the person to be contacted
let subject = "subject_example"; // String | Subject line of the task.
let taskType = "taskType_example"; // String | Task type, valid options are: call, email, general
let userId = 56; // Number | ID of the user linked to the task
let opts = {
  'description': "description_example", // String | A description of the task recorded for person at completion time
  'idempotencyKey': "idempotencyKey_example", // String | Establishes a unique identifier to prevent duplicates from being created
  'remindAt': "remindAt_example" // String | Datetime of when the user will be reminded of the task, ISO-8601 datetime format required
};
apiInstance.v2TasksJsonPost(currentState, dueDate, personId, subject, taskType, userId, opts, (error, data, response) => {
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
 **currentState** | **String**| Current state of the task, valid options are: scheduled | 
 **dueDate** | **String**| Date of when the Task is due, ISO-8601 date format required | 
 **personId** | **String**| ID of the person to be contacted | 
 **subject** | **String**| Subject line of the task. | 
 **taskType** | **String**| Task type, valid options are: call, email, general | 
 **userId** | **Number**| ID of the user linked to the task | 
 **description** | **String**| A description of the task recorded for person at completion time | [optional] 
 **idempotencyKey** | **String**| Establishes a unique identifier to prevent duplicates from being created | [optional] 
 **remindAt** | **String**| Datetime of when the user will be reminded of the task, ISO-8601 datetime format required | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

