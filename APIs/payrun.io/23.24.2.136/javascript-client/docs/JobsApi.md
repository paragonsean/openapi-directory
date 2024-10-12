# PayRunIo.JobsApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteBatchJob**](JobsApi.md#deleteBatchJob) | **DELETE** /Jobs/Batch/{JobId} | Delete the Batch job
[**deleteCisJob**](JobsApi.md#deleteCisJob) | **DELETE** /Jobs/Cis/{JobId} | Delete the CIS job
[**deleteDpsJob**](JobsApi.md#deleteDpsJob) | **DELETE** /Jobs/Dps/{JobId} | Delete the DPS job
[**deletePayRunJob**](JobsApi.md#deletePayRunJob) | **DELETE** /Jobs/PayRuns/{JobId} | Delete the pay run job
[**deleteRtiJob**](JobsApi.md#deleteRtiJob) | **DELETE** /Jobs/Rti/{JobId} | Delete the RTI job
[**deleteThirdPartyJob**](JobsApi.md#deleteThirdPartyJob) | **DELETE** /Jobs/ThirdParty/{JobId} | Delete the Third Party job
[**getBatchJobInfo**](JobsApi.md#getBatchJobInfo) | **GET** /Jobs/Batch/{JobId}/Info | Get the Batch job information
[**getBatchJobProgress**](JobsApi.md#getBatchJobProgress) | **GET** /Jobs/Batch/{JobId}/Progress | Get the Batch job progress
[**getBatchJobStatus**](JobsApi.md#getBatchJobStatus) | **GET** /Jobs/Batch/{JobId}/Status | Get the Batch job status
[**getBatchJobs**](JobsApi.md#getBatchJobs) | **GET** /Jobs/Batch | Get all Batch jobs
[**getCisJobInfo**](JobsApi.md#getCisJobInfo) | **GET** /Jobs/Cis/{JobId}/Info | Get the CIS job information
[**getCisJobProgress**](JobsApi.md#getCisJobProgress) | **GET** /Jobs/Cis/{JobId}/Progress | Get the CIS job progress
[**getCisJobStatus**](JobsApi.md#getCisJobStatus) | **GET** /Jobs/Cis/{JobId}/Status | Get the CIS job status
[**getCisJobs**](JobsApi.md#getCisJobs) | **GET** /Jobs/Cis | Get all CIS jobs
[**getDpsJobInfo**](JobsApi.md#getDpsJobInfo) | **GET** /Jobs/Dps/{JobId}/Info | Get the DPS job information
[**getDpsJobProgress**](JobsApi.md#getDpsJobProgress) | **GET** /Jobs/Dps/{JobId}/Progress | Get the DPS job progress
[**getDpsJobStatus**](JobsApi.md#getDpsJobStatus) | **GET** /Jobs/Dps/{JobId}/Status | Get the DPS job status
[**getDpsJobs**](JobsApi.md#getDpsJobs) | **GET** /Jobs/Dps | Get all DPS jobs
[**getEmployerJobs**](JobsApi.md#getEmployerJobs) | **GET** /Jobs/Employer/{EmployerId} | Gets all jobs relating to the employer.
[**getPayRunJobInfo**](JobsApi.md#getPayRunJobInfo) | **GET** /Jobs/PayRuns/{JobId}/Info | Get the pay run job information
[**getPayRunJobProgress**](JobsApi.md#getPayRunJobProgress) | **GET** /Jobs/PayRuns/{JobId}/Progress | Get the pay run job progress
[**getPayRunJobStatus**](JobsApi.md#getPayRunJobStatus) | **GET** /Jobs/PayRuns/{JobId}/Status | Get the pay run job status
[**getPayRunJobs**](JobsApi.md#getPayRunJobs) | **GET** /Jobs/PayRuns | Get all PayRun jobs
[**getRtiJobInfo**](JobsApi.md#getRtiJobInfo) | **GET** /Jobs/Rti/{JobId}/Info | Get the RTI job information
[**getRtiJobProgress**](JobsApi.md#getRtiJobProgress) | **GET** /Jobs/Rti/{JobId}/Progress | Get the RTI job progress
[**getRtiJobStatus**](JobsApi.md#getRtiJobStatus) | **GET** /Jobs/Rti/{JobId}/Status | Get the RTI job status
[**getRtiJobs**](JobsApi.md#getRtiJobs) | **GET** /Jobs/Rti | Get all RTI jobs
[**getThirdPartyJobInfo**](JobsApi.md#getThirdPartyJobInfo) | **GET** /Jobs/ThirdParty/{JobId}/Info | Get the Third Party job information
[**getThirdPartyJobProgress**](JobsApi.md#getThirdPartyJobProgress) | **GET** /Jobs/ThirdParty/{JobId}/Progress | Get the Third Party job progress
[**getThirdPartyJobStatus**](JobsApi.md#getThirdPartyJobStatus) | **GET** /Jobs/ThirdParty/{JobId}/Status | Get the Third Party job status
[**getThirdPartyJobs**](JobsApi.md#getThirdPartyJobs) | **GET** /Jobs/ThirdParty | Get all Third Party jobs
[**postNewBatchJob**](JobsApi.md#postNewBatchJob) | **POST** /Jobs/Batch | Create new Batch job
[**postNewCisJob**](JobsApi.md#postNewCisJob) | **POST** /Jobs/Cis | Create new CIS job
[**postNewDpsJob**](JobsApi.md#postNewDpsJob) | **POST** /Jobs/Dps | Create new DPS job
[**postNewPayRunJob**](JobsApi.md#postNewPayRunJob) | **POST** /Jobs/PayRuns | Create new PayRun job
[**postNewRtiJob**](JobsApi.md#postNewRtiJob) | **POST** /Jobs/Rti | Create new RTI job
[**postNewThirdPartyJob**](JobsApi.md#postNewThirdPartyJob) | **POST** /Jobs/ThirdParty | Create new Third Party job



## deleteBatchJob

> deleteBatchJob(jobId, authorization, apiVersion)

Delete the Batch job

Deletes the the Batch job

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteBatchJob(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCisJob

> deleteCisJob(jobId, authorization, apiVersion)

Delete the CIS job

Deletes the the CIS job

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisJob(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDpsJob

> deleteDpsJob(jobId, authorization, apiVersion)

Delete the DPS job

Deletes the the DPS job

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteDpsJob(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePayRunJob

> deletePayRunJob(jobId, authorization, apiVersion)

Delete the pay run job

Deletes the the payrun job

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayRunJob(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRtiJob

> deleteRtiJob(jobId, authorization, apiVersion)

Delete the RTI job

Deletes the the RTI job

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteRtiJob(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteThirdPartyJob

> deleteThirdPartyJob(jobId, authorization, apiVersion)

Delete the Third Party job

Deletes the the Third Party job

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteThirdPartyJob(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatchJobInfo

> JobInfo getBatchJobInfo(jobId, authorization, apiVersion)

Get the Batch job information

Return the the Batch job information

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getBatchJobInfo(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JobInfo**](JobInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatchJobProgress

> getBatchJobProgress(jobId, authorization, apiVersion)

Get the Batch job progress

Return the the Batch job progress

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getBatchJobProgress(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatchJobStatus

> getBatchJobStatus(jobId, authorization, apiVersion)

Get the Batch job status

Return the the Batch job status

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getBatchJobStatus(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatchJobs

> LinkCollection getBatchJobs(authorization, apiVersion)

Get all Batch jobs

Gets all the Batch jobs

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getBatchJobs(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCisJobInfo

> JobInfo getCisJobInfo(jobId, authorization, apiVersion)

Get the CIS job information

Return the the CIS job information

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisJobInfo(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JobInfo**](JobInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCisJobProgress

> getCisJobProgress(jobId, authorization, apiVersion)

Get the CIS job progress

Return the the CIS job progress

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisJobProgress(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCisJobStatus

> getCisJobStatus(jobId, authorization, apiVersion)

Get the CIS job status

Return the the CIS job status

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisJobStatus(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCisJobs

> LinkCollection getCisJobs(authorization, apiVersion)

Get all CIS jobs

Gets all the CIS jobs

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisJobs(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDpsJobInfo

> JobInfo getDpsJobInfo(jobId, authorization, apiVersion)

Get the DPS job information

Return the the DPS job information

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getDpsJobInfo(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JobInfo**](JobInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDpsJobProgress

> getDpsJobProgress(jobId, authorization, apiVersion)

Get the DPS job progress

Return the the DPS job progress

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getDpsJobProgress(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDpsJobStatus

> getDpsJobStatus(jobId, authorization, apiVersion)

Get the DPS job status

Return the the DPS job status

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getDpsJobStatus(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDpsJobs

> LinkCollection getDpsJobs(authorization, apiVersion)

Get all DPS jobs

Gets all the DPS jobs

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getDpsJobs(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployerJobs

> File getEmployerJobs(employerId, authorization, apiVersion)

Gets all jobs relating to the employer.

Returns all job information objects for the specified employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerJobs(employerId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayRunJobInfo

> JobInfo getPayRunJobInfo(jobId, authorization, apiVersion)

Get the pay run job information

Return the the payrun job information

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayRunJobInfo(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JobInfo**](JobInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayRunJobProgress

> getPayRunJobProgress(jobId, authorization, apiVersion)

Get the pay run job progress

Return the the payrun job progress

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayRunJobProgress(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayRunJobStatus

> getPayRunJobStatus(jobId, authorization, apiVersion)

Get the pay run job status

Return the the payrun job status

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayRunJobStatus(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayRunJobs

> LinkCollection getPayRunJobs(authorization, apiVersion)

Get all PayRun jobs

Gets all the pay run jobs

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayRunJobs(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRtiJobInfo

> JobInfo getRtiJobInfo(jobId, authorization, apiVersion)

Get the RTI job information

Return the the RTI job information

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiJobInfo(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JobInfo**](JobInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRtiJobProgress

> getRtiJobProgress(jobId, authorization, apiVersion)

Get the RTI job progress

Return the the RTI job progress

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiJobProgress(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRtiJobStatus

> getRtiJobStatus(jobId, authorization, apiVersion)

Get the RTI job status

Return the the RTI job status

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiJobStatus(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRtiJobs

> LinkCollection getRtiJobs(authorization, apiVersion)

Get all RTI jobs

Gets all the RTI jobs

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiJobs(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThirdPartyJobInfo

> JobInfo getThirdPartyJobInfo(jobId, authorization, apiVersion)

Get the Third Party job information

Return the the Third Party job information

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getThirdPartyJobInfo(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JobInfo**](JobInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThirdPartyJobProgress

> getThirdPartyJobProgress(jobId, authorization, apiVersion)

Get the Third Party job progress

Return the the Third Party job progress

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getThirdPartyJobProgress(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThirdPartyJobStatus

> getThirdPartyJobStatus(jobId, authorization, apiVersion)

Get the Third Party job status

Return the the Third Party job status

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let jobId = "jobId_example"; // String | The job unique identifier.
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getThirdPartyJobStatus(jobId, authorization, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job unique identifier. | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThirdPartyJobs

> LinkCollection getThirdPartyJobs(authorization, apiVersion)

Get all Third Party jobs

Gets all the Third Party jobs

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getThirdPartyJobs(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postNewBatchJob

> Link postNewBatchJob(authorization, apiVersion, batchJobInstruction)

Create new Batch job

Adds a new Batch job to the queue and returns the job info

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let batchJobInstruction = new PayRunIo.BatchJobInstruction(); // BatchJobInstruction | The the batch job instruction object.
apiInstance.postNewBatchJob(authorization, apiVersion, batchJobInstruction, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **batchJobInstruction** | [**BatchJobInstruction**](BatchJobInstruction.md)| The the batch job instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postNewCisJob

> Link postNewCisJob(authorization, apiVersion, cisJobInstructionBase)

Create new CIS job

Adds a new CIS job to the queue and returns the job info

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let cisJobInstructionBase = new PayRunIo.CisJobInstructionBase(); // CisJobInstructionBase | The the CIS job instruction object.
apiInstance.postNewCisJob(authorization, apiVersion, cisJobInstructionBase, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **cisJobInstructionBase** | [**CisJobInstructionBase**](CisJobInstructionBase.md)| The the CIS job instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postNewDpsJob

> Link postNewDpsJob(authorization, apiVersion, dpsJobInstruction)

Create new DPS job

Creates the new DPS job to the queue and returns the job info

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let dpsJobInstruction = new PayRunIo.DpsJobInstruction(); // DpsJobInstruction | The the DPS job instruction object.
apiInstance.postNewDpsJob(authorization, apiVersion, dpsJobInstruction, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **dpsJobInstruction** | [**DpsJobInstruction**](DpsJobInstruction.md)| The the DPS job instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postNewPayRunJob

> Link postNewPayRunJob(authorization, apiVersion, payRunJobInstruction)

Create new PayRun job

Creates the new pay run job to the queue and returns the job info

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let payRunJobInstruction = new PayRunIo.PayRunJobInstruction(); // PayRunJobInstruction | The pay run job instruction object.
apiInstance.postNewPayRunJob(authorization, apiVersion, payRunJobInstruction, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **payRunJobInstruction** | [**PayRunJobInstruction**](PayRunJobInstruction.md)| The pay run job instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postNewRtiJob

> Link postNewRtiJob(authorization, apiVersion, rtiJobInstruction)

Create new RTI job

Creates the new RTI job to the queue and returns the job info

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let rtiJobInstruction = new PayRunIo.RtiJobInstruction(); // RtiJobInstruction | The the RTI job instruction object.
apiInstance.postNewRtiJob(authorization, apiVersion, rtiJobInstruction, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **rtiJobInstruction** | [**RtiJobInstruction**](RtiJobInstruction.md)| The the RTI job instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postNewThirdPartyJob

> Link postNewThirdPartyJob(authorization, apiVersion, thirdPartyJobInstruction)

Create new Third Party job

Adds a new Third Party job to the queue and returns the job info

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JobsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let thirdPartyJobInstruction = new PayRunIo.ThirdPartyJobInstruction(); // ThirdPartyJobInstruction | The the third party job instruction object.
apiInstance.postNewThirdPartyJob(authorization, apiVersion, thirdPartyJobInstruction, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **thirdPartyJobInstruction** | [**ThirdPartyJobInstruction**](ThirdPartyJobInstruction.md)| The the third party job instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

