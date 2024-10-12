# AkeneoPimRestApi.ProductIdentifierApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteProductsCode**](ProductIdentifierApi.md#deleteProductsCode) | **DELETE** /api/rest/v1/products/{code} | Delete a product
[**getDraftCode**](ProductIdentifierApi.md#getDraftCode) | **GET** /api/rest/v1/products/{code}/draft | Get a draft
[**getProducts**](ProductIdentifierApi.md#getProducts) | **GET** /api/rest/v1/products | Get list of products
[**getProductsCode**](ProductIdentifierApi.md#getProductsCode) | **GET** /api/rest/v1/products/{code} | Get a product
[**patchProducts**](ProductIdentifierApi.md#patchProducts) | **PATCH** /api/rest/v1/products | Update/create several products
[**patchProductsCode**](ProductIdentifierApi.md#patchProductsCode) | **PATCH** /api/rest/v1/products/{code} | Update/create a product
[**postProducts**](ProductIdentifierApi.md#postProducts) | **POST** /api/rest/v1/products | Create a new product
[**postProposal**](ProductIdentifierApi.md#postProposal) | **POST** /api/rest/v1/products/{code}/proposal | Submit a draft for approval



## deleteProductsCode

> deleteProductsCode(code)

Delete a product

This endpoint allows you to delete a given product. In the Enterprise Edition, since the 2.0, permissions based on your user groups are applied to the product you try to delete.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductIdentifierApi();
let code = "code_example"; // String | Code of the resource
apiInstance.deleteProductsCode(code, (error, data, response) => {
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


## getDraftCode

> PostProductsRequest getDraftCode(code)

Get a draft

This endpoint allows you to get the information about a given draft.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductIdentifierApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getDraftCode(code, (error, data, response) => {
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

[**PostProductsRequest**](PostProductsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getProducts

> Products1 getProducts(opts)

Get list of products

This endpoint allows you to get a list of products. Products are paginated and they can be filtered. In the Enterprise Edition, since the 2.0, permissions based on your user groups are applied to the set of products you request.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductIdentifierApi();
let opts = {
  'search': "search_example", // String | Filter products, for more details see the <a href=\"/documentation/filter.html\">Filters</a> section
  'scope': "scope_example", // String | Filter product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#via-channel\">Filter product values via channel</a> section
  'locales': "locales_example", // String | Filter product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#via-locale\">Filter product values via locale</a> section
  'attributes': "attributes_example", // String | Filter product values to only return those concerning the given attributes, for more details see the <a href=\"/documentation/filter.html#filter-product-values\">Filter on product values</a> section
  'paginationType': "'page'", // String | Pagination method type, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'searchAfter': "'cursor to the first page'", // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false, // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
  'withAttributeOptions': false, // Boolean | Return labels of attribute options in the response. (Only available since the 5.0 version)
  'withQualityScores': false, // Boolean | Return product quality scores in the response. (Only available since the 5.0 version)
  'withCompletenesses': false // Boolean | Return product completenesses in the response. (Only available since the 6.0 version)
};
apiInstance.getProducts(opts, (error, data, response) => {
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
 **search** | **String**| Filter products, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section | [optional] 
 **scope** | **String**| Filter product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-channel\&quot;&gt;Filter product values via channel&lt;/a&gt; section | [optional] 
 **locales** | **String**| Filter product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-locale\&quot;&gt;Filter product values via locale&lt;/a&gt; section | [optional] 
 **attributes** | **String**| Filter product values to only return those concerning the given attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-product-values\&quot;&gt;Filter on product values&lt;/a&gt; section | [optional] 
 **paginationType** | **String**| Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;page&#39;]
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]
 **withAttributeOptions** | **Boolean**| Return labels of attribute options in the response. (Only available since the 5.0 version) | [optional] [default to false]
 **withQualityScores** | **Boolean**| Return product quality scores in the response. (Only available since the 5.0 version) | [optional] [default to false]
 **withCompletenesses** | **Boolean**| Return product completenesses in the response. (Only available since the 6.0 version) | [optional] [default to false]

### Return type

[**Products1**](Products1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## getProductsCode

> PostProductsRequest getProductsCode(code, opts)

Get a product

This endpoint allows you to get the information about a given product. In the Entreprise Edition, since the v2.0, permissions based on your user groups are applied to the product you request.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductIdentifierApi();
let code = "code_example"; // String | Code of the resource
let opts = {
  'withAttributeOptions': false, // Boolean | Return labels of attribute options in the response. (Only available since the 5.0 version)
  'withQualityScores': false, // Boolean | Return product quality scores in the response. (Only available since the 5.0 version)
  'withCompletenesses': false // Boolean | Return product completenesses in the response. (Only available since the 6.0 version)
};
apiInstance.getProductsCode(code, opts, (error, data, response) => {
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
 **withAttributeOptions** | **Boolean**| Return labels of attribute options in the response. (Only available since the 5.0 version) | [optional] [default to false]
 **withQualityScores** | **Boolean**| Return product quality scores in the response. (Only available since the 5.0 version) | [optional] [default to false]
 **withCompletenesses** | **Boolean**| Return product completenesses in the response. (Only available since the 6.0 version) | [optional] [default to false]

### Return type

[**PostProductsRequest**](PostProductsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchProducts

> PatchAssetCategories200Response patchProducts(opts)

Update/create several products

This endpoint allows you to update and/or create several products at once. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no product exists for the given identifier, it creates it. In the Enterprise Edition, since the v2.0, permissions based on your user groups are applied to the products you try to update. It may result in the creation of drafts if you only have edit rights through the product&#39;s categories.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductIdentifierApi();
let opts = {
  'body': new AkeneoPimRestApi.PatchProductsRequest() // PatchProductsRequest | 
};
apiInstance.patchProducts(opts, (error, data, response) => {
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
 **body** | [**PatchProductsRequest**](PatchProductsRequest.md)|  | [optional] 

### Return type

[**PatchAssetCategories200Response**](PatchAssetCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, x-example-1, x-example-2, x-example-3, code, message


## patchProductsCode

> patchProductsCode(code, body)

Update/create a product

This endpoint allows you to update a given product. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no product exists for the given identifier, it creates it. In the Entreprise Edition, since the v2.0, permissions based on your user groups are applied to the product you try to update. It may result in the creation of a draft if you only have edit rights through the product&#39;s categories.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductIdentifierApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PostProductsRequest(); // PostProductsRequest | 
apiInstance.patchProductsCode(code, body, (error, data, response) => {
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
 **body** | [**PostProductsRequest**](PostProductsRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postProducts

> postProducts(opts)

Create a new product

This endpoint allows you to create a new product. In the Enterprise Edition, since the v2.0, permissions based on your user groups are applied to the product you try to create.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductIdentifierApi();
let opts = {
  'body': new AkeneoPimRestApi.PostProductsRequest() // PostProductsRequest | 
};
apiInstance.postProducts(opts, (error, data, response) => {
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
 **body** | [**PostProductsRequest**](PostProductsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## postProposal

> postProposal(code)

Submit a draft for approval

This endpoint allows you to submit a draft for approval.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.ProductIdentifierApi();
let code = "code_example"; // String | Code of the resource
apiInstance.postProposal(code, (error, data, response) => {
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

