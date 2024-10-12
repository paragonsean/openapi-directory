# HdInsightJobManagementClient.JobApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobGet**](JobApi.md#jobGet) | **GET** /templeton/v1/jobs/{jobId} | 
[**jobGetAppState**](JobApi.md#jobGetAppState) | **GET** /ws/v1/cluster/apps/{appId}/state | 
[**jobKill**](JobApi.md#jobKill) | **DELETE** /templeton/v1/jobs/{jobId} | 
[**jobList**](JobApi.md#jobList) | **GET** /templeton/v1/jobs | 
[**jobListAfterJobId**](JobApi.md#jobListAfterJobId) | **GET** /templeton/v1/jobs?op&#x3D;LISTAFTERID | 
[**jobSubmitHiveJob**](JobApi.md#jobSubmitHiveJob) | **POST** /templeton/v1/hive | 
[**jobSubmitMapReduceJob**](JobApi.md#jobSubmitMapReduceJob) | **POST** /templeton/v1/mapreduce/jar | 
[**jobSubmitMapReduceStreamingJob**](JobApi.md#jobSubmitMapReduceStreamingJob) | **POST** /templeton/v1/mapreduce/streaming | 
[**jobSubmitPigJob**](JobApi.md#jobSubmitPigJob) | **POST** /templeton/v1/pig | 
[**jobSubmitSqoopJob**](JobApi.md#jobSubmitSqoopJob) | **POST** /templeton/v1/sqoop | 



## jobGet

> JobDetailRootJsonObject jobGet(userName, jobId, fields)



Gets job details from the specified HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let jobId = "jobId_example"; // String | The id of the job.
let fields = "fields_example"; // String | If fields set to '*', the request will return full details of the job. Currently the value can only be '*'.
apiInstance.jobGet(userName, jobId, fields, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **jobId** | **String**| The id of the job. | 
 **fields** | **String**| If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;. | 

### Return type

[**JobDetailRootJsonObject**](JobDetailRootJsonObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobGetAppState

> AppState jobGetAppState(appId)



Gets application state from the specified HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let appId = "appId_example"; // String | The id of the job.
apiInstance.jobGetAppState(appId, (error, data, response) => {
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
 **appId** | **String**| The id of the job. | 

### Return type

[**AppState**](AppState.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobKill

> JobDetailRootJsonObject jobKill(userName, jobId)



Initiates cancel on given running job in the specified HDInsight.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let jobId = "jobId_example"; // String | The id of the job.
apiInstance.jobKill(userName, jobId, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **jobId** | **String**| The id of the job. | 

### Return type

[**JobDetailRootJsonObject**](JobDetailRootJsonObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobList

> [JobListJsonObject] jobList(userName, showall, fields)



Gets the list of jobs from the specified HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let showall = "showall_example"; // String | If showall is set to 'true', the request will return all jobs the user has permission to view, not only the jobs belonging to the user.
let fields = "fields_example"; // String | If fields set to '*', the request will return full details of the job. Currently the value can only be '*'.
apiInstance.jobList(userName, showall, fields, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **showall** | **String**| If showall is set to &#39;true&#39;, the request will return all jobs the user has permission to view, not only the jobs belonging to the user. | 
 **fields** | **String**| If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;. | 

### Return type

[**[JobListJsonObject]**](JobListJsonObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobListAfterJobId

> [JobListJsonObject] jobListAfterJobId(userName, showall, fields, opts)



Gets numrecords Of Jobs after jobid from the specified HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let showall = "showall_example"; // String | If showall is set to 'true', the request will return all jobs the user has permission to view, not only the jobs belonging to the user.
let fields = "fields_example"; // String | If fields set to '*', the request will return full details of the job. Currently the value can only be '*'.
let opts = {
  'jobid': "jobid_example", // String | JobId from where to list jobs.
  'numrecords': 56 // Number | Number of jobs to fetch.
};
apiInstance.jobListAfterJobId(userName, showall, fields, opts, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **showall** | **String**| If showall is set to &#39;true&#39;, the request will return all jobs the user has permission to view, not only the jobs belonging to the user. | 
 **fields** | **String**| If fields set to &#39;*&#39;, the request will return full details of the job. Currently the value can only be &#39;*&#39;. | 
 **jobid** | **String**| JobId from where to list jobs. | [optional] 
 **numrecords** | **Number**| Number of jobs to fetch. | [optional] 

### Return type

[**[JobListJsonObject]**](JobListJsonObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobSubmitHiveJob

> JobSubmissionJsonResponse jobSubmitHiveJob(userName, content)



Submits a Hive job to an HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let content = {key: null}; // Object | The content of the Hive job request.
apiInstance.jobSubmitHiveJob(userName, content, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **content** | **Object**| The content of the Hive job request. | 

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/text
- **Accept**: application/json


## jobSubmitMapReduceJob

> JobSubmissionJsonResponse jobSubmitMapReduceJob(userName, content)



Submits a MapReduce job to an HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let content = {key: null}; // Object | The content of the MapReduce job request.
apiInstance.jobSubmitMapReduceJob(userName, content, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **content** | **Object**| The content of the MapReduce job request. | 

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## jobSubmitMapReduceStreamingJob

> JobSubmissionJsonResponse jobSubmitMapReduceStreamingJob(userName, content)



Submits a MapReduce streaming job to an HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let content = {key: null}; // Object | The content of the MapReduce job request.
apiInstance.jobSubmitMapReduceStreamingJob(userName, content, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **content** | **Object**| The content of the MapReduce job request. | 

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## jobSubmitPigJob

> JobSubmissionJsonResponse jobSubmitPigJob(userName, content)



Submits a Pig job to an HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let content = {key: null}; // Object | The content of the Pig job request.
apiInstance.jobSubmitPigJob(userName, content, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **content** | **Object**| The content of the Pig job request. | 

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## jobSubmitSqoopJob

> JobSubmissionJsonResponse jobSubmitSqoopJob(userName, content)



Submits a Sqoop job to an HDInsight cluster.

### Example

```javascript
import HdInsightJobManagementClient from 'hd_insight_job_management_client';
let defaultClient = HdInsightJobManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightJobManagementClient.JobApi();
let userName = "userName_example"; // String | The user name used for running job.
let content = {key: null}; // Object | The content of the Sqoop job request.
apiInstance.jobSubmitSqoopJob(userName, content, (error, data, response) => {
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
 **userName** | **String**| The user name used for running job. | 
 **content** | **Object**| The content of the Sqoop job request. | 

### Return type

[**JobSubmissionJsonResponse**](JobSubmissionJsonResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

