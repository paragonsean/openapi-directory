# MagentoB2B.BundleProductsSkuOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundleProductOptionRepositoryV1DeleteByIdDelete**](BundleProductsSkuOptionsOptionIdApi.md#bundleProductOptionRepositoryV1DeleteByIdDelete) | **DELETE** /V1/bundle-products/{sku}/options/{optionId} | bundle-products/{sku}/options/{optionId}
[**bundleProductOptionRepositoryV1GetGet**](BundleProductsSkuOptionsOptionIdApi.md#bundleProductOptionRepositoryV1GetGet) | **GET** /V1/bundle-products/{sku}/options/{optionId} | bundle-products/{sku}/options/{optionId}



## bundleProductOptionRepositoryV1DeleteByIdDelete

> Boolean bundleProductOptionRepositoryV1DeleteByIdDelete(sku, optionId)

bundle-products/{sku}/options/{optionId}

Remove bundle option

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsSkuOptionsOptionIdApi();
let sku = "sku_example"; // String | 
let optionId = 56; // Number | 
apiInstance.bundleProductOptionRepositoryV1DeleteByIdDelete(sku, optionId, (error, data, response) => {
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

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## bundleProductOptionRepositoryV1GetGet

> BundleDataOptionInterface bundleProductOptionRepositoryV1GetGet(sku, optionId)

bundle-products/{sku}/options/{optionId}

Get option for bundle product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.BundleProductsSkuOptionsOptionIdApi();
let sku = "sku_example"; // String | 
let optionId = 56; // Number | 
apiInstance.bundleProductOptionRepositoryV1GetGet(sku, optionId, (error, data, response) => {
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

### Return type

[**BundleDataOptionInterface**](BundleDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

