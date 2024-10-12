# MdesCustomerService.TokenResendActivationCodeApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenResendactivationcodePost**](TokenResendActivationCodeApi.md#tokenResendactivationcodePost) | **POST** /token/resendactivationcode | 



## tokenResendactivationcodePost

> TokenResendActivationCodeResponseSchema tokenResendactivationcodePost(opts)



Used to trigger the process of generating and sending a new Activation Code (for a specific token) to the cardholder via the requested Activation Method. When successful, a new Activation Code Expiration Date Time period will begin, and a new Activation Code will be sent to the issuer using the Activation Code Notification (ACN) pre-digitization network message. It can only be used to do this for Activation Methods that involve the external distribution of an Activation Code to the cardholder. For example, via email or SMS. It cannot be used to send a new activation code via the \&quot;Mobile Application\&quot; activation method, for instance. A new Activation Code can be sent even if the previous code has not expired. A new Activation Code can also be sent even after the previous code has expired; however, it can only be done up to 30 days after the token was created  (the number of days is subject to change at the discretion of Mastercard). 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenResendActivationCodeApi();
let opts = {
  'tokenResendActivationCodeRequestSchema': new MdesCustomerService.TokenResendActivationCodeRequestSchema() // TokenResendActivationCodeRequestSchema | Contains the details of the request message.
};
apiInstance.tokenResendactivationcodePost(opts, (error, data, response) => {
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
 **tokenResendActivationCodeRequestSchema** | [**TokenResendActivationCodeRequestSchema**](TokenResendActivationCodeRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenResendActivationCodeResponseSchema**](TokenResendActivationCodeResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

