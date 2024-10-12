# MagentoB2B.ProductsOptionsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductCustomOptionRepositoryV1SavePost**](ProductsOptionsApi.md#catalogProductCustomOptionRepositoryV1SavePost) | **POST** /V1/products/options | products/options



## catalogProductCustomOptionRepositoryV1SavePost

> CatalogDataProductCustomOptionInterface catalogProductCustomOptionRepositoryV1SavePost(opts)

products/options

Save Custom Option

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsOptionsApi();
let opts = {
  'catalogProductCustomOptionRepositoryV1SavePostRequest': new MagentoB2B.CatalogProductCustomOptionRepositoryV1SavePostRequest() // CatalogProductCustomOptionRepositoryV1SavePostRequest | 
};
apiInstance.catalogProductCustomOptionRepositoryV1SavePost(opts, (error, data, response) => {
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
 **catalogProductCustomOptionRepositoryV1SavePostRequest** | [**CatalogProductCustomOptionRepositoryV1SavePostRequest**](CatalogProductCustomOptionRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CatalogDataProductCustomOptionInterface**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

