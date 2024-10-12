# NooshApiApplication.SpecTemplateApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSpecTemplate**](SpecTemplateApi.md#getSpecTemplate) | **GET** /v1/workgroups/{workgroup_id}/specTemplates/{spec_template_id} | Get a specific Spec Template
[**getSpecTemplateList**](SpecTemplateApi.md#getSpecTemplateList) | **GET** /v1/workgroups/{workgroup_id}/specTemplates | List Spec Templates of Workgroup Level 



## getSpecTemplate

> SpecTemplateExpandVO getSpecTemplate(workgroupId, specTemplateId)

Get a specific Spec Template

Get a specific Spec Template

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecTemplateApi();
let workgroupId = "workgroupId_example"; // String | 
let specTemplateId = "specTemplateId_example"; // String | 
apiInstance.getSpecTemplate(workgroupId, specTemplateId, (error, data, response) => {
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
 **specTemplateId** | **String**|  | 

### Return type

[**SpecTemplateExpandVO**](SpecTemplateExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSpecTemplateList

> SpecTemplateListVO getSpecTemplateList(workgroupId)

List Spec Templates of Workgroup Level 

List Spec Templates of Workgroup Level 

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecTemplateApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getSpecTemplateList(workgroupId, (error, data, response) => {
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

[**SpecTemplateListVO**](SpecTemplateListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

