# AdyenPayoutApi.ReviewingApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payout/v30*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postConfirmThirdParty**](ReviewingApi.md#postConfirmThirdParty) | **POST** /confirmThirdParty | Confirm a payout
[**postDeclineThirdParty**](ReviewingApi.md#postDeclineThirdParty) | **POST** /declineThirdParty | Cancel a payout



## postConfirmThirdParty

> ModifyResponse postConfirmThirdParty(opts)

Confirm a payout

Confirms a previously submitted payout.  To cancel a payout, use the &#x60;/declineThirdParty&#x60; endpoint.

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

let apiInstance = new AdyenPayoutApi.ReviewingApi();
let opts = {
  'modifyRequest': new AdyenPayoutApi.ModifyRequest() // ModifyRequest | 
};
apiInstance.postConfirmThirdParty(opts, (error, data, response) => {
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
 **modifyRequest** | [**ModifyRequest**](ModifyRequest.md)|  | [optional] 

### Return type

[**ModifyResponse**](ModifyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDeclineThirdParty

> ModifyResponse postDeclineThirdParty(opts)

Cancel a payout

Cancels a previously submitted payout.  To confirm and send a payout, use the &#x60;/confirmThirdParty&#x60; endpoint.

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

let apiInstance = new AdyenPayoutApi.ReviewingApi();
let opts = {
  'modifyRequest': new AdyenPayoutApi.ModifyRequest() // ModifyRequest | 
};
apiInstance.postDeclineThirdParty(opts, (error, data, response) => {
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
 **modifyRequest** | [**ModifyRequest**](ModifyRequest.md)|  | [optional] 

### Return type

[**ModifyResponse**](ModifyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

