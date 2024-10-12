# MagentoB2B.ProductsOptionsTypesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductCustomOptionTypeListV1GetItemsGet**](ProductsOptionsTypesApi.md#catalogProductCustomOptionTypeListV1GetItemsGet) | **GET** /V1/products/options/types | products/options/types



## catalogProductCustomOptionTypeListV1GetItemsGet

> [CatalogDataProductCustomOptionTypeInterface] catalogProductCustomOptionTypeListV1GetItemsGet()

products/options/types

Get custom option types

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsOptionsTypesApi();
apiInstance.catalogProductCustomOptionTypeListV1GetItemsGet((error, data, response) => {
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

[**[CatalogDataProductCustomOptionTypeInterface]**](CatalogDataProductCustomOptionTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

