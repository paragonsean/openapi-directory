# MagentoB2B.BundleProductsProductSkuChildrenApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductLinkManagementV1GetChildrenGet**](BundleProductsProductSkuChildrenApi.md#bundleProductLinkManagementV1GetChildrenGet) | **GET** /V1/bundle-products/{productSku}/children | bundle-products/{productSku}/children



## bundleProductLinkManagementV1GetChildrenGet

> [BundleDataLinkInterface] bundleProductLinkManagementV1GetChildrenGet(productSku, opts)

bundle-products/{productSku}/children

Get all children for Bundle product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsProductSkuChildrenApi();
let productSku = "productSku_example"; // String | 
let opts = {
  'optionId': 56 // Number | 
};
apiInstance.bundleProductLinkManagementV1GetChildrenGet(productSku, opts, (error, data, response) => {
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
 **optionId** | **Number**|  | [optional] 

### Return type

[**[BundleDataLinkInterface]**](BundleDataLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

