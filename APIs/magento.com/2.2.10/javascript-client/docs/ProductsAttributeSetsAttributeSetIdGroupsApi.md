# MagentoB2B.ProductsAttributeSetsAttributeSetIdGroupsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeGroupRepositoryV1SavePut**](ProductsAttributeSetsAttributeSetIdGroupsApi.md#catalogProductAttributeGroupRepositoryV1SavePut) | **PUT** /V1/products/attribute-sets/{attributeSetId}/groups | products/attribute-sets/{attributeSetId}/groups



## catalogProductAttributeGroupRepositoryV1SavePut

> EavDataAttributeGroupInterface catalogProductAttributeGroupRepositoryV1SavePut(attributeSetId, opts)

products/attribute-sets/{attributeSetId}/groups

Save attribute group

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsAttributeSetIdGroupsApi();
let attributeSetId = "attributeSetId_example"; // String | 
let opts = {
  'catalogProductAttributeGroupRepositoryV1SavePostRequest': new MagentoB2B.CatalogProductAttributeGroupRepositoryV1SavePostRequest() // CatalogProductAttributeGroupRepositoryV1SavePostRequest | 
};
apiInstance.catalogProductAttributeGroupRepositoryV1SavePut(attributeSetId, opts, (error, data, response) => {
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
 **attributeSetId** | **String**|  | 
 **catalogProductAttributeGroupRepositoryV1SavePostRequest** | [**CatalogProductAttributeGroupRepositoryV1SavePostRequest**](CatalogProductAttributeGroupRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**EavDataAttributeGroupInterface**](EavDataAttributeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

