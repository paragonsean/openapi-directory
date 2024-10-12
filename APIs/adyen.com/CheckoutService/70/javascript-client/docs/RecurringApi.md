# AdyenCheckoutApi.RecurringApi

All URIs are relative to *https://checkout-test.adyen.com/v70*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteStoredPaymentMethodsStoredPaymentMethodId**](RecurringApi.md#deleteStoredPaymentMethodsStoredPaymentMethodId) | **DELETE** /storedPaymentMethods/{storedPaymentMethodId} | Delete a token for stored payment details
[**getStoredPaymentMethods**](RecurringApi.md#getStoredPaymentMethods) | **GET** /storedPaymentMethods | Get tokens for stored payment details



## deleteStoredPaymentMethodsStoredPaymentMethodId

> deleteStoredPaymentMethodsStoredPaymentMethodId(storedPaymentMethodId, shopperReference, merchantAccount)

Delete a token for stored payment details

Deletes the token identified in the path. The token can no longer be used with payment requests.

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

let apiInstance = new AdyenCheckoutApi.RecurringApi();
let storedPaymentMethodId = "storedPaymentMethodId_example"; // String | The unique identifier of the token.
let shopperReference = "shopperReference_example"; // String | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identifiable information (PII), for example name or email address.
let merchantAccount = "merchantAccount_example"; // String | Your merchant account.
apiInstance.deleteStoredPaymentMethodsStoredPaymentMethodId(storedPaymentMethodId, shopperReference, merchantAccount, (error, data, response) => {
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
 **storedPaymentMethodId** | **String**| The unique identifier of the token. | 
 **shopperReference** | **String**| Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | 
 **merchantAccount** | **String**| Your merchant account. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getStoredPaymentMethods

> ListStoredPaymentMethodsResponse getStoredPaymentMethods(opts)

Get tokens for stored payment details

Lists the tokens for stored payment details for the shopper identified in the path, if there are any available. The token ID can be used with payment requests for the shopper&#39;s payment. A summary of the stored details is included.  

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

let apiInstance = new AdyenCheckoutApi.RecurringApi();
let opts = {
  'shopperReference': "shopperReference_example", // String | Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identifiable information (PII), for example name or email address.
  'merchantAccount': "merchantAccount_example" // String | Your merchant account.
};
apiInstance.getStoredPaymentMethods(opts, (error, data, response) => {
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
 **shopperReference** | **String**| Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. &gt; Your reference must not include personally identifiable information (PII), for example name or email address. | [optional] 
 **merchantAccount** | **String**| Your merchant account. | [optional] 

### Return type

[**ListStoredPaymentMethodsResponse**](ListStoredPaymentMethodsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

