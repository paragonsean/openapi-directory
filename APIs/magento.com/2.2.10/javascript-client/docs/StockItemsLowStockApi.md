# MagentoB2B.StockItemsLowStockApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogInventoryStockRegistryV1GetLowStockItemsGet**](StockItemsLowStockApi.md#catalogInventoryStockRegistryV1GetLowStockItemsGet) | **GET** /V1/stockItems/lowStock/ | stockItems/lowStock/



## catalogInventoryStockRegistryV1GetLowStockItemsGet

> CatalogInventoryDataStockItemCollectionInterface catalogInventoryStockRegistryV1GetLowStockItemsGet(scopeId, qty, opts)

stockItems/lowStock/

Retrieves a list of SKU&#39;s with low inventory qty

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.StockItemsLowStockApi();
let scopeId = 56; // Number | 
let qty = 3.4; // Number | 
let opts = {
  'currentPage': 56, // Number | 
  'pageSize': 56 // Number | 
};
apiInstance.catalogInventoryStockRegistryV1GetLowStockItemsGet(scopeId, qty, opts, (error, data, response) => {
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
 **scopeId** | **Number**|  | 
 **qty** | **Number**|  | 
 **currentPage** | **Number**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 

### Return type

[**CatalogInventoryDataStockItemCollectionInterface**](CatalogInventoryDataStockItemCollectionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

