# MagentoB2B.SharedCatalogIdUnassignCategoriesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogCategoryManagementV1UnassignCategoriesPost**](SharedCatalogIdUnassignCategoriesApi.md#sharedCatalogCategoryManagementV1UnassignCategoriesPost) | **POST** /V1/sharedCatalog/{id}/unassignCategories | sharedCatalog/{id}/unassignCategories



## sharedCatalogCategoryManagementV1UnassignCategoriesPost

> Boolean sharedCatalogCategoryManagementV1UnassignCategoriesPost(id, opts)

sharedCatalog/{id}/unassignCategories

Remove the specified categories from the shared catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogIdUnassignCategoriesApi();
let id = 56; // Number | 
let opts = {
  'sharedCatalogCategoryManagementV1AssignCategoriesPostRequest': new MagentoB2B.SharedCatalogCategoryManagementV1AssignCategoriesPostRequest() // SharedCatalogCategoryManagementV1AssignCategoriesPostRequest | 
};
apiInstance.sharedCatalogCategoryManagementV1UnassignCategoriesPost(id, opts, (error, data, response) => {
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

