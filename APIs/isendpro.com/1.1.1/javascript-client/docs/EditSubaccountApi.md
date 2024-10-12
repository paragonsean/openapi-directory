# ApiISendPro.EditSubaccountApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccountEdit**](EditSubaccountApi.md#subaccountEdit) | **PUT** /subaccount | Edit a subaccount



## subaccountEdit

> SubaccountResponse subaccountEdit(subaccountRequest)

Edit a subaccount

Edit a subaccount

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.EditSubaccountApi();
let subaccountRequest = new ApiISendPro.SubaccountRequest(); // SubaccountRequest | edit sub account request
apiInstance.subaccountEdit(subaccountRequest, (error, data, response) => {
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
 **subaccountRequest** | [**SubaccountRequest**](SubaccountRequest.md)| edit sub account request | 

### Return type

[**SubaccountResponse**](SubaccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

