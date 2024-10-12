# MagentoB2B.BundleProductsOptionsAddApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductOptionManagementV1SavePost**](BundleProductsOptionsAddApi.md#bundleProductOptionManagementV1SavePost) | **POST** /V1/bundle-products/options/add | bundle-products/options/add



## bundleProductOptionManagementV1SavePost

> Number bundleProductOptionManagementV1SavePost(opts)

bundle-products/options/add

Add new option for bundle product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsOptionsAddApi();
let opts = {
  'bundleProductOptionManagementV1SavePostRequest': new MagentoB2B.BundleProductOptionManagementV1SavePostRequest() // BundleProductOptionManagementV1SavePostRequest | 
};
apiInstance.bundleProductOptionManagementV1SavePost(opts, (error, data, response) => {
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
 **bundleProductOptionManagementV1SavePostRequest** | [**BundleProductOptionManagementV1SavePostRequest**](BundleProductOptionManagementV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

