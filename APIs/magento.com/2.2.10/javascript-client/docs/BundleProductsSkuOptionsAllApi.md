# MagentoB2B.BundleProductsSkuOptionsAllApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductOptionRepositoryV1GetListGet**](BundleProductsSkuOptionsAllApi.md#bundleProductOptionRepositoryV1GetListGet) | **GET** /V1/bundle-products/{sku}/options/all | bundle-products/{sku}/options/all



## bundleProductOptionRepositoryV1GetListGet

> [BundleDataOptionInterface] bundleProductOptionRepositoryV1GetListGet(sku)

bundle-products/{sku}/options/all

Get all options for bundle product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsSkuOptionsAllApi();
let sku = "sku_example"; // String | 
apiInstance.bundleProductOptionRepositoryV1GetListGet(sku, (error, data, response) => {
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

[**[BundleDataOptionInterface]**](BundleDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

