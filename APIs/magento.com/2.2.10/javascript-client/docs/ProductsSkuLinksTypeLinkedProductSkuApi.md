# MagentoB2B.ProductsSkuLinksTypeLinkedProductSkuApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductLinkRepositoryV1DeleteByIdDelete**](ProductsSkuLinksTypeLinkedProductSkuApi.md#catalogProductLinkRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/{sku}/links/{type}/{linkedProductSku} | products/{sku}/links/{type}/{linkedProductSku}



## catalogProductLinkRepositoryV1DeleteByIdDelete

> Boolean catalogProductLinkRepositoryV1DeleteByIdDelete(sku, type, linkedProductSku)

products/{sku}/links/{type}/{linkedProductSku}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuLinksTypeLinkedProductSkuApi();
let sku = "sku_example"; // String | 
let type = "type_example"; // String | 
let linkedProductSku = "linkedProductSku_example"; // String | 
apiInstance.catalogProductLinkRepositoryV1DeleteByIdDelete(sku, type, linkedProductSku, (error, data, response) => {
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
 **type** | **String**|  | 
 **linkedProductSku** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

