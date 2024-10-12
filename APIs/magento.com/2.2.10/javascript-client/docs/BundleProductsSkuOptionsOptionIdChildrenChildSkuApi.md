# MagentoB2B.BundleProductsSkuOptionsOptionIdChildrenChildSkuApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductLinkManagementV1RemoveChildDelete**](BundleProductsSkuOptionsOptionIdChildrenChildSkuApi.md#bundleProductLinkManagementV1RemoveChildDelete) | **DELETE** /V1/bundle-products/{sku}/options/{optionId}/children/{childSku} | bundle-products/{sku}/options/{optionId}/children/{childSku}



## bundleProductLinkManagementV1RemoveChildDelete

> Boolean bundleProductLinkManagementV1RemoveChildDelete(sku, optionId, childSku)

bundle-products/{sku}/options/{optionId}/children/{childSku}

Remove product from Bundle product option

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsSkuOptionsOptionIdChildrenChildSkuApi();
let sku = "sku_example"; // String | 
let optionId = 56; // Number | 
let childSku = "childSku_example"; // String | 
apiInstance.bundleProductLinkManagementV1RemoveChildDelete(sku, optionId, childSku, (error, data, response) => {
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
 **optionId** | **Number**|  | 
 **childSku** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

