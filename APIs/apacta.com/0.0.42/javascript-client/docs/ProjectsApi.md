# Apacta.ProjectsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectsGet**](ProjectsApi.md#projectsGet) | **GET** /projects | View list of projects
[**projectsHasProjectsWithCustomStatusesGet_0**](ProjectsApi.md#projectsHasProjectsWithCustomStatusesGet_0) | **GET** /projects/has_projects_with_custom_statuses | Check if the company has projects with custom statuses
[**projectsPost**](ProjectsApi.md#projectsPost) | **POST** /projects | Add a project
[**projectsProjectIdAllFilesGet**](ProjectsApi.md#projectsProjectIdAllFilesGet) | **GET** /projects/{project_id}/all_files | Show list of all files uploaded to project
[**projectsProjectIdDelete**](ProjectsApi.md#projectsProjectIdDelete) | **DELETE** /projects/{project_id} | Delete a project
[**projectsProjectIdFilesFileIdDelete**](ProjectsApi.md#projectsProjectIdFilesFileIdDelete) | **DELETE** /projects/{project_id}/files/{file_id}/ | Delete file
[**projectsProjectIdFilesFileIdGet**](ProjectsApi.md#projectsProjectIdFilesFileIdGet) | **GET** /projects/{project_id}/files/{file_id}/ | Show file
[**projectsProjectIdFilesFileIdPut**](ProjectsApi.md#projectsProjectIdFilesFileIdPut) | **PUT** /projects/{project_id}/files/{file_id}/ | Edit file
[**projectsProjectIdFilesGet**](ProjectsApi.md#projectsProjectIdFilesGet) | **GET** /projects/{project_id}/files | Show list of files uploaded to project
[**projectsProjectIdGet**](ProjectsApi.md#projectsProjectIdGet) | **GET** /projects/{project_id} | View specific project
[**projectsProjectIdProjectFilesGet**](ProjectsApi.md#projectsProjectIdProjectFilesGet) | **GET** /projects/{project_id}/project_files | Show list of project files uploaded to project
[**projectsProjectIdProjectFilesPost**](ProjectsApi.md#projectsProjectIdProjectFilesPost) | **POST** /projects/{project_id}/project_files | Add project file to projects
[**projectsProjectIdProjectFilesProjectFileIdDelete**](ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdDelete) | **DELETE** /projects/{project_id}/project_files/{project_file_id}/ | Delete project file
[**projectsProjectIdProjectFilesProjectFileIdGet**](ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdGet) | **GET** /projects/{project_id}/project_files/{project_file_id}/ | Show project file
[**projectsProjectIdProjectFilesProjectFileIdPut**](ProjectsApi.md#projectsProjectIdProjectFilesProjectFileIdPut) | **PUT** /projects/{project_id}/project_files/{project_file_id}/ | Edit project file
[**projectsProjectIdPut**](ProjectsApi.md#projectsProjectIdPut) | **PUT** /projects/{project_id} | Edit a project
[**projectsProjectIdSendBulkPdfPost**](ProjectsApi.md#projectsProjectIdSendBulkPdfPost) | **POST** /projects/{project_id}/send_bulk_pdf | Send bulk forms pdf by email
[**projectsProjectIdUsersGet**](ProjectsApi.md#projectsProjectIdUsersGet) | **GET** /projects/{project_id}/users/ | Show list of users added to project
[**projectsProjectIdUsersPost**](ProjectsApi.md#projectsProjectIdUsersPost) | **POST** /projects/{project_id}/users/ | Add user to project
[**projectsProjectIdUsersUserIdDelete**](ProjectsApi.md#projectsProjectIdUsersUserIdDelete) | **DELETE** /projects/{project_id}/users/{user_id} | Delete user from project
[**projectsProjectIdUsersUserIdGet**](ProjectsApi.md#projectsProjectIdUsersUserIdGet) | **GET** /projects/{project_id}/users/{user_id} | View specific user assigned to project



## projectsGet

> ProjectsGet200Response projectsGet(opts)

View list of projects

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let opts = {
  'showAll': false, // Boolean | Unless this is set to `true` only open projects will be shown
  'sort': "sort_example", // String | Sort projects by `not_invoiced_amount`
  'direction': "direction_example", // String | 
  'contactId': "contactId_example", // String | Used to filter on the `contact_id` of the projects
  'companyId': "companyId_example", // String | Used to filter on the `company_id` of the projects
  'projectStatusId': "projectStatusId_example", // String | Used to filter on the `project_status_id` of the projects
  'projectStatusIds': ["null"], // [String] | Used to filter on the `project_status_id` of the projects (match any of the provided values)
  'name': "name_example", // String | Used to search on the `name` of the projects
  'erpProjectId': "erpProjectId_example", // String | Used to search on the `erp_project_id` of the projects
  'erpTaskId': "erpTaskId_example", // String | Used to search on the `erp_task_id` of the projects
  'startTimeGte': "startTimeGte_example", // String | Show projects with start time after than this value
  'startTimeLte': "startTimeLte_example", // String | Show projects with start time before this value
  'startTimeEq': "startTimeEq_example", // String | Show only projects with start time on specific date
  'eventStartGt': "eventStartGt_example", // String | 
  'eventStartLt': "eventStartLt_example", // String | 
  'eventStartEq': "eventStartEq_example", // String | 
  'eventEndGt': "eventEndGt_example", // String | 
  'eventEndLt': "eventEndLt_example", // String | 
  'eventEndEq': "eventEndEq_example" // String | 
};
apiInstance.projectsGet(opts, (error, data, response) => {
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
 **showAll** | **Boolean**| Unless this is set to &#x60;true&#x60; only open projects will be shown | [optional] [default to false]
 **sort** | **String**| Sort projects by &#x60;not_invoiced_amount&#x60; | [optional] 
 **direction** | **String**|  | [optional] 
 **contactId** | **String**| Used to filter on the &#x60;contact_id&#x60; of the projects | [optional] 
 **companyId** | **String**| Used to filter on the &#x60;company_id&#x60; of the projects | [optional] 
 **projectStatusId** | **String**| Used to filter on the &#x60;project_status_id&#x60; of the projects | [optional] 
 **projectStatusIds** | [**[String]**](String.md)| Used to filter on the &#x60;project_status_id&#x60; of the projects (match any of the provided values) | [optional] 
 **name** | **String**| Used to search on the &#x60;name&#x60; of the projects | [optional] 
 **erpProjectId** | **String**| Used to search on the &#x60;erp_project_id&#x60; of the projects | [optional] 
 **erpTaskId** | **String**| Used to search on the &#x60;erp_task_id&#x60; of the projects | [optional] 
 **startTimeGte** | **String**| Show projects with start time after than this value | [optional] 
 **startTimeLte** | **String**| Show projects with start time before this value | [optional] 
 **startTimeEq** | **String**| Show only projects with start time on specific date | [optional] 
 **eventStartGt** | **String**|  | [optional] 
 **eventStartLt** | **String**|  | [optional] 
 **eventStartEq** | **String**|  | [optional] 
 **eventEndGt** | **String**|  | [optional] 
 **eventEndLt** | **String**|  | [optional] 
 **eventEndEq** | **String**|  | [optional] 

### Return type

[**ProjectsGet200Response**](ProjectsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsHasProjectsWithCustomStatusesGet_0

> ProjectsHasProjectsWithCustomStatusesGet200Response projectsHasProjectsWithCustomStatusesGet_0()

Check if the company has projects with custom statuses

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
apiInstance.projectsHasProjectsWithCustomStatusesGet_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ProjectsHasProjectsWithCustomStatusesGet200Response**](ProjectsHasProjectsWithCustomStatusesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsPost

> ClockingRecordsPost201Response projectsPost(opts)

Add a project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let opts = {
  'projectsPostRequest': new Apacta.ProjectsPostRequest() // ProjectsPostRequest | 
};
apiInstance.projectsPost(opts, (error, data, response) => {
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
 **projectsPostRequest** | [**ProjectsPostRequest**](ProjectsPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsProjectIdAllFilesGet

> ProjectsProjectIdAllFilesGet200Response projectsProjectIdAllFilesGet(projectId)

Show list of all files uploaded to project

Used to show files uploaded to a project from form, expense and project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdAllFilesGet(projectId, (error, data, response) => {
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

[**ProjectsProjectIdAllFilesGet200Response**](ProjectsProjectIdAllFilesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdDelete

> ClockingRecordsClockingRecordIdDelete200Response projectsProjectIdDelete(projectId)

Delete a project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdDelete(projectId, (error, data, response) => {
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

[**ClockingRecordsClockingRecordIdDelete200Response**](ClockingRecordsClockingRecordIdDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdFilesFileIdDelete

> ExpenseFilesExpenseFileIdPut200Response projectsProjectIdFilesFileIdDelete(projectId, fileId)

Delete file

Delete file uploaded to a project from wall post or form

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let fileId = "fileId_example"; // String | 
apiInstance.projectsProjectIdFilesFileIdDelete(projectId, fileId, (error, data, response) => {
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
 **fileId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdFilesFileIdGet

> ExpenseFilesExpenseFileIdPut200Response projectsProjectIdFilesFileIdGet(projectId, fileId)

Show file

Show file uploaded to a project from wall post or form

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let fileId = "fileId_example"; // String | 
apiInstance.projectsProjectIdFilesFileIdGet(projectId, fileId, (error, data, response) => {
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
 **fileId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdFilesFileIdPut

> ExpenseFilesExpenseFileIdPut200Response projectsProjectIdFilesFileIdPut(projectId, fileId)

Edit file

Edit file uploaded to a project from wall post or form

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let fileId = "fileId_example"; // String | 
apiInstance.projectsProjectIdFilesFileIdPut(projectId, fileId, (error, data, response) => {
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
 **fileId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdFilesGet

> ProjectsProjectIdAllFilesGet200Response projectsProjectIdFilesGet(projectId)

Show list of files uploaded to project

Used to show files uploaded to a project from wall post or form

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdFilesGet(projectId, (error, data, response) => {
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

[**ProjectsProjectIdAllFilesGet200Response**](ProjectsProjectIdAllFilesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdGet

> ProjectsProjectIdGet200Response projectsProjectIdGet(projectId)

View specific project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdGet(projectId, (error, data, response) => {
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

[**ProjectsProjectIdGet200Response**](ProjectsProjectIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdProjectFilesGet

> ProjectsProjectIdAllFilesGet200Response projectsProjectIdProjectFilesGet(projectId)

Show list of project files uploaded to project

Returns files belonging to the project, not uploaded from wall post or form

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdProjectFilesGet(projectId, (error, data, response) => {
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

[**ProjectsProjectIdAllFilesGet200Response**](ProjectsProjectIdAllFilesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdProjectFilesPost

> ClockingRecordsPost201Response projectsProjectIdProjectFilesPost(projectId, file)

Add project file to projects

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let file = "/path/to/file"; // File | 
apiInstance.projectsProjectIdProjectFilesPost(projectId, file, (error, data, response) => {
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
 **file** | **File**|  | 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## projectsProjectIdProjectFilesProjectFileIdDelete

> ExpenseFilesExpenseFileIdPut200Response projectsProjectIdProjectFilesProjectFileIdDelete(projectFileId, projectId)

Delete project file

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectFileId = "projectFileId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdProjectFilesProjectFileIdDelete(projectFileId, projectId, (error, data, response) => {
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
 **projectFileId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdProjectFilesProjectFileIdGet

> ExpenseFilesExpenseFileIdPut200Response projectsProjectIdProjectFilesProjectFileIdGet(projectId, projectFileId)

Show project file

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let projectFileId = "projectFileId_example"; // String | 
apiInstance.projectsProjectIdProjectFilesProjectFileIdGet(projectId, projectFileId, (error, data, response) => {
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
 **projectFileId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdProjectFilesProjectFileIdPut

> ExpenseFilesExpenseFileIdPut200Response projectsProjectIdProjectFilesProjectFileIdPut(projectId, projectFileId)

Edit project file

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let projectFileId = "projectFileId_example"; // String | 
apiInstance.projectsProjectIdProjectFilesProjectFileIdPut(projectId, projectFileId, (error, data, response) => {
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
 **projectFileId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdPut

> ClockingRecordsClockingRecordIdPut200Response projectsProjectIdPut(projectId, opts)

Edit a project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let opts = {
  'projectsProjectIdPutRequest': new Apacta.ProjectsProjectIdPutRequest() // ProjectsProjectIdPutRequest | 
};
apiInstance.projectsProjectIdPut(projectId, opts, (error, data, response) => {
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
 **projectsProjectIdPutRequest** | [**ProjectsProjectIdPutRequest**](ProjectsProjectIdPutRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsProjectIdSendBulkPdfPost

> EmptySuccessResponse projectsProjectIdSendBulkPdfPost(projectId, projectsProjectIdSendBulkPdfPostRequest)

Send bulk forms pdf by email

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let projectsProjectIdSendBulkPdfPostRequest = new Apacta.ProjectsProjectIdSendBulkPdfPostRequest(); // ProjectsProjectIdSendBulkPdfPostRequest | 
apiInstance.projectsProjectIdSendBulkPdfPost(projectId, projectsProjectIdSendBulkPdfPostRequest, (error, data, response) => {
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
 **projectsProjectIdSendBulkPdfPostRequest** | [**ProjectsProjectIdSendBulkPdfPostRequest**](ProjectsProjectIdSendBulkPdfPostRequest.md)|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsProjectIdUsersGet

> ProjectsProjectIdUsersGet200Response projectsProjectIdUsersGet(projectId)

Show list of users added to project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdUsersGet(projectId, (error, data, response) => {
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

[**ProjectsProjectIdUsersGet200Response**](ProjectsProjectIdUsersGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdUsersPost

> ClockingRecordsPost201Response projectsProjectIdUsersPost(projectId, opts)

Add user to project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let projectId = "projectId_example"; // String | 
let opts = {
  'projectsProjectIdUsersPostRequest': new Apacta.ProjectsProjectIdUsersPostRequest() // ProjectsProjectIdUsersPostRequest | 
};
apiInstance.projectsProjectIdUsersPost(projectId, opts, (error, data, response) => {
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
 **projectsProjectIdUsersPostRequest** | [**ProjectsProjectIdUsersPostRequest**](ProjectsProjectIdUsersPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsProjectIdUsersUserIdDelete

> ClockingRecordsClockingRecordIdPut200Response projectsProjectIdUsersUserIdDelete(userId, projectId)

Delete user from project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let userId = "userId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdUsersUserIdDelete(userId, projectId, (error, data, response) => {
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
 **userId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsProjectIdUsersUserIdGet

> ProjectsProjectIdUsersUserIdGet200Response projectsProjectIdUsersUserIdGet(userId, projectId)

View specific user assigned to project

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ProjectsApi();
let userId = "userId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.projectsProjectIdUsersUserIdGet(userId, projectId, (error, data, response) => {
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
 **userId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**ProjectsProjectIdUsersUserIdGet200Response**](ProjectsProjectIdUsersUserIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

