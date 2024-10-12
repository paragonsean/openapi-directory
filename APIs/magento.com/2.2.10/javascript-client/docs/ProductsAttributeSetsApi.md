# MagentoB2B.ProductsAttributeSetsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogAttributeSetManagementV1CreatePost**](ProductsAttributeSetsApi.md#catalogAttributeSetManagementV1CreatePost) | **POST** /V1/products/attribute-sets | products/attribute-sets



## catalogAttributeSetManagementV1CreatePost

> EavDataAttributeSetInterface catalogAttributeSetManagementV1CreatePost(opts)

products/attribute-sets

Create attribute set from data

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsApi();
let opts = {
  'catalogAttributeSetManagementV1CreatePostRequest': new MagentoB2B.CatalogAttributeSetManagementV1CreatePostRequest() // CatalogAttributeSetManagementV1CreatePostRequest | 
};
apiInstance.catalogAttributeSetManagementV1CreatePost(opts, (error, data, response) => {
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
 **catalogAttributeSetManagementV1CreatePostRequest** | [**CatalogAttributeSetManagementV1CreatePostRequest**](CatalogAttributeSetManagementV1CreatePostRequest.md)|  | [optional] 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

