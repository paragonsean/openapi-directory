# MagentoB2B.CategoriesAttributesAttributeCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCategoryAttributeRepositoryV1GetGet**](CategoriesAttributesAttributeCodeApi.md#catalogCategoryAttributeRepositoryV1GetGet) | **GET** /V1/categories/attributes/{attributeCode} | categories/attributes/{attributeCode}



## catalogCategoryAttributeRepositoryV1GetGet

> CatalogDataCategoryAttributeInterface catalogCategoryAttributeRepositoryV1GetGet(attributeCode)

categories/attributes/{attributeCode}

Retrieve specific attribute

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesAttributesAttributeCodeApi();
let attributeCode = "attributeCode_example"; // String | 
apiInstance.catalogCategoryAttributeRepositoryV1GetGet(attributeCode, (error, data, response) => {
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

[**CatalogDataCategoryAttributeInterface**](CatalogDataCategoryAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

