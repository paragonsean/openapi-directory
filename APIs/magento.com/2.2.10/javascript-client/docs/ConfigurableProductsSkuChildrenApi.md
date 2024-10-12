# MagentoB2B.ConfigurableProductsSkuChildrenApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurableProductLinkManagementV1GetChildrenGet**](ConfigurableProductsSkuChildrenApi.md#configurableProductLinkManagementV1GetChildrenGet) | **GET** /V1/configurable-products/{sku}/children | configurable-products/{sku}/children



## configurableProductLinkManagementV1GetChildrenGet

> [CatalogDataProductInterface] configurableProductLinkManagementV1GetChildrenGet(sku)

configurable-products/{sku}/children

Get all children for Configurable product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsSkuChildrenApi();
let sku = "sku_example"; // String | 
apiInstance.configurableProductLinkManagementV1GetChildrenGet(sku, (error, data, response) => {
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

[**[CatalogDataProductInterface]**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

