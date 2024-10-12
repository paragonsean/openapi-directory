# NooshApiApplication.UserFieldsApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProjectHomeUserFieldListOfClient**](UserFieldsApi.md#getProjectHomeUserFieldListOfClient) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}/projectHomeUserFields | List projec home user fields of client workgroup
[**getProjectHomeUserFieldsList**](UserFieldsApi.md#getProjectHomeUserFieldsList) | **GET** /v1/workgroups/{workgroup_id}/projectHomeUserFields | List projec home user fields



## getProjectHomeUserFieldListOfClient

> ProjectHomeUserFieldsListVO getProjectHomeUserFieldListOfClient(workgroupId, clientWorkgroupId)

List projec home user fields of client workgroup

List projec home user fields of client workgroup

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.UserFieldsApi();
let workgroupId = "workgroupId_example"; // String | 
let clientWorkgroupId = "clientWorkgroupId_example"; // String | 
apiInstance.getProjectHomeUserFieldListOfClient(workgroupId, clientWorkgroupId, (error, data, response) => {
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

[**ProjectHomeUserFieldsListVO**](ProjectHomeUserFieldsListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getProjectHomeUserFieldsList

> ProjectHomeUserFieldsListVO getProjectHomeUserFieldsList(workgroupId)

List projec home user fields

List projec home user fields

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.UserFieldsApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getProjectHomeUserFieldsList(workgroupId, (error, data, response) => {
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

[**ProjectHomeUserFieldsListVO**](ProjectHomeUserFieldsListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

