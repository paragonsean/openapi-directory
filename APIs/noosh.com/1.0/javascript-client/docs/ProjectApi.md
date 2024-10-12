# NooshApiApplication.ProjectApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachProject**](ProjectApi.md#attachProject) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/children | Attach children projects to specific Project
[**deleteProject**](ProjectApi.md#deleteProject) | **DELETE** /v1/workgroups/{workgroup_id}/projects/{project_id} | Archieve a specific Project
[**getProject**](ProjectApi.md#getProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id} | Get a specific Project
[**getProjectList**](ProjectApi.md#getProjectList) | **GET** /v1/workgroups/{workgroup_id}/projects | List the projects
[**patchProject**](ProjectApi.md#patchProject) | **PATCH** /v1/workgroups/{workgroup_id}/projects/{project_id} | Patch a specific Project
[**postProject**](ProjectApi.md#postProject) | **POST** /v1/workgroups/{workgroup_id}/projects | Create a Project
[**putProject**](ProjectApi.md#putProject) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id} | Update a specific Project



## attachProject

> HTTPStatusVO attachProject(workgroupId, projectId, opts)

Attach children projects to specific Project

Attach children projects to specific Project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'projectIdListVO': new NooshApiApplication.ProjectIdListVO() // ProjectIdListVO | 
};
apiInstance.attachProject(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **projectIdListVO** | [**ProjectIdListVO**](ProjectIdListVO.md)|  | [optional] 

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## deleteProject

> HTTPStatusVO deleteProject(workgroupId, projectId)

Archieve a specific Project

Archieve a specific Project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.deleteProject(workgroupId, projectId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getProject

> ProjectExpandVO getProject(workgroupId, projectId)

Get a specific Project

Get a specific Project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getProject(workgroupId, projectId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**ProjectExpandVO**](ProjectExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getProjectList

> ProjectListVO getProjectList(workgroupId)

List the projects

List the projects

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getProjectList(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**ProjectListVO**](ProjectListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## patchProject

> HTTPStatusVO patchProject(workgroupId, projectId, opts)

Patch a specific Project

Patch a specific Project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'projectPatchPO': new NooshApiApplication.ProjectPatchPO() // ProjectPatchPO | 
};
apiInstance.patchProject(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **projectPatchPO** | [**ProjectPatchPO**](ProjectPatchPO.md)|  | [optional] 

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postProject

> ProjectVO postProject(workgroupId, opts)

Create a Project

Create a Project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectApi();
let workgroupId = "workgroupId_example"; // String | 
let opts = {
  'projectPersistVO': new NooshApiApplication.ProjectPersistVO() // ProjectPersistVO | 
};
apiInstance.postProject(workgroupId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectPersistVO** | [**ProjectPersistVO**](ProjectPersistVO.md)|  | [optional] 

### Return type

[**ProjectVO**](ProjectVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## putProject

> HTTPStatusVO putProject(workgroupId, projectId, opts)

Update a specific Project

Update a specific Project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'projectPersistVO': new NooshApiApplication.ProjectPersistVO() // ProjectPersistVO | 
};
apiInstance.putProject(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **projectPersistVO** | [**ProjectPersistVO**](ProjectPersistVO.md)|  | [optional] 

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

