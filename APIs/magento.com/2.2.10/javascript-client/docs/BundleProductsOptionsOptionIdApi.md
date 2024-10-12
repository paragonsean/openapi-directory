# MagentoB2B.BundleProductsOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductOptionManagementV1SavePut**](BundleProductsOptionsOptionIdApi.md#bundleProductOptionManagementV1SavePut) | **PUT** /V1/bundle-products/options/{optionId} | bundle-products/options/{optionId}



## bundleProductOptionManagementV1SavePut

> Number bundleProductOptionManagementV1SavePut(optionId, opts)

bundle-products/options/{optionId}

Add new option for bundle product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsOptionsOptionIdApi();
let optionId = "optionId_example"; // String | 
let opts = {
  'bundleProductOptionManagementV1SavePostRequest': new MagentoB2B.BundleProductOptionManagementV1SavePostRequest() // BundleProductOptionManagementV1SavePostRequest | 
};
apiInstance.bundleProductOptionManagementV1SavePut(optionId, opts, (error, data, response) => {
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
 **optionId** | **String**|  | 
 **bundleProductOptionManagementV1SavePostRequest** | [**BundleProductOptionManagementV1SavePostRequest**](BundleProductOptionManagementV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

