# AkeneoPimRestApi.ReferenceEntityAttributeOptionApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReferenceEntityAttributesAttributeCodeOptions**](ReferenceEntityAttributeOptionApi.md#getReferenceEntityAttributesAttributeCodeOptions) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options | Get a list of attribute options of a given attribute for a given reference entity
[**getReferenceEntityAttributesAttributeCodeOptionsCode**](ReferenceEntityAttributeOptionApi.md#getReferenceEntityAttributesAttributeCodeOptionsCode) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options/{code} | Get an attribute option for a given attribute of a given reference entity
[**patchReferenceEntityAttributesAttributeCodeOptionsCode**](ReferenceEntityAttributeOptionApi.md#patchReferenceEntityAttributesAttributeCodeOptionsCode) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{attribute_code}/options/{code} | Update/create a reference entity attribute option



## getReferenceEntityAttributesAttributeCodeOptions

> [GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner] getReferenceEntityAttributesAttributeCodeOptions(referenceEntityCode, attributeCode)

Get a list of attribute options of a given attribute for a given reference entity

This endpoint allows you to get a list of attribute options for a given reference entity.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityAttributeOptionApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let attributeCode = "attributeCode_example"; // String | Code of the attribute
apiInstance.getReferenceEntityAttributesAttributeCodeOptions(referenceEntityCode, attributeCode, (error, data, response) => {
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
 **referenceEntityCode** | **String**| Code of the reference entity | 
 **attributeCode** | **String**| Code of the attribute | 

### Return type

[**[GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner]**](GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getReferenceEntityAttributesAttributeCodeOptionsCode

> GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner getReferenceEntityAttributesAttributeCodeOptionsCode(referenceEntityCode, attributeCode, code)

Get an attribute option for a given attribute of a given reference entity

This endpoint allows you to get the information about a given attribute option.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityAttributeOptionApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let code = "code_example"; // String | Code of the resource
apiInstance.getReferenceEntityAttributesAttributeCodeOptionsCode(referenceEntityCode, attributeCode, code, (error, data, response) => {
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
 **referenceEntityCode** | **String**| Code of the reference entity | 
 **attributeCode** | **String**| Code of the attribute | 
 **code** | **String**| Code of the resource | 

### Return type

[**GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner**](GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchReferenceEntityAttributesAttributeCodeOptionsCode

> patchReferenceEntityAttributesAttributeCodeOptionsCode(referenceEntityCode, attributeCode, code, body)

Update/create a reference entity attribute option

This endpoint allows you to update a given option for a given attribute and a given reference entity. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the option does not already exist for the given attribute of the given reference entity, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityAttributeOptionApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner(); // GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner | 
apiInstance.patchReferenceEntityAttributesAttributeCodeOptionsCode(referenceEntityCode, attributeCode, code, body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referenceEntityCode** | **String**| Code of the reference entity | 
 **attributeCode** | **String**| Code of the attribute | 
 **code** | **String**| Code of the resource | 
 **body** | [**GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner**](GetReferenceEntityAttributesAttributeCodeOptions200ResponseInner.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

