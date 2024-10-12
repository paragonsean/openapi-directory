# MagentoB2B.AttributeMetadataCustomerAddressAttributeAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAddressMetadataV1GetAttributeMetadataGet**](AttributeMetadataCustomerAddressAttributeAttributeCodeApi.md#customerAddressMetadataV1GetAttributeMetadataGet) | **GET** /V1/attributeMetadata/customerAddress/attribute/{attributeCode} | attributeMetadata/customerAddress/attribute/{attributeCode}



## customerAddressMetadataV1GetAttributeMetadataGet

> CustomerDataAttributeMetadataInterface customerAddressMetadataV1GetAttributeMetadataGet(attributeCode)

attributeMetadata/customerAddress/attribute/{attributeCode}

Retrieve attribute metadata.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AttributeMetadataCustomerAddressAttributeAttributeCodeApi();
let attributeCode = "attributeCode_example"; // String | 
apiInstance.customerAddressMetadataV1GetAttributeMetadataGet(attributeCode, (error, data, response) => {
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

