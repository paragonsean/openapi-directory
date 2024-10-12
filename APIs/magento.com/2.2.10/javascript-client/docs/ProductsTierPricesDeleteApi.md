# MagentoB2B.ProductsTierPricesDeleteApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogTierPriceStorageV1DeletePost**](ProductsTierPricesDeleteApi.md#catalogTierPriceStorageV1DeletePost) | **POST** /V1/products/tier-prices-delete | products/tier-prices-delete



## catalogTierPriceStorageV1DeletePost

> [CatalogDataPriceUpdateResultInterface] catalogTierPriceStorageV1DeletePost(opts)

products/tier-prices-delete

Delete product tier prices. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from delete list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsTierPricesDeleteApi();
let opts = {
  'catalogTierPriceStorageV1ReplacePutRequest': new MagentoB2B.CatalogTierPriceStorageV1ReplacePutRequest() // CatalogTierPriceStorageV1ReplacePutRequest | 
};
apiInstance.catalogTierPriceStorageV1DeletePost(opts, (error, data, response) => {
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
 **catalogTierPriceStorageV1ReplacePutRequest** | [**CatalogTierPriceStorageV1ReplacePutRequest**](CatalogTierPriceStorageV1ReplacePutRequest.md)|  | [optional] 

### Return type

[**[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

