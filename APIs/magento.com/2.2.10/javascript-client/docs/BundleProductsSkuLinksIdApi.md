# MagentoB2B.BundleProductsSkuLinksIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductLinkManagementV1SaveChildPut**](BundleProductsSkuLinksIdApi.md#bundleProductLinkManagementV1SaveChildPut) | **PUT** /V1/bundle-products/{sku}/links/{id} | bundle-products/{sku}/links/{id}



## bundleProductLinkManagementV1SaveChildPut

> Boolean bundleProductLinkManagementV1SaveChildPut(sku, id, opts)

bundle-products/{sku}/links/{id}



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsSkuLinksIdApi();
let sku = "sku_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'bundleProductLinkManagementV1SaveChildPutRequest': new MagentoB2B.BundleProductLinkManagementV1SaveChildPutRequest() // BundleProductLinkManagementV1SaveChildPutRequest | 
};
apiInstance.bundleProductLinkManagementV1SaveChildPut(sku, id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **bundleProductLinkManagementV1SaveChildPutRequest** | [**BundleProductLinkManagementV1SaveChildPutRequest**](BundleProductLinkManagementV1SaveChildPutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

