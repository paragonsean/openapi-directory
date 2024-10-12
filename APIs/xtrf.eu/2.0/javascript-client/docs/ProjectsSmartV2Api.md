# XtrfHomePortalApi.ProjectsSmartV2Api

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addExternalFileLinks**](ProjectsSmartV2Api.md#addExternalFileLinks) | **POST** /v2/projects/{projectId}/files/addExternalLink | 
[**addFileLinks1**](ProjectsSmartV2Api.md#addFileLinks1) | **POST** /v2/projects/{projectId}/files/addLink | Adds file links to the project as added by PM.
[**addFiles1**](ProjectsSmartV2Api.md#addFiles1) | **PUT** /v2/projects/{projectId}/files/add | Adds files to the project as added by PM.
[**addJobToProcess**](ProjectsSmartV2Api.md#addJobToProcess) | **POST** /v2/projects/{projectId}/addJob | Returns process id.
[**archive**](ProjectsSmartV2Api.md#archive) | **POST** /v2/projects/files/archive | Prepares a ZIP archive that contains the specified files.
[**changeStatus2**](ProjectsSmartV2Api.md#changeStatus2) | **PUT** /v2/projects/{projectId}/status | Changes project status if possible (400 Bad Request is returned otherwise).
[**create6**](ProjectsSmartV2Api.md#create6) | **POST** /v2/projects | Creates a new Smart Project.
[**createPayable2**](ProjectsSmartV2Api.md#createPayable2) | **POST** /v2/projects/{projectId}/finance/payables | Adds a payable to a project.
[**createReceivable2**](ProjectsSmartV2Api.md#createReceivable2) | **POST** /v2/projects/{projectId}/finance/receivables | Adds a receivable to a project.
[**deletePayable2**](ProjectsSmartV2Api.md#deletePayable2) | **DELETE** /v2/projects/{projectId}/finance/payables/{payableId} | Deletes a payable.
[**deleteReceivable2**](ProjectsSmartV2Api.md#deleteReceivable2) | **DELETE** /v2/projects/{projectId}/finance/receivables/{receivableId} | Deletes a receivable.
[**getByExternalId1**](ProjectsSmartV2Api.md#getByExternalId1) | **GET** /v2/projects/for-external-id/{externalProjectId} | Returns project details.
[**getById9**](ProjectsSmartV2Api.md#getById9) | **GET** /v2/projects/{projectId} | Returns project details.
[**getCATToolProjectInfo**](ProjectsSmartV2Api.md#getCATToolProjectInfo) | **GET** /v2/projects/{projectId}/catToolProject | Returns if cat tool project is created or queued.
[**getContacts2**](ProjectsSmartV2Api.md#getContacts2) | **GET** /v2/projects/{projectId}/clientContacts | Returns Client Contacts information for a project.
[**getCustomFields8**](ProjectsSmartV2Api.md#getCustomFields8) | **GET** /v2/projects/{projectId}/customFields | Returns a list of custom field keys and values for a project.
[**getDeliverableFiles**](ProjectsSmartV2Api.md#getDeliverableFiles) | **GET** /v2/projects/{projectId}/files/deliverable | Returns list of files in a project, that are ready to be delivered to client.
[**getFileById2**](ProjectsSmartV2Api.md#getFileById2) | **GET** /v2/projects/files/{fileId} | Returns details of a file.
[**getFileContentById**](ProjectsSmartV2Api.md#getFileContentById) | **GET** /v2/projects/files/{fileId}/download/{fileName} | Downloads a file content.
[**getFiles**](ProjectsSmartV2Api.md#getFiles) | **GET** /v2/projects/{projectId}/files | Returns list of files in a project.
[**getFinance2**](ProjectsSmartV2Api.md#getFinance2) | **GET** /v2/projects/{projectId}/finance | Returns finance information for a project.
[**getJobs**](ProjectsSmartV2Api.md#getJobs) | **GET** /v2/projects/{projectId}/jobs | Returns list of jobs in a project.
[**getProcessId**](ProjectsSmartV2Api.md#getProcessId) | **GET** /v2/projects/{projectId}/process | Returns process id.
[**updateClientDeadline**](ProjectsSmartV2Api.md#updateClientDeadline) | **PUT** /v2/projects/{projectId}/clientDeadline | Updates Client Deadline for a project.
[**updateClientNotes**](ProjectsSmartV2Api.md#updateClientNotes) | **PUT** /v2/projects/{projectId}/clientNotes | Updates Client Notes for a project.
[**updateClientReferenceNumber**](ProjectsSmartV2Api.md#updateClientReferenceNumber) | **PUT** /v2/projects/{projectId}/clientReferenceNumber | Updates Client Reference Number for a project.
[**updateContacts2**](ProjectsSmartV2Api.md#updateContacts2) | **PUT** /v2/projects/{projectId}/clientContacts | Updates Client Contacts for a project.
[**updateCustomField2**](ProjectsSmartV2Api.md#updateCustomField2) | **PUT** /v2/projects/{projectId}/customFields/{key} | Updates a custom field with a specified key in a project
[**updateInternalNotes**](ProjectsSmartV2Api.md#updateInternalNotes) | **PUT** /v2/projects/{projectId}/internalNotes | Updates Internal Notes for a project.
[**updateOrderedOn**](ProjectsSmartV2Api.md#updateOrderedOn) | **PUT** /v2/projects/{projectId}/orderDate | Updates Order Date for a project.
[**updatePayable2**](ProjectsSmartV2Api.md#updatePayable2) | **PUT** /v2/projects/{projectId}/finance/payables/{payableId} | Updates a payable.
[**updateReceivable2**](ProjectsSmartV2Api.md#updateReceivable2) | **PUT** /v2/projects/{projectId}/finance/receivables/{receivableId} | Updates a receivable.
[**updateSourceLanguage**](ProjectsSmartV2Api.md#updateSourceLanguage) | **PUT** /v2/projects/{projectId}/sourceLanguage | Updates source language for a project.
[**updateSpecialization**](ProjectsSmartV2Api.md#updateSpecialization) | **PUT** /v2/projects/{projectId}/specialization | Updates specialization for a project.
[**updateTargetLanguages**](ProjectsSmartV2Api.md#updateTargetLanguages) | **PUT** /v2/projects/{projectId}/targetLanguages | Updates target languages for a project.
[**updateVendorInstructions**](ProjectsSmartV2Api.md#updateVendorInstructions) | **PUT** /v2/projects/{projectId}/vendorInstructions | Updates instructions for all vendors performing the jobs in a project.
[**updateVolume**](ProjectsSmartV2Api.md#updateVolume) | **PUT** /v2/projects/{projectId}/volume | Updates volume for a project.
[**uploadFile2**](ProjectsSmartV2Api.md#uploadFile2) | **POST** /v2/projects/{projectId}/files/upload | Uploads file to the project as a file uploaded by PM.



## addExternalFileLinks

> addExternalFileLinks(projectId, externalFileDto)



### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let externalFileDto = new XtrfHomePortalApi.ExternalFileDto(); // ExternalFileDto | Added file links to the project as added by PM.
apiInstance.addExternalFileLinks(projectId, externalFileDto, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **externalFileDto** | [**ExternalFileDto**](ExternalFileDto.md)| Added file links to the project as added by PM. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## addFileLinks1

> FilesDto addFileLinks1(projectId, fileLinkCategorizationsDto)

Adds file links to the project as added by PM.

Adds file links to the project as added by PM. The following properties can be specified for each file link:&lt;ul&gt;&lt;li&gt;url (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let fileLinkCategorizationsDto = /home-api/assets/examples/v2/projects/addFileLinks.json#requestBody; // FileLinkCategorizationsDto | Added file links to the project as added by PM.
apiInstance.addFileLinks1(projectId, fileLinkCategorizationsDto, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **fileLinkCategorizationsDto** | [**FileLinkCategorizationsDto**](FileLinkCategorizationsDto.md)| Added file links to the project as added by PM. | 

### Return type

[**FilesDto**](FilesDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## addFiles1

> addFiles1(projectId, fileCategorizationsDto)

Adds files to the project as added by PM.

Adds files to the project as added by PM. The files have to be uploaded beforehand (see \&quot;POST /v2/projects/{projectId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let fileCategorizationsDto = /home-api/assets/examples/v2/projects/addFiles.json#requestBody; // FileCategorizationsDto | Added files to the project as added by PM.
apiInstance.addFiles1(projectId, fileCategorizationsDto, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **fileCategorizationsDto** | [**FileCategorizationsDto**](FileCategorizationsDto.md)| Added files to the project as added by PM. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addJobToProcess

> CATToolProjectDTO addJobToProcess(projectId)

Returns process id.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | 
apiInstance.addJobToProcess(projectId, (error, data, response) => {
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
 **projectId** | **String**|  | 

### Return type

[**CATToolProjectDTO**](CATToolProjectDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## archive

> FilesArchiveDto archive(filesDto)

Prepares a ZIP archive that contains the specified files.

Prepares a ZIP archive that contains the specified files.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let filesDto = /home-api/assets/examples/v2/projects/archive.json#requestBody; // FilesDto | Prepared ZIP archive that contains the specified files.
apiInstance.archive(filesDto, (error, data, response) => {
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
 **filesDto** | [**FilesDto**](FilesDto.md)| Prepared ZIP archive that contains the specified files. | 

### Return type

[**FilesArchiveDto**](FilesArchiveDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## changeStatus2

> changeStatus2(projectId, projectStatusDTO)

Changes project status if possible (400 Bad Request is returned otherwise).

Changes project status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys: &lt;ul&gt;&lt;li&gt;CANCELLED – available when the job has one of the following statuses: OPEN, STARTED&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let projectStatusDTO = /home-api/assets/examples/v2/projects/changeStatus.json#requestBody; // ProjectStatusDTO | Changed project status.
apiInstance.changeStatus2(projectId, projectStatusDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **projectStatusDTO** | [**ProjectStatusDTO**](ProjectStatusDTO.md)| Changed project status. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## create6

> ProjectDTOv2 create6(opts)

Creates a new Smart Project.

Creates a new Smart Project. If the specified service ID refers to Classic Project, 400 Bad Request is returned instead.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let opts = {
  'projectCreateDTO': new XtrfHomePortalApi.ProjectCreateDTO() // ProjectCreateDTO | 
};
apiInstance.create6(opts, (error, data, response) => {
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
 **projectCreateDTO** | [**ProjectCreateDTO**](ProjectCreateDTO.md)|  | [optional] 

### Return type

[**ProjectDTOv2**](ProjectDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## createPayable2

> PayableDTO createPayable2(projectId, payableCreateDTO)

Adds a payable to a project.

Adds a payable to a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let payableCreateDTO = /home-api/assets/examples/v2/projects/createPayable.json#requestBody; // PayableCreateDTO | 
apiInstance.createPayable2(projectId, payableCreateDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **payableCreateDTO** | [**PayableCreateDTO**](PayableCreateDTO.md)|  | 

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## createReceivable2

> ReceivableDTO createReceivable2(projectId, receivableCreateDTO)

Adds a receivable to a project.

Adds a receivable to a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let receivableCreateDTO = /home-api/assets/examples/v2/projects/createReceivable.json#requestBody; // ReceivableCreateDTO | 
apiInstance.createReceivable2(projectId, receivableCreateDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **receivableCreateDTO** | [**ReceivableCreateDTO**](ReceivableCreateDTO.md)|  | 

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## deletePayable2

> deletePayable2(projectId, payableId)

Deletes a payable.

Deletes a payable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let payableId = 789; // Number | payable's internal identifier
apiInstance.deletePayable2(projectId, payableId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **payableId** | **Number**| payable&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteReceivable2

> deleteReceivable2(projectId, receivableId)

Deletes a receivable.

Deletes a receivable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let receivableId = 789; // Number | receivable's internal identifier
apiInstance.deleteReceivable2(projectId, receivableId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **receivableId** | **Number**| receivable&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getByExternalId1

> ProjectDTOv2 getByExternalId1(externalProjectId)

Returns project details.

Returns project details.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let externalProjectId = "externalProjectId_example"; // String | project's external identifier
apiInstance.getByExternalId1(externalProjectId, (error, data, response) => {
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
 **externalProjectId** | **String**| project&#39;s external identifier | 

### Return type

[**ProjectDTOv2**](ProjectDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getById9

> ProjectDTOv2 getById9(projectId)

Returns project details.

Returns project details. If the specified project ID refers to Classic Project, 400 Bad Request is returned instead.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getById9(projectId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 

### Return type

[**ProjectDTOv2**](ProjectDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getCATToolProjectInfo

> CATToolProjectDTO getCATToolProjectInfo(projectId)

Returns if cat tool project is created or queued.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | 
apiInstance.getCATToolProjectInfo(projectId, (error, data, response) => {
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
 **projectId** | **String**|  | 

### Return type

[**CATToolProjectDTO**](CATToolProjectDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getContacts2

> SmartContactsDTO getContacts2(projectId)

Returns Client Contacts information for a project.

Returns Client Contacts information for a project

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getContacts2(projectId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 

### Return type

[**SmartContactsDTO**](SmartContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getCustomFields8

> [CustomFieldDTO] getCustomFields8(projectId)

Returns a list of custom field keys and values for a project.

Returns a list of custom field keys and values for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getCustomFields8(projectId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getDeliverableFiles

> [ProjectFileDto] getDeliverableFiles(projectId)

Returns list of files in a project, that are ready to be delivered to client.

Returns list of files in a project, that are ready to be delivered to client. A file is considered deliverable to client when all of the following criteria are met:&lt;ul&gt;&lt;li&gt;the file was added to a job in the last step in the process&lt;/li&gt;&lt;li&gt;the file is marked as verified (if it was added in a verification step and the file is verifiable, according to its category)&lt;/li&gt;&lt;li&gt;the job is finished (has Ready status)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getDeliverableFiles(projectId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 

### Return type

[**[ProjectFileDto]**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getFileById2

> ProjectFileDto getFileById2(fileId)

Returns details of a file.

Returns details of a file.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let fileId = "fileId_example"; // String | file's internal identifier
apiInstance.getFileById2(fileId, (error, data, response) => {
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
 **fileId** | **String**| file&#39;s internal identifier | 

### Return type

[**ProjectFileDto**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getFileContentById

> getFileContentById(fileId, fileName)

Downloads a file content.

Downloads a file content.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let fileId = "fileId_example"; // String | file's internal identifier
let fileName = "fileName_example"; // String | file's name
apiInstance.getFileContentById(fileId, fileName, (error, data, response) => {
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
 **fileId** | **String**| file&#39;s internal identifier | 
 **fileName** | **String**| file&#39;s name | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: multipart/form-data


## getFiles

> [ProjectFileDto] getFiles(projectId)

Returns list of files in a project.

Returns list of files in a project. Only files added to the project (i.e. files that have assigned category and languages) are listed.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getFiles(projectId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 

### Return type

[**[ProjectFileDto]**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getFinance2

> FinanceDTO getFinance2(projectId)

Returns finance information for a project.

Returns finance information for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getFinance2(projectId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 

### Return type

[**FinanceDTO**](FinanceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getJobs

> [JobDto] getJobs(projectId)

Returns list of jobs in a project.

Returns list of jobs in a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getJobs(projectId, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 

### Return type

[**[JobDto]**](JobDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getProcessId

> CATToolProjectDTO getProcessId(projectId)

Returns process id.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | 
apiInstance.getProcessId(projectId, (error, data, response) => {
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
 **projectId** | **String**|  | 

### Return type

[**CATToolProjectDTO**](CATToolProjectDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## updateClientDeadline

> updateClientDeadline(projectId, timeDTO)

Updates Client Deadline for a project.

Updates Client Deadline for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let timeDTO = /home-api/assets/examples/v2/projects/updateClientDeadline.json#requestBody; // TimeDTO | Updated Client Deadline for a project.
apiInstance.updateClientDeadline(projectId, timeDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **timeDTO** | [**TimeDTO**](TimeDTO.md)| Updated Client Deadline for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateClientNotes

> updateClientNotes(projectId, stringDTO)

Updates Client Notes for a project.

Updates Client Notes for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let stringDTO = /home-api/assets/examples/v2/projects/updateClientNotes.json#requestBody; // StringDTO | Updated Client Notes for a project.
apiInstance.updateClientNotes(projectId, stringDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Notes for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateClientReferenceNumber

> updateClientReferenceNumber(projectId, stringDTO)

Updates Client Reference Number for a project.

Updates Client Reference Number for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let stringDTO = /home-api/assets/examples/v2/projects/updateClientReferenceNumber.json#requestBody; // StringDTO | Updated Client Reference Number for a project.
apiInstance.updateClientReferenceNumber(projectId, stringDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Reference Number for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateContacts2

> SmartContactsDTO updateContacts2(projectId, smartContactsDTO)

Updates Client Contacts for a project.

Updates Client Contacts for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let smartContactsDTO = /home-api/assets/examples/v2/projects/updateClientContacts.json#requestBody; // SmartContactsDTO | Updated Client Contacts for a project.
apiInstance.updateContacts2(projectId, smartContactsDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **smartContactsDTO** | [**SmartContactsDTO**](SmartContactsDTO.md)| Updated Client Contacts for a project. | 

### Return type

[**SmartContactsDTO**](SmartContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## updateCustomField2

> updateCustomField2(projectId, key, smartCustomFieldDTO)

Updates a custom field with a specified key in a project

Updates a custom field with a specified key in a project

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let key = "key_example"; // String | custom field's key
let smartCustomFieldDTO = /home-api/assets/examples/v2/projects/updateCustomField.json#requestBody; // SmartCustomFieldDTO | Updated custom field with a specified key in a project.
apiInstance.updateCustomField2(projectId, key, smartCustomFieldDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **key** | **String**| custom field&#39;s key | 
 **smartCustomFieldDTO** | [**SmartCustomFieldDTO**](SmartCustomFieldDTO.md)| Updated custom field with a specified key in a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateInternalNotes

> updateInternalNotes(projectId, stringDTO)

Updates Internal Notes for a project.

Updates Internal Notes for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let stringDTO = /home-api/assets/examples/v2/projects/updateInternalNotes.json#requestBody; // StringDTO | Updated Internal Notes for a project.
apiInstance.updateInternalNotes(projectId, stringDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Internal Notes for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateOrderedOn

> updateOrderedOn(projectId, timeDTO)

Updates Order Date for a project.

Updates Order Date for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let timeDTO = /home-api/assets/examples/v2/projects/updateOrderedOn.json#requestBody; // TimeDTO | Updated Order Date for a project.
apiInstance.updateOrderedOn(projectId, timeDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **timeDTO** | [**TimeDTO**](TimeDTO.md)| Updated Order Date for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updatePayable2

> PayableDTO updatePayable2(projectId, payableId, payableDTO)

Updates a payable.

Updates a payable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let payableId = 789; // Number | payable's internal identifier
let payableDTO = /home-api/assets/examples/v2/projects/updatePayable.json#requestBody; // PayableDTO | 
apiInstance.updatePayable2(projectId, payableId, payableDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **payableId** | **Number**| payable&#39;s internal identifier | 
 **payableDTO** | [**PayableDTO**](PayableDTO.md)|  | 

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## updateReceivable2

> ReceivableDTO updateReceivable2(projectId, receivableId, receivableDTO)

Updates a receivable.

Updates a receivable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let receivableId = 789; // Number | receivable's internal identifier
let receivableDTO = /home-api/assets/examples/v2/projects/updateReceivable.json#requestBody; // ReceivableDTO | 
apiInstance.updateReceivable2(projectId, receivableId, receivableDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **receivableId** | **Number**| receivable&#39;s internal identifier | 
 **receivableDTO** | [**ReceivableDTO**](ReceivableDTO.md)|  | 

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## updateSourceLanguage

> updateSourceLanguage(projectId, sourceLanguageDTO)

Updates source language for a project.

Updates source language for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let sourceLanguageDTO = /home-api/assets/examples/v2/projects/updateSourceLanguage.json#requestBody; // SourceLanguageDTO | Updated source language for a project.
apiInstance.updateSourceLanguage(projectId, sourceLanguageDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **sourceLanguageDTO** | [**SourceLanguageDTO**](SourceLanguageDTO.md)| Updated source language for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateSpecialization

> updateSpecialization(projectId, specializationDTO)

Updates specialization for a project.

Updates specialization for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let specializationDTO = /home-api/assets/examples/v2/projects/updateSpecialization.json#requestBody; // SpecializationDTO | Updated specialization for a project.
apiInstance.updateSpecialization(projectId, specializationDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **specializationDTO** | [**SpecializationDTO**](SpecializationDTO.md)| Updated specialization for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateTargetLanguages

> updateTargetLanguages(projectId, targetLanguagesDTO)

Updates target languages for a project.

Updates target languages for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let targetLanguagesDTO = /home-api/assets/examples/v2/projects/updateTargetLanguages.json#requestBody; // TargetLanguagesDTO | Updated target languages for a project.
apiInstance.updateTargetLanguages(projectId, targetLanguagesDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **targetLanguagesDTO** | [**TargetLanguagesDTO**](TargetLanguagesDTO.md)| Updated target languages for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateVendorInstructions

> updateVendorInstructions(projectId, stringDTO)

Updates instructions for all vendors performing the jobs in a project.

Updates instructions for all vendors performing the jobs in a project. See also \&quot;PUT /jobs/{jobId}/instructions\&quot; for updating instructions for a specific job in a project or quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let stringDTO = /home-api/assets/examples/v2/projects/updateSpecialization.json#requestBody; // StringDTO | Updated instructions for all vendors performing the jobs in a project.
apiInstance.updateVendorInstructions(projectId, stringDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated instructions for all vendors performing the jobs in a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateVolume

> updateVolume(projectId, bigDecimalDTO)

Updates volume for a project.

Updates volume for a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let bigDecimalDTO = /home-api/assets/examples/v2/projects/updateVolume.json#requestBody; // BigDecimalDTO | Updated volume for a project.
apiInstance.updateVolume(projectId, bigDecimalDTO, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **bigDecimalDTO** | [**BigDecimalDTO**](BigDecimalDTO.md)| Updated volume for a project. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## uploadFile2

> FileDto uploadFile2(projectId, opts)

Uploads file to the project as a file uploaded by PM.

Uploads file to the project as a file uploaded by PM. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /v2/projects/{projectId}/files/add\&quot; operation

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsSmartV2Api();
let projectId = "projectId_example"; // String | project's internal identifier
let opts = {
  'file': "/path/to/file" // File | 
};
apiInstance.uploadFile2(projectId, opts, (error, data, response) => {
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
 **projectId** | **String**| project&#39;s internal identifier | 
 **file** | **File**|  | [optional] 

### Return type

[**FileDto**](FileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json;charset=UTF-8

