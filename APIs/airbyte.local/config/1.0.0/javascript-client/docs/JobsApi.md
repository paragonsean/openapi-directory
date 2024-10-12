# AirbyteConfigurationApi.JobsApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelJob**](JobsApi.md#cancelJob) | **POST** /v1/jobs/cancel | Cancels a job
[**getAttemptNormalizationStatusesForJob**](JobsApi.md#getAttemptNormalizationStatusesForJob) | **POST** /v1/jobs/get_normalization_status | Get normalization status to determine if we can bypass normalization phase
[**getJobDebugInfo**](JobsApi.md#getJobDebugInfo) | **POST** /v1/jobs/get_debug_info | Gets all information needed to debug this job
[**getJobInfo**](JobsApi.md#getJobInfo) | **POST** /v1/jobs/get | Get information about a job
[**getJobInfoLight**](JobsApi.md#getJobInfoLight) | **POST** /v1/jobs/get_light | Get information about a job excluding attempt info and logs
[**getLastReplicationJob**](JobsApi.md#getLastReplicationJob) | **POST** /v1/jobs/get_last_replication_job | 
[**listJobsFor**](JobsApi.md#listJobsFor) | **POST** /v1/jobs/list | Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.



## cancelJob

> JobInfoRead cancelJob(jobIdRequestBody)

Cancels a job

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.JobsApi();
let jobIdRequestBody = new AirbyteConfigurationApi.JobIdRequestBody(); // JobIdRequestBody | 
apiInstance.cancelJob(jobIdRequestBody, (error, data, response) => {
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
 **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | 

### Return type

[**JobInfoRead**](JobInfoRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAttemptNormalizationStatusesForJob

> AttemptNormalizationStatusReadList getAttemptNormalizationStatusesForJob(opts)

Get normalization status to determine if we can bypass normalization phase

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.JobsApi();
let opts = {
  'jobIdRequestBody': new AirbyteConfigurationApi.JobIdRequestBody() // JobIdRequestBody | 
};
apiInstance.getAttemptNormalizationStatusesForJob(opts, (error, data, response) => {
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
 **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | [optional] 

### Return type

[**AttemptNormalizationStatusReadList**](AttemptNormalizationStatusReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getJobDebugInfo

> JobDebugInfoRead getJobDebugInfo(jobIdRequestBody)

Gets all information needed to debug this job

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.JobsApi();
let jobIdRequestBody = new AirbyteConfigurationApi.JobIdRequestBody(); // JobIdRequestBody | 
apiInstance.getJobDebugInfo(jobIdRequestBody, (error, data, response) => {
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
 **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | 

### Return type

[**JobDebugInfoRead**](JobDebugInfoRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getJobInfo

> JobInfoRead getJobInfo(jobIdRequestBody)

Get information about a job

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.JobsApi();
let jobIdRequestBody = new AirbyteConfigurationApi.JobIdRequestBody(); // JobIdRequestBody | 
apiInstance.getJobInfo(jobIdRequestBody, (error, data, response) => {
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
 **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | 

### Return type

[**JobInfoRead**](JobInfoRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getJobInfoLight

> JobInfoLightRead getJobInfoLight(jobIdRequestBody)

Get information about a job excluding attempt info and logs

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.JobsApi();
let jobIdRequestBody = new AirbyteConfigurationApi.JobIdRequestBody(); // JobIdRequestBody | 
apiInstance.getJobInfoLight(jobIdRequestBody, (error, data, response) => {
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
 **jobIdRequestBody** | [**JobIdRequestBody**](JobIdRequestBody.md)|  | 

### Return type

[**JobInfoLightRead**](JobInfoLightRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getLastReplicationJob

> JobOptionalRead getLastReplicationJob(connectionIdRequestBody)



### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.JobsApi();
let connectionIdRequestBody = new AirbyteConfigurationApi.ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
apiInstance.getLastReplicationJob(connectionIdRequestBody, (error, data, response) => {
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
 **connectionIdRequestBody** | [**ConnectionIdRequestBody**](ConnectionIdRequestBody.md)|  | 

### Return type

[**JobOptionalRead**](JobOptionalRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listJobsFor

> JobReadList listJobsFor(jobListRequestBody)

Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.JobsApi();
let jobListRequestBody = new AirbyteConfigurationApi.JobListRequestBody(); // JobListRequestBody | 
apiInstance.listJobsFor(jobListRequestBody, (error, data, response) => {
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
 **jobListRequestBody** | [**JobListRequestBody**](JobListRequestBody.md)|  | 

### Return type

[**JobReadList**](JobReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

