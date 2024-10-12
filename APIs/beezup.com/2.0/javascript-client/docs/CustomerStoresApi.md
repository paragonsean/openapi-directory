# BeezUpMerchantApi.CustomerStoresApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createStore**](CustomerStoresApi.md#createStore) | **POST** /v2/user/customer/stores | Create a new store
[**deleteStore**](CustomerStoresApi.md#deleteStore) | **DELETE** /v2/user/customer/stores/{storeId} | Delete a store
[**getStore**](CustomerStoresApi.md#getStore) | **GET** /v2/user/customer/stores/{storeId} | Get store&#39;s information
[**getStores**](CustomerStoresApi.md#getStores) | **GET** /v2/user/customer/stores | Get store list
[**updateStore**](CustomerStoresApi.md#updateStore) | **PATCH** /v2/user/customer/stores/{storeId} | Update some store&#39;s information.



## createStore

> LinksGetStoreLink createStore(createStoreRequest)

Create a new store

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerStoresApi();
let createStoreRequest = new BeezUpMerchantApi.CreateStoreRequest(); // CreateStoreRequest | 
apiInstance.createStore(createStoreRequest, (error, data, response) => {
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
 **createStoreRequest** | [**CreateStoreRequest**](CreateStoreRequest.md)|  | 

### Return type

[**LinksGetStoreLink**](LinksGetStoreLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteStore

> deleteStore(storeId)

Delete a store

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerStoresApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.deleteStore(storeId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStore

> Store getStore(storeId, opts)

Get store&#39;s information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerStoresApi();
let storeId = "storeId_example"; // String | Your store identifier
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getStore(storeId, opts, (error, data, response) => {
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

[**Store**](Store.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStores

> StoreList getStores(opts)

Get store list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerStoresApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
};
apiInstance.getStores(opts, (error, data, response) => {
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

[**StoreList**](StoreList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateStore

> updateStore(storeId, updateStoreRequest)

Update some store&#39;s information.

Update some store&#39;s information. FYI, you cannot change the country. 

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerStoresApi();
let storeId = "storeId_example"; // String | Your store identifier
let updateStoreRequest = new BeezUpMerchantApi.UpdateStoreRequest(); // UpdateStoreRequest | 
apiInstance.updateStore(storeId, updateStoreRequest, (error, data, response) => {
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
 **updateStoreRequest** | [**UpdateStoreRequest**](UpdateStoreRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

