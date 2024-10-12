# MdesCustomerService.TokenUnsuspendApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenUnsuspendPost**](TokenUnsuspendApi.md#tokenUnsuspendPost) | **POST** /token/unsuspend | 



## tokenUnsuspendPost

> TokenUnsuspendResponseSchema tokenUnsuspendPost(opts)



Used to unsuspend or resume a suspended token and return it to the active state where it may initiate new transactions. Tokens may be suspended by multiple parties (suspenders) concurrently. The token status is updated from ACTIVE to SUSPENDED when the first suspender triggers a suspend action. Additional suspenders can add their suspend action to the list of suspenders. Suspenders can unsuspend only their own suspend action. All suspenders need to perform an unsuspend action to move a token from SUSPENDED to ACTIVE. The token status will only change when the last suspender has unsuspended the token. &lt;br&gt;For CoF tokens, the only two supported suspenders are issuer and token requestor.&lt;br&gt;For Apple Pay tokens, there are some differences in behavior versus the general principles. An issuer may add themselves as a suspender to a token already suspended by a cardholder, as above. However, a cardholder cannot suspend a token already suspended by the issuer. As a special case for Apple Pay, an issuer may unsuspend (override) a token already suspended by a cardholder. However, a cardholder cannot unsuspend a token already suspended by the issuer. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenUnsuspendApi();
let opts = {
  'tokenUnsuspendRequestSchema': new MdesCustomerService.TokenUnsuspendRequestSchema() // TokenUnsuspendRequestSchema | Contains the details of the request message.
};
apiInstance.tokenUnsuspendPost(opts, (error, data, response) => {
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
 **tokenUnsuspendRequestSchema** | [**TokenUnsuspendRequestSchema**](TokenUnsuspendRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenUnsuspendResponseSchema**](TokenUnsuspendResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

