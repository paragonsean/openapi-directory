# MagentoB2B.ProductsTierPricesInformationApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogTierPriceStorageV1GetPost**](ProductsTierPricesInformationApi.md#catalogTierPriceStorageV1GetPost) | **POST** /V1/products/tier-prices-information | products/tier-prices-information



## catalogTierPriceStorageV1GetPost

> [CatalogDataTierPriceInterface] catalogTierPriceStorageV1GetPost(opts)

products/tier-prices-information

Return product prices. In case of at least one of skus is not found exception will be thrown.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsTierPricesInformationApi();
let opts = {
  'catalogBasePriceStorageV1GetPostRequest': new MagentoB2B.CatalogBasePriceStorageV1GetPostRequest() // CatalogBasePriceStorageV1GetPostRequest | 
};
apiInstance.catalogTierPriceStorageV1GetPost(opts, (error, data, response) => {
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

[**[CatalogDataTierPriceInterface]**](CatalogDataTierPriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

