# VonageIntegrationSuite.UsersApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUser**](UsersApi.md#getUser) | **GET** /self | User info



## getUser

> User getUser()

User info

### Example

```javascript
import VonageIntegrationSuite from 'vonage_integration_suite';

let apiInstance = new VonageIntegrationSuite.UsersApi();
apiInstance.getUser((error, data, response) => {
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

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

