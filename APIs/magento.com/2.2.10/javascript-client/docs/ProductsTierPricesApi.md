# MagentoB2B.ProductsTierPricesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogTierPriceStorageV1ReplacePut**](ProductsTierPricesApi.md#catalogTierPriceStorageV1ReplacePut) | **PUT** /V1/products/tier-prices | products/tier-prices
[**catalogTierPriceStorageV1UpdatePost**](ProductsTierPricesApi.md#catalogTierPriceStorageV1UpdatePost) | **POST** /V1/products/tier-prices | products/tier-prices



## catalogTierPriceStorageV1ReplacePut

> [CatalogDataPriceUpdateResultInterface] catalogTierPriceStorageV1ReplacePut(opts)

products/tier-prices

Remove existing tier prices and replace them with the new ones. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from replace list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsTierPricesApi();
let opts = {
  'catalogTierPriceStorageV1ReplacePutRequest': new MagentoB2B.CatalogTierPriceStorageV1ReplacePutRequest() // CatalogTierPriceStorageV1ReplacePutRequest | 
};
apiInstance.catalogTierPriceStorageV1ReplacePut(opts, (error, data, response) => {
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


## catalogTierPriceStorageV1UpdatePost

> [CatalogDataPriceUpdateResultInterface] catalogTierPriceStorageV1UpdatePost(opts)

products/tier-prices

Add or update product prices. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsTierPricesApi();
let opts = {
  'catalogTierPriceStorageV1ReplacePutRequest': new MagentoB2B.CatalogTierPriceStorageV1ReplacePutRequest() // CatalogTierPriceStorageV1ReplacePutRequest | 
};
apiInstance.catalogTierPriceStorageV1UpdatePost(opts, (error, data, response) => {
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

