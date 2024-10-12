# AirflowApiStable.DAGRunApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clearDagRun**](DAGRunApi.md#clearDagRun) | **POST** /dags/{dag_id}/dagRuns/{dag_run_id}/clear | Clear a DAG run
[**deleteDagRun**](DAGRunApi.md#deleteDagRun) | **DELETE** /dags/{dag_id}/dagRuns/{dag_run_id} | Delete a DAG run
[**getDagRun**](DAGRunApi.md#getDagRun) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Get a DAG run
[**getDagRuns**](DAGRunApi.md#getDagRuns) | **GET** /dags/{dag_id}/dagRuns | List DAG runs
[**getDagRunsBatch**](DAGRunApi.md#getDagRunsBatch) | **POST** /dags/~/dagRuns/list | List DAG runs (batch)
[**getUpstreamDatasetEvents**](DAGRunApi.md#getUpstreamDatasetEvents) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents | Get dataset events for a DAG run
[**postDagRun**](DAGRunApi.md#postDagRun) | **POST** /dags/{dag_id}/dagRuns | Trigger a new DAG run
[**setDagRunNote**](DAGRunApi.md#setDagRunNote) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id}/setNote | Update the DagRun note.
[**updateDagRunState**](DAGRunApi.md#updateDagRunState) | **PATCH** /dags/{dag_id}/dagRuns/{dag_run_id} | Modify a DAG run



## clearDagRun

> ClearDagRun200Response clearDagRun(dagId, dagRunId, clearDagRun)

Clear a DAG run

Clear a DAG run.  *New in version 2.4.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let clearDagRun = new AirflowApiStable.ClearDagRun(); // ClearDagRun | 
apiInstance.clearDagRun(dagId, dagRunId, clearDagRun, (error, data, response) => {
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
 **clearDagRun** | [**ClearDagRun**](ClearDagRun.md)|  | 

### Return type

[**ClearDagRun200Response**](ClearDagRun200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDagRun

> deleteDagRun(dagId, dagRunId)

Delete a DAG run

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
apiInstance.deleteDagRun(dagId, dagRunId, (error, data, response) => {
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
 **dagId** | **String**| The DAG ID. | 
 **dagRunId** | **String**| The DAG run ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDagRun

> DAGRun getDagRun(dagId, dagRunId)

Get a DAG run

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
apiInstance.getDagRun(dagId, dagRunId, (error, data, response) => {
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

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDagRuns

> DAGRunCollection getDagRuns(dagId, opts)

List DAG runs

This endpoint allows specifying &#x60;~&#x60; as the dag_id to retrieve DAG runs for all DAGs. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let dagId = "dagId_example"; // String | The DAG ID.
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'executionDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period. 
  'executionDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period. 
  'startDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
  'startDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
  'endDateGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period. 
  'endDateLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period. 
  'state': ["null"], // [String] | The value can be repeated to retrieve multiple matching values (OR condition).
  'orderBy': "orderBy_example" // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
};
apiInstance.getDagRuns(dagId, opts, (error, data, response) => {
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
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 
 **executionDateGte** | **Date**| Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
 **executionDateLte** | **Date**| Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
 **startDateGte** | **Date**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **startDateLte** | **Date**| Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **endDateGte** | **Date**| Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
 **endDateLte** | **Date**| Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
 **state** | [**[String]**](String.md)| The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
 **orderBy** | **String**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**DAGRunCollection**](DAGRunCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDagRunsBatch

> DAGRunCollection getDagRunsBatch(listDagRunsForm)

List DAG runs (batch)

This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would run in to maximum HTTP request URL length limit. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let listDagRunsForm = new AirflowApiStable.ListDagRunsForm(); // ListDagRunsForm | 
apiInstance.getDagRunsBatch(listDagRunsForm, (error, data, response) => {
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
 **listDagRunsForm** | [**ListDagRunsForm**](ListDagRunsForm.md)|  | 

### Return type

[**DAGRunCollection**](DAGRunCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getUpstreamDatasetEvents

> DatasetEventCollection getUpstreamDatasetEvents(dagId, dagRunId)

Get dataset events for a DAG run

Get datasets for a dag run.  *New in version 2.4.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
apiInstance.getUpstreamDatasetEvents(dagId, dagRunId, (error, data, response) => {
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

### Return type

[**DatasetEventCollection**](DatasetEventCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDagRun

> DAGRun postDagRun(dagId, dAGRun)

Trigger a new DAG run

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dAGRun = new AirflowApiStable.DAGRun(); // DAGRun | 
apiInstance.postDagRun(dagId, dAGRun, (error, data, response) => {
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
 **dAGRun** | [**DAGRun**](DAGRun.md)|  | 

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setDagRunNote

> DAGRun setDagRunNote(dagId, dagRunId, setDagRunNote)

Update the DagRun note.

Update the manual user note of a DagRun.  *New in version 2.5.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let setDagRunNote = new AirflowApiStable.SetDagRunNote(); // SetDagRunNote | Parameters of set DagRun note.
apiInstance.setDagRunNote(dagId, dagRunId, setDagRunNote, (error, data, response) => {
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
 **setDagRunNote** | [**SetDagRunNote**](SetDagRunNote.md)| Parameters of set DagRun note. | 

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDagRunState

> DAGRun updateDagRunState(dagId, dagRunId, updateDagRunState)

Modify a DAG run

Modify a DAG run.  *New in version 2.2.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGRunApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
let updateDagRunState = new AirflowApiStable.UpdateDagRunState(); // UpdateDagRunState | 
apiInstance.updateDagRunState(dagId, dagRunId, updateDagRunState, (error, data, response) => {
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
 **updateDagRunState** | [**UpdateDagRunState**](UpdateDagRunState.md)|  | 

### Return type

[**DAGRun**](DAGRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

