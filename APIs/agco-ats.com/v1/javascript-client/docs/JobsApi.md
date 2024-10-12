# AgcoApi.JobsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobsDeleteJob**](JobsApi.md#jobsDeleteJob) | **DELETE** /api/v2/jobs/{jobID} | Mark the delete flag for the Job
[**jobsGetJob**](JobsApi.md#jobsGetJob) | **GET** /api/v2/jobs/{jobID} | Get a Job by ID
[**jobsGetJobs**](JobsApi.md#jobsGetJobs) | **GET** /api/v2/jobs | Get Jobs
[**jobsPostJob**](JobsApi.md#jobsPostJob) | **POST** /api/v2/jobs | Create a Job
[**jobsPutJob**](JobsApi.md#jobsPutJob) | **PUT** /api/v2/jobs/{jobID} | Update a Job



## jobsDeleteJob

> jobsDeleteJob(jobID)

Mark the delete flag for the Job

Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobsApi();
let jobID = 56; // Number | The id of the job to delete
apiInstance.jobsDeleteJob(jobID, (error, data, response) => {
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
 **jobID** | **Number**| The id of the job to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## jobsGetJob

> BuildSystemSharedDTOJob jobsGetJob(jobID, opts)

Get a Job by ID

Gets a Job by ID. When successful, the response is the requested Job.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobsApi();
let jobID = 56; // Number | The ID of the Job to get.
let opts = {
  'isIncludeDeleted': true // Boolean | Does it include deleted job, or not
};
apiInstance.jobsGetJob(jobID, opts, (error, data, response) => {
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
 **jobID** | **Number**| The ID of the Job to get. | 
 **isIncludeDeleted** | **Boolean**| Does it include deleted job, or not | [optional] 

### Return type

[**BuildSystemSharedDTOJob**](BuildSystemSharedDTOJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## jobsGetJobs

> APIPagedResponseBuildSystemSharedDTOJob jobsGetJobs(opts)

Get Jobs

Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.              If unsuccessful, an appropriate ApiError is returned.               ///

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'isIncludeDeleted': true // Boolean | Does it include deleted job, or not
};
apiInstance.jobsGetJobs(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **isIncludeDeleted** | **Boolean**| Does it include deleted job, or not | [optional] 

### Return type

[**APIPagedResponseBuildSystemSharedDTOJob**](APIPagedResponseBuildSystemSharedDTOJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## jobsPostJob

> Number jobsPostJob(buildSystemSharedDTOJob)

Create a Job

Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on              creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an               appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobsApi();
let buildSystemSharedDTOJob = new AgcoApi.BuildSystemSharedDTOJob(); // BuildSystemSharedDTOJob | The job to create.  The JobID will be assigned on creation of the Job.
apiInstance.jobsPostJob(buildSystemSharedDTOJob, (error, data, response) => {
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
 **buildSystemSharedDTOJob** | [**BuildSystemSharedDTOJob**](BuildSystemSharedDTOJob.md)| The job to create.  The JobID will be assigned on creation of the Job. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## jobsPutJob

> jobsPutJob(jobID, buildSystemSharedDTOJob)

Update a Job

Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.JobsApi();
let jobID = 56; // Number | The id of the job to update
let buildSystemSharedDTOJob = new AgcoApi.BuildSystemSharedDTOJob(); // BuildSystemSharedDTOJob | The updated job
apiInstance.jobsPutJob(jobID, buildSystemSharedDTOJob, (error, data, response) => {
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
 **jobID** | **Number**| The id of the job to update | 
 **buildSystemSharedDTOJob** | [**BuildSystemSharedDTOJob**](BuildSystemSharedDTOJob.md)| The updated job | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

