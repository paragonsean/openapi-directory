# MagentoB2B.CategoriesAttributesAttributeCodeOptionsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCategoryAttributeOptionManagementV1GetItemsGet**](CategoriesAttributesAttributeCodeOptionsApi.md#catalogCategoryAttributeOptionManagementV1GetItemsGet) | **GET** /V1/categories/attributes/{attributeCode}/options | categories/attributes/{attributeCode}/options



## catalogCategoryAttributeOptionManagementV1GetItemsGet

> [EavDataAttributeOptionInterface] catalogCategoryAttributeOptionManagementV1GetItemsGet(attributeCode)

categories/attributes/{attributeCode}/options

Retrieve list of attribute options

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesAttributesAttributeCodeOptionsApi();
let attributeCode = "attributeCode_example"; // String | 
apiInstance.catalogCategoryAttributeOptionManagementV1GetItemsGet(attributeCode, (error, data, response) => {
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

### Return type

[**[EavDataAttributeOptionInterface]**](EavDataAttributeOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

