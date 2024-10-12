# MagentoB2B.BundleProductsSkuLinksOptionIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductLinkManagementV1AddChildByProductSkuPost**](BundleProductsSkuLinksOptionIdApi.md#bundleProductLinkManagementV1AddChildByProductSkuPost) | **POST** /V1/bundle-products/{sku}/links/{optionId} | bundle-products/{sku}/links/{optionId}



## bundleProductLinkManagementV1AddChildByProductSkuPost

> Number bundleProductLinkManagementV1AddChildByProductSkuPost(sku, optionId, opts)

bundle-products/{sku}/links/{optionId}

Add child product to specified Bundle option by product sku

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsSkuLinksOptionIdApi();
let sku = "sku_example"; // String | 
let optionId = 56; // Number | 
let opts = {
  'bundleProductLinkManagementV1SaveChildPutRequest': new MagentoB2B.BundleProductLinkManagementV1SaveChildPutRequest() // BundleProductLinkManagementV1SaveChildPutRequest | 
};
apiInstance.bundleProductLinkManagementV1AddChildByProductSkuPost(sku, optionId, opts, (error, data, response) => {
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
 **bundleProductLinkManagementV1SaveChildPutRequest** | [**BundleProductLinkManagementV1SaveChildPutRequest**](BundleProductLinkManagementV1SaveChildPutRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

