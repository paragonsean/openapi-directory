# MdesCustomerService.TokenStatusHistoryApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tokenStatushistoryPost**](TokenStatusHistoryApi.md#tokenStatushistoryPost) | **POST** /token/statushistory | 



## tokenStatushistoryPost

> TokenStatusHistoryResponseSchema tokenStatushistoryPost(opts)



Used to retrieve the historical statuses and lifecycle events for a token, such as when it was initially activated, subsequently suspended or resumed, and finally deleted. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TokenStatusHistoryApi();
let opts = {
  'tokenStatusHistoryRequestSchema': new MdesCustomerService.TokenStatusHistoryRequestSchema() // TokenStatusHistoryRequestSchema | Contains the details of the request message.
};
apiInstance.tokenStatushistoryPost(opts, (error, data, response) => {
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
 **tokenStatusHistoryRequestSchema** | [**TokenStatusHistoryRequestSchema**](TokenStatusHistoryRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TokenStatusHistoryResponseSchema**](TokenStatusHistoryResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

