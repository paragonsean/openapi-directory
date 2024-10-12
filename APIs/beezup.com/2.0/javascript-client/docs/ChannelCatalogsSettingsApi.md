# BeezUpMerchantApi.ChannelCatalogsSettingsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureChannelCatalogCostSettings**](ChannelCatalogsSettingsApi.md#configureChannelCatalogCostSettings) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/settings/cost | Configure channel catalog cost settings
[**configureChannelCatalogGeneralSettings**](ChannelCatalogsSettingsApi.md#configureChannelCatalogGeneralSettings) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/settings/general | Configure channel catalog general settings
[**disableChannelCatalog**](ChannelCatalogsSettingsApi.md#disableChannelCatalog) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/disable | Disable a channel catalog
[**enableChannelCatalog**](ChannelCatalogsSettingsApi.md#enableChannelCatalog) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/enable | Enable a channel catalog



## configureChannelCatalogCostSettings

> configureChannelCatalogCostSettings(channelCatalogId, costSettings)

Configure channel catalog cost settings

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsSettingsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let costSettings = new BeezUpMerchantApi.CostSettings(); // CostSettings | 
apiInstance.configureChannelCatalogCostSettings(channelCatalogId, costSettings, (error, data, response) => {
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
 **costSettings** | [**CostSettings**](CostSettings.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configureChannelCatalogGeneralSettings

> configureChannelCatalogGeneralSettings(channelCatalogId, generalSettings)

Configure channel catalog general settings

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsSettingsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let generalSettings = new BeezUpMerchantApi.GeneralSettings(); // GeneralSettings | 
apiInstance.configureChannelCatalogGeneralSettings(channelCatalogId, generalSettings, (error, data, response) => {
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
 **generalSettings** | [**GeneralSettings**](GeneralSettings.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disableChannelCatalog

> disableChannelCatalog(channelCatalogId)

Disable a channel catalog

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsSettingsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.disableChannelCatalog(channelCatalogId, (error, data, response) => {
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


## enableChannelCatalog

> enableChannelCatalog(channelCatalogId)

Enable a channel catalog

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsSettingsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.enableChannelCatalog(channelCatalogId, (error, data, response) => {
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

