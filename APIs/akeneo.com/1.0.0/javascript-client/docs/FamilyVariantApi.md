# AkeneoPimRestApi.FamilyVariantApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFamiliesFamilyCodeVariants**](FamilyVariantApi.md#getFamiliesFamilyCodeVariants) | **GET** /api/rest/v1/families/{family_code}/variants | Get list of family variants
[**getFamiliesFamilyCodeVariantsCode**](FamilyVariantApi.md#getFamiliesFamilyCodeVariantsCode) | **GET** /api/rest/v1/families/{family_code}/variants/{code} | Get a family variant
[**patchFamiliesFamilyCodeVariants**](FamilyVariantApi.md#patchFamiliesFamilyCodeVariants) | **PATCH** /api/rest/v1/families/{family_code}/variants | Update/create several family variants
[**patchFamiliesFamilyCodeVariantsCode**](FamilyVariantApi.md#patchFamiliesFamilyCodeVariantsCode) | **PATCH** /api/rest/v1/families/{family_code}/variants/{code} | Update/create a family variant



## getFamiliesFamilyCodeVariants

> FamilyVariants getFamiliesFamilyCodeVariants(familyCode, opts)

Get list of family variants

This endpoint allows you to get a list of family variants. Family variants are paginated and sorted by code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyVariantApi();
let familyCode = "familyCode_example"; // String | Code of the family
let opts = {
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getFamiliesFamilyCodeVariants(familyCode, opts, (error, data, response) => {
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
 **familyCode** | **String**| Code of the family | 
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**FamilyVariants**](FamilyVariants.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, labels, variant_attribute_sets, message


## getFamiliesFamilyCodeVariantsCode

> PostFamiliesFamilyCodeVariantsRequest getFamiliesFamilyCodeVariantsCode(familyCode, code)

Get a family variant

This endpoint allows you to get the information about a given family variant.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyVariantApi();
let familyCode = "familyCode_example"; // String | Code of the family
let code = "code_example"; // String | Code of the resource
apiInstance.getFamiliesFamilyCodeVariantsCode(familyCode, code, (error, data, response) => {
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
 **familyCode** | **String**| Code of the family | 
 **code** | **String**| Code of the resource | 

### Return type

[**PostFamiliesFamilyCodeVariantsRequest**](PostFamiliesFamilyCodeVariantsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchFamiliesFamilyCodeVariants

> PatchAssetCategories200Response patchFamiliesFamilyCodeVariants(familyCode, opts)

Update/create several family variants

This endpoint allows you to update and/or create several family variants at once, for a given family.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyVariantApi();
let familyCode = "familyCode_example"; // String | Code of the family
let opts = {
  'body': new AkeneoPimRestApi.PatchFamiliesFamilyCodeVariantsRequest() // PatchFamiliesFamilyCodeVariantsRequest | 
};
apiInstance.patchFamiliesFamilyCodeVariants(familyCode, opts, (error, data, response) => {
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
 **familyCode** | **String**| Code of the family | 
 **body** | [**PatchFamiliesFamilyCodeVariantsRequest**](PatchFamiliesFamilyCodeVariantsRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchFamiliesFamilyCodeVariantsCode

> patchFamiliesFamilyCodeVariantsCode(familyCode, code, body)

Update/create a family variant

This endpoint allows you to update a given family variant. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no family variant exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyVariantApi();
let familyCode = "familyCode_example"; // String | Code of the family
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostFamiliesFamilyCodeVariantsRequest(); // PostFamiliesFamilyCodeVariantsRequest | 
apiInstance.patchFamiliesFamilyCodeVariantsCode(familyCode, code, body, (error, data, response) => {
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
 **familyCode** | **String**| Code of the family | 
 **code** | **String**| Code of the resource | 
 **body** | [**PostFamiliesFamilyCodeVariantsRequest**](PostFamiliesFamilyCodeVariantsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

