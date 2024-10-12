# MagentoB2B.ReturnsAttributeMetadataApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaRmaAttributesManagementV1GetAllAttributesMetadataGet**](ReturnsAttributeMetadataApi.md#rmaRmaAttributesManagementV1GetAllAttributesMetadataGet) | **GET** /V1/returnsAttributeMetadata | returnsAttributeMetadata



## rmaRmaAttributesManagementV1GetAllAttributesMetadataGet

> [CustomerDataAttributeMetadataInterface] rmaRmaAttributesManagementV1GetAllAttributesMetadataGet()

returnsAttributeMetadata

Get all attribute metadata.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsAttributeMetadataApi();
apiInstance.rmaRmaAttributesManagementV1GetAllAttributesMetadataGet((error, data, response) => {
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

