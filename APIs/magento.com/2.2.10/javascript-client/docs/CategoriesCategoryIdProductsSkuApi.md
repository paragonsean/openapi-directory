# MagentoB2B.CategoriesCategoryIdProductsSkuApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCategoryLinkRepositoryV1DeleteByIdsDelete**](CategoriesCategoryIdProductsSkuApi.md#catalogCategoryLinkRepositoryV1DeleteByIdsDelete) | **DELETE** /V1/categories/{categoryId}/products/{sku} | categories/{categoryId}/products/{sku}



## catalogCategoryLinkRepositoryV1DeleteByIdsDelete

> Boolean catalogCategoryLinkRepositoryV1DeleteByIdsDelete(categoryId, sku)

categories/{categoryId}/products/{sku}

Remove the product assignment from the category by category id and sku

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesCategoryIdProductsSkuApi();
let categoryId = "categoryId_example"; // String | 
let sku = "sku_example"; // String | 
apiInstance.catalogCategoryLinkRepositoryV1DeleteByIdsDelete(categoryId, sku, (error, data, response) => {
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
 **sku** | **String**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

