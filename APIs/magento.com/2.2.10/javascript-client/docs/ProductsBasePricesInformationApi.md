# MagentoB2B.ProductsBasePricesInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogBasePriceStorageV1GetPost**](ProductsBasePricesInformationApi.md#catalogBasePriceStorageV1GetPost) | **POST** /V1/products/base-prices-information | products/base-prices-information



## catalogBasePriceStorageV1GetPost

> [CatalogDataBasePriceInterface] catalogBasePriceStorageV1GetPost(opts)

products/base-prices-information

Return product prices. In case of at least one of skus is not found exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsBasePricesInformationApi();
let opts = {
  'catalogBasePriceStorageV1GetPostRequest': new MagentoB2B.CatalogBasePriceStorageV1GetPostRequest() // CatalogBasePriceStorageV1GetPostRequest | 
};
apiInstance.catalogBasePriceStorageV1GetPost(opts, (error, data, response) => {
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

[**[CatalogDataBasePriceInterface]**](CatalogDataBasePriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

