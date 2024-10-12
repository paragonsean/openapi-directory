# AirflowApiStable.DAGApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDag**](DAGApi.md#deleteDag) | **DELETE** /dags/{dag_id} | Delete a DAG
[**getDag**](DAGApi.md#getDag) | **GET** /dags/{dag_id} | Get basic information about a DAG
[**getDagDetails**](DAGApi.md#getDagDetails) | **GET** /dags/{dag_id}/details | Get a simplified representation of DAG
[**getDagSource**](DAGApi.md#getDagSource) | **GET** /dagSources/{file_token} | Get a source code
[**getDags**](DAGApi.md#getDags) | **GET** /dags | List DAGs
[**getTask**](DAGApi.md#getTask) | **GET** /dags/{dag_id}/tasks/{task_id} | Get simplified representation of a task
[**getTasks**](DAGApi.md#getTasks) | **GET** /dags/{dag_id}/tasks | Get tasks for DAG
[**patchDag**](DAGApi.md#patchDag) | **PATCH** /dags/{dag_id} | Update a DAG
[**patchDags**](DAGApi.md#patchDags) | **PATCH** /dags | Update DAGs
[**postClearTaskInstances**](DAGApi.md#postClearTaskInstances) | **POST** /dags/{dag_id}/clearTaskInstances | Clear a set of task instances
[**postSetTaskInstancesState**](DAGApi.md#postSetTaskInstancesState) | **POST** /dags/{dag_id}/updateTaskInstancesState | Set a state of task instances



## deleteDag

> deleteDag(dagId)

Delete a DAG

Deletes all metadata related to the DAG, including finished DAG Runs and Tasks. Logs are not deleted. This action cannot be undone.  *New in version 2.2.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagId = "dagId_example"; // String | The DAG ID.
apiInstance.deleteDag(dagId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDag

> DAG getDag(dagId)

Get basic information about a DAG

Presents only information available in database (DAGModel). If you need detailed information, consider using GET /dags/{dag_id}/details. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagId = "dagId_example"; // String | The DAG ID.
apiInstance.getDag(dagId, (error, data, response) => {
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

### Return type

[**DAG**](DAG.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDagDetails

> DAGDetail getDagDetails(dagId)

Get a simplified representation of DAG

The response contains many DAG attributes, so the response can be large. If possible, consider using GET /dags/{dag_id}. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagId = "dagId_example"; // String | The DAG ID.
apiInstance.getDagDetails(dagId, (error, data, response) => {
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

### Return type

[**DAGDetail**](DAGDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDagSource

> GetDagSource200Response getDagSource(fileToken)

Get a source code

Get a source code using file token. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let fileToken = "fileToken_example"; // String | The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change. 
apiInstance.getDagSource(fileToken, (error, data, response) => {
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
 **fileToken** | **String**| The key containing the encrypted path to the file. Encryption and decryption take place only on the server. This prevents the client from reading an non-DAG file. This also ensures API extensibility, because the format of encrypted data may change.  | 

### Return type

[**GetDagSource200Response**](GetDagSource200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, plain/text


## getDags

> DAGCollection getDags(opts)

List DAGs

List DAGs in the database. &#x60;dag_id_pattern&#x60; can be set to match dags of a specific pattern 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'orderBy': "orderBy_example", // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
  'tags': ["null"], // [String] | List of tags to filter results.  *New in version 2.2.0* 
  'onlyActive': true, // Boolean | Only filter active DAGs.  *New in version 2.1.1* 
  'dagIdPattern': "dagIdPattern_example" // String | If set, only return DAGs with dag_ids matching this pattern. 
};
apiInstance.getDags(opts, (error, data, response) => {
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
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 
 **orderBy** | **String**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 
 **tags** | [**[String]**](String.md)| List of tags to filter results.  *New in version 2.2.0*  | [optional] 
 **onlyActive** | **Boolean**| Only filter active DAGs.  *New in version 2.1.1*  | [optional] [default to true]
 **dagIdPattern** | **String**| If set, only return DAGs with dag_ids matching this pattern.  | [optional] 

### Return type

[**DAGCollection**](DAGCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTask

> Task getTask(dagId, taskId)

Get simplified representation of a task

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagId = "dagId_example"; // String | The DAG ID.
let taskId = "taskId_example"; // String | The task ID.
apiInstance.getTask(dagId, taskId, (error, data, response) => {
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
 **taskId** | **String**| The task ID. | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTasks

> TaskCollection getTasks(dagId, opts)

Get tasks for DAG

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagId = "dagId_example"; // String | The DAG ID.
let opts = {
  'orderBy': "orderBy_example" // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
};
apiInstance.getTasks(dagId, opts, (error, data, response) => {
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
 **orderBy** | **String**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**TaskCollection**](TaskCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchDag

> DAG patchDag(dagId, DAG, opts)

Update a DAG

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagId = "dagId_example"; // String | The DAG ID.
let DAG = {"is_paused":true}; // DAG | 
let opts = {
  'updateMask': ["null"] // [String] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
};
apiInstance.patchDag(dagId, DAG, opts, (error, data, response) => {
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
 **DAG** | [**DAG**](DAG.md)|  | 
 **updateMask** | [**[String]**](String.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 

### Return type

[**DAG**](DAG.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchDags

> DAGCollection patchDags(dagIdPattern, DAG, opts)

Update DAGs

Update DAGs of a given dag_id_pattern using UpdateMask. This endpoint allows specifying &#x60;~&#x60; as the dag_id_pattern to update all DAGs. *New in version 2.3.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagIdPattern = "dagIdPattern_example"; // String | If set, only update DAGs with dag_ids matching this pattern. 
let DAG = {"is_paused":true}; // DAG | 
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'tags': ["null"], // [String] | List of tags to filter results.  *New in version 2.2.0* 
  'updateMask': ["null"], // [String] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
  'onlyActive': true // Boolean | Only filter active DAGs.  *New in version 2.1.1* 
};
apiInstance.patchDags(dagIdPattern, DAG, opts, (error, data, response) => {
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
 **dagIdPattern** | **String**| If set, only update DAGs with dag_ids matching this pattern.  | 
 **DAG** | [**DAG**](DAG.md)|  | 
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 
 **tags** | [**[String]**](String.md)| List of tags to filter results.  *New in version 2.2.0*  | [optional] 
 **updateMask** | [**[String]**](String.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 
 **onlyActive** | **Boolean**| Only filter active DAGs.  *New in version 2.1.1*  | [optional] [default to true]

### Return type

[**DAGCollection**](DAGCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postClearTaskInstances

> TaskInstanceReferenceCollection postClearTaskInstances(dagId, clearTaskInstances)

Clear a set of task instances

Clears a set of task instances associated with the DAG for a specified date range. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagId = "dagId_example"; // String | The DAG ID.
let clearTaskInstances = new AirflowApiStable.ClearTaskInstances(); // ClearTaskInstances | Parameters of action
apiInstance.postClearTaskInstances(dagId, clearTaskInstances, (error, data, response) => {
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
 **clearTaskInstances** | [**ClearTaskInstances**](ClearTaskInstances.md)| Parameters of action | 

### Return type

[**TaskInstanceReferenceCollection**](TaskInstanceReferenceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSetTaskInstancesState

> TaskInstanceReferenceCollection postSetTaskInstancesState(dagId, updateTaskInstancesState)

Set a state of task instances

Updates the state for multiple task instances simultaneously. 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DAGApi();
let dagId = "dagId_example"; // String | The DAG ID.
let updateTaskInstancesState = new AirflowApiStable.UpdateTaskInstancesState(); // UpdateTaskInstancesState | Parameters of action
apiInstance.postSetTaskInstancesState(dagId, updateTaskInstancesState, (error, data, response) => {
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
 **updateTaskInstancesState** | [**UpdateTaskInstancesState**](UpdateTaskInstancesState.md)| Parameters of action | 

### Return type

[**TaskInstanceReferenceCollection**](TaskInstanceReferenceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

