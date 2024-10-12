# MagentoB2B.SharedCatalogIdCategoriesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogCategoryManagementV1GetCategoriesGet**](SharedCatalogIdCategoriesApi.md#sharedCatalogCategoryManagementV1GetCategoriesGet) | **GET** /V1/sharedCatalog/{id}/categories | sharedCatalog/{id}/categories



## sharedCatalogCategoryManagementV1GetCategoriesGet

> [Number] sharedCatalogCategoryManagementV1GetCategoriesGet(id)

sharedCatalog/{id}/categories

Return the list of categories in the selected shared catalog.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogIdCategoriesApi();
let id = 56; // Number | 
apiInstance.sharedCatalogCategoryManagementV1GetCategoriesGet(id, (error, data, response) => {
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

### Return type

**[Number]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

