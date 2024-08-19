# XtrfHomePortalApi.TasksClassicApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFile**](TasksClassicApi.md#addFile) | **POST** /tasks/{taskId}/files/input | Adds files to a given task.
[**delete14**](TasksClassicApi.md#delete14) | **DELETE** /tasks/{taskId} | Removes a task.
[**getContacts1**](TasksClassicApi.md#getContacts1) | **GET** /tasks/{taskId}/contacts | Returns contacts of a given task.
[**getCustomFields7**](TasksClassicApi.md#getCustomFields7) | **GET** /tasks/{taskId}/customFields | Returns custom fields of a given task.
[**getDates3**](TasksClassicApi.md#getDates3) | **GET** /tasks/{taskId}/dates | Returns dates of a given task.
[**getInstructions2**](TasksClassicApi.md#getInstructions2) | **GET** /tasks/{taskId}/instructions | Returns instructions of a given task.
[**getProgress**](TasksClassicApi.md#getProgress) | **GET** /tasks/{taskId}/progress | Returns progress of a given task.
[**getTaskFiles**](TasksClassicApi.md#getTaskFiles) | **GET** /tasks/{taskId}/files | Returns lists of files of a given task.
[**start1**](TasksClassicApi.md#start1) | **POST** /tasks/{taskId}/start | Starts a task.
[**updateClientTaskPONumber**](TasksClassicApi.md#updateClientTaskPONumber) | **PUT** /tasks/{taskId}/clientTaskPONumber | Updates Client Task PO Number of a given task.
[**updateContacts1**](TasksClassicApi.md#updateContacts1) | **PUT** /tasks/{taskId}/contacts | Updates contacts of a given task.
[**updateCustomFields5**](TasksClassicApi.md#updateCustomFields5) | **PUT** /tasks/{taskId}/customFields | Updates custom fields of a given task.
[**updateDates2**](TasksClassicApi.md#updateDates2) | **PUT** /tasks/{taskId}/dates | Updates dates of a given task.
[**updateInstructions3**](TasksClassicApi.md#updateInstructions3) | **PUT** /tasks/{taskId}/instructions | Updates instructions of a given task.
[**updateName**](TasksClassicApi.md#updateName) | **PUT** /tasks/{taskId}/name | Updates name of a given task.



## addFile

> addFile(taskId, fileDTO)

Adds files to a given task.

Adds files to a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
let fileDTO = /home-api/assets/examples/v1/tasks/addFile.json#requestBody; // FileDTO | 
apiInstance.addFile(taskId, fileDTO, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 
 **fileDTO** | [**FileDTO**](FileDTO.md)|  | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## delete14

> delete14(taskId, opts)

Removes a task.

Removes a task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
let opts = {
  'removeFilesFromDisc': true, // Boolean | remove files from disc
  'removeExternalProjects': true, // Boolean | remove external projects (ie. from CAT Tool)
  'forceJobsRemoval': true // Boolean | force jobs removal (ie. started or ready)
};
apiInstance.delete14(taskId, opts, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 
 **removeFilesFromDisc** | **Boolean**| remove files from disc | [optional] 
 **removeExternalProjects** | **Boolean**| remove external projects (ie. from CAT Tool) | [optional] 
 **forceJobsRemoval** | **Boolean**| force jobs removal (ie. started or ready) | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getContacts1

> ContactsDTO getContacts1(taskId)

Returns contacts of a given task.

Returns contacts of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
apiInstance.getContacts1(taskId, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 

### Return type

[**ContactsDTO**](ContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCustomFields7

> [CustomFieldDTO] getCustomFields7(taskId)

Returns custom fields of a given task.

Returns custom fields of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
apiInstance.getCustomFields7(taskId, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getDates3

> ProjectDatesDTO getDates3(taskId)

Returns dates of a given task.

Returns dates of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
apiInstance.getDates3(taskId, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 

### Return type

[**ProjectDatesDTO**](ProjectDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getInstructions2

> InstructionsDTO getInstructions2(taskId)

Returns instructions of a given task.

Returns instructions of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
apiInstance.getInstructions2(taskId, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getProgress

> TaskProgressDTO getProgress(taskId)

Returns progress of a given task.

Returns progress of a given task. Progress contains information about task&#39;s status (ie. opened or ready) and current phase (ie. translation). Workflow phase is defined as the first one which contains not ready jobs (ie. opened or started). When no such job exists then workflow phase is not included.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
apiInstance.getProgress(taskId, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 

### Return type

[**TaskProgressDTO**](TaskProgressDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getTaskFiles

> TaskFilesDTO getTaskFiles(taskId)

Returns lists of files of a given task.

Returns several lists of files for a given task: input files divided by type, output files, bundles, files per job, preview files.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
apiInstance.getTaskFiles(taskId, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 

### Return type

[**TaskFilesDTO**](TaskFilesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## start1

> start1(taskId)

Starts a task.

Starts a task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
apiInstance.start1(taskId, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateClientTaskPONumber

> StringDTO updateClientTaskPONumber(taskId, stringDTO)

Updates Client Task PO Number of a given task.

Updates Client Task PO Number of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
let stringDTO = /home-api/assets/examples/v1/tasks/updateClientTaskPONumber.json#requestBody; // StringDTO | Updated Client Task PO Number of a given task.
apiInstance.updateClientTaskPONumber(taskId, stringDTO, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Task PO Number of a given task. | 

### Return type

[**StringDTO**](StringDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateContacts1

> ContactsDTO updateContacts1(taskId, contactsDTO)

Updates contacts of a given task.

Updates contacts of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
let contactsDTO = /home-api/assets/examples/v1/tasks/updateContacts.json#requestBody; // ContactsDTO | Updated contacts of given task.
apiInstance.updateContacts1(taskId, contactsDTO, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 
 **contactsDTO** | [**ContactsDTO**](ContactsDTO.md)| Updated contacts of given task. | 

### Return type

[**ContactsDTO**](ContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCustomFields5

> [CustomFieldDTO] updateCustomFields5(taskId, customFieldDTO)

Updates custom fields of a given task.

Updates custom fields of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
let customFieldDTO = /home-api/assets/examples/v1/tasks/updateCustomFields.json#requestBody; // [CustomFieldDTO] | Updated custom fields
apiInstance.updateCustomFields5(taskId, customFieldDTO, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 
 **customFieldDTO** | [**[CustomFieldDTO]**](CustomFieldDTO.md)| Updated custom fields | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateDates2

> ProjectDatesDTO updateDates2(taskId, projectDatesDTO)

Updates dates of a given task.

Updates dates of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
let projectDatesDTO = /home-api/assets/examples/v1/tasks/updateDates.json#requestBody; // ProjectDatesDTO | Updated dates of a given task.
apiInstance.updateDates2(taskId, projectDatesDTO, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 
 **projectDatesDTO** | [**ProjectDatesDTO**](ProjectDatesDTO.md)| Updated dates of a given task. | 

### Return type

[**ProjectDatesDTO**](ProjectDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateInstructions3

> InstructionsDTO updateInstructions3(taskId, instructionsDTO)

Updates instructions of a given task.

Updates instructions of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
let instructionsDTO = /home-api/assets/examples/v1/tasks/updateInstructions.json#requestBody; // InstructionsDTO | Updated instructions of a given task.
apiInstance.updateInstructions3(taskId, instructionsDTO, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 
 **instructionsDTO** | [**InstructionsDTO**](InstructionsDTO.md)| Updated instructions of a given task. | 

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateName

> StringDTO updateName(taskId, stringDTO)

Updates name of a given task.

Updates name of a given task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.TasksClassicApi();
let taskId = "taskId_example"; // String | task's internal identifier
let stringDTO = /home-api/assets/examples/v1/tasks/updateName.json#requestBody; // StringDTO | 
apiInstance.updateName(taskId, stringDTO, (error, data, response) => {
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
 **taskId** | **String**| task&#39;s internal identifier | 
 **stringDTO** | [**StringDTO**](StringDTO.md)|  | 

### Return type

[**StringDTO**](StringDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

