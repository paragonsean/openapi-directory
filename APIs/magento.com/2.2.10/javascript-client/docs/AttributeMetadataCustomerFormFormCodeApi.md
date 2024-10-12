# MagentoB2B.AttributeMetadataCustomerFormFormCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerCustomerMetadataV1GetAttributesGet**](AttributeMetadataCustomerFormFormCodeApi.md#customerCustomerMetadataV1GetAttributesGet) | **GET** /V1/attributeMetadata/customer/form/{formCode} | attributeMetadata/customer/form/{formCode}



## customerCustomerMetadataV1GetAttributesGet

> [CustomerDataAttributeMetadataInterface] customerCustomerMetadataV1GetAttributesGet(formCode)

attributeMetadata/customer/form/{formCode}

Retrieve all attributes filtered by form code

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AttributeMetadataCustomerFormFormCodeApi();
let formCode = "formCode_example"; // String | 
apiInstance.customerCustomerMetadataV1GetAttributesGet(formCode, (error, data, response) => {
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
 **formCode** | **String**|  | 

### Return type

[**[CustomerDataAttributeMetadataInterface]**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

