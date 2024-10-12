# AkeneoPimRestApi.ProductModelApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteProductModelsCode**](ProductModelApi.md#deleteProductModelsCode) | **DELETE** /api/rest/v1/product-models/{code} | Delete a product model
[**getProductModelDraftCode**](ProductModelApi.md#getProductModelDraftCode) | **GET** /api/rest/v1/product-models/{code}/draft | Get a draft
[**getProductModels**](ProductModelApi.md#getProductModels) | **GET** /api/rest/v1/product-models | Get list of product models
[**getProductModelsCode**](ProductModelApi.md#getProductModelsCode) | **GET** /api/rest/v1/product-models/{code} | Get a product model
[**patchProductModels**](ProductModelApi.md#patchProductModels) | **PATCH** /api/rest/v1/product-models | Update/create several product models
[**patchProductModelsCode**](ProductModelApi.md#patchProductModelsCode) | **PATCH** /api/rest/v1/product-models/{code} | Update/create a product model
[**postProductModelProposal**](ProductModelApi.md#postProductModelProposal) | **POST** /api/rest/v1/product-models/{code}/proposal | Submit a draft for approval
[**postProductModels**](ProductModelApi.md#postProductModels) | **POST** /api/rest/v1/product-models | Create a new product model



## deleteProductModelsCode

> deleteProductModelsCode(code)

Delete a product model

This endpoint allows you to delete a given product model. All its children, product models and variant products, will be also deleted. In the Enterprise Edition, the permissions based on your connection user group are applied to the product model you try to delete.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductModelApi();
let code = "code_example"; // String | Code of the resource
apiInstance.deleteProductModelsCode(code, (error, data, response) => {
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


## getProductModelDraftCode

> PostProductModelsRequest getProductModelDraftCode(code)

Get a draft

This endpoint allows you to get the information about a given product model draft.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductModelApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getProductModelDraftCode(code, (error, data, response) => {
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

[**PostProductModelsRequest**](PostProductModelsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getProductModels

> ProductModels getProductModels(opts)

Get list of product models

This endpoint allows you to get a list of product models. Product models are paginated. In the Enterprise Edition, since the 2.0, permissions based on your user groups are applied to the set of products you request.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductModelApi();
let opts = {
  'search': "search_example", // String | Filter product models, for more details see the <a href=\"/documentation/filter.html\">Filters</a> section
  'scope': "scope_example", // String | Filter product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#via-channel\">Filter product values via channel</a> section
  'locales': "locales_example", // String | Filter product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#via-locale\">Filter product values via locale</a> section
  'attributes': "attributes_example", // String | Filter product values to only return those concerning the given attributes, for more details see the <a href=\"/documentation/filter.html#filter-product-values\">Filter on product values</a> section and the <a href=\"/documentation/filter.html#filter-on-product-model-properties\">Filter on product model properties</a> section
  'paginationType': "'page'", // String | Pagination method type, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'searchAfter': "'cursor to the first page'", // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false, // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
  'withQualityScores': true // Boolean | Return product model quality scores in the response. <strong>(Only available since the 6.0 version)</strong>
};
apiInstance.getProductModels(opts, (error, data, response) => {
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
 **search** | **String**| Filter product models, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section | [optional] 
 **scope** | **String**| Filter product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-channel\&quot;&gt;Filter product values via channel&lt;/a&gt; section | [optional] 
 **locales** | **String**| Filter product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-locale\&quot;&gt;Filter product values via locale&lt;/a&gt; section | [optional] 
 **attributes** | **String**| Filter product values to only return those concerning the given attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-product-values\&quot;&gt;Filter on product values&lt;/a&gt; section and the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-on-product-model-properties\&quot;&gt;Filter on product model properties&lt;/a&gt; section | [optional] 
 **paginationType** | **String**| Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;page&#39;]
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]
 **withQualityScores** | **Boolean**| Return product model quality scores in the response. &lt;strong&gt;(Only available since the 6.0 version)&lt;/strong&gt; | [optional] 

### Return type

[**ProductModels**](ProductModels.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, code, message


## getProductModelsCode

> PostProductModelsRequest getProductModelsCode(code, opts)

Get a product model

This endpoint allows you to get the information about a given product model. In the Entreprise Edition, since the v2.0, permissions based on your user groups are applied to the product model you request.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductModelApi();
let code = "code_example"; // String | Code of the resource
let opts = {
  'withQualityScores': true // Boolean | Return product model quality scores in the response. <strong>(Only available since the 6.0 version)</strong>
};
apiInstance.getProductModelsCode(code, opts, (error, data, response) => {
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
 **withQualityScores** | **Boolean**| Return product model quality scores in the response. &lt;strong&gt;(Only available since the 6.0 version)&lt;/strong&gt; | [optional] 

### Return type

[**PostProductModelsRequest**](PostProductModelsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchProductModels

> PatchAssetCategories200Response patchProductModels(opts)

Update/create several product models

This endpoint allows you to update and/or create several product models at once. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no product models exists for the given code, it creates it. In the Enterprise Edition, since the v2.3, permissions based on your user groups are applied to the product models you try to update. It may result in the creation of drafts if you only have edit rights through the product model&#39;s categories.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductModelApi();
let opts = {
  'body': new AkeneoPimRestApi.PatchProductModelsRequest() // PatchProductModelsRequest | 
};
apiInstance.patchProductModels(opts, (error, data, response) => {
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
 **body** | [**PatchProductModelsRequest**](PatchProductModelsRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchProductModelsCode

> patchProductModelsCode(code, body)

Update/create a product model

This endpoint allows you to update a given product model. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no product model exists for the given code, it creates it. In the Enterprise Edition PIM since the 2.3, permissions based on your user groups are applied to the product model you try to update. It may result in the creation of a draft if you only have edit rights through the product model&#39;s categories.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductModelApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostProductModelsRequest(); // PostProductModelsRequest | 
apiInstance.patchProductModelsCode(code, body, (error, data, response) => {
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
 **body** | [**PostProductModelsRequest**](PostProductModelsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postProductModelProposal

> postProductModelProposal(code)

Submit a draft for approval

This endpoint allows you to submit a product model draft for approval.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductModelApi();
let code = "code_example"; // String | Code of the resource
apiInstance.postProductModelProposal(code, (error, data, response) => {
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
- **Accept**: application/json, code, message, _links


## postProductModels

> postProductModels(opts)

Create a new product model

This endpoint allows you to create a new product model. In the Enterprise Edition, since the v2.3, permissions based on your user groups are applied to the product model you try to create.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductModelApi();
let opts = {
  'body': new AkeneoPimRestApi.PostProductModelsRequest() // PostProductModelsRequest | 
};
apiInstance.postProductModels(opts, (error, data, response) => {
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
 **body** | [**PostProductModelsRequest**](PostProductModelsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

