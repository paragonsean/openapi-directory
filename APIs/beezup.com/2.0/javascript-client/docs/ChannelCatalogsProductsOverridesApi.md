# BeezUpMerchantApi.ChannelCatalogsProductsOverridesApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureChannelCatalogProductValueOverrideCopy**](ChannelCatalogsProductsOverridesApi.md#configureChannelCatalogProductValueOverrideCopy) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/overrides/copy | Copy channel catalog product value override
[**deleteChannelCatalogProductValueOverride**](ChannelCatalogsProductsOverridesApi.md#deleteChannelCatalogProductValueOverride) | **DELETE** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/overrides/{channelColumnId} | Delete a specific channel catalog product value override
[**getChannelCatalogProductValueOverrideCopy**](ChannelCatalogsProductsOverridesApi.md#getChannelCatalogProductValueOverrideCopy) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/overrides/copy | Get channel catalog product value override compatibilities status
[**overrideChannelCatalogProductValues**](ChannelCatalogsProductsOverridesApi.md#overrideChannelCatalogProductValues) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/overrides | Override channel catalog product values



## configureChannelCatalogProductValueOverrideCopy

> configureChannelCatalogProductValueOverrideCopy(channelCatalogId, productId)

Copy channel catalog product value override

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsOverridesApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
apiInstance.configureChannelCatalogProductValueOverrideCopy(channelCatalogId, productId, (error, data, response) => {
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


## deleteChannelCatalogProductValueOverride

> deleteChannelCatalogProductValueOverride(channelCatalogId, productId, channelColumnId)

Delete a specific channel catalog product value override

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsOverridesApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
let channelColumnId = "8a76f06a-fefc-4c0d-bcfe-b210f1482977"; // String | The channel column identifier
apiInstance.deleteChannelCatalogProductValueOverride(channelCatalogId, productId, channelColumnId, (error, data, response) => {
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
 **channelColumnId** | **String**| The channel column identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCatalogProductValueOverrideCopy

> getChannelCatalogProductValueOverrideCopy(channelCatalogId, productId)

Get channel catalog product value override compatibilities status

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsOverridesApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
apiInstance.getChannelCatalogProductValueOverrideCopy(channelCatalogId, productId, (error, data, response) => {
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


## overrideChannelCatalogProductValues

> overrideChannelCatalogProductValues(channelCatalogId, productId, requestBody)

Override channel catalog product values

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsOverridesApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
let requestBody = {key: "null"}; // {String: String} | 
apiInstance.overrideChannelCatalogProductValues(channelCatalogId, productId, requestBody, (error, data, response) => {
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
 **requestBody** | [**{String: String}**](String.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

