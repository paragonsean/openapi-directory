# AkeneoPimRestApi.PAMAssetCategoryApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetCategories**](PAMAssetCategoryApi.md#getAssetCategories) | **GET** /api/rest/v1/asset-categories | Get list of PAM asset categories
[**getAssetCategoriesCode**](PAMAssetCategoryApi.md#getAssetCategoriesCode) | **GET** /api/rest/v1/asset-categories/{code} | Get a PAM asset category
[**patchAssetCategories**](PAMAssetCategoryApi.md#patchAssetCategories) | **PATCH** /api/rest/v1/asset-categories | Update/create several PAM asset categories
[**patchAssetCategoriesCode**](PAMAssetCategoryApi.md#patchAssetCategoriesCode) | **PATCH** /api/rest/v1/asset-categories/{code} | Update/create a PAM asset category
[**postAssetCategories**](PAMAssetCategoryApi.md#postAssetCategories) | **POST** /api/rest/v1/asset-categories | Create a new PAM asset category



## getAssetCategories

> PAMAssetCategories getAssetCategories(opts)

Get list of PAM asset categories

This endpoint allows you to get a list of PAM asset categories. PAM asset categories are paginated and sorted by &#x60;root/left&#x60;.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetCategoryApi();
let opts = {
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getAssetCategories(opts, (error, data, response) => {
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
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**PAMAssetCategories**](PAMAssetCategories.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getAssetCategoriesCode

> PostAssetCategoriesRequest getAssetCategoriesCode(code)

Get a PAM asset category

This endpoint allows you to get the information about a given PAM asset category.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetCategoryApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getAssetCategoriesCode(code, (error, data, response) => {
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

[**PostAssetCategoriesRequest**](PostAssetCategoriesRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAssetCategories

> PatchAssetCategories200Response patchAssetCategories(opts)

Update/create several PAM asset categories

This endpoint allows you to update several PAM asset categories at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetCategoryApi();
let opts = {
  'body': new AkeneoPimRestApi.PatchAssetCategoriesRequest() // PatchAssetCategoriesRequest | 
};
apiInstance.patchAssetCategories(opts, (error, data, response) => {
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
 **body** | [**PatchAssetCategoriesRequest**](PatchAssetCategoriesRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchAssetCategoriesCode

> patchAssetCategoriesCode(code, body)

Update/create a PAM asset category

This endpoint allows you to update a given PAM asset category. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no category exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetCategoryApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostAssetCategoriesRequest(); // PostAssetCategoriesRequest | 
apiInstance.patchAssetCategoriesCode(code, body, (error, data, response) => {
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
 **body** | [**PostAssetCategoriesRequest**](PostAssetCategoriesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postAssetCategories

> postAssetCategories(opts)

Create a new PAM asset category

This endpoint allows you to create a new PAM asset category.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetCategoryApi();
let opts = {
  'body': new AkeneoPimRestApi.PostAssetCategoriesRequest() // PostAssetCategoriesRequest | 
};
apiInstance.postAssetCategories(opts, (error, data, response) => {
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
 **body** | [**PostAssetCategoriesRequest**](PostAssetCategoriesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

