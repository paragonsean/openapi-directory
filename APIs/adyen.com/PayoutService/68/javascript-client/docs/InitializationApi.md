# AdyenPayoutApi.InitializationApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payout/v68*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postStoreDetail**](InitializationApi.md#postStoreDetail) | **POST** /storeDetail | Store payout details
[**postStoreDetailAndSubmitThirdParty**](InitializationApi.md#postStoreDetailAndSubmitThirdParty) | **POST** /storeDetailAndSubmitThirdParty | Store details and submit a payout
[**postSubmitThirdParty**](InitializationApi.md#postSubmitThirdParty) | **POST** /submitThirdParty | Submit a payout



## postStoreDetail

> StoreDetailResponse postStoreDetail(opts)

Store payout details

Stores payment details under the &#x60;PAYOUT&#x60; recurring contract. These payment details can be used later to submit a payout via the &#x60;/submitThirdParty&#x60; call.

### Example

```javascript
import AdyenPayoutApi from 'adyen_payout_api';
let defaultClient = AdyenPayoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenPayoutApi.InitializationApi();
let opts = {
  'storeDetailRequest': new AdyenPayoutApi.StoreDetailRequest() // StoreDetailRequest | 
};
apiInstance.postStoreDetail(opts, (error, data, response) => {
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
 **storeDetailRequest** | [**StoreDetailRequest**](StoreDetailRequest.md)|  | [optional] 

### Return type

[**StoreDetailResponse**](StoreDetailResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postStoreDetailAndSubmitThirdParty

> StoreDetailAndSubmitResponse postStoreDetailAndSubmitThirdParty(opts)

Store details and submit a payout

Submits a payout and stores its details for subsequent payouts.  The submitted payout must be confirmed or declined either by a reviewer or via &#x60;/confirmThirdParty&#x60; or &#x60;/declineThirdParty&#x60; calls.

### Example

```javascript
import AdyenPayoutApi from 'adyen_payout_api';
let defaultClient = AdyenPayoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenPayoutApi.InitializationApi();
let opts = {
  'storeDetailAndSubmitRequest': new AdyenPayoutApi.StoreDetailAndSubmitRequest() // StoreDetailAndSubmitRequest | 
};
apiInstance.postStoreDetailAndSubmitThirdParty(opts, (error, data, response) => {
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
 **storeDetailAndSubmitRequest** | [**StoreDetailAndSubmitRequest**](StoreDetailAndSubmitRequest.md)|  | [optional] 

### Return type

[**StoreDetailAndSubmitResponse**](StoreDetailAndSubmitResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSubmitThirdParty

> SubmitResponse postSubmitThirdParty(opts)

Submit a payout

Submits a payout using the previously stored payment details. To store payment details, use the &#x60;/storeDetail&#x60; API call.  The submitted payout must be confirmed or declined either by a reviewer or via &#x60;/confirmThirdParty&#x60; or &#x60;/declineThirdParty&#x60; calls.

### Example

```javascript
import AdyenPayoutApi from 'adyen_payout_api';
let defaultClient = AdyenPayoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenPayoutApi.InitializationApi();
let opts = {
  'submitRequest': new AdyenPayoutApi.SubmitRequest() // SubmitRequest | 
};
apiInstance.postSubmitThirdParty(opts, (error, data, response) => {
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
 **submitRequest** | [**SubmitRequest**](SubmitRequest.md)|  | [optional] 

### Return type

[**SubmitResponse**](SubmitResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

