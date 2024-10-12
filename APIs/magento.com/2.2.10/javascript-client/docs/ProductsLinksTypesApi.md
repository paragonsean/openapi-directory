# MagentoB2B.ProductsLinksTypesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductLinkTypeListV1GetItemsGet**](ProductsLinksTypesApi.md#catalogProductLinkTypeListV1GetItemsGet) | **GET** /V1/products/links/types | products/links/types



## catalogProductLinkTypeListV1GetItemsGet

> [CatalogDataProductLinkTypeInterface] catalogProductLinkTypeListV1GetItemsGet()

products/links/types

Retrieve information about available product link types

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsLinksTypesApi();
apiInstance.catalogProductLinkTypeListV1GetItemsGet((error, data, response) => {
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

[**[CatalogDataProductLinkTypeInterface]**](CatalogDataProductLinkTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

