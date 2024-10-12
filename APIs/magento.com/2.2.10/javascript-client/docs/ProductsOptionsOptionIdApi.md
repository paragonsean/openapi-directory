# MagentoB2B.ProductsOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductCustomOptionRepositoryV1SavePut**](ProductsOptionsOptionIdApi.md#catalogProductCustomOptionRepositoryV1SavePut) | **PUT** /V1/products/options/{optionId} | products/options/{optionId}



## catalogProductCustomOptionRepositoryV1SavePut

> CatalogDataProductCustomOptionInterface catalogProductCustomOptionRepositoryV1SavePut(optionId, opts)

products/options/{optionId}

Save Custom Option

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsOptionsOptionIdApi();
let optionId = "optionId_example"; // String | 
let opts = {
  'catalogProductCustomOptionRepositoryV1SavePostRequest': new MagentoB2B.CatalogProductCustomOptionRepositoryV1SavePostRequest() // CatalogProductCustomOptionRepositoryV1SavePostRequest | 
};
apiInstance.catalogProductCustomOptionRepositoryV1SavePut(optionId, opts, (error, data, response) => {
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
 **optionId** | **String**|  | 
 **catalogProductCustomOptionRepositoryV1SavePostRequest** | [**CatalogProductCustomOptionRepositoryV1SavePostRequest**](CatalogProductCustomOptionRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CatalogDataProductCustomOptionInterface**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

