# MagentoB2B.ProductsAttributesAttributeCodeOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeOptionManagementV1DeleteDelete**](ProductsAttributesAttributeCodeOptionsOptionIdApi.md#catalogProductAttributeOptionManagementV1DeleteDelete) | **DELETE** /V1/products/attributes/{attributeCode}/options/{optionId} | products/attributes/{attributeCode}/options/{optionId}



## catalogProductAttributeOptionManagementV1DeleteDelete

> Boolean catalogProductAttributeOptionManagementV1DeleteDelete(attributeCode, optionId)

products/attributes/{attributeCode}/options/{optionId}

Delete option from attribute

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesAttributeCodeOptionsOptionIdApi();
let attributeCode = "attributeCode_example"; // String | 
let optionId = "optionId_example"; // String | 
apiInstance.catalogProductAttributeOptionManagementV1DeleteDelete(attributeCode, optionId, (error, data, response) => {
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
 **attributeCode** | **String**|  | 
 **optionId** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

