# MagentoB2B.ProductsSpecialPriceDeleteApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogSpecialPriceStorageV1DeletePost**](ProductsSpecialPriceDeleteApi.md#catalogSpecialPriceStorageV1DeletePost) | **POST** /V1/products/special-price-delete | products/special-price-delete



## catalogSpecialPriceStorageV1DeletePost

> [CatalogDataPriceUpdateResultInterface] catalogSpecialPriceStorageV1DeletePost(opts)

products/special-price-delete

Delete product&#39;s special price. If any items will have invalid price, store id, sku or dates, they will be marked as failed and excluded from delete list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the delete exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSpecialPriceDeleteApi();
let opts = {
  'catalogSpecialPriceStorageV1UpdatePostRequest': new MagentoB2B.CatalogSpecialPriceStorageV1UpdatePostRequest() // CatalogSpecialPriceStorageV1UpdatePostRequest | 
};
apiInstance.catalogSpecialPriceStorageV1DeletePost(opts, (error, data, response) => {
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
 **catalogSpecialPriceStorageV1UpdatePostRequest** | [**CatalogSpecialPriceStorageV1UpdatePostRequest**](CatalogSpecialPriceStorageV1UpdatePostRequest.md)|  | [optional] 

### Return type

[**[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

