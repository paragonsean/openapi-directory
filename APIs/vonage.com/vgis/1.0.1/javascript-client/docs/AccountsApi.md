# VonageIntegrationSuite.AccountsApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccount**](AccountsApi.md#getAccount) | **GET** /self/account | Account info



## getAccount

> Account getAccount()

Account info

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.AccountsApi();
apiInstance.getAccount((error, data, response) => {
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

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

