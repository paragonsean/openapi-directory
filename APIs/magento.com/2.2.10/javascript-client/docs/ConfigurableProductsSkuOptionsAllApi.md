# MagentoB2B.ConfigurableProductsSkuOptionsAllApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurableProductOptionRepositoryV1GetListGet**](ConfigurableProductsSkuOptionsAllApi.md#configurableProductOptionRepositoryV1GetListGet) | **GET** /V1/configurable-products/{sku}/options/all | configurable-products/{sku}/options/all



## configurableProductOptionRepositoryV1GetListGet

> [ConfigurableProductDataOptionInterface] configurableProductOptionRepositoryV1GetListGet(sku)

configurable-products/{sku}/options/all

Get all options for configurable product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsSkuOptionsAllApi();
let sku = "sku_example"; // String | 
apiInstance.configurableProductOptionRepositoryV1GetListGet(sku, (error, data, response) => {
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

### Return type

[**[ConfigurableProductDataOptionInterface]**](ConfigurableProductDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

