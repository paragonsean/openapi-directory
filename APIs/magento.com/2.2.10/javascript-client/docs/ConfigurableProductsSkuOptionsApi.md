# MagentoB2B.ConfigurableProductsSkuOptionsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurableProductOptionRepositoryV1SavePost**](ConfigurableProductsSkuOptionsApi.md#configurableProductOptionRepositoryV1SavePost) | **POST** /V1/configurable-products/{sku}/options | configurable-products/{sku}/options



## configurableProductOptionRepositoryV1SavePost

> Number configurableProductOptionRepositoryV1SavePost(sku, opts)

configurable-products/{sku}/options

Save option

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsSkuOptionsApi();
let sku = "sku_example"; // String | 
let opts = {
  'configurableProductOptionRepositoryV1SavePostRequest': new MagentoB2B.ConfigurableProductOptionRepositoryV1SavePostRequest() // ConfigurableProductOptionRepositoryV1SavePostRequest | 
};
apiInstance.configurableProductOptionRepositoryV1SavePost(sku, opts, (error, data, response) => {
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
 **configurableProductOptionRepositoryV1SavePostRequest** | [**ConfigurableProductOptionRepositoryV1SavePostRequest**](ConfigurableProductOptionRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

