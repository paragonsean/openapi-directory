# MagentoB2B.AttributeMetadataCustomerAttributeAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerCustomerMetadataV1GetAttributeMetadataGet**](AttributeMetadataCustomerAttributeAttributeCodeApi.md#customerCustomerMetadataV1GetAttributeMetadataGet) | **GET** /V1/attributeMetadata/customer/attribute/{attributeCode} | attributeMetadata/customer/attribute/{attributeCode}



## customerCustomerMetadataV1GetAttributeMetadataGet

> CustomerDataAttributeMetadataInterface customerCustomerMetadataV1GetAttributeMetadataGet(attributeCode)

attributeMetadata/customer/attribute/{attributeCode}

Retrieve attribute metadata.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AttributeMetadataCustomerAttributeAttributeCodeApi();
let attributeCode = "attributeCode_example"; // String | 
apiInstance.customerCustomerMetadataV1GetAttributeMetadataGet(attributeCode, (error, data, response) => {
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
 **attributeCode** | **String**|  | 

### Return type

[**CustomerDataAttributeMetadataInterface**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

