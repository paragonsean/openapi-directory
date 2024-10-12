# MagentoB2B.AttributeMetadataCustomerAddressFormFormCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAddressMetadataV1GetAttributesGet**](AttributeMetadataCustomerAddressFormFormCodeApi.md#customerAddressMetadataV1GetAttributesGet) | **GET** /V1/attributeMetadata/customerAddress/form/{formCode} | attributeMetadata/customerAddress/form/{formCode}



## customerAddressMetadataV1GetAttributesGet

> [CustomerDataAttributeMetadataInterface] customerAddressMetadataV1GetAttributesGet(formCode)

attributeMetadata/customerAddress/form/{formCode}

Retrieve all attributes filtered by form code

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AttributeMetadataCustomerAddressFormFormCodeApi();
let formCode = "formCode_example"; // String | 
apiInstance.customerAddressMetadataV1GetAttributesGet(formCode, (error, data, response) => {
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

