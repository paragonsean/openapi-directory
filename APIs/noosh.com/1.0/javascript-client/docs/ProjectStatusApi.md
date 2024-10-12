# NooshApiApplication.ProjectStatusApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProjectStatus**](ProjectStatusApi.md#getProjectStatus) | **GET** /v1/workgroups/{workgroup_id}/projectStatus | List the project status
[**getProjectStatusOfClient**](ProjectStatusApi.md#getProjectStatusOfClient) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}/projectStatus | List the project status of client



## getProjectStatus

> ProjectStatusListVO getProjectStatus(workgroupId)

List the project status

List the project status

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectStatusApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getProjectStatus(workgroupId, (error, data, response) => {
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

[**ProjectStatusListVO**](ProjectStatusListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getProjectStatusOfClient

> ProjectStatusListVO getProjectStatusOfClient(workgroupId, clientWorkgroupId)

List the project status of client

List the project status of client

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectStatusApi();
let workgroupId = "workgroupId_example"; // String | 
let clientWorkgroupId = "clientWorkgroupId_example"; // String | 
apiInstance.getProjectStatusOfClient(workgroupId, clientWorkgroupId, (error, data, response) => {
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
 **clientWorkgroupId** | **String**|  | 

### Return type

[**ProjectStatusListVO**](ProjectStatusListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

