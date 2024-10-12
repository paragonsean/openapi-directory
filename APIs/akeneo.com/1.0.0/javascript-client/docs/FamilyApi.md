# AkeneoPimRestApi.FamilyApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFamilies**](FamilyApi.md#getFamilies) | **GET** /api/rest/v1/families | Get list of families
[**getFamiliesCode**](FamilyApi.md#getFamiliesCode) | **GET** /api/rest/v1/families/{code} | Get a family
[**patchFamilies**](FamilyApi.md#patchFamilies) | **PATCH** /api/rest/v1/families | Update/create several families
[**patchFamiliesCode**](FamilyApi.md#patchFamiliesCode) | **PATCH** /api/rest/v1/families/{code} | Update/create a family
[**postFamilies**](FamilyApi.md#postFamilies) | **POST** /api/rest/v1/families | Create a new family
[**postFamiliesFamilyCodeVariants**](FamilyApi.md#postFamiliesFamilyCodeVariants) | **POST** /api/rest/v1/families/{family_code}/variants | Create a new family variant



## getFamilies

> Families getFamilies(opts)

Get list of families

This endpoint allows you to get a list of families. Families are paginated and sorted by code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyApi();
let opts = {
  'search': "search_example", // String | Filter families, for more details see the <a href=\"/documentation/filter.html#filter-families\">Filters</a> section.
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getFamilies(opts, (error, data, response) => {
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
 **search** | **String**| Filter families, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-families\&quot;&gt;Filters&lt;/a&gt; section. | [optional] 
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**Families**](Families.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getFamiliesCode

> PostFamiliesRequest getFamiliesCode(code)

Get a family

This endpoint allows you to get the information about a given family.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getFamiliesCode(code, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 

### Return type

[**PostFamiliesRequest**](PostFamiliesRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchFamilies

> PatchAssetCategories200Response patchFamilies(opts)

Update/create several families

This endpoint allows you to update and/or create several families at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyApi();
let opts = {
  'body': new AkeneoPimRestApi.PatchFamiliesRequest() // PatchFamiliesRequest | 
};
apiInstance.patchFamilies(opts, (error, data, response) => {
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
 **body** | [**PatchFamiliesRequest**](PatchFamiliesRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchFamiliesCode

> patchFamiliesCode(code, body)

Update/create a family

This endpoint allows you to update a given family. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no family exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostFamiliesRequest(); // PostFamiliesRequest | 
apiInstance.patchFamiliesCode(code, body, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 
 **body** | [**PostFamiliesRequest**](PostFamiliesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postFamilies

> postFamilies(opts)

Create a new family

This endpoint allows you to create a new family.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyApi();
let opts = {
  'body': new AkeneoPimRestApi.PostFamiliesRequest() // PostFamiliesRequest | 
};
apiInstance.postFamilies(opts, (error, data, response) => {
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
 **body** | [**PostFamiliesRequest**](PostFamiliesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postFamiliesFamilyCodeVariants

> postFamiliesFamilyCodeVariants(familyCode, opts)

Create a new family variant

This endpoint allows you to create a family variant.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.FamilyApi();
let familyCode = "familyCode_example"; // String | Code of the family
let opts = {
  'body': new AkeneoPimRestApi.PostFamiliesFamilyCodeVariantsRequest() // PostFamiliesFamilyCodeVariantsRequest | 
};
apiInstance.postFamiliesFamilyCodeVariants(familyCode, opts, (error, data, response) => {
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
 **body** | [**PostFamiliesFamilyCodeVariantsRequest**](PostFamiliesFamilyCodeVariantsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

