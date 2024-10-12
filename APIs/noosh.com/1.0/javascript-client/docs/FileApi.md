# NooshApiApplication.FileApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFile**](FileApi.md#getFile) | **GET** /1.1/workgroups/{workgroup_id}/projects/{project_id}/files/{file_id} | Get File from Project.  Works for Regular and Remote Files
[**getFileTags**](FileApi.md#getFileTags) | **GET** /1.1/workgroups/{workgroup_id}/projects/{project_id}/fileTags | List Tags from Workgroup and Project.
[**getFiles**](FileApi.md#getFiles) | **GET** /1.1/workgroups/{workgroup_id}/projects/{project_id}/files | List Files from Project.  Works for Regular and Remote Files
[**uploadFile**](FileApi.md#uploadFile) | **POST** /1.1/workgroups/{workgroup_id}/projects/{project_id}/files | Upload File to Project.  A multipart/form-data request with a name \&quot;file\&quot;



## getFile

> FileResponseVO getFile(workgroupId, projectId, fileId)

Get File from Project.  Works for Regular and Remote Files

Get File from Project.  Works for Regular and Remote Files

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.FileApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let fileId = "fileId_example"; // String | 
apiInstance.getFile(workgroupId, projectId, fileId, (error, data, response) => {
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
 **fileId** | **String**|  | 

### Return type

[**FileResponseVO**](FileResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getFileTags

> FileTagResponseVO getFileTags(workgroupId, projectId)

List Tags from Workgroup and Project.

List Tags from Workgroup and Project.

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.FileApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getFileTags(workgroupId, projectId, (error, data, response) => {
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

[**FileTagResponseVO**](FileTagResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getFiles

> FileResponseVO getFiles(workgroupId, projectId)

List Files from Project.  Works for Regular and Remote Files

List Files from Project.  Works for Regular and Remote Files

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.FileApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getFiles(workgroupId, projectId, (error, data, response) => {
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

[**FileResponseVO**](FileResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## uploadFile

> FileResponseVO uploadFile(workgroupId, projectId)

Upload File to Project.  A multipart/form-data request with a name \&quot;file\&quot;

Upload File to Project.  A multipart/form-data request with a name \&quot;file\&quot;

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.FileApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.uploadFile(workgroupId, projectId, (error, data, response) => {
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

[**FileResponseVO**](FileResponseVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

