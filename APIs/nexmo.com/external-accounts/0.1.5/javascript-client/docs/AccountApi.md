# ExternalAccountsApi.AccountApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllAccounts**](AccountApi.md#getAllAccounts) | **GET** / | Retrieve all accounts you own



## getAllAccounts

> GetAllAccounts200Response getAllAccounts(opts)

Retrieve all accounts you own

### Example

```javascript
import ExternalAccountsApi from 'external_accounts_api';
let defaultClient = ExternalAccountsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ExternalAccountsApi.AccountApi();
let opts = {
  'provider': "provider_example", // String | Filter by provider
  'pageNumber': 1, // Number | Page number of the results
  'pageSize': 1 // Number | Page size of the results
};
apiInstance.getAllAccounts(opts, (error, data, response) => {
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
 **provider** | **String**| Filter by provider | [optional] 
 **pageNumber** | **Number**| Page number of the results | [optional] [default to 1]
 **pageSize** | **Number**| Page size of the results | [optional] [default to 20]

### Return type

[**GetAllAccounts200Response**](GetAllAccounts200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

