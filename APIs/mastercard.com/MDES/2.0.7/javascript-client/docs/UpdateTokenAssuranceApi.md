# MdesCustomerService.UpdateTokenAssuranceApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updatetokenassurancePost**](UpdateTokenAssuranceApi.md#updatetokenassurancePost) | **POST** /updatetokenassurance | 



## updatetokenassurancePost

> UpdateTokenAssuranceResponseSchema updatetokenassurancePost(opts)



Used after an issuer has performed additional cardholder authentication to indicate an increased level of token assurance. It will only be applied to tokens that actually have a Token Assurance Level, and those that are in ACTIVE or SUSPENDED state. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.UpdateTokenAssuranceApi();
let opts = {
  'updateTokenAssuranceRequestSchema': new MdesCustomerService.UpdateTokenAssuranceRequestSchema() // UpdateTokenAssuranceRequestSchema | Contains the details of the request message.
};
apiInstance.updatetokenassurancePost(opts, (error, data, response) => {
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
 **updateTokenAssuranceRequestSchema** | [**UpdateTokenAssuranceRequestSchema**](UpdateTokenAssuranceRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**UpdateTokenAssuranceResponseSchema**](UpdateTokenAssuranceResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

