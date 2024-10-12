# BeezUpMerchantApi.ChannelCatalogsColumnMappingsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureChannelCatalogColumnMappings**](ChannelCatalogsColumnMappingsApi.md#configureChannelCatalogColumnMappings) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/columnMappings | Configure channel catalog column mappings



## configureChannelCatalogColumnMappings

> configureChannelCatalogColumnMappings(channelCatalogId, channelCatalogColumnMapping)

Configure channel catalog column mappings

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsColumnMappingsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let channelCatalogColumnMapping = [new BeezUpMerchantApi.ChannelCatalogColumnMapping()]; // [ChannelCatalogColumnMapping] | 
apiInstance.configureChannelCatalogColumnMappings(channelCatalogId, channelCatalogColumnMapping, (error, data, response) => {
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
 **channelCatalogColumnMapping** | [**[ChannelCatalogColumnMapping]**](ChannelCatalogColumnMapping.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

