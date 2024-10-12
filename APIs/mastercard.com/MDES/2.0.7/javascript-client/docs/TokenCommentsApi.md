# MdesCustomerService.TokenCommentsApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenCommentsPost**](TokenCommentsApi.md#tokenCommentsPost) | **POST** /token/comments | 



## tokenCommentsPost

> TokenCommentsResponseSchema tokenCommentsPost(opts)



Used to retrieve all comments associated with a token. Typically the response includes comments created earlier by Issuer Customer Service representatives detailing additional information about a particular inquiry or event. There may also be comments with warnings of potential fraud. These comments are created automatically by the MDES system when a Token requestor indicates a high risk of fraud during digitization. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenCommentsApi();
let opts = {
  'tokenCommentsRequestSchema': new MdesCustomerService.TokenCommentsRequestSchema() // TokenCommentsRequestSchema | Contains the details of the request message.
};
apiInstance.tokenCommentsPost(opts, (error, data, response) => {
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
 **tokenCommentsRequestSchema** | [**TokenCommentsRequestSchema**](TokenCommentsRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenCommentsResponseSchema**](TokenCommentsResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

