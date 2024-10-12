# MagentoB2B.AttributeMetadataCustomerAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAddressMetadataV1GetAllAttributesMetadataGet**](AttributeMetadataCustomerAddressApi.md#customerAddressMetadataV1GetAllAttributesMetadataGet) | **GET** /V1/attributeMetadata/customerAddress | attributeMetadata/customerAddress



## customerAddressMetadataV1GetAllAttributesMetadataGet

> [CustomerDataAttributeMetadataInterface] customerAddressMetadataV1GetAllAttributesMetadataGet()

attributeMetadata/customerAddress

Get all attribute metadata.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AttributeMetadataCustomerAddressApi();
apiInstance.customerAddressMetadataV1GetAllAttributesMetadataGet((error, data, response) => {
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

[**[CustomerDataAttributeMetadataInterface]**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

