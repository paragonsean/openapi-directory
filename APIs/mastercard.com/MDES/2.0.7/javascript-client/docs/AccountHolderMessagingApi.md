# MdesCustomerService.AccountHolderMessagingApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountholdermessagingPost**](AccountHolderMessagingApi.md#accountholdermessagingPost) | **POST** /accountholdermessaging | 



## accountholdermessagingPost

> AccountHolderMessagingResponseSchema accountholdermessagingPost(opts)



Allows issuers to display customized messages per token within the Apple Pay wallet, below the digitized image of the card. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.AccountHolderMessagingApi();
let opts = {
  'accountholderMessagingRequestSchema': new MdesCustomerService.AccountHolderMessagingRequest() // AccountHolderMessagingRequest | Contains the details of the request message.
};
apiInstance.accountholdermessagingPost(opts, (error, data, response) => {
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
 **accountholderMessagingRequestSchema** | [**AccountHolderMessagingRequest**](AccountHolderMessagingRequest.md)| Contains the details of the request message. | [optional] 

### Return type

[**AccountHolderMessagingResponseSchema**](AccountHolderMessagingResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

