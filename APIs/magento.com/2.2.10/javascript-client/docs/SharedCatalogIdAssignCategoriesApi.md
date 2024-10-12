# MagentoB2B.SharedCatalogIdAssignCategoriesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogCategoryManagementV1AssignCategoriesPost**](SharedCatalogIdAssignCategoriesApi.md#sharedCatalogCategoryManagementV1AssignCategoriesPost) | **POST** /V1/sharedCatalog/{id}/assignCategories | sharedCatalog/{id}/assignCategories



## sharedCatalogCategoryManagementV1AssignCategoriesPost

> Boolean sharedCatalogCategoryManagementV1AssignCategoriesPost(id, opts)

sharedCatalog/{id}/assignCategories

Add categories into the shared catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogIdAssignCategoriesApi();
let id = 56; // Number | 
let opts = {
  'sharedCatalogCategoryManagementV1AssignCategoriesPostRequest': new MagentoB2B.SharedCatalogCategoryManagementV1AssignCategoriesPostRequest() // SharedCatalogCategoryManagementV1AssignCategoriesPostRequest | 
};
apiInstance.sharedCatalogCategoryManagementV1AssignCategoriesPost(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **sharedCatalogCategoryManagementV1AssignCategoriesPostRequest** | [**SharedCatalogCategoryManagementV1AssignCategoriesPostRequest**](SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

