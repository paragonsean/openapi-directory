# MagentoB2B.CategoriesCategoryIdProductsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCategoryLinkManagementV1GetAssignedProductsGet**](CategoriesCategoryIdProductsApi.md#catalogCategoryLinkManagementV1GetAssignedProductsGet) | **GET** /V1/categories/{categoryId}/products | categories/{categoryId}/products
[**catalogCategoryLinkRepositoryV1SavePost**](CategoriesCategoryIdProductsApi.md#catalogCategoryLinkRepositoryV1SavePost) | **POST** /V1/categories/{categoryId}/products | categories/{categoryId}/products
[**catalogCategoryLinkRepositoryV1SavePut**](CategoriesCategoryIdProductsApi.md#catalogCategoryLinkRepositoryV1SavePut) | **PUT** /V1/categories/{categoryId}/products | categories/{categoryId}/products



## catalogCategoryLinkManagementV1GetAssignedProductsGet

> [CatalogDataCategoryProductLinkInterface] catalogCategoryLinkManagementV1GetAssignedProductsGet(categoryId)

categories/{categoryId}/products

Get products assigned to category

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesCategoryIdProductsApi();
let categoryId = 56; // Number | 
apiInstance.catalogCategoryLinkManagementV1GetAssignedProductsGet(categoryId, (error, data, response) => {
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

[**[CatalogDataCategoryProductLinkInterface]**](CatalogDataCategoryProductLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## catalogCategoryLinkRepositoryV1SavePost

> Boolean catalogCategoryLinkRepositoryV1SavePost(categoryId, opts)

categories/{categoryId}/products

Assign a product to the required category

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesCategoryIdProductsApi();
let categoryId = "categoryId_example"; // String | 
let opts = {
  'catalogCategoryLinkRepositoryV1SavePutRequest': new MagentoB2B.CatalogCategoryLinkRepositoryV1SavePutRequest() // CatalogCategoryLinkRepositoryV1SavePutRequest | 
};
apiInstance.catalogCategoryLinkRepositoryV1SavePost(categoryId, opts, (error, data, response) => {
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
 **categoryId** | **String**|  | 
 **catalogCategoryLinkRepositoryV1SavePutRequest** | [**CatalogCategoryLinkRepositoryV1SavePutRequest**](CatalogCategoryLinkRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## catalogCategoryLinkRepositoryV1SavePut

> Boolean catalogCategoryLinkRepositoryV1SavePut(categoryId, opts)

categories/{categoryId}/products

Assign a product to the required category

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesCategoryIdProductsApi();
let categoryId = "categoryId_example"; // String | 
let opts = {
  'catalogCategoryLinkRepositoryV1SavePutRequest': new MagentoB2B.CatalogCategoryLinkRepositoryV1SavePutRequest() // CatalogCategoryLinkRepositoryV1SavePutRequest | 
};
apiInstance.catalogCategoryLinkRepositoryV1SavePut(categoryId, opts, (error, data, response) => {
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
 **categoryId** | **String**|  | 
 **catalogCategoryLinkRepositoryV1SavePutRequest** | [**CatalogCategoryLinkRepositoryV1SavePutRequest**](CatalogCategoryLinkRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

