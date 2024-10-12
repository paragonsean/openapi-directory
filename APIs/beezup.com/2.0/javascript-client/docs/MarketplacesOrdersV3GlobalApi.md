# BeezUpMerchantApi.MarketplacesOrdersV3GlobalApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMarketplaceAccountsSynchronizationV3**](MarketplacesOrdersV3GlobalApi.md#getMarketplaceAccountsSynchronizationV3) | **GET** /orders/v3/status | 
[**getOrderManagementReadyMarketplaceBusinessCode**](MarketplacesOrdersV3GlobalApi.md#getOrderManagementReadyMarketplaceBusinessCode) | **GET** /orders/v3/lov/orderManagementReadyMarketplaceBusinessCode | 
[**harvestAllV3**](MarketplacesOrdersV3GlobalApi.md#harvestAllV3) | **POST** /orders/v3/harvest | Send harvest request to all your marketplaces



## getMarketplaceAccountsSynchronizationV3

> AccountSynchronizationList getMarketplaceAccountsSynchronizationV3(opts)



Get current synchronization status between your marketplaces and BeezUP accounts

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3GlobalApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example", // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
  'storeIds': ["null"] // [String] | StoredIds to filter
};
apiInstance.getMarketplaceAccountsSynchronizationV3(opts, (error, data, response) => {
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
 **storeIds** | [**[String]**](String.md)| StoredIds to filter | [optional] 

### Return type

[**AccountSynchronizationList**](AccountSynchronizationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrderManagementReadyMarketplaceBusinessCode

> [ListOfValueItem] getOrderManagementReadyMarketplaceBusinessCode(opts)



Get the list of MarketplaceBusinessCode ready for Order Management

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3GlobalApi();
let opts = {
  'acceptLanguage': ["null"], // [String] | Indicates that the client accepts the following languages.
  'storeIds': ["null"] // [String] | StoredIds to filter
};
apiInstance.getOrderManagementReadyMarketplaceBusinessCode(opts, (error, data, response) => {
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
 **acceptLanguage** | [**[String]**](String.md)| Indicates that the client accepts the following languages. | [optional] 
 **storeIds** | [**[String]**](String.md)| StoredIds to filter | [optional] 

### Return type

[**[ListOfValueItem]**](ListOfValueItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## harvestAllV3

> harvestAllV3(opts)

Send harvest request to all your marketplaces

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.MarketplacesOrdersV3GlobalApi();
let opts = {
  'storeId': "04730364-9826-4ff3-92e4-51fccd02bf10" // String | The StoreId to filter by
};
apiInstance.harvestAllV3(opts, (error, data, response) => {
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

