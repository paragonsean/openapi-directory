# AirflowApiStable.DatasetApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDataset**](DatasetApi.md#getDataset) | **GET** /datasets/{uri} | Get a dataset
[**getDatasetEvents**](DatasetApi.md#getDatasetEvents) | **GET** /datasets/events | Get dataset events
[**getDatasets**](DatasetApi.md#getDatasets) | **GET** /datasets | List datasets
[**getUpstreamDatasetEvents_0**](DatasetApi.md#getUpstreamDatasetEvents_0) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/upstreamDatasetEvents | Get dataset events for a DAG run



## getDataset

> Dataset getDataset(uri)

Get a dataset

Get a dataset by uri.

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DatasetApi();
let uri = "uri_example"; // String | The encoded Dataset URI
apiInstance.getDataset(uri, (error, data, response) => {
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
 **uri** | **String**| The encoded Dataset URI | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatasetEvents

> DatasetEventCollection getDatasetEvents(opts)

Get dataset events

Get dataset events

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DatasetApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'orderBy': "orderBy_example", // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
  'datasetId': 56, // Number | The Dataset ID that updated the dataset.
  'sourceDagId': "sourceDagId_example", // String | The DAG ID that updated the dataset.
  'sourceTaskId': "sourceTaskId_example", // String | The task ID that updated the dataset.
  'sourceRunId': "sourceRunId_example", // String | The DAG run ID that updated the dataset.
  'sourceMapIndex': 56 // Number | The map index that updated the dataset.
};
apiInstance.getDatasetEvents(opts, (error, data, response) => {
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
 **datasetId** | **Number**| The Dataset ID that updated the dataset. | [optional] 
 **sourceDagId** | **String**| The DAG ID that updated the dataset. | [optional] 
 **sourceTaskId** | **String**| The task ID that updated the dataset. | [optional] 
 **sourceRunId** | **String**| The DAG run ID that updated the dataset. | [optional] 
 **sourceMapIndex** | **Number**| The map index that updated the dataset. | [optional] 

### Return type

[**DatasetEventCollection**](DatasetEventCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatasets

> DatasetCollection getDatasets(opts)

List datasets

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DatasetApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'orderBy': "orderBy_example", // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
  'uriPattern': "uriPattern_example" // String | If set, only return datasets with uris matching this pattern. 
};
apiInstance.getDatasets(opts, (error, data, response) => {
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
 **uriPattern** | **String**| If set, only return datasets with uris matching this pattern.  | [optional] 

### Return type

[**DatasetCollection**](DatasetCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUpstreamDatasetEvents_0

> DatasetEventCollection getUpstreamDatasetEvents_0(dagId, dagRunId)

Get dataset events for a DAG run

Get datasets for a dag run.  *New in version 2.4.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DatasetApi();
let dagId = "dagId_example"; // String | The DAG ID.
let dagRunId = "dagRunId_example"; // String | The DAG run ID.
apiInstance.getUpstreamDatasetEvents_0(dagId, dagRunId, (error, data, response) => {
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

