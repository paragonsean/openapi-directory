# AkeneoPimRestApi.ReferenceEntityAttributeApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReferenceEntitiesCodeAttributes**](ReferenceEntityAttributeApi.md#getReferenceEntitiesCodeAttributes) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes | Get the list of attributes of a given reference entity
[**getReferenceEntityAttributesCode**](ReferenceEntityAttributeApi.md#getReferenceEntityAttributesCode) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{code} | Get an attribute of a given reference entity
[**patchReferenceEntityAttributesCode**](ReferenceEntityAttributeApi.md#patchReferenceEntityAttributesCode) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/attributes/{code} | Update/create an attribute of a given reference entity



## getReferenceEntitiesCodeAttributes

> [GetReferenceEntitiesCodeAttributes200ResponseInner] getReferenceEntitiesCodeAttributes(referenceEntityCode)

Get the list of attributes of a given reference entity

This endpoint allows you to get the list of attributes of a given reference entity.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityAttributeApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
apiInstance.getReferenceEntitiesCodeAttributes(referenceEntityCode, (error, data, response) => {
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

### Return type

[**[GetReferenceEntitiesCodeAttributes200ResponseInner]**](GetReferenceEntitiesCodeAttributes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getReferenceEntityAttributesCode

> GetReferenceEntitiesCodeAttributes200ResponseInner getReferenceEntityAttributesCode(referenceEntityCode, code)

Get an attribute of a given reference entity

This endpoint allows you to get the information about a given attribute for a given reference entity.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityAttributeApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let code = "code_example"; // String | Code of the resource
apiInstance.getReferenceEntityAttributesCode(referenceEntityCode, code, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 

### Return type

[**GetReferenceEntitiesCodeAttributes200ResponseInner**](GetReferenceEntitiesCodeAttributes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchReferenceEntityAttributesCode

> patchReferenceEntityAttributesCode(referenceEntityCode, code, body)

Update/create an attribute of a given reference entity

This endpoint allows you to update a given attribute for a given renference entity. Note that if the attribute does not already exist for the given reference entity, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ReferenceEntityAttributeApi();
let referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.GetReferenceEntitiesCodeAttributes200ResponseInner(); // GetReferenceEntitiesCodeAttributes200ResponseInner | 
apiInstance.patchReferenceEntityAttributesCode(referenceEntityCode, code, body, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 
 **body** | [**GetReferenceEntitiesCodeAttributes200ResponseInner**](GetReferenceEntitiesCodeAttributes200ResponseInner.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

