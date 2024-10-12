# NooshApiApplication.ProjectCategoryApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProjectCategoryList**](ProjectCategoryApi.md#getProjectCategoryList) | **GET** /v1/workgroups/{workgroup_id}/projectCategory | List the project categories
[**getProjectCategoryListOfClient**](ProjectCategoryApi.md#getProjectCategoryListOfClient) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}/projectCategory | List the project categories of client side



## getProjectCategoryList

> ProjectCategoryListVO getProjectCategoryList(workgroupId)

List the project categories

List the project categories

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectCategoryApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getProjectCategoryList(workgroupId, (error, data, response) => {
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

[**ProjectCategoryListVO**](ProjectCategoryListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getProjectCategoryListOfClient

> ProjectCategoryListVO getProjectCategoryListOfClient(workgroupId, clientWorkgroupId)

List the project categories of client side

List the project categories of client side

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ProjectCategoryApi();
let workgroupId = "workgroupId_example"; // String | 
let clientWorkgroupId = "clientWorkgroupId_example"; // String | 
apiInstance.getProjectCategoryListOfClient(workgroupId, clientWorkgroupId, (error, data, response) => {
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

[**ProjectCategoryListVO**](ProjectCategoryListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

