# MdesCustomerService.TokenActivateApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenActivatePost**](TokenActivateApi.md#tokenActivatePost) | **POST** /token/activate | 



## tokenActivatePost

> TokenActivateResponseSchema tokenActivatePost(opts)



Used to activate a token for a digitization that has been approved and provisioned, but requires additional cardholder authentication prior to activation. If the provisioning was not completed successfully, activation cannot be accomplished using Customer Service API. It is expected that a cardholder will complete the authentication process using an issuer&#39;s call center or using an issuer-supplied mobile application, and only then should the issuer use this API to activate the token. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenActivateApi();
let opts = {
  'tokenActivateRequestSchema': new MdesCustomerService.TokenActivateRequestSchema() // TokenActivateRequestSchema | Contains the details of the request message.
};
apiInstance.tokenActivatePost(opts, (error, data, response) => {
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
 **tokenActivateRequestSchema** | [**TokenActivateRequestSchema**](TokenActivateRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenActivateResponseSchema**](TokenActivateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

