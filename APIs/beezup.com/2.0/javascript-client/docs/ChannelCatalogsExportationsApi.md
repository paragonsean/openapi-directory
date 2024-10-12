# BeezUpMerchantApi.ChannelCatalogsExportationsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clearChannelCatalogExportationCache**](ChannelCatalogsExportationsApi.md#clearChannelCatalogExportationCache) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/exportations/cache/clear | Clear the exportation cache
[**getChannelCatalogExportationCacheInfo**](ChannelCatalogsExportationsApi.md#getChannelCatalogExportationCacheInfo) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/exportations/cache | Get the exportation cache information
[**getChannelCatalogExportationHistory**](ChannelCatalogsExportationsApi.md#getChannelCatalogExportationHistory) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/exportations/history | Get the exportation history



## clearChannelCatalogExportationCache

> clearChannelCatalogExportationCache(channelCatalogId)

Clear the exportation cache

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsExportationsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.clearChannelCatalogExportationCache(channelCatalogId, (error, data, response) => {
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


## getChannelCatalogExportationCacheInfo

> ChannelCatalogExportCacheInfoResponse getChannelCatalogExportationCacheInfo(channelCatalogId)

Get the exportation cache information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsExportationsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.getChannelCatalogExportationCacheInfo(channelCatalogId, (error, data, response) => {
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

[**ChannelCatalogExportCacheInfoResponse**](ChannelCatalogExportCacheInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCatalogExportationHistory

> ChannelCatalogExportationHistory getChannelCatalogExportationHistory(channelCatalogId, pageNumber, pageSize)

Get the exportation history

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsExportationsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let pageNumber = 1; // Number | The page number you want to get
let pageSize = 25; // Number | The entry count you want to get
apiInstance.getChannelCatalogExportationHistory(channelCatalogId, pageNumber, pageSize, (error, data, response) => {
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
 **pageNumber** | **Number**| The page number you want to get | 
 **pageSize** | **Number**| The entry count you want to get | 

### Return type

[**ChannelCatalogExportationHistory**](ChannelCatalogExportationHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

