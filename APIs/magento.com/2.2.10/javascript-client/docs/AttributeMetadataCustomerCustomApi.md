# MagentoB2B.AttributeMetadataCustomerCustomApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerCustomerMetadataV1GetCustomAttributesMetadataGet**](AttributeMetadataCustomerCustomApi.md#customerCustomerMetadataV1GetCustomAttributesMetadataGet) | **GET** /V1/attributeMetadata/customer/custom | attributeMetadata/customer/custom



## customerCustomerMetadataV1GetCustomAttributesMetadataGet

> [CustomerDataAttributeMetadataInterface] customerCustomerMetadataV1GetCustomAttributesMetadataGet(opts)

attributeMetadata/customer/custom

Get custom attributes metadata for the given data interface.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AttributeMetadataCustomerCustomApi();
let opts = {
  'dataInterfaceName': "dataInterfaceName_example" // String | 
};
apiInstance.customerCustomerMetadataV1GetCustomAttributesMetadataGet(opts, (error, data, response) => {
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
 **dataInterfaceName** | **String**|  | [optional] 

### Return type

[**[CustomerDataAttributeMetadataInterface]**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

