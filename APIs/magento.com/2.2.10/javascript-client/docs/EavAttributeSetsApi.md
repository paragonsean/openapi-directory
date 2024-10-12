# MagentoB2B.EavAttributeSetsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eavAttributeSetManagementV1CreatePost**](EavAttributeSetsApi.md#eavAttributeSetManagementV1CreatePost) | **POST** /V1/eav/attribute-sets | eav/attribute-sets



## eavAttributeSetManagementV1CreatePost

> EavDataAttributeSetInterface eavAttributeSetManagementV1CreatePost(opts)

eav/attribute-sets

Create attribute set from data

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.EavAttributeSetsApi();
let opts = {
  'eavAttributeSetManagementV1CreatePostRequest': new MagentoB2B.EavAttributeSetManagementV1CreatePostRequest() // EavAttributeSetManagementV1CreatePostRequest | 
};
apiInstance.eavAttributeSetManagementV1CreatePost(opts, (error, data, response) => {
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
 **eavAttributeSetManagementV1CreatePostRequest** | [**EavAttributeSetManagementV1CreatePostRequest**](EavAttributeSetManagementV1CreatePostRequest.md)|  | [optional] 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

