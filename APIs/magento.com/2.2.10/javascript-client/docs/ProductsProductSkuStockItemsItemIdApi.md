# MagentoB2B.ProductsProductSkuStockItemsItemIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogInventoryStockRegistryV1UpdateStockItemBySkuPut**](ProductsProductSkuStockItemsItemIdApi.md#catalogInventoryStockRegistryV1UpdateStockItemBySkuPut) | **PUT** /V1/products/{productSku}/stockItems/{itemId} | products/{productSku}/stockItems/{itemId}



## catalogInventoryStockRegistryV1UpdateStockItemBySkuPut

> Number catalogInventoryStockRegistryV1UpdateStockItemBySkuPut(productSku, itemId, opts)

products/{productSku}/stockItems/{itemId}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsProductSkuStockItemsItemIdApi();
let productSku = "productSku_example"; // String | 
let itemId = "itemId_example"; // String | 
let opts = {
  'catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest': new MagentoB2B.CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest() // CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest | 
};
apiInstance.catalogInventoryStockRegistryV1UpdateStockItemBySkuPut(productSku, itemId, opts, (error, data, response) => {
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
 **itemId** | **String**|  | 
 **catalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest** | [**CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest**](CatalogInventoryStockRegistryV1UpdateStockItemBySkuPutRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

