# MagentoB2B.ConfigurableProductsSkuChildApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurableProductLinkManagementV1AddChildPost**](ConfigurableProductsSkuChildApi.md#configurableProductLinkManagementV1AddChildPost) | **POST** /V1/configurable-products/{sku}/child | configurable-products/{sku}/child



## configurableProductLinkManagementV1AddChildPost

> Boolean configurableProductLinkManagementV1AddChildPost(sku, opts)

configurable-products/{sku}/child



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsSkuChildApi();
let sku = "sku_example"; // String | 
let opts = {
  'configurableProductLinkManagementV1AddChildPostRequest': new MagentoB2B.ConfigurableProductLinkManagementV1AddChildPostRequest() // ConfigurableProductLinkManagementV1AddChildPostRequest | 
};
apiInstance.configurableProductLinkManagementV1AddChildPost(sku, opts, (error, data, response) => {
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
 **configurableProductLinkManagementV1AddChildPostRequest** | [**ConfigurableProductLinkManagementV1AddChildPostRequest**](ConfigurableProductLinkManagementV1AddChildPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

