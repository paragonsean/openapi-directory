# MdesCustomerService.TokenUpdateApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenUpdatePost**](TokenUpdateApi.md#tokenUpdatePost) | **POST** /token/update | 



## tokenUpdatePost

> TokenUpdateResponseSchema tokenUpdatePost(opts)



Used to update Account PAN Mapping Information or Issuer Product Configuration ID associated to a provisioned token. To update a specific token, the API should be requested using the Token Unique Reference. To update all tokens mapped to a specific Account PAN, the API should be requested using the Account PAN. In either case, updates will only be applied to tokens in ACTIVE or SUSPENDED state, not those in IN PROGRESS or DELETED state. When updating Account PAN Mapping Information, the Account PAN, Expiration Date and Sequence Number, may be updated individually or in any combination. Only information provided will be updated. The account mapping will only update an Account PAN for a new Account PAN when they are both in the same Account Range. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenUpdateApi();
let opts = {
  'tokenUpdateRequestSchema': new MdesCustomerService.TokenUpdateRequestSchema() // TokenUpdateRequestSchema | Contains the details of the request message.
};
apiInstance.tokenUpdatePost(opts, (error, data, response) => {
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
 **tokenUpdateRequestSchema** | [**TokenUpdateRequestSchema**](TokenUpdateRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenUpdateResponseSchema**](TokenUpdateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

