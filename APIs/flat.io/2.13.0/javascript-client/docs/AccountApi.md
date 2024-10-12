# FlatApi.AccountApi

All URIs are relative to *https://api.flat.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuthenticatedUser**](AccountApi.md#getAuthenticatedUser) | **GET** /me | Get current user profile



## getAuthenticatedUser

> UserDetails getAuthenticatedUser(opts)

Get current user profile

Get details about the current authenticated User. 

### Example

```javascript
import FlatApi from 'flat_api';
let defaultClient = FlatApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FlatApi.AccountApi();
let opts = {
  'onlyId': false // Boolean | Only return the user id
};
apiInstance.getAuthenticatedUser(opts, (error, data, response) => {
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
 **onlyId** | **Boolean**| Only return the user id | [optional] [default to false]

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

