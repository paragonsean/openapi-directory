# MagentoB2B.CategoriesCategoryIdMoveApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCategoryManagementV1MovePut**](CategoriesCategoryIdMoveApi.md#catalogCategoryManagementV1MovePut) | **PUT** /V1/categories/{categoryId}/move | categories/{categoryId}/move



## catalogCategoryManagementV1MovePut

> Boolean catalogCategoryManagementV1MovePut(categoryId, opts)

categories/{categoryId}/move

Move category

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesCategoryIdMoveApi();
let categoryId = 56; // Number | 
let opts = {
  'catalogCategoryManagementV1MovePutRequest': new MagentoB2B.CatalogCategoryManagementV1MovePutRequest() // CatalogCategoryManagementV1MovePutRequest | 
};
apiInstance.catalogCategoryManagementV1MovePut(categoryId, opts, (error, data, response) => {
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
 **categoryId** | **Number**|  | 
 **catalogCategoryManagementV1MovePutRequest** | [**CatalogCategoryManagementV1MovePutRequest**](CatalogCategoryManagementV1MovePutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

