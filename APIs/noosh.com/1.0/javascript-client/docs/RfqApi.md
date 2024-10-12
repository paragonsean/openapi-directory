# NooshApiApplication.RfqApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRfq**](RfqApi.md#getRfq) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfqs/{rfq_id} | Get a specific Rfq
[**getRfqList**](RfqApi.md#getRfqList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfqs | List the rfqs



## getRfq

> RfqExpandVO getRfq(workgroupId, projectId, rfqId)

Get a specific Rfq

Get a specific Rfq

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.RfqApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let rfqId = "rfqId_example"; // String | 
apiInstance.getRfq(workgroupId, projectId, rfqId, (error, data, response) => {
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
 **rfqId** | **String**|  | 

### Return type

[**RfqExpandVO**](RfqExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getRfqList

> RfqListVO getRfqList(workgroupId, projectId)

List the rfqs

List the rfqs

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.RfqApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getRfqList(workgroupId, projectId, (error, data, response) => {
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

[**RfqListVO**](RfqListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

