# MdesCustomerService.TokenResetMobilePINApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenResetmobilepinPost**](TokenResetMobilePINApi.md#tokenResetmobilepinPost) | **POST** /token/resetmobilepin | 



## tokenResetmobilepinPost

> TokenResetMobilePinResponseSchema tokenResetmobilepinPost(opts)



Used to request that the Mobile PIN for a Mastercard Cloud-Based Payment token in a single issuer wallet is reset. The request is passed to the Credential Management System for processing. When the Mobile PIN is a token-level PIN (as opposed to a wallet-level PIN), the cardholder must choose a new PIN within 10 minutes of a Reset Mobile PIN action. Otherwise, the reset will need to be re-requested. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenResetMobilePINApi();
let opts = {
  'tokenResetMobilePinRequestSchema': new MdesCustomerService.TokenResetMobilePinRequestSchema() // TokenResetMobilePinRequestSchema | Contains the details of the request message.
};
apiInstance.tokenResetmobilepinPost(opts, (error, data, response) => {
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
 **tokenResetMobilePinRequestSchema** | [**TokenResetMobilePinRequestSchema**](TokenResetMobilePinRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenResetMobilePinResponseSchema**](TokenResetMobilePinResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

