# AdyenCheckoutApi.UtilityApi

All URIs are relative to *https://checkout-test.adyen.com/v69*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postApplePaySessions**](UtilityApi.md#postApplePaySessions) | **POST** /applePay/sessions | Get an Apple Pay session
[**postOriginKeys**](UtilityApi.md#postOriginKeys) | **POST** /originKeys | Create originKey values for domains



## postApplePaySessions

> ApplePaySessionResponse postApplePaySessions(opts)

Get an Apple Pay session

You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen&#39;s Apple Pay certificate.  The endpoint returns the Apple Pay session data which you need to complete the [Apple Pay session validation](https://docs.adyen.com/payment-methods/apple-pay/api-only?tab&#x3D;adyen-certificate-validation_1#complete-apple-pay-session-validation).

### Example

```javascript
import AdyenCheckoutApi from 'adyen_checkout_api';
let defaultClient = AdyenCheckoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenCheckoutApi.UtilityApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'applePaySessionRequest': new AdyenCheckoutApi.ApplePaySessionRequest() // ApplePaySessionRequest | 
};
apiInstance.postApplePaySessions(opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **applePaySessionRequest** | [**ApplePaySessionRequest**](ApplePaySessionRequest.md)|  | [optional] 

### Return type

[**ApplePaySessionResponse**](ApplePaySessionResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postOriginKeys

> UtilityResponse postOriginKeys(opts)

Create originKey values for domains

This operation takes the origin domains and returns a JSON object containing the corresponding origin keys for the domains.  &gt; If you&#39;re still using origin key for your Web Drop-in or Components integration, we recommend [switching to client key](https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key). This allows you to use a single key for all origins, add or remove origins without generating a new key, and detect the card type from the number entered in your payment form. 

### Example

```javascript
import AdyenCheckoutApi from 'adyen_checkout_api';
let defaultClient = AdyenCheckoutApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenCheckoutApi.UtilityApi();
let opts = {
  'idempotencyKey': "37ca9c97-d1d1-4c62-89e8-706891a563ed", // String | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
  'utilityRequest': new AdyenCheckoutApi.UtilityRequest() // UtilityRequest | 
};
apiInstance.postOriginKeys(opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). | [optional] 
 **utilityRequest** | [**UtilityRequest**](UtilityRequest.md)|  | [optional] 

### Return type

[**UtilityResponse**](UtilityResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

