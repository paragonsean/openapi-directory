# BeezUpMerchantApi.MarketplacesChannelCatalogsGlobalApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMarketplaceChannelCatalogs**](MarketplacesChannelCatalogsGlobalApi.md#getMarketplaceChannelCatalogs) | **GET** /v2/user/marketplaces/channelcatalogs/ | Get your marketplace channel catalog list



## getMarketplaceChannelCatalogs

> MarketplaceChannelCatalogList getMarketplaceChannelCatalogs(opts)

Get your marketplace channel catalog list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesChannelCatalogsGlobalApi();
let opts = {
  'storeId': "04730364-9826-4ff3-92e4-51fccd02bf10" // String | The StoreId to filter by
};
apiInstance.getMarketplaceChannelCatalogs(opts, (error, data, response) => {
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
 **storeId** | **String**| The StoreId to filter by | [optional] 

### Return type

[**MarketplaceChannelCatalogList**](MarketplaceChannelCatalogList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

