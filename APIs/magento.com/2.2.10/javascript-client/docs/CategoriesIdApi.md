# MagentoB2B.CategoriesIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogCategoryRepositoryV1SavePut**](CategoriesIdApi.md#catalogCategoryRepositoryV1SavePut) | **PUT** /V1/categories/{id} | categories/{id}



## catalogCategoryRepositoryV1SavePut

> CatalogDataCategoryInterface catalogCategoryRepositoryV1SavePut(id, opts)

categories/{id}

Create category service

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CategoriesIdApi();
let id = "id_example"; // String | 
let opts = {
  'catalogCategoryRepositoryV1SavePostRequest': new MagentoB2B.CatalogCategoryRepositoryV1SavePostRequest() // CatalogCategoryRepositoryV1SavePostRequest | 
};
apiInstance.catalogCategoryRepositoryV1SavePut(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **catalogCategoryRepositoryV1SavePostRequest** | [**CatalogCategoryRepositoryV1SavePostRequest**](CatalogCategoryRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CatalogDataCategoryInterface**](CatalogDataCategoryInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

