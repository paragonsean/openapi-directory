# AkeneoPimRestApi.AttributeOptionApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAttributesAttributeCodeOptions**](AttributeOptionApi.md#getAttributesAttributeCodeOptions) | **GET** /api/rest/v1/attributes/{attribute_code}/options | Get list of attribute options
[**getAttributesAttributeCodeOptionsCode**](AttributeOptionApi.md#getAttributesAttributeCodeOptionsCode) | **GET** /api/rest/v1/attributes/{attribute_code}/options/{code} | Get an attribute option
[**patchAttributesAttributeCodeOptions**](AttributeOptionApi.md#patchAttributesAttributeCodeOptions) | **PATCH** /api/rest/v1/attributes/{attribute_code}/options | Update/create several attribute options
[**patchAttributesAttributeCodeOptionsCode**](AttributeOptionApi.md#patchAttributesAttributeCodeOptionsCode) | **PATCH** /api/rest/v1/attributes/{attribute_code}/options/{code} | Update/create an attribute option
[**postAttributesAttributeCodeOptions**](AttributeOptionApi.md#postAttributesAttributeCodeOptions) | **POST** /api/rest/v1/attributes/{attribute_code}/options | Create a new attribute option



## getAttributesAttributeCodeOptions

> AttributeOptions getAttributesAttributeCodeOptions(attributeCode, opts)

Get list of attribute options

This endpoint allows you to get a list of attribute options. Attribute options are paginated and sorted by code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeOptionApi();
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let opts = {
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getAttributesAttributeCodeOptions(attributeCode, opts, (error, data, response) => {
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
 **attributeCode** | **String**| Code of the attribute | 
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**AttributeOptions**](AttributeOptions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getAttributesAttributeCodeOptionsCode

> PostAttributesAttributeCodeOptionsRequest getAttributesAttributeCodeOptionsCode(attributeCode, code)

Get an attribute option

This endpoint allows you to get the information about a given attribute option.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeOptionApi();
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let code = "code_example"; // String | Code of the resource
apiInstance.getAttributesAttributeCodeOptionsCode(attributeCode, code, (error, data, response) => {
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
 **attributeCode** | **String**| Code of the attribute | 
 **code** | **String**| Code of the resource | 

### Return type

[**PostAttributesAttributeCodeOptionsRequest**](PostAttributesAttributeCodeOptionsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAttributesAttributeCodeOptions

> PatchAssetCategories200Response patchAttributesAttributeCodeOptions(attributeCode, opts)

Update/create several attribute options

This endpoint allows you to update several attribute options at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeOptionApi();
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let opts = {
  'body': new AkeneoPimRestApi.PatchAttributesAttributeCodeOptionsRequest() // PatchAttributesAttributeCodeOptionsRequest | 
};
apiInstance.patchAttributesAttributeCodeOptions(attributeCode, opts, (error, data, response) => {
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
 **attributeCode** | **String**| Code of the attribute | 
 **body** | [**PatchAttributesAttributeCodeOptionsRequest**](PatchAttributesAttributeCodeOptionsRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchAttributesAttributeCodeOptionsCode

> patchAttributesAttributeCodeOptionsCode(attributeCode, code, body)

Update/create an attribute option

This endpoint allows you to update a given attribute option. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute option exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeOptionApi();
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostAttributesAttributeCodeOptionsRequest(); // PostAttributesAttributeCodeOptionsRequest | 
apiInstance.patchAttributesAttributeCodeOptionsCode(attributeCode, code, body, (error, data, response) => {
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
 **attributeCode** | **String**| Code of the attribute | 
 **code** | **String**| Code of the resource | 
 **body** | [**PostAttributesAttributeCodeOptionsRequest**](PostAttributesAttributeCodeOptionsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postAttributesAttributeCodeOptions

> postAttributesAttributeCodeOptions(attributeCode, opts)

Create a new attribute option

This endpoint allows you to create a new attribute option.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AttributeOptionApi();
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let opts = {
  'body': new AkeneoPimRestApi.PostAttributesAttributeCodeOptionsRequest() // PostAttributesAttributeCodeOptionsRequest | 
};
apiInstance.postAttributesAttributeCodeOptions(attributeCode, opts, (error, data, response) => {
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
 **attributeCode** | **String**| Code of the attribute | 
 **body** | [**PostAttributesAttributeCodeOptionsRequest**](PostAttributesAttributeCodeOptionsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

