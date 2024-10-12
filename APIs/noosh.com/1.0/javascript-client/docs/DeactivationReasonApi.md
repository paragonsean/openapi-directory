# NooshApiApplication.DeactivationReasonApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeactivationReasonList**](DeactivationReasonApi.md#getDeactivationReasonList) | **GET** /v1/workgroups/{workgroup_id}/deactivationReasons | List all deactivation reasons



## getDeactivationReasonList

> DeactivationReasonListVO getDeactivationReasonList(workgroupId)

List all deactivation reasons

List all deactivation reasons

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.DeactivationReasonApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getDeactivationReasonList(workgroupId, (error, data, response) => {
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

[**DeactivationReasonListVO**](DeactivationReasonListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

