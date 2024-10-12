# AkeneoPimRestApi.CatalogProductsApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAppCatalogMappedProducts**](CatalogProductsApi.md#getAppCatalogMappedProducts) | **GET** /api/rest/v1/catalogs/{id}/mapped-products | Get the list of mapped products related to a catalog
[**getAppCatalogProductUuids**](CatalogProductsApi.md#getAppCatalogProductUuids) | **GET** /api/rest/v1/catalogs/{id}/product-uuids | Get the list of product uuids
[**getAppCatalogProducts**](CatalogProductsApi.md#getAppCatalogProducts) | **GET** /api/rest/v1/catalogs/{id}/products | Get the list of products related to a catalog
[**getAppCatalogProductsUuid**](CatalogProductsApi.md#getAppCatalogProductsUuid) | **GET** /api/rest/v1/catalogs/{id}/products/{uuid} | Get a product related to a catalog



## getAppCatalogMappedProducts

> Products getAppCatalogMappedProducts(id, opts)

Get the list of mapped products related to a catalog

This endpoint allows you to get the list of products related to a catalog when the mapping is enabled. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogProductsApi();
let id = "id_example"; // String | Catalog ID
let opts = {
  'searchAfter': "'cursor to the first page'", // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'limit': 100, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'updatedBefore': new Date("2013-10-20"), // Date | Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
  'updatedAfter': new Date("2013-10-20") // Date | Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
};
apiInstance.getAppCatalogMappedProducts(id, opts, (error, data, response) => {
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
 **id** | **String**| Catalog ID | 
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100]
 **updatedBefore** | **Date**| Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints) | [optional] 
 **updatedAfter** | **Date**| Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints) | [optional] 

### Return type

[**Products**](Products.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getAppCatalogProductUuids

> ProductUuids getAppCatalogProductUuids(id, opts)

Get the list of product uuids

This endpoint allows you to get the list of uuids of products contained in a catalog. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogProductsApi();
let id = "id_example"; // String | Id of the catalog
let opts = {
  'searchAfter': "'cursor to the first page'", // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'limit': 100, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'updatedBefore': new Date("2013-10-20"), // Date | Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
  'updatedAfter': new Date("2013-10-20") // Date | Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
};
apiInstance.getAppCatalogProductUuids(id, opts, (error, data, response) => {
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
 **id** | **String**| Id of the catalog | 
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100]
 **updatedBefore** | **Date**| Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints) | [optional] 
 **updatedAfter** | **Date**| Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints) | [optional] 

### Return type

[**ProductUuids**](ProductUuids.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getAppCatalogProducts

> Products getAppCatalogProducts(id, opts)

Get the list of products related to a catalog

This endpoint allows you to get the list of products related to a catalog. Products are paginated and they can be filtered. In the Enterprise Edition, permissions based on your app settings are applied to the set of products you request. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogProductsApi();
let id = "id_example"; // String | Catalog ID
let opts = {
  'searchAfter': "'cursor to the first page'", // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'limit': 100, // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
  'updatedBefore': new Date("2013-10-20"), // Date | Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
  'updatedAfter': new Date("2013-10-20") // Date | Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
};
apiInstance.getAppCatalogProducts(id, opts, (error, data, response) => {
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
 **id** | **String**| Catalog ID | 
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100]
 **updatedBefore** | **Date**| Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints) | [optional] 
 **updatedAfter** | **Date**| Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints) | [optional] 

### Return type

[**Products**](Products.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getAppCatalogProductsUuid

> getAppCatalogProductsUuid(id, uuid)

Get a product related to a catalog

This endpoint allows you to get a specific product related to a catalog. In the Enterprise Edition, permissions based on your app settings are applied on the product you request. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogProductsApi();
let id = "id_example"; // String | Catalog ID
let uuid = "uuid_example"; // String | Product UUID
apiInstance.getAppCatalogProductsUuid(id, uuid, (error, data, response) => {
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
 **id** | **String**| Catalog ID | 
 **uuid** | **String**| Product UUID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message

