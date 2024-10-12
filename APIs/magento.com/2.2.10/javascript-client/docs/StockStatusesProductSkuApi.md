# MagentoB2B.StockStatusesProductSkuApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogInventoryStockRegistryV1GetStockStatusBySkuGet**](StockStatusesProductSkuApi.md#catalogInventoryStockRegistryV1GetStockStatusBySkuGet) | **GET** /V1/stockStatuses/{productSku} | stockStatuses/{productSku}



## catalogInventoryStockRegistryV1GetStockStatusBySkuGet

> CatalogInventoryDataStockStatusInterface catalogInventoryStockRegistryV1GetStockStatusBySkuGet(productSku, opts)

stockStatuses/{productSku}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.StockStatusesProductSkuApi();
let productSku = "productSku_example"; // String | 
let opts = {
  'scopeId': 56 // Number | 
};
apiInstance.catalogInventoryStockRegistryV1GetStockStatusBySkuGet(productSku, opts, (error, data, response) => {
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

[**CatalogInventoryDataStockStatusInterface**](CatalogInventoryDataStockStatusInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

