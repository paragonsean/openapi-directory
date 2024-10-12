# LegacySearchApi.OffersApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogSystemPubProductsOffersProductIdGet**](OffersApi.md#apiCatalogSystemPubProductsOffersProductIdGet) | **GET** /api/catalog_system/pub/products/offers/{productId} | Search Product offers
[**apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet**](OffersApi.md#apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet) | **GET** /api/catalog_system/pub/products/offers/{productId}/sku/{skuId} | Search SKU offers



## apiCatalogSystemPubProductsOffersProductIdGet

> [ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner] apiCatalogSystemPubProductsOffersProductIdGet(accept, contentType, productId)

Search Product offers

Retrieves existing offers of a specific product.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LegacySearchApi.OffersApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = "3"; // String | Product unique number identifier.
apiInstance.apiCatalogSystemPubProductsOffersProductIdGet(accept, contentType, productId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **String**| Product unique number identifier. | 

### Return type

[**[ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner]**](ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet

> [ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner] apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet(accept, contentType, productId, skuId)

Search SKU offers

Retrieves existing offers of a specific SKU.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LegacySearchApi.OffersApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = "3"; // String | Product unique number identifier.
let skuId = "5"; // String | Product unique number identifier.
apiInstance.apiCatalogSystemPubProductsOffersProductIdSkuSkuIdGet(accept, contentType, productId, skuId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **String**| Product unique number identifier. | 
 **skuId** | **String**| Product unique number identifier. | 

### Return type

[**[ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner]**](ApiCatalogSystemPubProductsOffersProductIdGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

