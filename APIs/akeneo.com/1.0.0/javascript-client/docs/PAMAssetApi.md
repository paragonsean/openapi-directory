# AkeneoPimRestApi.PAMAssetApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPamAssets**](PAMAssetApi.md#getPamAssets) | **GET** /api/rest/v1/assets | Get list of PAM assets
[**getPamAssetsCode**](PAMAssetApi.md#getPamAssetsCode) | **GET** /api/rest/v1/assets/{code} | Get a PAM asset
[**patchPamAssets**](PAMAssetApi.md#patchPamAssets) | **PATCH** /api/rest/v1/assets | Update/create several PAM assets
[**patchPamAssetsCode**](PAMAssetApi.md#patchPamAssetsCode) | **PATCH** /api/rest/v1/assets/{code} | Update/create a PAM asset
[**postPamAssets**](PAMAssetApi.md#postPamAssets) | **POST** /api/rest/v1/assets | Create a new PAM asset



## getPamAssets

> PAMAssets getPamAssets(opts)

Get list of PAM assets

This endpoint allows you to get a list of PAM assets. PAM assets are paginated.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetApi();
let opts = {
  'paginationType': "'page'", // String | Pagination method type, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'searchAfter': "'cursor to the first page'", // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getPamAssets(opts, (error, data, response) => {
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
 **paginationType** | **String**| Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;page&#39;]
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**PAMAssets**](PAMAssets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getPamAssetsCode

> PostPamAssetsRequest getPamAssetsCode(code)

Get a PAM asset

This endpoint allows you to get the information about a given PAM asset.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getPamAssetsCode(code, (error, data, response) => {
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

[**PostPamAssetsRequest**](PostPamAssetsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchPamAssets

> PatchAssetCategories200Response patchPamAssets(opts)

Update/create several PAM assets

This endpoint allows you to update several PAM assets at once.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetApi();
let opts = {
  'body': new AkeneoPimRestApi.PatchPamAssetsRequest() // PatchPamAssetsRequest | 
};
apiInstance.patchPamAssets(opts, (error, data, response) => {
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
 **body** | [**PatchPamAssetsRequest**](PatchPamAssetsRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchPamAssetsCode

> patchPamAssetsCode(code, body)

Update/create a PAM asset

This endpoint allows you to update a given PAM asset. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no asset exists for the given code, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostPamAssetsRequest(); // PostPamAssetsRequest | 
apiInstance.patchPamAssetsCode(code, body, (error, data, response) => {
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
 **body** | [**PostPamAssetsRequest**](PostPamAssetsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postPamAssets

> postPamAssets(opts)

Create a new PAM asset

This endpoint allows you to create a new PAM asset.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetApi();
let opts = {
  'body': new AkeneoPimRestApi.PostPamAssetsRequest() // PostPamAssetsRequest | 
};
apiInstance.postPamAssets(opts, (error, data, response) => {
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
 **body** | [**PostPamAssetsRequest**](PostPamAssetsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

