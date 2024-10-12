# Mailscript.InputsApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllInputs**](InputsApi.md#getAllInputs) | **GET** /inputs | Get all inputs you have access to



## getAllInputs

> GetAllInputsResponse getAllInputs(opts)

Get all inputs you have access to



### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.InputsApi();
let opts = {
  'name': "name_example" // String | 
};
apiInstance.getAllInputs(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 

### Return type

[**GetAllInputsResponse**](GetAllInputsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

