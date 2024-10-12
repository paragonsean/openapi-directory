# MagentoB2B.ProductsAttributeSetsAttributeSetIdAttributesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeManagementV1GetAttributesGet**](ProductsAttributeSetsAttributeSetIdAttributesApi.md#catalogProductAttributeManagementV1GetAttributesGet) | **GET** /V1/products/attribute-sets/{attributeSetId}/attributes | products/attribute-sets/{attributeSetId}/attributes



## catalogProductAttributeManagementV1GetAttributesGet

> [CatalogDataProductAttributeInterface] catalogProductAttributeManagementV1GetAttributesGet(attributeSetId)

products/attribute-sets/{attributeSetId}/attributes

Retrieve related attributes based on given attribute set ID

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsAttributeSetIdAttributesApi();
let attributeSetId = "attributeSetId_example"; // String | 
apiInstance.catalogProductAttributeManagementV1GetAttributesGet(attributeSetId, (error, data, response) => {
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

### Return type

[**[CatalogDataProductAttributeInterface]**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

