# FilesComApi.SessionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSessions**](SessionsApi.md#deleteSessions) | **DELETE** /sessions | Delete user session (log out)
[**postSessions**](SessionsApi.md#postSessions) | **POST** /sessions | Create user session (log in)



## deleteSessions

> deleteSessions()

Delete user session (log out)

Delete user session (log out)

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SessionsApi();
apiInstance.deleteSessions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postSessions

> SessionEntity postSessions(opts)

Create user session (log in)

Create user session (log in)

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SessionsApi();
let opts = {
  'otp': "otp_example", // String | If this user has a 2FA device, provide its OTP or code here.
  'partialSessionId': "partialSessionId_example", // String | Identifier for a partially-completed login
  'password': "password_example", // String | Password for sign in
  'username': "username_example" // String | Username to sign in as
};
apiInstance.postSessions(opts, (error, data, response) => {
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
 **otp** | **String**| If this user has a 2FA device, provide its OTP or code here. | [optional] 
 **partialSessionId** | **String**| Identifier for a partially-completed login | [optional] 
 **password** | **String**| Password for sign in | [optional] 
 **username** | **String**| Username to sign in as | [optional] 

### Return type

[**SessionEntity**](SessionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

