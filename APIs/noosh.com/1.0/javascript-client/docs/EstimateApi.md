# NooshApiApplication.EstimateApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEstimate**](EstimateApi.md#getEstimate) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/estimates/{estimate_id} | Get a specific estimate of project
[**getEstimateList**](EstimateApi.md#getEstimateList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/estimates | List the Estimates
[**postEstimate**](EstimateApi.md#postEstimate) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/estimates | Create a Estimate



## getEstimate

> EstimateExpandVO getEstimate(workgroupId, projectId, estimateId)

Get a specific estimate of project

Get a specific estimate of project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.EstimateApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let estimateId = "estimateId_example"; // String | 
apiInstance.getEstimate(workgroupId, projectId, estimateId, (error, data, response) => {
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
 **estimateId** | **String**|  | 

### Return type

[**EstimateExpandVO**](EstimateExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getEstimateList

> EstimateListExpandVO getEstimateList(workgroupId, projectId)

List the Estimates

List the Estimates

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.EstimateApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getEstimateList(workgroupId, projectId, (error, data, response) => {
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

[**EstimateListExpandVO**](EstimateListExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postEstimate

> EstimatePO postEstimate(workgroupId, projectId, opts)

Create a Estimate

Create a Estimate

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.EstimateApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'estimatePO': new NooshApiApplication.EstimatePO() // EstimatePO | 
};
apiInstance.postEstimate(workgroupId, projectId, opts, (error, data, response) => {
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
 **estimatePO** | [**EstimatePO**](EstimatePO.md)|  | [optional] 

### Return type

[**EstimatePO**](EstimatePO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

