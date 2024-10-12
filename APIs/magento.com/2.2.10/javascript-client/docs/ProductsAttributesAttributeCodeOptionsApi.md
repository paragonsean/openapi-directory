# MagentoB2B.ProductsAttributesAttributeCodeOptionsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeOptionManagementV1AddPost**](ProductsAttributesAttributeCodeOptionsApi.md#catalogProductAttributeOptionManagementV1AddPost) | **POST** /V1/products/attributes/{attributeCode}/options | products/attributes/{attributeCode}/options
[**catalogProductAttributeOptionManagementV1GetItemsGet**](ProductsAttributesAttributeCodeOptionsApi.md#catalogProductAttributeOptionManagementV1GetItemsGet) | **GET** /V1/products/attributes/{attributeCode}/options | products/attributes/{attributeCode}/options



## catalogProductAttributeOptionManagementV1AddPost

> Boolean catalogProductAttributeOptionManagementV1AddPost(attributeCode, opts)

products/attributes/{attributeCode}/options

Add option to attribute

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesAttributeCodeOptionsApi();
let attributeCode = "attributeCode_example"; // String | 
let opts = {
  'catalogProductAttributeOptionManagementV1AddPostRequest': new MagentoB2B.CatalogProductAttributeOptionManagementV1AddPostRequest() // CatalogProductAttributeOptionManagementV1AddPostRequest | 
};
apiInstance.catalogProductAttributeOptionManagementV1AddPost(attributeCode, opts, (error, data, response) => {
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
 **catalogProductAttributeOptionManagementV1AddPostRequest** | [**CatalogProductAttributeOptionManagementV1AddPostRequest**](CatalogProductAttributeOptionManagementV1AddPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## catalogProductAttributeOptionManagementV1GetItemsGet

> [EavDataAttributeOptionInterface] catalogProductAttributeOptionManagementV1GetItemsGet(attributeCode)

products/attributes/{attributeCode}/options

Retrieve list of attribute options

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributesAttributeCodeOptionsApi();
let attributeCode = "attributeCode_example"; // String | 
apiInstance.catalogProductAttributeOptionManagementV1GetItemsGet(attributeCode, (error, data, response) => {
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

