# BeezUpMerchantApi.ChannelCatalogsCategoriesApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureChannelCatalogCategory**](ChannelCatalogsCategoriesApi.md#configureChannelCatalogCategory) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/categories/configure | Configure channel catalog category
[**disableChannelCatalogCategoryMapping**](ChannelCatalogsCategoriesApi.md#disableChannelCatalogCategoryMapping) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/categories/disableMapping | Disable a channel catalog category mapping
[**getChannelCatalogCategories**](ChannelCatalogsCategoriesApi.md#getChannelCatalogCategories) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/categories | Get channel catalog categories
[**reenableChannelCatalogCategoryMapping**](ChannelCatalogsCategoriesApi.md#reenableChannelCatalogCategoryMapping) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/categories/reenableMapping | Reenable a channel catalog category mapping



## configureChannelCatalogCategory

> configureChannelCatalogCategory(channelCatalogId, configureCategoryRequest)

Configure channel catalog category

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsCategoriesApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let configureCategoryRequest = new BeezUpMerchantApi.ConfigureCategoryRequest(); // ConfigureCategoryRequest | 
apiInstance.configureChannelCatalogCategory(channelCatalogId, configureCategoryRequest, (error, data, response) => {
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
 **configureCategoryRequest** | [**ConfigureCategoryRequest**](ConfigureCategoryRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disableChannelCatalogCategoryMapping

> disableChannelCatalogCategoryMapping(channelCatalogId)

Disable a channel catalog category mapping

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsCategoriesApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.disableChannelCatalogCategoryMapping(channelCatalogId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCatalogCategories

> ChannelCatalogCategoryConfigurationList getChannelCatalogCategories(channelCatalogId)

Get channel catalog categories

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsCategoriesApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.getChannelCatalogCategories(channelCatalogId, (error, data, response) => {
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
 **channelCatalogId** | **String**| The channel catalog identifier | 

### Return type

[**ChannelCatalogCategoryConfigurationList**](ChannelCatalogCategoryConfigurationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reenableChannelCatalogCategoryMapping

> reenableChannelCatalogCategoryMapping(channelCatalogId)

Reenable a channel catalog category mapping

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsCategoriesApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.reenableChannelCatalogCategoryMapping(channelCatalogId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

