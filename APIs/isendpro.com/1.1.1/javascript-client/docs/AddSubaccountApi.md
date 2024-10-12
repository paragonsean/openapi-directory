# ApiISendPro.AddSubaccountApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subaccountAdd**](AddSubaccountApi.md#subaccountAdd) | **POST** /subaccount | Ajoute un sous compte



## subaccountAdd

> SubaccountAddResponse subaccountAdd(subaccountAddRequest)

Ajoute un sous compte

Ajoute un sous compte

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.AddSubaccountApi();
let subaccountAddRequest = new ApiISendPro.SubaccountAddRequest(); // SubaccountAddRequest | add sub account request
apiInstance.subaccountAdd(subaccountAddRequest, (error, data, response) => {
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
 **subaccountAddRequest** | [**SubaccountAddRequest**](SubaccountAddRequest.md)| add sub account request | 

### Return type

[**SubaccountAddResponse**](SubaccountAddResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, exemple1

