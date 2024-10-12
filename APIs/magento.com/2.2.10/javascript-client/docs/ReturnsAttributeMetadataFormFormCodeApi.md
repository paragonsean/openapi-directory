# MagentoB2B.ReturnsAttributeMetadataFormFormCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaRmaAttributesManagementV1GetAttributesGet**](ReturnsAttributeMetadataFormFormCodeApi.md#rmaRmaAttributesManagementV1GetAttributesGet) | **GET** /V1/returnsAttributeMetadata/form/{formCode} | returnsAttributeMetadata/form/{formCode}



## rmaRmaAttributesManagementV1GetAttributesGet

> [CustomerDataAttributeMetadataInterface] rmaRmaAttributesManagementV1GetAttributesGet(formCode)

returnsAttributeMetadata/form/{formCode}

Retrieve all attributes filtered by form code

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsAttributeMetadataFormFormCodeApi();
let formCode = "formCode_example"; // String | 
apiInstance.rmaRmaAttributesManagementV1GetAttributesGet(formCode, (error, data, response) => {
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

