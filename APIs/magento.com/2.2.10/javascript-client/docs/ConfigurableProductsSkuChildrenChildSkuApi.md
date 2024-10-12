# MagentoB2B.ConfigurableProductsSkuChildrenChildSkuApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurableProductLinkManagementV1RemoveChildDelete**](ConfigurableProductsSkuChildrenChildSkuApi.md#configurableProductLinkManagementV1RemoveChildDelete) | **DELETE** /V1/configurable-products/{sku}/children/{childSku} | configurable-products/{sku}/children/{childSku}



## configurableProductLinkManagementV1RemoveChildDelete

> Boolean configurableProductLinkManagementV1RemoveChildDelete(sku, childSku)

configurable-products/{sku}/children/{childSku}

Remove configurable product option

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsSkuChildrenChildSkuApi();
let sku = "sku_example"; // String | 
let childSku = "childSku_example"; // String | 
apiInstance.configurableProductLinkManagementV1RemoveChildDelete(sku, childSku, (error, data, response) => {
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
 **childSku** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

