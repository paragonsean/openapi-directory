# MagentoB2B.ConfigurableProductsVariationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurableProductConfigurableProductManagementV1GenerateVariationPut**](ConfigurableProductsVariationApi.md#configurableProductConfigurableProductManagementV1GenerateVariationPut) | **PUT** /V1/configurable-products/variation | configurable-products/variation



## configurableProductConfigurableProductManagementV1GenerateVariationPut

> [CatalogDataProductInterface] configurableProductConfigurableProductManagementV1GenerateVariationPut(opts)

configurable-products/variation

Generate variation based on same product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsVariationApi();
let opts = {
  'configurableProductConfigurableProductManagementV1GenerateVariationPutRequest': new MagentoB2B.ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest() // ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest | 
};
apiInstance.configurableProductConfigurableProductManagementV1GenerateVariationPut(opts, (error, data, response) => {
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
 **configurableProductConfigurableProductManagementV1GenerateVariationPutRequest** | [**ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest**](ConfigurableProductConfigurableProductManagementV1GenerateVariationPutRequest.md)|  | [optional] 

### Return type

[**[CatalogDataProductInterface]**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

