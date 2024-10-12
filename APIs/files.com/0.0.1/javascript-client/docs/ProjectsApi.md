# FilesComApi.ProjectsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteProjectsId**](ProjectsApi.md#deleteProjectsId) | **DELETE** /projects/{id} | Delete Project
[**getProjects**](ProjectsApi.md#getProjects) | **GET** /projects | List Projects
[**getProjectsId**](ProjectsApi.md#getProjectsId) | **GET** /projects/{id} | Show Project
[**patchProjectsId**](ProjectsApi.md#patchProjectsId) | **PATCH** /projects/{id} | Update Project
[**postProjects**](ProjectsApi.md#postProjects) | **POST** /projects | Create Project



## deleteProjectsId

> deleteProjectsId(id)

Delete Project

Delete Project

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ProjectsApi();
let id = 56; // Number | Project ID.
apiInstance.deleteProjectsId(id, (error, data, response) => {
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
 **id** | **Number**| Project ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProjects

> [ProjectEntity] getProjects(opts)

List Projects

List Projects

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ProjectsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getProjects(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[ProjectEntity]**](ProjectEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectsId

> ProjectEntity getProjectsId(id)

Show Project

Show Project

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ProjectsApi();
let id = 56; // Number | Project ID.
apiInstance.getProjectsId(id, (error, data, response) => {
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
 **id** | **Number**| Project ID. | 

### Return type

[**ProjectEntity**](ProjectEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchProjectsId

> ProjectEntity patchProjectsId(id, globalAccess)

Update Project

Update Project

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ProjectsApi();
let id = 56; // Number | Project ID.
let globalAccess = "globalAccess_example"; // String | Global permissions.  Can be: `none`, `anyone_with_read`, `anyone_with_full`.
apiInstance.patchProjectsId(id, globalAccess, (error, data, response) => {
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
 **id** | **Number**| Project ID. | 
 **globalAccess** | **String**| Global permissions.  Can be: &#x60;none&#x60;, &#x60;anyone_with_read&#x60;, &#x60;anyone_with_full&#x60;. | 

### Return type

[**ProjectEntity**](ProjectEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postProjects

> ProjectEntity postProjects(globalAccess)

Create Project

Create Project

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.ProjectsApi();
let globalAccess = "globalAccess_example"; // String | Global permissions.  Can be: `none`, `anyone_with_read`, `anyone_with_full`.
apiInstance.postProjects(globalAccess, (error, data, response) => {
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
 **globalAccess** | **String**| Global permissions.  Can be: &#x60;none&#x60;, &#x60;anyone_with_read&#x60;, &#x60;anyone_with_full&#x60;. | 

### Return type

[**ProjectEntity**](ProjectEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

