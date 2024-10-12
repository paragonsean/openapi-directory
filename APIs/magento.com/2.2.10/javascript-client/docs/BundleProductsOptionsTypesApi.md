# MagentoB2B.BundleProductsOptionsTypesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductOptionTypeListV1GetItemsGet**](BundleProductsOptionsTypesApi.md#bundleProductOptionTypeListV1GetItemsGet) | **GET** /V1/bundle-products/options/types | bundle-products/options/types



## bundleProductOptionTypeListV1GetItemsGet

> [BundleDataOptionTypeInterface] bundleProductOptionTypeListV1GetItemsGet()

bundle-products/options/types

Get all types for options for bundle products

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsOptionsTypesApi();
apiInstance.bundleProductOptionTypeListV1GetItemsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[BundleDataOptionTypeInterface]**](BundleDataOptionTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

