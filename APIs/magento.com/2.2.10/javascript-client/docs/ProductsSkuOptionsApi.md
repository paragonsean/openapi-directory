# MagentoB2B.ProductsSkuOptionsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductCustomOptionRepositoryV1GetListGet**](ProductsSkuOptionsApi.md#catalogProductCustomOptionRepositoryV1GetListGet) | **GET** /V1/products/{sku}/options | products/{sku}/options



## catalogProductCustomOptionRepositoryV1GetListGet

> [CatalogDataProductCustomOptionInterface] catalogProductCustomOptionRepositoryV1GetListGet(sku)

products/{sku}/options

Get the list of custom options for a specific product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuOptionsApi();
let sku = "sku_example"; // String | 
apiInstance.catalogProductCustomOptionRepositoryV1GetListGet(sku, (error, data, response) => {
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
 **sku** | **String**|  | 

### Return type

[**[CatalogDataProductCustomOptionInterface]**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

