# MagentoB2B.ProductsTypesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductTypeListV1GetProductTypesGet**](ProductsTypesApi.md#catalogProductTypeListV1GetProductTypesGet) | **GET** /V1/products/types | products/types



## catalogProductTypeListV1GetProductTypesGet

> [CatalogDataProductTypeInterface] catalogProductTypeListV1GetProductTypesGet()

products/types

Retrieve available product types

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsTypesApi();
apiInstance.catalogProductTypeListV1GetProductTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[CatalogDataProductTypeInterface]**](CatalogDataProductTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

