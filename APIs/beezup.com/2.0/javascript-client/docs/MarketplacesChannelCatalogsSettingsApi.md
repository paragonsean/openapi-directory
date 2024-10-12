# BeezUpMerchantApi.MarketplacesChannelCatalogsSettingsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChannelCatalogMarketplaceProperties**](MarketplacesChannelCatalogsSettingsApi.md#getChannelCatalogMarketplaceProperties) | **GET** /v2/user/marketplaces/channelcatalogs/{channelCatalogId}/properties | Get the marketplace properties for a channel catalog
[**getChannelCatalogMarketplaceSettings**](MarketplacesChannelCatalogsSettingsApi.md#getChannelCatalogMarketplaceSettings) | **GET** /v2/user/marketplaces/channelcatalogs/{channelCatalogId}/settings | Get the marketplace settings for a channel catalog
[**setChannelCatalogMarketplaceSettings**](MarketplacesChannelCatalogsSettingsApi.md#setChannelCatalogMarketplaceSettings) | **POST** /v2/user/marketplaces/channelcatalogs/{channelCatalogId}/settings | Save new marketplace settings for a channel catalog



## getChannelCatalogMarketplaceProperties

> ChannelCatalogMarketplaceProperties getChannelCatalogMarketplaceProperties(channelCatalogId, redirectionPageUrl, opts)

Get the marketplace properties for a channel catalog

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesChannelCatalogsSettingsApi();
let channelCatalogId = "channelCatalogId_example"; // String | 
let redirectionPageUrl = "redirectionPageUrl_example"; // String | 
let opts = {
  'acceptLanguage': ["null"] // [String] | Indicates that the client accepts the following languages.
};
apiInstance.getChannelCatalogMarketplaceProperties(channelCatalogId, redirectionPageUrl, opts, (error, data, response) => {
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
 **channelCatalogId** | **String**|  | 
 **redirectionPageUrl** | **String**|  | 
 **acceptLanguage** | [**[String]**](String.md)| Indicates that the client accepts the following languages. | [optional] 

### Return type

[**ChannelCatalogMarketplaceProperties**](ChannelCatalogMarketplaceProperties.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCatalogMarketplaceSettings

> ChannelCatalogMarketplaceSettings getChannelCatalogMarketplaceSettings(channelCatalogId)

Get the marketplace settings for a channel catalog

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesChannelCatalogsSettingsApi();
let channelCatalogId = "channelCatalogId_example"; // String | Channel Catalog Id to query (required)
apiInstance.getChannelCatalogMarketplaceSettings(channelCatalogId, (error, data, response) => {
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
 **channelCatalogId** | **String**| Channel Catalog Id to query (required) | 

### Return type

[**ChannelCatalogMarketplaceSettings**](ChannelCatalogMarketplaceSettings.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setChannelCatalogMarketplaceSettings

> setChannelCatalogMarketplaceSettings(channelCatalogId, setChannelCatalogMarketplaceSettingsRequest)

Save new marketplace settings for a channel catalog

Allow you to configure your marketplace settings. Partial update accepted. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesChannelCatalogsSettingsApi();
let channelCatalogId = "channelCatalogId_example"; // String | Channel Catalog Id to query
let setChannelCatalogMarketplaceSettingsRequest = new BeezUpMerchantApi.SetChannelCatalogMarketplaceSettingsRequest(); // SetChannelCatalogMarketplaceSettingsRequest | Settings to save
apiInstance.setChannelCatalogMarketplaceSettings(channelCatalogId, setChannelCatalogMarketplaceSettingsRequest, (error, data, response) => {
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
 **channelCatalogId** | **String**| Channel Catalog Id to query | 
 **setChannelCatalogMarketplaceSettingsRequest** | [**SetChannelCatalogMarketplaceSettingsRequest**](SetChannelCatalogMarketplaceSettingsRequest.md)| Settings to save | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

