# AkeneoPimRestApi.PublishedProductApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPublishedProducts**](PublishedProductApi.md#getPublishedProducts) | **GET** /api/rest/v1/published-products | Get list of published products
[**getPublishedProductsCode**](PublishedProductApi.md#getPublishedProductsCode) | **GET** /api/rest/v1/published-products/{code} | Get a published product



## getPublishedProducts

> PublishedProducts getPublishedProducts(opts)

Get list of published products

This endpoint allows you to get a list of published products. Published products are paginated and they can be filtered.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PublishedProductApi();
let opts = {
  'search': "search_example", // String | Filter published products, for more details see the <a href=\"/documentation/filter.html\">Filters</a> section
  'scope': "scope_example", // String | Filter published product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#filter-published-product-values\">Filter on published product values</a> section
  'locales': "locales_example", // String | Filter published product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#filter-published-product-values\">Filter on published product values</a> section
  'attributes': "attributes_example", // String | Filter published product values to only return those concerning the given attributes, for more details see the <a href=\"/documentation/filter.html#filter-product-values\">Filter on product values</a> section
  'paginationType': "'page'", // String | Pagination method type, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'searchAfter': "'cursor to the first page'", // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'limit': 10, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'withCount': false // Boolean | Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
};
apiInstance.getPublishedProducts(opts, (error, data, response) => {
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
 **search** | **String**| Filter published products, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section | [optional] 
 **scope** | **String**| Filter published product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-published-product-values\&quot;&gt;Filter on published product values&lt;/a&gt; section | [optional] 
 **locales** | **String**| Filter published product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-published-product-values\&quot;&gt;Filter on published product values&lt;/a&gt; section | [optional] 
 **attributes** | **String**| Filter published product values to only return those concerning the given attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-product-values\&quot;&gt;Filter on product values&lt;/a&gt; section | [optional] 
 **paginationType** | **String**| Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;page&#39;]
 **page** | **Number**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1]
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 10]
 **withCount** | **Boolean**| Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way | [optional] [default to false]

### Return type

[**PublishedProducts**](PublishedProducts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, current_page, code, message


## getPublishedProductsCode

> GetPublishedProductsCode200Response getPublishedProductsCode(code)

Get a published product

This endpoint allows you to get the information about a given published product.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PublishedProductApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getPublishedProductsCode(code, (error, data, response) => {
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

[**GetPublishedProductsCode200Response**](GetPublishedProductsCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message

