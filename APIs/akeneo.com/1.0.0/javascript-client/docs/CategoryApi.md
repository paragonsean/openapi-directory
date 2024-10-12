# AkeneoPimRestApi.CategoryApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCategories**](CategoryApi.md#getCategories) | **GET** /api/rest/v1/categories | Get list of categories
[**getCategoriesCode**](CategoryApi.md#getCategoriesCode) | **GET** /api/rest/v1/categories/{code} | Get a category
[**getCategoryMediaFilesCodeDownload**](CategoryApi.md#getCategoryMediaFilesCodeDownload) | **GET** /api/rest/v1/category-media-files/{code}/download | Download a category media file
[**patchCategories**](CategoryApi.md#patchCategories) | **PATCH** /api/rest/v1/categories | Update/create several categories
[**patchCategoriesCode**](CategoryApi.md#patchCategoriesCode) | **PATCH** /api/rest/v1/categories/{code} | Update/create a category
[**postCategories**](CategoryApi.md#postCategories) | **POST** /api/rest/v1/categories | Create a new category



## getCategories

> Categories getCategories(opts)

Get list of categories

This endpoint allows you to get a list of categories. Categories are paginated and sorted by &#x60;root/left&#x60;.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CategoryApi();
let opts = {
  'search': "search_example", // String | Filter categories, for more details see the <a href=\"/documentation/filter.html#filter-categories\">Filters</a> section.
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false, // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
  'withPosition': true, // Boolean | Return information about category position into its category tree (only available since the 7.0 version)
  'withEnrichedAttributes': true // Boolean | Return attribute values of the category (only available on SaaS platforms)
};
apiInstance.getCategories(opts, (error, data, response) => {
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
 **search** | **String**| Filter categories, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-categories\&quot;&gt;Filters&lt;/a&gt; section. | [optional] 
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]
 **withPosition** | **Boolean**| Return information about category position into its category tree (only available since the 7.0 version) | [optional] 
 **withEnrichedAttributes** | **Boolean**| Return attribute values of the category (only available on SaaS platforms) | [optional] 

### Return type

[**Categories**](Categories.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getCategoriesCode

> PostCategoriesRequest getCategoriesCode(code, opts)

Get a category

This endpoint allows you to get the information about a given category.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CategoryApi();
let code = "code_example"; // String | Code of the resource
let opts = {
  'withPosition': true, // Boolean | Return information about category position into its category tree (only available since the 7.0 version)
  'withEnrichedAttributes': true // Boolean | Return attribute values of the category (only available on SaaS platforms)
};
apiInstance.getCategoriesCode(code, opts, (error, data, response) => {
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
 **withPosition** | **Boolean**| Return information about category position into its category tree (only available since the 7.0 version) | [optional] 
 **withEnrichedAttributes** | **Boolean**| Return attribute values of the category (only available on SaaS platforms) | [optional] 

### Return type

[**PostCategoriesRequest**](PostCategoriesRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getCategoryMediaFilesCodeDownload

> getCategoryMediaFilesCodeDownload(code)

Download a category media file

This endpoint allows you to download a given media file that is used as an attribute value of a enriched category.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CategoryApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getCategoryMediaFilesCodeDownload(code, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchCategories

> PatchAssetCategories200Response patchCategories(opts)

Update/create several categories

This endpoint allows you to update several categories at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CategoryApi();
let opts = {
  'body': new AkeneoPimRestApi.PatchCategoriesRequest() // PatchCategoriesRequest | 
};
apiInstance.patchCategories(opts, (error, data, response) => {
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
 **body** | [**PatchCategoriesRequest**](PatchCategoriesRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchCategoriesCode

> patchCategoriesCode(code, body)

Update/create a category

This endpoint allows you to update a given category. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no category exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CategoryApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostCategoriesRequest(); // PostCategoriesRequest | 
apiInstance.patchCategoriesCode(code, body, (error, data, response) => {
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
 **body** | [**PostCategoriesRequest**](PostCategoriesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postCategories

> postCategories(opts)

Create a new category

This endpoint allows you to create a new category.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CategoryApi();
let opts = {
  'body': new AkeneoPimRestApi.PostCategoriesRequest() // PostCategoriesRequest | 
};
apiInstance.postCategories(opts, (error, data, response) => {
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
 **body** | [**PostCategoriesRequest**](PostCategoriesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

