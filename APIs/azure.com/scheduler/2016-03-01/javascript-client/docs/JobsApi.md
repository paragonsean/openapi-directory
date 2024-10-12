# SchedulerManagementClient.JobsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobsCreateOrUpdate**](JobsApi.md#jobsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName} | 
[**jobsDelete**](JobsApi.md#jobsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName} | 
[**jobsGet**](JobsApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName} | 
[**jobsList**](JobsApi.md#jobsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs | 
[**jobsListJobHistory**](JobsApi.md#jobsListJobHistory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName}/history | 
[**jobsPatch**](JobsApi.md#jobsPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName} | 
[**jobsRun**](JobsApi.md#jobsRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName}/run | 



## jobsCreateOrUpdate

> JobDefinition jobsCreateOrUpdate(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, job)



Provisions a new job or updates an existing job.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';

let apiInstance = new SchedulerManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let jobName = "jobName_example"; // String | The job name.
let apiVersion = "apiVersion_example"; // String | The API version.
let job = new SchedulerManagementClient.JobDefinition(); // JobDefinition | The job definition.
apiInstance.jobsCreateOrUpdate(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, job, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **jobName** | **String**| The job name. | 
 **apiVersion** | **String**| The API version. | 
 **job** | [**JobDefinition**](JobDefinition.md)| The job definition. | 

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## jobsDelete

> jobsDelete(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion)



Deletes a job.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';

let apiInstance = new SchedulerManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let jobName = "jobName_example"; // String | The job name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobsDelete(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **jobName** | **String**| The job name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobsGet

> JobDefinition jobsGet(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion)



Gets a job.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';

let apiInstance = new SchedulerManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let jobName = "jobName_example"; // String | The job name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobsGet(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **jobName** | **String**| The job name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## jobsList

> JobListResult jobsList(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, opts)



Lists all jobs under the specified job collection.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';

let apiInstance = new SchedulerManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of jobs to request, in the of range of [1..100].
  'skip': 56, // Number | The (0-based) index of the job history list from which to begin requesting entries.
  'filter': "filter_example" // String | The filter to apply on the job state.
};
apiInstance.jobsList(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of jobs to request, in the of range of [1..100]. | [optional] 
 **skip** | **Number**| The (0-based) index of the job history list from which to begin requesting entries. | [optional] 
 **filter** | **String**| The filter to apply on the job state. | [optional] 

### Return type

[**JobListResult**](JobListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## jobsListJobHistory

> JobHistoryListResult jobsListJobHistory(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, opts)



Lists job history.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';

let apiInstance = new SchedulerManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let jobName = "jobName_example"; // String | The job name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | the number of job history to request, in the of range of [1..100].
  'skip': 56, // Number | The (0-based) index of the job history list from which to begin requesting entries.
  'filter': "filter_example" // String | The filter to apply on the job state.
};
apiInstance.jobsListJobHistory(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **jobName** | **String**| The job name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| the number of job history to request, in the of range of [1..100]. | [optional] 
 **skip** | **Number**| The (0-based) index of the job history list from which to begin requesting entries. | [optional] 
 **filter** | **String**| The filter to apply on the job state. | [optional] 

### Return type

[**JobHistoryListResult**](JobHistoryListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## jobsPatch

> JobDefinition jobsPatch(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, job)



Patches an existing job.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';

let apiInstance = new SchedulerManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let jobName = "jobName_example"; // String | The job name.
let apiVersion = "apiVersion_example"; // String | The API version.
let job = new SchedulerManagementClient.JobDefinition(); // JobDefinition | The job definition.
apiInstance.jobsPatch(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, job, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **jobName** | **String**| The job name. | 
 **apiVersion** | **String**| The API version. | 
 **job** | [**JobDefinition**](JobDefinition.md)| The job definition. | 

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## jobsRun

> jobsRun(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion)



Runs a job.

### Example

```javascript
import SchedulerManagementClient from 'scheduler_management_client';

let apiInstance = new SchedulerManagementClient.JobsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
let jobName = "jobName_example"; // String | The job name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.jobsRun(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **jobCollectionName** | **String**| The job collection name. | 
 **jobName** | **String**| The job name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

