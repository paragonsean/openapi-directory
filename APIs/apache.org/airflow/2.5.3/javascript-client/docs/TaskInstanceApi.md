# AirflowApiStable.TaskInstanceApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExtraLinks**](TaskInstanceApi.md#getExtraLinks) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links | List extra links
[**getLog**](TaskInstanceApi.md#getLog) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number} | Get logs
[**getMappedTaskInstance**](TaskInstanceApi.md#getMappedTaskInstance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Get a mapped task instance
[**getMappedTaskInstances**](TaskInstanceApi.md#getMappedTaskInstances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped | List mapped task instances
[**getTaskInstance**](TaskInstanceApi.md#getTaskInstance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Get a task instance
[**getTaskInstances**](TaskInstanceApi.md#getTaskInstances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances | List task instances
[**getTaskInstancesBatch**](TaskInstanceApi.md#getTaskInstancesBatch) | **POST** /dags/~/dagRuns/~/taskInstances/list | List task instances (batch)
[**patchMappedTaskInstance**](TaskInstanceApi.md#patchMappedTaskInstance) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index} | Updates the state of a mapped task instance
[**patchTaskInstance**](TaskInstanceApi.md#patchTaskInstance) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Updates the state of a task instance
[**setMappedTaskInstanceNote**](TaskInstanceApi.md#setMappedTaskInstanceNote) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/setNote | Update the TaskInstance note.
[**setTaskInstanceNote**](TaskInstanceApi.md#setTaskInstanceNote) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/setNote | Update the TaskInstance note.



## getExtraLinks

> ExtraLinkCollection getExtraLinks(dagId, dagRunId, taskId)

List extra links

List extra links for task instance. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
apiInstance.getExtraLinks(dagId, dagRunId, taskId, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 

### Return type

[**ExtraLinkCollection**](ExtraLinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLog

> GetLog200Response getLog(dagId, dagRunId, taskId, taskTryNumber, opts)

Get logs

Get logs for a specific task instance and its try number.

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
let taskTryNumber = 56; // Number | The task try number.
let opts = {
  'fullContent': true, // Boolean | A full content will be returned. By default, only the first fragment will be returned. 
  'mapIndex': 56, // Number | Filter on map index for mapped task.
  'token': "token_example" // String | A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued. 
};
apiInstance.getLog(dagId, dagRunId, taskId, taskTryNumber, opts, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 
 **taskTryNumber** | **Number**| The task try number. | 
 **fullContent** | **Boolean**| A full content will be returned. By default, only the first fragment will be returned.  | [optional] 
 **mapIndex** | **Number**| Filter on map index for mapped task. | [optional] 
 **token** | **String**| A token that allows you to continue fetching logs. If passed, it will specify the location from which the download should be continued.  | [optional] 

### Return type

[**GetLog200Response**](GetLog200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## getMappedTaskInstance

> TaskInstance getMappedTaskInstance(dagId, dagRunId, taskId, mapIndex)

Get a mapped task instance

Get details of a mapped task instance.  *New in version 2.3.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
let mapIndex = 56; // Number | The map index.
apiInstance.getMappedTaskInstance(dagId, dagRunId, taskId, mapIndex, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 
 **mapIndex** | **Number**| The map index. | 

### Return type

[**TaskInstance**](TaskInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMappedTaskInstances

> TaskInstanceCollection getMappedTaskInstances(dagId, dagRunId, taskId, opts)

List mapped task instances

Get details of all mapped task instances.  *New in version 2.3.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'executionDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
  'executionDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
  'startDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
  'startDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
  'endDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
  'endDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
  'durationGte': 3.4, // Number | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period. 
  'durationLte': 3.4, // Number | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range. 
  'state': ["null"], // [String] | The value can be repeated to retrieve multiple matching values (OR condition).
  'pool': ["null"], // [String] | The value can be repeated to retrieve multiple matching values (OR condition).
  'queue': ["null"], // [String] | The value can be repeated to retrieve multiple matching values (OR condition).
  'orderBy': "orderBy_example" // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
};
apiInstance.getMappedTaskInstances(dagId, dagRunId, taskId, opts, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 
 **executionDateGte** | **Date**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
 **executionDateLte** | **Date**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
 **startDateGte** | **Date**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **startDateLte** | **Date**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **endDateGte** | **Date**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **endDateLte** | **Date**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **durationGte** | **Number**| Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional] 
 **durationLte** | **Number**| Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional] 
 **state** | [**[String]**](String.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **pool** | [**[String]**](String.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **queue** | [**[String]**](String.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **orderBy** | **String**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**TaskInstanceCollection**](TaskInstanceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaskInstance

> TaskInstance getTaskInstance(dagId, dagRunId, taskId)

Get a task instance

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
apiInstance.getTaskInstance(dagId, dagRunId, taskId, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 

### Return type

[**TaskInstance**](TaskInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaskInstances

> TaskInstanceCollection getTaskInstances(dagId, dagRunId, opts)

List task instances

This endpoint allows specifying &#x60;~&#x60; as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and DAG runs. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let opts = {
  'executionDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
  'executionDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
  'startDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
  'startDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
  'endDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
  'endDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
  'durationGte': 3.4, // Number | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period. 
  'durationLte': 3.4, // Number | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range. 
  'state': ["null"], // [String] | The value can be repeated to retrieve multiple matching values (OR condition).
  'pool': ["null"], // [String] | The value can be repeated to retrieve multiple matching values (OR condition).
  'queue': ["null"], // [String] | The value can be repeated to retrieve multiple matching values (OR condition).
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56 // Number | The number of items to skip before starting to collect the result set.
};
apiInstance.getTaskInstances(dagId, dagRunId, opts, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **executionDateGte** | **Date**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
 **executionDateLte** | **Date**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
 **startDateGte** | **Date**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **startDateLte** | **Date**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **endDateGte** | **Date**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **endDateLte** | **Date**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **durationGte** | **Number**| Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional] 
 **durationLte** | **Number**| Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional] 
 **state** | [**[String]**](String.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **pool** | [**[String]**](String.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **queue** | [**[String]**](String.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 

### Return type

[**TaskInstanceCollection**](TaskInstanceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaskInstancesBatch

> TaskInstanceCollection getTaskInstancesBatch(listTaskInstanceForm)

List task instances (batch)

List task instances from all DAGs and DAG runs. This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limits. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let listTaskInstanceForm = new AirflowApiStable.ListTaskInstanceForm(); // ListTaskInstanceForm | 
apiInstance.getTaskInstancesBatch(listTaskInstanceForm, (error, data, response) => {
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
 **listTaskInstanceForm** | [**ListTaskInstanceForm**](ListTaskInstanceForm.md)|  | 

### Return type

[**TaskInstanceCollection**](TaskInstanceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchMappedTaskInstance

> TaskInstanceReference patchMappedTaskInstance(dagId, dagRunId, taskId, mapIndex, opts)

Updates the state of a mapped task instance

Updates the state for single mapped task instance. *New in version 2.5.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
let mapIndex = 56; // Number | The map index.
let opts = {
  'updateTaskInstance': new AirflowApiStable.UpdateTaskInstance() // UpdateTaskInstance | Parameters of action
};
apiInstance.patchMappedTaskInstance(dagId, dagRunId, taskId, mapIndex, opts, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 
 **mapIndex** | **Number**| The map index. | 
 **updateTaskInstance** | [**UpdateTaskInstance**](UpdateTaskInstance.md)| Parameters of action | [optional] 

### Return type

[**TaskInstanceReference**](TaskInstanceReference.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchTaskInstance

> TaskInstanceReference patchTaskInstance(dagId, dagRunId, taskId, updateTaskInstance)

Updates the state of a task instance

Updates the state for single task instance. *New in version 2.5.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
let updateTaskInstance = new AirflowApiStable.UpdateTaskInstance(); // UpdateTaskInstance | Parameters of action
apiInstance.patchTaskInstance(dagId, dagRunId, taskId, updateTaskInstance, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 
 **updateTaskInstance** | [**UpdateTaskInstance**](UpdateTaskInstance.md)| Parameters of action | 

### Return type

[**TaskInstanceReference**](TaskInstanceReference.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setMappedTaskInstanceNote

> TaskInstance setMappedTaskInstanceNote(dagId, dagRunId, taskId, mapIndex, setTaskInstanceNote)

Update the TaskInstance note.

Update the manual user note of a mapped Task Instance.  *New in version 2.5.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
let mapIndex = 56; // Number | The map index.
let setTaskInstanceNote = new AirflowApiStable.SetTaskInstanceNote(); // SetTaskInstanceNote | Parameters of set Task Instance note.
apiInstance.setMappedTaskInstanceNote(dagId, dagRunId, taskId, mapIndex, setTaskInstanceNote, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 
 **mapIndex** | **Number**| The map index. | 
 **setTaskInstanceNote** | [**SetTaskInstanceNote**](SetTaskInstanceNote.md)| Parameters of set Task Instance note. | 

### Return type

[**TaskInstance**](TaskInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setTaskInstanceNote

> TaskInstance setTaskInstanceNote(dagId, dagRunId, taskId, setTaskInstanceNote)

Update the TaskInstance note.

Update the manual user note of a non-mapped Task Instance.  *New in version 2.5.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.TaskInstanceApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let taskId = "taskId_example"; // String | The task ID.
let setTaskInstanceNote = new AirflowApiStable.SetTaskInstanceNote(); // SetTaskInstanceNote | Parameters of set Task Instance note.
apiInstance.setTaskInstanceNote(dagId, dagRunId, taskId, setTaskInstanceNote, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 
 **taskId** | **String**| The task ID. | 
 **setTaskInstanceNote** | [**SetTaskInstanceNote**](SetTaskInstanceNote.md)| Parameters of set Task Instance note. | 

### Return type

[**TaskInstance**](TaskInstance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

