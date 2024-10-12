# MagentoB2B.ProductsCostApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCostStorageV1UpdatePost**](ProductsCostApi.md#catalogCostStorageV1UpdatePost) | **POST** /V1/products/cost | products/cost



## catalogCostStorageV1UpdatePost

> [CatalogDataPriceUpdateResultInterface] catalogCostStorageV1UpdatePost(opts)

products/cost

Add or update product cost. Input item should correspond to \\Magento\\Catalog\\Api\\Data\\CostInterface. If any items will have invalid cost, store id or sku, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsCostApi();
let opts = {
  'catalogCostStorageV1UpdatePostRequest': new MagentoB2B.CatalogCostStorageV1UpdatePostRequest() // CatalogCostStorageV1UpdatePostRequest | 
};
apiInstance.catalogCostStorageV1UpdatePost(opts, (error, data, response) => {
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
 **catalogCostStorageV1UpdatePostRequest** | [**CatalogCostStorageV1UpdatePostRequest**](CatalogCostStorageV1UpdatePostRequest.md)|  | [optional] 

### Return type

[**[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

