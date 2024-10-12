# MagentoB2B.ProductsSpecialPriceInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogSpecialPriceStorageV1GetPost**](ProductsSpecialPriceInformationApi.md#catalogSpecialPriceStorageV1GetPost) | **POST** /V1/products/special-price-information | products/special-price-information



## catalogSpecialPriceStorageV1GetPost

> [CatalogDataSpecialPriceInterface] catalogSpecialPriceStorageV1GetPost(opts)

products/special-price-information

Return product&#39;s special price. In case of at least one of skus is not found exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSpecialPriceInformationApi();
let opts = {
  'catalogBasePriceStorageV1GetPostRequest': new MagentoB2B.CatalogBasePriceStorageV1GetPostRequest() // CatalogBasePriceStorageV1GetPostRequest | 
};
apiInstance.catalogSpecialPriceStorageV1GetPost(opts, (error, data, response) => {
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
 **catalogBasePriceStorageV1GetPostRequest** | [**CatalogBasePriceStorageV1GetPostRequest**](CatalogBasePriceStorageV1GetPostRequest.md)|  | [optional] 

### Return type

[**[CatalogDataSpecialPriceInterface]**](CatalogDataSpecialPriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

