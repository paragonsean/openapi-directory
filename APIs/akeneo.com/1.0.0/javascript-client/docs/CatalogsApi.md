# AkeneoPimRestApi.CatalogsApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAppCatalog**](CatalogsApi.md#deleteAppCatalog) | **DELETE** /api/rest/v1/catalogs/{id} | Delete a catalog
[**getAppCatalog**](CatalogsApi.md#getAppCatalog) | **GET** /api/rest/v1/catalogs/{id} | Get a catalog
[**getAppCatalogs**](CatalogsApi.md#getAppCatalogs) | **GET** /api/rest/v1/catalogs | Get the list of owned catalogs
[**patchAppCatalog**](CatalogsApi.md#patchAppCatalog) | **PATCH** /api/rest/v1/catalogs/{id} | Update a catalog
[**postAppCatalog**](CatalogsApi.md#postAppCatalog) | **POST** /api/rest/v1/catalogs | Create a new catalog



## deleteAppCatalog

> deleteAppCatalog(id)

Delete a catalog

This endpoint allows you to delete a catalog.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogsApi();
let id = "id_example"; // String | Catalog ID
apiInstance.deleteAppCatalog(id, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getAppCatalog

> PostAppCatalog201Response getAppCatalog(id)

Get a catalog

This endpoint allows you to get the information about a catalog.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogsApi();
let id = "id_example"; // String | Catalog ID
apiInstance.getAppCatalog(id, (error, data, response) => {
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

### Return type

[**PostAppCatalog201Response**](PostAppCatalog201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getAppCatalogs

> Catalogs getAppCatalogs(opts)

Get the list of owned catalogs

This endpoint allows you to get the list of catalogs you owned.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogsApi();
let opts = {
  'page': 1, // Number | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
  'limit': 100 // Number | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
};
apiInstance.getAppCatalogs(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100]

### Return type

[**Catalogs**](Catalogs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAppCatalog

> PostAppCatalog201Response patchAppCatalog(id, opts)

Update a catalog

This endpoint allows you to update a catalog.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogsApi();
let id = "id_example"; // String | Catalog ID
let opts = {
  'body': new AkeneoPimRestApi.PostAppCatalogRequest() // PostAppCatalogRequest | 
};
apiInstance.patchAppCatalog(id, opts, (error, data, response) => {
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
 **body** | [**PostAppCatalogRequest**](PostAppCatalogRequest.md)|  | [optional] 

### Return type

[**PostAppCatalog201Response**](PostAppCatalog201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## postAppCatalog

> PostAppCatalog201Response postAppCatalog(opts)

Create a new catalog

This endpoint allows you to create a new catalog.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.CatalogsApi();
let opts = {
  'body': new AkeneoPimRestApi.PostAppCatalogRequest() // PostAppCatalogRequest | 
};
apiInstance.postAppCatalog(opts, (error, data, response) => {
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
 **body** | [**PostAppCatalogRequest**](PostAppCatalogRequest.md)|  | [optional] 

### Return type

[**PostAppCatalog201Response**](PostAppCatalog201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message

