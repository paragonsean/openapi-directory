# MagentoB2B.ProductsAttributesTypesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeTypesListV1GetItemsGet**](ProductsAttributesTypesApi.md#catalogProductAttributeTypesListV1GetItemsGet) | **GET** /V1/products/attributes/types | products/attributes/types



## catalogProductAttributeTypesListV1GetItemsGet

> [CatalogDataProductAttributeTypeInterface] catalogProductAttributeTypesListV1GetItemsGet()

products/attributes/types

Retrieve list of product attribute types

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesTypesApi();
apiInstance.catalogProductAttributeTypesListV1GetItemsGet((error, data, response) => {
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

[**[CatalogDataProductAttributeTypeInterface]**](CatalogDataProductAttributeTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

