# MagentoB2B.ProductsAttributeSetsGroupsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeGroupRepositoryV1SavePost**](ProductsAttributeSetsGroupsApi.md#catalogProductAttributeGroupRepositoryV1SavePost) | **POST** /V1/products/attribute-sets/groups | products/attribute-sets/groups



## catalogProductAttributeGroupRepositoryV1SavePost

> EavDataAttributeGroupInterface catalogProductAttributeGroupRepositoryV1SavePost(opts)

products/attribute-sets/groups

Save attribute group

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsGroupsApi();
let opts = {
  'catalogProductAttributeGroupRepositoryV1SavePostRequest': new MagentoB2B.CatalogProductAttributeGroupRepositoryV1SavePostRequest() // CatalogProductAttributeGroupRepositoryV1SavePostRequest | 
};
apiInstance.catalogProductAttributeGroupRepositoryV1SavePost(opts, (error, data, response) => {
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
 **catalogProductAttributeGroupRepositoryV1SavePostRequest** | [**CatalogProductAttributeGroupRepositoryV1SavePostRequest**](CatalogProductAttributeGroupRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**EavDataAttributeGroupInterface**](EavDataAttributeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

