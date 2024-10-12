# BeezUpMerchantApi.ChannelCatalogsProductsOptimisationApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disableChannelCatalogProduct**](ChannelCatalogsProductsOptimisationApi.md#disableChannelCatalogProduct) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/disable | Disable channel catalog product
[**reenableChannelCatalogProduct**](ChannelCatalogsProductsOptimisationApi.md#reenableChannelCatalogProduct) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/reenable | Reenable channel catalog product



## disableChannelCatalogProduct

> disableChannelCatalogProduct(channelCatalogId, productId)

Disable channel catalog product

By default a all your catalog products are exposed to the channel. You can disable a product by using this operation. /!\\ In case of massive optimisation we recommand you to use the analytics api 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsOptimisationApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
apiInstance.disableChannelCatalogProduct(channelCatalogId, productId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelCatalogId** | **String**| The channel catalog identifier | 
 **productId** | **String**| The product identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reenableChannelCatalogProduct

> reenableChannelCatalogProduct(channelCatalogId, productId)

Reenable channel catalog product

By default a all your catalog products are exposed to the channel. You can reenable a product by using this operation. /!\\ In case of massive optimisation we recommand you to use the analytics api 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsOptimisationApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
apiInstance.reenableChannelCatalogProduct(channelCatalogId, productId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelCatalogId** | **String**| The channel catalog identifier | 
 **productId** | **String**| The product identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

