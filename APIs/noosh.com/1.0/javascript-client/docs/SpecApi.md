# NooshApiApplication.SpecApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProductTypeListOfWorkgroup**](SpecApi.md#getProductTypeListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/productTypes | Get product type of workgroup level
[**getSpec**](SpecApi.md#getSpec) | **GET** /1.1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id} | List a specific spec of project Level
[**getSpecList**](SpecApi.md#getSpecList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/specs | List specs of project Level
[**getSpecProductTypeListOfWorkgroup**](SpecApi.md#getSpecProductTypeListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/productTypesOfSpecTypes | Get product type of spec level by workgroupId
[**getSpecTypeFields**](SpecApi.md#getSpecTypeFields) | **GET** /1.1/workgroups/{workgroup_id}/specTypes/{spec_type_id}/specTypeFields | Get Spec Type Fields
[**postSpec**](SpecApi.md#postSpec) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/specs | Create a Spec
[**postSpecProductTypeListOfWorkgroup**](SpecApi.md#postSpecProductTypeListOfWorkgroup) | **POST** /v1/workgroups/{workgroup_id}/productTypesOfSpecTypes | Register product types for spec types
[**putSpec**](SpecApi.md#putSpec) | **PUT** /1.1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id} | Update a specific Spec
[**v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet**](SpecApi.md#v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id} | List a specific spec of project Level
[**v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut**](SpecApi.md#v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id} | Update a specific Spec
[**v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet**](SpecApi.md#v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet) | **GET** /v1/workgroups/{workgroup_id}/specTypes/{spec_type_id}/specTypeFields | Get Spec Type Fields



## getProductTypeListOfWorkgroup

> WorkgroupAttributeListVO getProductTypeListOfWorkgroup(workgroupId)

Get product type of workgroup level

Get product type of workgroup level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getProductTypeListOfWorkgroup(workgroupId, (error, data, response) => {
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

[**WorkgroupAttributeListVO**](WorkgroupAttributeListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSpec

> V1x1SpecExpandVO getSpec(workgroupId, projectId, specId)

List a specific spec of project Level

List a specific spec of project Level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let specId = "specId_example"; // String | 
apiInstance.getSpec(workgroupId, projectId, specId, (error, data, response) => {
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
 **specId** | **String**|  | 

### Return type

[**V1x1SpecExpandVO**](V1x1SpecExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSpecList

> SpecListVO getSpecList(workgroupId, projectId)

List specs of project Level

List specs of project Level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getSpecList(workgroupId, projectId, (error, data, response) => {
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

[**SpecListVO**](SpecListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSpecProductTypeListOfWorkgroup

> WorkgroupAttributeListVO getSpecProductTypeListOfWorkgroup(workgroupId)

Get product type of spec level by workgroupId

Get product type of spec level by workgroupId

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getSpecProductTypeListOfWorkgroup(workgroupId, (error, data, response) => {
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

[**WorkgroupAttributeListVO**](WorkgroupAttributeListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSpecTypeFields

> SpecTypeFieldsListVO getSpecTypeFields(workgroupId, specTypeId)

Get Spec Type Fields

Get Spec Type Fields

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let specTypeId = "specTypeId_example"; // String | 
apiInstance.getSpecTypeFields(workgroupId, specTypeId, (error, data, response) => {
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
 **specTypeId** | **String**|  | 

### Return type

[**SpecTypeFieldsListVO**](SpecTypeFieldsListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postSpec

> SpecVO postSpec(workgroupId, projectId, opts)

Create a Spec

Create a Spec

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'specPersistVO': new NooshApiApplication.SpecPersistVO() // SpecPersistVO | 
};
apiInstance.postSpec(workgroupId, projectId, opts, (error, data, response) => {
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
 **specPersistVO** | [**SpecPersistVO**](SpecPersistVO.md)|  | [optional] 

### Return type

[**SpecVO**](SpecVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postSpecProductTypeListOfWorkgroup

> WgSpecPrdTypeRegPersistVO postSpecProductTypeListOfWorkgroup(workgroupId, opts)

Register product types for spec types

Register product types for spec types

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let opts = {
  'wgSpecPrdTypeRegPersistVO': new NooshApiApplication.WgSpecPrdTypeRegPersistVO() // WgSpecPrdTypeRegPersistVO | 
};
apiInstance.postSpecProductTypeListOfWorkgroup(workgroupId, opts, (error, data, response) => {
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
 **wgSpecPrdTypeRegPersistVO** | [**WgSpecPrdTypeRegPersistVO**](WgSpecPrdTypeRegPersistVO.md)|  | [optional] 

### Return type

[**WgSpecPrdTypeRegPersistVO**](WgSpecPrdTypeRegPersistVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## putSpec

> SpecHTTPStatusVO putSpec(workgroupId, projectId, specId, opts)

Update a specific Spec

Update a specific Spec

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let specId = "specId_example"; // String | 
let opts = {
  'v1X1SpecUpdatingPO': new NooshApiApplication.V1X1SpecUpdatingPO() // V1X1SpecUpdatingPO | 
};
apiInstance.putSpec(workgroupId, projectId, specId, opts, (error, data, response) => {
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
 **specId** | **String**|  | 
 **v1X1SpecUpdatingPO** | [**V1X1SpecUpdatingPO**](V1X1SpecUpdatingPO.md)|  | [optional] 

### Return type

[**SpecHTTPStatusVO**](SpecHTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet

> SpecListVO v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet(workgroupId, projectId, specId)

List a specific spec of project Level

List a specific spec of project Level

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let specId = "specId_example"; // String | 
apiInstance.v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet(workgroupId, projectId, specId, (error, data, response) => {
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
 **specId** | **String**|  | 

### Return type

[**SpecListVO**](SpecListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut

> SpecHTTPStatusVO v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut(workgroupId, projectId, specId, opts)

Update a specific Spec

Update a specific Spec

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let specId = "specId_example"; // String | 
let opts = {
  'specUpdatePersistVO': new NooshApiApplication.SpecUpdatePersistVO() // SpecUpdatePersistVO | 
};
apiInstance.v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut(workgroupId, projectId, specId, opts, (error, data, response) => {
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
 **specId** | **String**|  | 
 **specUpdatePersistVO** | [**SpecUpdatePersistVO**](SpecUpdatePersistVO.md)|  | [optional] 

### Return type

[**SpecHTTPStatusVO**](SpecHTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet

> PropertyParamListVO v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet(workgroupId, specTypeId)

Get Spec Type Fields

Get Spec Type Fields

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.SpecApi();
let workgroupId = "workgroupId_example"; // String | 
let specTypeId = "specTypeId_example"; // String | 
apiInstance.v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet(workgroupId, specTypeId, (error, data, response) => {
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
 **specTypeId** | **String**|  | 

### Return type

[**PropertyParamListVO**](PropertyParamListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

