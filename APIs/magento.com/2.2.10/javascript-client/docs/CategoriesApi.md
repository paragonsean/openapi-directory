# MagentoB2B.CategoriesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCategoryManagementV1GetTreeGet**](CategoriesApi.md#catalogCategoryManagementV1GetTreeGet) | **GET** /V1/categories | categories
[**catalogCategoryRepositoryV1SavePost**](CategoriesApi.md#catalogCategoryRepositoryV1SavePost) | **POST** /V1/categories | categories



## catalogCategoryManagementV1GetTreeGet

> CatalogDataCategoryTreeInterface catalogCategoryManagementV1GetTreeGet(opts)

categories

Retrieve list of categories

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesApi();
let opts = {
  'rootCategoryId': 56, // Number | 
  'depth': 56 // Number | 
};
apiInstance.catalogCategoryManagementV1GetTreeGet(opts, (error, data, response) => {
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
 **rootCategoryId** | **Number**|  | [optional] 
 **depth** | **Number**|  | [optional] 

### Return type

[**CatalogDataCategoryTreeInterface**](CatalogDataCategoryTreeInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogCategoryRepositoryV1SavePost

> CatalogDataCategoryInterface catalogCategoryRepositoryV1SavePost(opts)

categories

Create category service

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesApi();
let opts = {
  'catalogCategoryRepositoryV1SavePostRequest': new MagentoB2B.CatalogCategoryRepositoryV1SavePostRequest() // CatalogCategoryRepositoryV1SavePostRequest | 
};
apiInstance.catalogCategoryRepositoryV1SavePost(opts, (error, data, response) => {
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
 **catalogCategoryRepositoryV1SavePostRequest** | [**CatalogCategoryRepositoryV1SavePostRequest**](CatalogCategoryRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CatalogDataCategoryInterface**](CatalogDataCategoryInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

