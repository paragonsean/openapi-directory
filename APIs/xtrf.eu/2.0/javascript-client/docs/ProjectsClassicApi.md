# XtrfHomePortalApi.ProjectsClassicApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create5**](ProjectsClassicApi.md#create5) | **POST** /projects | Creates a new Classic Project.
[**createLanguageCombination**](ProjectsClassicApi.md#createLanguageCombination) | **POST** /projects/{projectId}/languageCombinations | Creates a new language combination for a given project without creating a task.
[**createPayable**](ProjectsClassicApi.md#createPayable) | **POST** /projects/{projectId}/finance/payables | Adds a payable to a project.
[**createReceivable**](ProjectsClassicApi.md#createReceivable) | **POST** /projects/{projectId}/finance/receivables | Adds a receivable to a project.
[**createTask**](ProjectsClassicApi.md#createTask) | **POST** /projects/{projectId}/tasks | Creates a new task for a given project.
[**delete12**](ProjectsClassicApi.md#delete12) | **DELETE** /projects/{projectId} | Removes a project.
[**deletePayable**](ProjectsClassicApi.md#deletePayable) | **DELETE** /projects/{projectId}/finance/payables/{payableId} | Deletes a payable.
[**deleteReceivable**](ProjectsClassicApi.md#deleteReceivable) | **DELETE** /projects/{projectId}/finance/receivables/{receivableId} | Deletes a receivable.
[**getAllIds6**](ProjectsClassicApi.md#getAllIds6) | **GET** /projects/ids | Returns projects&#39; internal identifiers.
[**getById7**](ProjectsClassicApi.md#getById7) | **GET** /projects/{projectId} | Returns project details.
[**getContacts**](ProjectsClassicApi.md#getContacts) | **GET** /projects/{projectId}/contacts | Returns contacts of a given project.
[**getCustomFields5**](ProjectsClassicApi.md#getCustomFields5) | **GET** /projects/{projectId}/customFields | Returns custom fields of a given project.
[**getDates1**](ProjectsClassicApi.md#getDates1) | **GET** /projects/{projectId}/dates | Returns dates of a given project.
[**getFileById**](ProjectsClassicApi.md#getFileById) | **GET** /projects/files/{fileId}/download | Downloads a file.
[**getFinance**](ProjectsClassicApi.md#getFinance) | **GET** /projects/{projectId}/finance | Returns finance of a given project.
[**getInstructions**](ProjectsClassicApi.md#getInstructions) | **GET** /projects/{projectId}/instructions | Returns instructions of a given project.
[**updateContacts**](ProjectsClassicApi.md#updateContacts) | **PUT** /projects/{projectId}/contacts | Updates contacts of a given project.
[**updateCustomFields3**](ProjectsClassicApi.md#updateCustomFields3) | **PUT** /projects/{projectId}/customFields | Updates custom fields of a given project.
[**updateDates1**](ProjectsClassicApi.md#updateDates1) | **PUT** /projects/{projectId}/dates | Updates dates of a given project.
[**updateInstructions1**](ProjectsClassicApi.md#updateInstructions1) | **PUT** /projects/{projectId}/instructions | Updates instructions of a given project.
[**updatePayable**](ProjectsClassicApi.md#updatePayable) | **PUT** /projects/{projectId}/finance/payables/{payableId} | Updates a payable.
[**updateReceivable**](ProjectsClassicApi.md#updateReceivable) | **PUT** /projects/{projectId}/finance/receivables/{receivableId} | Updates a receivable.



## create5

> ProjectDTOv1 create5(classicProjectCreateDTO)

Creates a new Classic Project.

Creates a new Classic Project. If the specified service ID refers to Smart Project, 400 Bad Request is returned instead.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let classicProjectCreateDTO = /home-api/assets/examples/v1/projects/createProject.json#requestBody; // ClassicProjectCreateDTO | Created a new Classic Project.
apiInstance.create5(classicProjectCreateDTO, (error, data, response) => {
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
 **classicProjectCreateDTO** | [**ClassicProjectCreateDTO**](ClassicProjectCreateDTO.md)| Created a new Classic Project. | 

### Return type

[**ProjectDTOv1**](ProjectDTOv1.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## createLanguageCombination

> CommonLanguageCombinationDTO createLanguageCombination(projectId, commonLanguageCombinationDTO)

Creates a new language combination for a given project without creating a task.

Creates a new language combination for a given project without creating a task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let commonLanguageCombinationDTO = /home-api/assets/examples/v1/projects/createLanguageCombination.json#requestBody; // CommonLanguageCombinationDTO | Created language combination for a given project without creating a task.
apiInstance.createLanguageCombination(projectId, commonLanguageCombinationDTO, (error, data, response) => {
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
 **commonLanguageCombinationDTO** | [**CommonLanguageCombinationDTO**](CommonLanguageCombinationDTO.md)| Created language combination for a given project without creating a task. | 

### Return type

[**CommonLanguageCombinationDTO**](CommonLanguageCombinationDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## createPayable

> PayableDTO createPayable(projectId, payableCreateDTO)

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

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let payableCreateDTO = /home-api/assets/examples/v1/projects/createPayable.json#requestBody; // PayableCreateDTO | 
apiInstance.createPayable(projectId, payableCreateDTO, (error, data, response) => {
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


## createReceivable

> ReceivableDTO createReceivable(projectId, receivableCreateDTO)

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

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let receivableCreateDTO = /home-api/assets/examples/v1/projects/createReceivable.json#requestBody; // ReceivableCreateDTO | 
apiInstance.createReceivable(projectId, receivableCreateDTO, (error, data, response) => {
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


## createTask

> TaskDTO createTask(projectId, taskCreateDTO)

Creates a new task for a given project.

Creates a new task for a given project.&lt;p&gt;   Required fields:   &lt;ul&gt;     &lt;li&gt;languageCombination&lt;/li&gt;     &lt;li&gt;specializationId&lt;/li&gt;     &lt;li&gt;workflowId&lt;/li&gt;   &lt;/ul&gt; &lt;/p&gt; 

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let taskCreateDTO = /home-api/assets/examples/v1/projects/createTask.json#requestBody; // TaskCreateDTO | Created new task for a given project.
apiInstance.createTask(projectId, taskCreateDTO, (error, data, response) => {
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
 **taskCreateDTO** | [**TaskCreateDTO**](TaskCreateDTO.md)| Created new task for a given project. | 

### Return type

[**TaskDTO**](TaskDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## delete12

> delete12(projectId)

Removes a project.

Removes a project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.delete12(projectId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePayable

> deletePayable(projectId, payableId)

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

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let payableId = 789; // Number | payable's internal identifier
apiInstance.deletePayable(projectId, payableId, (error, data, response) => {
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


## deleteReceivable

> deleteReceivable(projectId, receivableId)

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

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let receivableId = 789; // Number | receivable's internal identifier
apiInstance.deleteReceivable(projectId, receivableId, (error, data, response) => {
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


## getAllIds6

> [Number] getAllIds6(opts)

Returns projects&#39; internal identifiers.

Returns projects&#39; internal identifiers.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let opts = {
  'updatedSince': 789 // Number | only projects modified since this timestamp
};
apiInstance.getAllIds6(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only projects modified since this timestamp | [optional] 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getById7

> ProjectDTOv1 getById7(projectId, opts)

Returns project details.

Returns project details. If the specified project ID refers to Smart Project, 400 Bad Request is returned instead.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let opts = {
  'embed': "embed_example" // String | list of additional fields which should be embedded in the response (available options: tasks)
};
apiInstance.getById7(projectId, opts, (error, data, response) => {
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
 **embed** | **String**| list of additional fields which should be embedded in the response (available options: tasks) | [optional] 

### Return type

[**ProjectDTOv1**](ProjectDTOv1.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getContacts

> ContactsDTO getContacts(projectId)

Returns contacts of a given project.

Returns contacts of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getContacts(projectId, (error, data, response) => {
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

[**ContactsDTO**](ContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCustomFields5

> [CustomFieldDTO] getCustomFields5(projectId)

Returns custom fields of a given project.

Returns custom fields of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getCustomFields5(projectId, (error, data, response) => {
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
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getDates1

> ProjectDatesDTO getDates1(projectId)

Returns dates of a given project.

Returns dates of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getDates1(projectId, (error, data, response) => {
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

[**ProjectDatesDTO**](ProjectDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getFileById

> getFileById(fileId)

Downloads a file.

Downloads a file.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let fileId = "fileId_example"; // String | file's internal identifier
apiInstance.getFileById(fileId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: multipart/form-data


## getFinance

> FinanceDTO getFinance(projectId)

Returns finance of a given project.

Returns finance of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getFinance(projectId, (error, data, response) => {
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
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getInstructions

> InstructionsDTO getInstructions(projectId)

Returns instructions of a given project.

Returns instructions of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
apiInstance.getInstructions(projectId, (error, data, response) => {
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

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateContacts

> ContactsDTO updateContacts(projectId, contactsDTO)

Updates contacts of a given project.

Updates contacts of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let contactsDTO = /home-api/assets/examples/v1/projects/updateContacts.json#requestBody; // ContactsDTO | Updated contacts of a given project.
apiInstance.updateContacts(projectId, contactsDTO, (error, data, response) => {
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
 **contactsDTO** | [**ContactsDTO**](ContactsDTO.md)| Updated contacts of a given project. | 

### Return type

[**ContactsDTO**](ContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCustomFields3

> [CustomFieldDTO] updateCustomFields3(projectId, customFieldDTO)

Updates custom fields of a given project.

Updates custom fields of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let customFieldDTO = /home-api/assets/examples/v1/projects/updateCustomFields.json#requestBody; // [CustomFieldDTO] | Updated custom fields of a given project.
apiInstance.updateCustomFields3(projectId, customFieldDTO, (error, data, response) => {
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
 **customFieldDTO** | [**[CustomFieldDTO]**](CustomFieldDTO.md)| Updated custom fields of a given project. | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateDates1

> ProjectDatesDTO updateDates1(projectId, projectDatesDTO)

Updates dates of a given project.

Updates dates of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let projectDatesDTO = /home-api/assets/examples/v1/projects/updateDates.json#requestBody; // ProjectDatesDTO | Updated dates of a given project..
apiInstance.updateDates1(projectId, projectDatesDTO, (error, data, response) => {
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
 **projectDatesDTO** | [**ProjectDatesDTO**](ProjectDatesDTO.md)| Updated dates of a given project.. | 

### Return type

[**ProjectDatesDTO**](ProjectDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateInstructions1

> InstructionsDTO updateInstructions1(projectId, instructionsDTO)

Updates instructions of a given project.

Updates instructions of a given project.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let instructionsDTO = /home-api/assets/examples/v1/projects/updateInstructions.json#requestBody; // InstructionsDTO | Updated instructions of a given project.
apiInstance.updateInstructions1(projectId, instructionsDTO, (error, data, response) => {
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
 **instructionsDTO** | [**InstructionsDTO**](InstructionsDTO.md)| Updated instructions of a given project. | 

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updatePayable

> PayableDTO updatePayable(projectId, payableId, payableDTO)

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

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let payableId = 789; // Number | payable's internal identifier
let payableDTO = /home-api/assets/examples/v1/projects/updatePayable.json#requestBody; // PayableDTO | 
apiInstance.updatePayable(projectId, payableId, payableDTO, (error, data, response) => {
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


## updateReceivable

> ReceivableDTO updateReceivable(projectId, receivableId, receivableDTO)

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

let apiInstance = new XtrfHomePortalApi.ProjectsClassicApi();
let projectId = "projectId_example"; // String | project's internal identifier
let receivableId = 789; // Number | receivable's internal identifier
let receivableDTO = /home-api/assets/examples/v1/projects/updateReceivable.json#requestBody; // ReceivableDTO | 
apiInstance.updateReceivable(projectId, receivableId, receivableDTO, (error, data, response) => {
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

