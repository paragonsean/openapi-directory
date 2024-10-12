# BeezUpMerchantApi.CustomerSharesApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteStoreShare**](CustomerSharesApi.md#deleteStoreShare) | **DELETE** /v2/user/customer/stores/{storeId}/shares/{userId} | Delete a share of a store to another user
[**getStoreShares**](CustomerSharesApi.md#getStoreShares) | **GET** /v2/user/customer/stores/{storeId}/shares | Get shares related to this store
[**shareStore**](CustomerSharesApi.md#shareStore) | **POST** /v2/user/customer/stores/{storeId}/shares | Share a store to another user



## deleteStoreShare

> deleteStoreShare(storeId, userId)

Delete a share of a store to another user

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerSharesApi();
let storeId = "storeId_example"; // String | Your store identifier
let userId = "userId_example"; // String | The friend user id
apiInstance.deleteStoreShare(storeId, userId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **userId** | **String**| The friend user id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStoreShares

> StoreShares getStoreShares(storeId, opts)

Get shares related to this store

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerSharesApi();
let storeId = "storeId_example"; // String | Your store identifier
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getStoreShares(storeId, opts, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] 

### Return type

[**StoreShares**](StoreShares.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shareStore

> shareStore(storeId, body)

Share a store to another user

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerSharesApi();
let storeId = "storeId_example"; // String | Your store identifier
let body = "body_example"; // String | Your friend's email
apiInstance.shareStore(storeId, body, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **body** | **String**| Your friend&#39;s email | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

