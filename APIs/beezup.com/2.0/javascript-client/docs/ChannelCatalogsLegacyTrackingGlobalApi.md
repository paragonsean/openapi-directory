# BeezUpMerchantApi.ChannelCatalogsLegacyTrackingGlobalApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLegacyTrackingChannelCatalog**](ChannelCatalogsLegacyTrackingGlobalApi.md#getLegacyTrackingChannelCatalog) | **GET** /v2/user/legacyTracking/channelCatalogs/{channelCatalogId} | Get the channel catalog configured to use legacy tracking format information
[**getLegacyTrackingChannelCatalogs**](ChannelCatalogsLegacyTrackingGlobalApi.md#getLegacyTrackingChannelCatalogs) | **GET** /v2/user/legacyTracking/channelCatalogs/ | List all your current channel catalogs configured to use legacy tracking format
[**migrateLegacyTrackingChannelCatalog**](ChannelCatalogsLegacyTrackingGlobalApi.md#migrateLegacyTrackingChannelCatalog) | **POST** /v2/user/legacyTracking/channelCatalogs/{channelCatalogId}/migrate | Migrate a channel catalog to current tracking format



## getLegacyTrackingChannelCatalog

> LegacyTrackingChannelCatalog getLegacyTrackingChannelCatalog(channelCatalogId)

Get the channel catalog configured to use legacy tracking format information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsLegacyTrackingGlobalApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.getLegacyTrackingChannelCatalog(channelCatalogId, (error, data, response) => {
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

[**LegacyTrackingChannelCatalog**](LegacyTrackingChannelCatalog.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLegacyTrackingChannelCatalogs

> LegacyTrackingChannelCatalogList getLegacyTrackingChannelCatalogs(opts)

List all your current channel catalogs configured to use legacy tracking format

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsLegacyTrackingGlobalApi();
let opts = {
  'storeId': "04730364-9826-4ff3-92e4-51fccd02bf10" // String | The store identifier
};
apiInstance.getLegacyTrackingChannelCatalogs(opts, (error, data, response) => {
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
 **storeId** | **String**| The store identifier | [optional] 

### Return type

[**LegacyTrackingChannelCatalogList**](LegacyTrackingChannelCatalogList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrateLegacyTrackingChannelCatalog

> migrateLegacyTrackingChannelCatalog(channelCatalogId)

Migrate a channel catalog to current tracking format

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsLegacyTrackingGlobalApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.migrateLegacyTrackingChannelCatalog(channelCatalogId, (error, data, response) => {
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

