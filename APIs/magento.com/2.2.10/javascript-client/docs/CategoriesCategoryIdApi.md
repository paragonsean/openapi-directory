# MagentoB2B.CategoriesCategoryIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCategoryRepositoryV1DeleteByIdentifierDelete**](CategoriesCategoryIdApi.md#catalogCategoryRepositoryV1DeleteByIdentifierDelete) | **DELETE** /V1/categories/{categoryId} | categories/{categoryId}
[**catalogCategoryRepositoryV1GetGet**](CategoriesCategoryIdApi.md#catalogCategoryRepositoryV1GetGet) | **GET** /V1/categories/{categoryId} | categories/{categoryId}



## catalogCategoryRepositoryV1DeleteByIdentifierDelete

> Boolean catalogCategoryRepositoryV1DeleteByIdentifierDelete(categoryId)

categories/{categoryId}

Delete category by identifier

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesCategoryIdApi();
let categoryId = 56; // Number | 
apiInstance.catalogCategoryRepositoryV1DeleteByIdentifierDelete(categoryId, (error, data, response) => {
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

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogCategoryRepositoryV1GetGet

> CatalogDataCategoryInterface catalogCategoryRepositoryV1GetGet(categoryId, opts)

categories/{categoryId}

Get info about category by category id

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesCategoryIdApi();
let categoryId = 56; // Number | 
let opts = {
  'storeId': 56 // Number | 
};
apiInstance.catalogCategoryRepositoryV1GetGet(categoryId, opts, (error, data, response) => {
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
 **storeId** | **Number**|  | [optional] 

### Return type

[**CatalogDataCategoryInterface**](CatalogDataCategoryInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

