# MagentoB2B.ProductsBasePricesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogBasePriceStorageV1UpdatePost**](ProductsBasePricesApi.md#catalogBasePriceStorageV1UpdatePost) | **POST** /V1/products/base-prices | products/base-prices



## catalogBasePriceStorageV1UpdatePost

> [CatalogDataPriceUpdateResultInterface] catalogBasePriceStorageV1UpdatePost(opts)

products/base-prices

Add or update product prices. Input item should correspond \\Magento\\Catalog\\Api\\Data\\CostInterface. If any items will have invalid price, store id or sku, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsBasePricesApi();
let opts = {
  'catalogBasePriceStorageV1UpdatePostRequest': new MagentoB2B.CatalogBasePriceStorageV1UpdatePostRequest() // CatalogBasePriceStorageV1UpdatePostRequest | 
};
apiInstance.catalogBasePriceStorageV1UpdatePost(opts, (error, data, response) => {
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
 **catalogBasePriceStorageV1UpdatePostRequest** | [**CatalogBasePriceStorageV1UpdatePostRequest**](CatalogBasePriceStorageV1UpdatePostRequest.md)|  | [optional] 

### Return type

[**[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

