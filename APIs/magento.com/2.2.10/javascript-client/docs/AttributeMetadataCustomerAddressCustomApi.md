# MagentoB2B.AttributeMetadataCustomerAddressCustomApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAddressMetadataV1GetCustomAttributesMetadataGet**](AttributeMetadataCustomerAddressCustomApi.md#customerAddressMetadataV1GetCustomAttributesMetadataGet) | **GET** /V1/attributeMetadata/customerAddress/custom | attributeMetadata/customerAddress/custom



## customerAddressMetadataV1GetCustomAttributesMetadataGet

> [CustomerDataAttributeMetadataInterface] customerAddressMetadataV1GetCustomAttributesMetadataGet(opts)

attributeMetadata/customerAddress/custom

Get custom attributes metadata for the given data interface.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AttributeMetadataCustomerAddressCustomApi();
let opts = {
  'dataInterfaceName': "dataInterfaceName_example" // String | 
};
apiInstance.customerAddressMetadataV1GetCustomAttributesMetadataGet(opts, (error, data, response) => {
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

