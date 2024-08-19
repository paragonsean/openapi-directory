# XtrfHomePortalApi.JobsClassicApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignFileToJobOutput**](JobsClassicApi.md#assignFileToJobOutput) | **POST** /jobs/{jobId}/files/output | 
[**assignVendor**](JobsClassicApi.md#assignVendor) | **PUT** /jobs/{jobId}/vendor | Assigns vendor to a job in a project.
[**changeStatus**](JobsClassicApi.md#changeStatus) | **PUT** /jobs/{jobId}/status | Changes job status if possible (400 Bad Request is returned otherwise).
[**getJobDetails**](JobsClassicApi.md#getJobDetails) | **GET** /jobs/{jobId} | Returns job details by jobId.
[**getJobFiles**](JobsClassicApi.md#getJobFiles) | **GET** /jobs/{jobId}/files | Returns list of input and output files of a job.
[**getJobFiles1**](JobsClassicApi.md#getJobFiles1) | **GET** /jobs/{jobId}/files/{fileId} | Returns file metadata.
[**updateDates**](JobsClassicApi.md#updateDates) | **PUT** /jobs/{jobId}/dates | Updates dates of a given job.
[**updateInstructions**](JobsClassicApi.md#updateInstructions) | **PUT** /jobs/{jobId}/instructions | Updates instructions for a job.



## assignFileToJobOutput

> assignFileToJobOutput(jobId, taskFileDTO)



### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsClassicApi();
let jobId = "jobId_example"; // String | job's internal identifier
let taskFileDTO = /home-api/assets/examples/v1/jobs/assignFileToJobOutput.json#requestBody; // TaskFileDTO | Assigns file to job output files.
apiInstance.assignFileToJobOutput(jobId, taskFileDTO, (error, data, response) => {
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
 **jobId** | **String**| job&#39;s internal identifier | 
 **taskFileDTO** | [**TaskFileDTO**](TaskFileDTO.md)| Assigns file to job output files. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## assignVendor

> assignVendor(jobId, assignVendorDTO)

Assigns vendor to a job in a project.

Assigns vendor to a job in a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsClassicApi();
let jobId = "jobId_example"; // String | job's internal identifier
let assignVendorDTO = /home-api/assets/examples/v1/jobs/assignVendor.json#requestBody; // AssignVendorDTO | Assigned vendor to a job in a project.
apiInstance.assignVendor(jobId, assignVendorDTO, (error, data, response) => {
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
 **jobId** | **String**| job&#39;s internal identifier | 
 **assignVendorDTO** | [**AssignVendorDTO**](AssignVendorDTO.md)| Assigned vendor to a job in a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeStatus

> changeStatus(jobId, jobStatusDTO)

Changes job status if possible (400 Bad Request is returned otherwise).

Changes job status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys:&lt;ul&gt;&lt;li&gt;OPEN – available when the job has one of the following statuses: ACCEPTED, CANCELED&lt;/li&gt;&lt;li&gt;ACCEPTED – available when the job has one of the following statuses: OPEN (Vendor and dates have to be set before calling the operation), STARTED&lt;/li&gt;&lt;li&gt;STARTED – available when the job has one of the following statuses: ACCEPTED, READY&lt;/li&gt;&lt;li&gt;READY – available when the job has one of the following statuses: STARTED&lt;/li&gt;&lt;li&gt;CANCELLED – available when the job has one of the following statuses: OPEN, ACCEPTED, STARTED, OFFERS_SENT&lt;/li&gt;&lt;li&gt;OFFERS_SENT – not available as a target status for this operation&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsClassicApi();
let jobId = "jobId_example"; // String | job's internal identifier
let jobStatusDTO = /home-api/assets/examples/v1/jobs/changeStatus.json#requestBody; // JobStatusDTO | Changed job status.
apiInstance.changeStatus(jobId, jobStatusDTO, (error, data, response) => {
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
 **jobId** | **String**| job&#39;s internal identifier | 
 **jobStatusDTO** | [**JobStatusDTO**](JobStatusDTO.md)| Changed job status. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getJobDetails

> JobDto getJobDetails(jobId)

Returns job details by jobId.

Returns job details by jobId.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsClassicApi();
let jobId = "jobId_example"; // String | job's internal identifier
apiInstance.getJobDetails(jobId, (error, data, response) => {
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
 **jobId** | **String**| job&#39;s internal identifier | 

### Return type

[**JobDto**](JobDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getJobFiles

> JobFilesDTO getJobFiles(jobId)

Returns list of input and output files of a job.

Returns list of input and output files of a job.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsClassicApi();
let jobId = "jobId_example"; // String | job's internal identifier
apiInstance.getJobFiles(jobId, (error, data, response) => {
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
 **jobId** | **String**| job&#39;s internal identifier | 

### Return type

[**JobFilesDTO**](JobFilesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getJobFiles1

> FileMetadataDTO getJobFiles1(jobId, fileId)

Returns file metadata.

Returns file metadata.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsClassicApi();
let jobId = "jobId_example"; // String | job's internal identifier
let fileId = 789; // Number | file's internal identifier
apiInstance.getJobFiles1(jobId, fileId, (error, data, response) => {
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
 **jobId** | **String**| job&#39;s internal identifier | 
 **fileId** | **Number**| file&#39;s internal identifier | 

### Return type

[**FileMetadataDTO**](FileMetadataDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateDates

> updateDates(jobId, jobDatesDto)

Updates dates of a given job.

Updates dates of a given job.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsClassicApi();
let jobId = "jobId_example"; // String | job's internal identifier
let jobDatesDto = /home-api/assets/examples/v1/jobs/updateDates.json#requestBody; // JobDatesDto | New job dates.
apiInstance.updateDates(jobId, jobDatesDto, (error, data, response) => {
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
 **jobId** | **String**| job&#39;s internal identifier | 
 **jobDatesDto** | [**JobDatesDto**](JobDatesDto.md)| New job dates. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateInstructions

> updateInstructions(jobId, instructionsDTO)

Updates instructions for a job.

Updates instructions for a job.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsClassicApi();
let jobId = "jobId_example"; // String | job's internal identifier
let instructionsDTO = /home-api/assets/examples/v1/jobs/updateInstructionsForJob.json#requestBody; // InstructionsDTO | Updated instructions for a job.
apiInstance.updateInstructions(jobId, instructionsDTO, (error, data, response) => {
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
 **jobId** | **String**| job&#39;s internal identifier | 
 **instructionsDTO** | [**InstructionsDTO**](InstructionsDTO.md)| Updated instructions for a job. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

