# MagentoB2B.ReturnsAttributeMetadataCustomApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet**](ReturnsAttributeMetadataCustomApi.md#rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet) | **GET** /V1/returnsAttributeMetadata/custom | returnsAttributeMetadata/custom



## rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet

> [FrameworkMetadataObjectInterface] rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet(opts)

returnsAttributeMetadata/custom

Get custom attribute metadata for the given Data object&#39;s attribute set

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsAttributeMetadataCustomApi();
let opts = {
  'dataObjectClassName': "dataObjectClassName_example" // String | Data object class name
};
apiInstance.rmaRmaAttributesManagementV1GetCustomAttributesMetadataGet(opts, (error, data, response) => {
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
 **dataObjectClassName** | **String**| Data object class name | [optional] 

### Return type

[**[FrameworkMetadataObjectInterface]**](FrameworkMetadataObjectInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

