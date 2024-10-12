# AdyenBalanceControlApi.GeneralApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/BalanceControl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postBalanceTransfer**](GeneralApi.md#postBalanceTransfer) | **POST** /balanceTransfer | Start a balance transfer



## postBalanceTransfer

> BalanceTransferResponse postBalanceTransfer(opts)

Start a balance transfer

Starts a balance transfer request between merchant accounts. The following conditions must be met before you can successfully transfer balances:  * The source and destination merchant accounts must be under the same company account and legal entity.  * The source merchant account must have sufficient funds.  * The source and destination merchant accounts must have at least one common processing currency.  When sending multiple API requests with the same source and destination merchant accounts, send the requests sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel. 

### Example

```javascript
import AdyenBalanceControlApi from 'adyen_balance_control_api';
let defaultClient = AdyenBalanceControlApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenBalanceControlApi.GeneralApi();
let opts = {
  'balanceTransferRequest': new AdyenBalanceControlApi.BalanceTransferRequest() // BalanceTransferRequest | 
};
apiInstance.postBalanceTransfer(opts, (error, data, response) => {
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
 **balanceTransferRequest** | [**BalanceTransferRequest**](BalanceTransferRequest.md)|  | [optional] 

### Return type

[**BalanceTransferResponse**](BalanceTransferResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

