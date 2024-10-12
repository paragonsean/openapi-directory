# NooshApiApplication.RFEApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRfe**](RFEApi.md#getRfe) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfes/{rfe_id} | Get a specific Rfe
[**getRfeList**](RFEApi.md#getRfeList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfes | List the RFES
[**postRfe**](RFEApi.md#postRfe) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfes | Create a RFE



## getRfe

> RfeExpandVO getRfe(workgroupId, projectId, rfeId)

Get a specific Rfe

Get a specific Rfe

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.RFEApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let rfeId = "rfeId_example"; // String | 
apiInstance.getRfe(workgroupId, projectId, rfeId, (error, data, response) => {
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
 **rfeId** | **String**|  | 

### Return type

[**RfeExpandVO**](RfeExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getRfeList

> RfeListVO getRfeList(workgroupId, projectId)

List the RFES

List the RFES

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.RFEApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getRfeList(workgroupId, projectId, (error, data, response) => {
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

[**RfeListVO**](RfeListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postRfe

> RfqVO postRfe(workgroupId, projectId, opts)

Create a RFE

Create a RFE

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.RFEApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'rfePO': new NooshApiApplication.RfePO() // RfePO | 
};
apiInstance.postRfe(workgroupId, projectId, opts, (error, data, response) => {
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
 **rfePO** | [**RfePO**](RfePO.md)|  | [optional] 

### Return type

[**RfqVO**](RfqVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

