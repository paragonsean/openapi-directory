# SevenIoApi.BalanceApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance**](BalanceApi.md#balance) | **GET** /balance | 



## balance

> Number balance()



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.BalanceApi();
apiInstance.balance((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Number**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

