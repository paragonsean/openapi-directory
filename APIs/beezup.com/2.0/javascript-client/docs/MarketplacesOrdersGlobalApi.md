# BeezUpMerchantApi.MarketplacesOrdersGlobalApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMarketplaceAccountsSynchronization**](MarketplacesOrdersGlobalApi.md#getMarketplaceAccountsSynchronization) | **GET** /v2/user/marketplaces/orders/status | [DEPRECATED] Get current synchronization status between your marketplaces and BeezUP accounts
[**getOrderIndex**](MarketplacesOrdersGlobalApi.md#getOrderIndex) | **GET** /v2/user/marketplaces/orders/ | [DEPRECATED] Get all actions you can do on the order API
[**harvestAll**](MarketplacesOrdersGlobalApi.md#harvestAll) | **POST** /v2/user/marketplaces/orders/harvest | [DEPRECATED] Send harvest request to all your marketplaces



## getMarketplaceAccountsSynchronization

> AccountSynchronizationList getMarketplaceAccountsSynchronization(opts)

[DEPRECATED] Get current synchronization status between your marketplaces and BeezUP accounts

Use /orders/v3

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersGlobalApi();
let opts = {
  'storeId': "04730364-9826-4ff3-92e4-51fccd02bf10", // String | The StoreId to filter by
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getMarketplaceAccountsSynchronization(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**AccountSynchronizationList**](AccountSynchronizationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrderIndex

> OrderIndex getOrderIndex(opts)

[DEPRECATED] Get all actions you can do on the order API

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersGlobalApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getOrderIndex(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**OrderIndex**](OrderIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## harvestAll

> harvestAll(opts)

[DEPRECATED] Send harvest request to all your marketplaces

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersGlobalApi();
let opts = {
  'storeId': "04730364-9826-4ff3-92e4-51fccd02bf10" // String | The StoreId to filter by
};
apiInstance.harvestAll(opts, (error, data, response) => {
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
 **storeId** | **String**| The StoreId to filter by | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

