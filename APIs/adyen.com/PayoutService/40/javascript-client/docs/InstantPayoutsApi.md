# AdyenPayoutApi.InstantPayoutsApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/Payout/v40*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postPayout**](InstantPayoutsApi.md#postPayout) | **POST** /payout | Make an instant card payout



## postPayout

> PayoutResponse postPayout(opts)

Make an instant card payout

With this call, you can pay out to your customers, and funds will be made available within 30 minutes on the cardholder&#39;s bank account (this is dependent on whether the issuer supports this functionality). Instant card payouts are only supported for Visa and Mastercard cards.

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

let apiInstance = new AdyenPayoutApi.InstantPayoutsApi();
let opts = {
  'payoutRequest': new AdyenPayoutApi.PayoutRequest() // PayoutRequest | 
};
apiInstance.postPayout(opts, (error, data, response) => {
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
 **payoutRequest** | [**PayoutRequest**](PayoutRequest.md)|  | [optional] 

### Return type

[**PayoutResponse**](PayoutResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

