# AkeneoPimRestApi.MappingSchemaForProductsApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAppCatalogsMappingSchemaProduct**](MappingSchemaForProductsApi.md#deleteAppCatalogsMappingSchemaProduct) | **DELETE** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Delete the product mapping schema related to a catalog
[**getAppCatalogsMappingSchemaProduct**](MappingSchemaForProductsApi.md#getAppCatalogsMappingSchemaProduct) | **GET** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Get the product mapping schema related to a catalog
[**putAppCatalogsMappingSchemaProduct**](MappingSchemaForProductsApi.md#putAppCatalogsMappingSchemaProduct) | **PUT** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Create or update the product mapping schema related to a catalog



## deleteAppCatalogsMappingSchemaProduct

> deleteAppCatalogsMappingSchemaProduct(id)

Delete the product mapping schema related to a catalog

This endpoint allows you to delete the product mapping schema related to a catalog

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.MappingSchemaForProductsApi();
let id = "id_example"; // String | Catalog ID
apiInstance.deleteAppCatalogsMappingSchemaProduct(id, (error, data, response) => {
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


## getAppCatalogsMappingSchemaProduct

> GetAppCatalogsMappingSchemaProduct200Response getAppCatalogsMappingSchemaProduct(id)

Get the product mapping schema related to a catalog

This endpoint allows you to retrieve the product mapping schema related to a catalog

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.MappingSchemaForProductsApi();
let id = "id_example"; // String | Catalog ID
apiInstance.getAppCatalogsMappingSchemaProduct(id, (error, data, response) => {
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

[**GetAppCatalogsMappingSchemaProduct200Response**](GetAppCatalogsMappingSchemaProduct200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## putAppCatalogsMappingSchemaProduct

> putAppCatalogsMappingSchemaProduct(id, opts)

Create or update the product mapping schema related to a catalog

This endpoint allows you to create or update the product mapping schema related to a catalog

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.MappingSchemaForProductsApi();
let id = "id_example"; // String | Catalog ID
let opts = {
  'body': new AkeneoPimRestApi.GetAppCatalogsMappingSchemaProduct200Response() // GetAppCatalogsMappingSchemaProduct200Response | 
};
apiInstance.putAppCatalogsMappingSchemaProduct(id, opts, (error, data, response) => {
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
 **body** | [**GetAppCatalogsMappingSchemaProduct200Response**](GetAppCatalogsMappingSchemaProduct200Response.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message

