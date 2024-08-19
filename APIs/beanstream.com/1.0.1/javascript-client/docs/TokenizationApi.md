# BeanstreamPayments.TokenizationApi

All URIs are relative to *https://www.beanstream.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scriptsTokenizationTokensPost**](TokenizationApi.md#scriptsTokenizationTokensPost) | **POST** /scripts/tokenization/tokens | Tokenize credit card



## scriptsTokenizationTokensPost

> TokenResponse scriptsTokenizationTokensPost(opts)

Tokenize credit card

NOTE that the full URL for this API call is https://www.beanstream.com/scripts/tokenization/tokens. Turn a credit card into a token using this service. This helps lessen your PCI scope by not passing the credit card information to your server. Instead you turn the card number into a token in the client app, then send the token to the server. When you send the token to Beanstream to make a payment, Beanstream then looks up the card number from that token and makes the payment. Tokens can also be used to create payment profiles.

### Example

```javascript
import BeanstreamPayments from 'beanstream_payments';

let apiInstance = new BeanstreamPayments.TokenizationApi();
let opts = {
  'tokenRequest': new BeanstreamPayments.TokenRequest() // TokenRequest | 
};
apiInstance.scriptsTokenizationTokensPost(opts, (error, data, response) => {
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
 **tokenRequest** | [**TokenRequest**](TokenRequest.md)|  | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

