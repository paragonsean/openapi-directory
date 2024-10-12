# MagentoB2B.StockItemsProductSkuApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogInventoryStockRegistryV1GetStockItemBySkuGet**](StockItemsProductSkuApi.md#catalogInventoryStockRegistryV1GetStockItemBySkuGet) | **GET** /V1/stockItems/{productSku} | stockItems/{productSku}



## catalogInventoryStockRegistryV1GetStockItemBySkuGet

> CatalogInventoryDataStockItemInterface catalogInventoryStockRegistryV1GetStockItemBySkuGet(productSku, opts)

stockItems/{productSku}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.StockItemsProductSkuApi();
let productSku = "productSku_example"; // String | 
let opts = {
  'scopeId': 56 // Number | 
};
apiInstance.catalogInventoryStockRegistryV1GetStockItemBySkuGet(productSku, opts, (error, data, response) => {
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
 **productSku** | **String**|  | 
 **scopeId** | **Number**|  | [optional] 

### Return type

[**CatalogInventoryDataStockItemInterface**](CatalogInventoryDataStockItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

