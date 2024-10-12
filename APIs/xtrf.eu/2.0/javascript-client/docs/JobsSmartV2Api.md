# XtrfHomePortalApi.JobsSmartV2Api

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addExternalFileLink**](JobsSmartV2Api.md#addExternalFileLink) | **POST** /v2/jobs/{jobId}/files/addExternalLink | 
[**addFileLinks**](JobsSmartV2Api.md#addFileLinks) | **POST** /v2/jobs/{jobId}/files/delivered/addLink | Adds file link to the project as a link delivered in the job.
[**addFiles**](JobsSmartV2Api.md#addFiles) | **PUT** /v2/jobs/{jobId}/files/delivered/add | Adds files to the project as delivered in the job.
[**assignVendor1**](JobsSmartV2Api.md#assignVendor1) | **PUT** /v2/jobs/{jobId}/vendor | Assigns vendor to a job in a project.
[**changeDates**](JobsSmartV2Api.md#changeDates) | **PUT** /v2/jobs/{jobId}/dates | Updates dates of a given job.
[**changeStatus1**](JobsSmartV2Api.md#changeStatus1) | **PUT** /v2/jobs/{jobId}/status | Changes job status if possible (400 Bad Request is returned otherwise).
[**getByExternalId**](JobsSmartV2Api.md#getByExternalId) | **GET** /v2/jobs/for-external-id | 
[**getDeliveredFiles**](JobsSmartV2Api.md#getDeliveredFiles) | **GET** /v2/jobs/{jobId}/files/delivered | Returns list of files delivered in the job.
[**getFileById1**](JobsSmartV2Api.md#getFileById1) | **GET** /v2/jobs/{jobId} | Returns details for a job.
[**getSharedReferenceFiles**](JobsSmartV2Api.md#getSharedReferenceFiles) | **GET** /v2/jobs/{jobId}/files/sharedReferenceFiles | Returns list of files shared with the job as Reference Files.
[**getSharedWorkFiles**](JobsSmartV2Api.md#getSharedWorkFiles) | **GET** /v2/jobs/{jobId}/files/sharedWorkFiles | Returns list of files shared with the job as Work Files.
[**shareAsReferenceFiles**](JobsSmartV2Api.md#shareAsReferenceFiles) | **PUT** /v2/jobs/{jobId}/files/sharedReferenceFiles/share | Shares selected files as Reference Files with a job in a project.
[**shareAsWorkFiles**](JobsSmartV2Api.md#shareAsWorkFiles) | **PUT** /v2/jobs/{jobId}/files/sharedWorkFiles/share | Shares selected files as Work Files with a job in a project.
[**stopSharing**](JobsSmartV2Api.md#stopSharing) | **PUT** /v2/jobs/{jobId}/files/stopSharing | Stops sharing selected files with a job in a project.
[**updateInstructions4**](JobsSmartV2Api.md#updateInstructions4) | **PUT** /v2/jobs/{jobId}/instructions | Updates instructions for a job.
[**uploadFile1**](JobsSmartV2Api.md#uploadFile1) | **POST** /v2/jobs/{jobId}/files/delivered/upload | Uploads file to the project as a file delivered in the job.



## addExternalFileLink

> addExternalFileLink(jobId, externalFileDto)



### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let externalFileDto = new XtrfHomePortalApi.ExternalFileDto(); // ExternalFileDto | Added file links to the project as added by PM.
apiInstance.addExternalFileLink(jobId, externalFileDto, (error, data, response) => {
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
 **externalFileDto** | [**ExternalFileDto**](ExternalFileDto.md)| Added file links to the project as added by PM. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## addFileLinks

> FilesDto addFileLinks(jobId, fileLinkCategorizationsDto)

Adds file link to the project as a link delivered in the job.

Adds file link to the project as a link delivered in the job. The following properties can be specified for each file link:&lt;ul&gt;&lt;li&gt;url (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let fileLinkCategorizationsDto = /home-api/assets/examples/v2/jobs/addFileLinksToJob.json#requestBody; // FileLinkCategorizationsDto | Adds file link to the project as a link delivered in the job.
apiInstance.addFileLinks(jobId, fileLinkCategorizationsDto, (error, data, response) => {
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
 **fileLinkCategorizationsDto** | [**FileLinkCategorizationsDto**](FileLinkCategorizationsDto.md)| Adds file link to the project as a link delivered in the job. | 

### Return type

[**FilesDto**](FilesDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## addFiles

> addFiles(jobId, fileCategorizationsDto)

Adds files to the project as delivered in the job.

Adds files to the project as delivered in the job. The files have to be uploaded beforehand (see \&quot;POST /jobs/{jobId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let fileCategorizationsDto = /home-api/assets/examples/v2/jobs/addFiles.json#requestBody; // FileCategorizationsDto | Added files to the project as delivered in the job.
apiInstance.addFiles(jobId, fileCategorizationsDto, (error, data, response) => {
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
 **fileCategorizationsDto** | [**FileCategorizationsDto**](FileCategorizationsDto.md)| Added files to the project as delivered in the job. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## assignVendor1

> assignVendor1(jobId, vendorPriceProfileDTO)

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

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let vendorPriceProfileDTO = /home-api/assets/examples/v2/jobs/assignVendor.json#requestBody; // VendorPriceProfileDTO | Assigned vendor to a job in a project.
apiInstance.assignVendor1(jobId, vendorPriceProfileDTO, (error, data, response) => {
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
 **vendorPriceProfileDTO** | [**VendorPriceProfileDTO**](VendorPriceProfileDTO.md)| Assigned vendor to a job in a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeDates

> changeDates(jobId, jobDatesDto)

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

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let jobDatesDto = /home-api/assets/examples/v2/jobs/changeDates.json#requestBody; // JobDatesDto | New job dates.
apiInstance.changeDates(jobId, jobDatesDto, (error, data, response) => {
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


## changeStatus1

> changeStatus1(jobId, jobStatusDTO)

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

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let jobStatusDTO = /home-api/assets/examples/v2/jobs/changeStatus.json#requestBody; // JobStatusDTO | Changed job status.
apiInstance.changeStatus1(jobId, jobStatusDTO, (error, data, response) => {
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


## getByExternalId

> getByExternalId(opts)



### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let opts = {
  'externalProjectId': "externalProjectId_example", // String | job's externalProjectId
  'externalId': "externalId_example" // String | job's external identifier
};
apiInstance.getByExternalId(opts, (error, data, response) => {
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
 **externalProjectId** | **String**| job&#39;s externalProjectId | [optional] 
 **externalId** | **String**| job&#39;s external identifier | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getDeliveredFiles

> [ProjectFileDto] getDeliveredFiles(jobId)

Returns list of files delivered in the job.

Returns list of files delivered in the job.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
apiInstance.getDeliveredFiles(jobId, (error, data, response) => {
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

[**[ProjectFileDto]**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getFileById1

> ProjectFileDto getFileById1(jobId)

Returns details for a job.

Returns details for a job.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
apiInstance.getFileById1(jobId, (error, data, response) => {
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

[**ProjectFileDto**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSharedReferenceFiles

> [ProjectFileDto] getSharedReferenceFiles(jobId)

Returns list of files shared with the job as Reference Files.

Returns list of files shared with the job as Reference Files.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
apiInstance.getSharedReferenceFiles(jobId, (error, data, response) => {
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

[**[ProjectFileDto]**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSharedWorkFiles

> [ProjectFileDto] getSharedWorkFiles(jobId)

Returns list of files shared with the job as Work Files.

Returns list of files shared with the job as Work Files.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
apiInstance.getSharedWorkFiles(jobId, (error, data, response) => {
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

[**[ProjectFileDto]**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## shareAsReferenceFiles

> FilesShareStatusDto shareAsReferenceFiles(jobId, filesDto)

Shares selected files as Reference Files with a job in a project.

Shares selected files as Reference Files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were already shared with the job. If a file was shared with the job as Work File, it will now be shared as Reference File (and not as Work File).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let filesDto = /home-api/assets/examples/v2/jobs/shareAsReferenceFiles.json#requestBody; // FilesDto | Shared selected files as Reference Files with a job in a project.
apiInstance.shareAsReferenceFiles(jobId, filesDto, (error, data, response) => {
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
 **filesDto** | [**FilesDto**](FilesDto.md)| Shared selected files as Reference Files with a job in a project. | 

### Return type

[**FilesShareStatusDto**](FilesShareStatusDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/json;charset=UTF-8


## shareAsWorkFiles

> FilesShareStatusDto shareAsWorkFiles(jobId, filesDto)

Shares selected files as Work Files with a job in a project.

Shares selected files as Work Files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were already shared with the job. If a file was shared with the job as Reference File, it will now be shared as Work File (and not as Reference File).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let filesDto = /home-api/assets/examples/v2/jobs/shareAsWorkFiles.json#requestBody; // FilesDto | Shared selected files as Work Files with a job in a project.
apiInstance.shareAsWorkFiles(jobId, filesDto, (error, data, response) => {
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
 **filesDto** | [**FilesDto**](FilesDto.md)| Shared selected files as Work Files with a job in a project. | 

### Return type

[**FilesShareStatusDto**](FilesShareStatusDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/json;charset=UTF-8


## stopSharing

> FilesShareStatusDto stopSharing(jobId, filesDto)

Stops sharing selected files with a job in a project.

Stops sharing selected files with a job in a project. The files and the job have to be part of the same project. The operation is finished successfully even if some of the selected files were not shared with the job.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let filesDto = /home-api/assets/examples/v2/jobs/stopSharing.json#requestBody; // FilesDto | File sharing stopped for a project task.
apiInstance.stopSharing(jobId, filesDto, (error, data, response) => {
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
 **filesDto** | [**FilesDto**](FilesDto.md)| File sharing stopped for a project task. | 

### Return type

[**FilesShareStatusDto**](FilesShareStatusDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/json;charset=UTF-8


## updateInstructions4

> updateInstructions4(jobId, stringDTO)

Updates instructions for a job.

Updates instructions for a job. See also \&quot;PUT /projects/{projectId}/vendorInstructions\&quot; and \&quot;PUT /quotes/{quoteId}/vendorInstructions\&quot; for updating instructions for all jobs in a project or quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let stringDTO = /home-api/assets/examples/v2/jobs/updateInstructionsForJob.json#requestBody; // StringDTO | Updated instructions for a job.
apiInstance.updateInstructions4(jobId, stringDTO, (error, data, response) => {
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
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated instructions for a job. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## uploadFile1

> FileDto uploadFile1(jobId, opts)

Uploads file to the project as a file delivered in the job.

Uploads file to the project as a file delivered in the job. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /jobs/{jobId}/files/add\&quot; operation).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.JobsSmartV2Api();
let jobId = "jobId_example"; // String | job's internal identifier
let opts = {
  'file': "/path/to/file" // File | 
};
apiInstance.uploadFile1(jobId, opts, (error, data, response) => {
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
 **file** | **File**|  | [optional] 

### Return type

[**FileDto**](FileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json;charset=UTF-8

