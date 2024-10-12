# BrowshotApi.AccountApi

All URIs are relative to *https://api.browshot.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccountInfo**](AccountApi.md#getAccountInfo) | **GET** /account/info | Get information about your account



## getAccountInfo

> Account getAccountInfo(opts)

Get information about your account

Get information about your account.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.AccountApi();
let opts = {
  'details': 1 // Number | level of information returned
};
apiInstance.getAccountInfo(opts, (error, data, response) => {
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
 **details** | **Number**| level of information returned | [optional] [default to 1]

### Return type

[**Account**](Account.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

