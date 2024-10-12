# MdesCustomerService.TokenDeleteApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenDeletePost**](TokenDeleteApi.md#tokenDeletePost) | **POST** /token/delete | 



## tokenDeletePost

> TokenDeleteResponseSchema tokenDeletePost(opts)



Used to delete a token so that it may not initiate any new transactions. All authorizations for a deleted token will be declined. A deleted token may not be returned to an active state. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenDeleteApi();
let opts = {
  'tokenDeleteRequestSchema': new MdesCustomerService.TokenDeleteRequestSchema() // TokenDeleteRequestSchema | Contains the details of the request message.
};
apiInstance.tokenDeletePost(opts, (error, data, response) => {
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
 **tokenDeleteRequestSchema** | [**TokenDeleteRequestSchema**](TokenDeleteRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenDeleteResponseSchema**](TokenDeleteResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

