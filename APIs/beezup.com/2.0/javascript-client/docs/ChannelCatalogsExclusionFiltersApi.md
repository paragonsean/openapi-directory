# BeezUpMerchantApi.ChannelCatalogsExclusionFiltersApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureChannelCatalogExclusionFilters**](ChannelCatalogsExclusionFiltersApi.md#configureChannelCatalogExclusionFilters) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/exclusionFilters | Configure channel catalog exclusion filters
[**getChannelCatalogExclusionFilters**](ChannelCatalogsExclusionFiltersApi.md#getChannelCatalogExclusionFilters) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/exclusionFilters | Get channel catalog exclusion filters



## configureChannelCatalogExclusionFilters

> configureChannelCatalogExclusionFilters(channelCatalogId, exclusionFilter)

Configure channel catalog exclusion filters

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsExclusionFiltersApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let exclusionFilter = [new BeezUpMerchantApi.ExclusionFilter()]; // [ExclusionFilter] | 
apiInstance.configureChannelCatalogExclusionFilters(channelCatalogId, exclusionFilter, (error, data, response) => {
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
 **exclusionFilter** | [**[ExclusionFilter]**](ExclusionFilter.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getChannelCatalogExclusionFilters

> ExclusionFiltersResponse getChannelCatalogExclusionFilters(channelCatalogId)

Get channel catalog exclusion filters

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsExclusionFiltersApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.getChannelCatalogExclusionFilters(channelCatalogId, (error, data, response) => {
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

[**ExclusionFiltersResponse**](ExclusionFiltersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

