# MagentoB2B.ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeManagementV1UnassignDelete**](ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi.md#catalogProductAttributeManagementV1UnassignDelete) | **DELETE** /V1/products/attribute-sets/{attributeSetId}/attributes/{attributeCode} | products/attribute-sets/{attributeSetId}/attributes/{attributeCode}



## catalogProductAttributeManagementV1UnassignDelete

> Boolean catalogProductAttributeManagementV1UnassignDelete(attributeSetId, attributeCode)

products/attribute-sets/{attributeSetId}/attributes/{attributeCode}

Remove attribute from attribute set

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsAttributeSetIdAttributesAttributeCodeApi();
let attributeSetId = "attributeSetId_example"; // String | 
let attributeCode = "attributeCode_example"; // String | 
apiInstance.catalogProductAttributeManagementV1UnassignDelete(attributeSetId, attributeCode, (error, data, response) => {
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
 **attributeCode** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

