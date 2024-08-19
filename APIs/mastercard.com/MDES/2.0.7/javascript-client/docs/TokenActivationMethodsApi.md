# MdesCustomerService.TokenActivationMethodsApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenActivationmethodsPost**](TokenActivationMethodsApi.md#tokenActivationmethodsPost) | **POST** /token/activationmethods | 



## tokenActivationmethodsPost

> TokenActivationMethodsResponseSchema tokenActivationmethodsPost(opts)



Used to retrieve the available Activation Methods for a token that is awaiting activation. Activation Methods are the means by which a cardholder may complete cardholder authentication with the issuer beyond the scope of MDES. It is possible that there are no Activation Methods for a token when an issuer did not provide any cardholder-specific information with the Tokenization Authorization Request (TAR) pre-digitization network message response. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenActivationMethodsApi();
let opts = {
  'tokenActivationMethodsRequestSchema': new MdesCustomerService.TokenActivationMethodsRequestSchema() // TokenActivationMethodsRequestSchema | Contains the details of the request message.
};
apiInstance.tokenActivationmethodsPost(opts, (error, data, response) => {
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
 **tokenActivationMethodsRequestSchema** | [**TokenActivationMethodsRequestSchema**](TokenActivationMethodsRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenActivationMethodsResponseSchema**](TokenActivationMethodsResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

