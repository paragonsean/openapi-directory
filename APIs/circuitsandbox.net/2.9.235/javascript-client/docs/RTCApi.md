# RestApiVersion2.RTCApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getActiveSessions**](RTCApi.md#getActiveSessions) | **GET** /rtc/sessions | Gets a list of active sessions



## getActiveSessions

> Label getActiveSessions()

Gets a list of active sessions

Gets a list of active RTCsessions OauthScopes: CALLS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.RTCApi();
apiInstance.getActiveSessions((error, data, response) => {
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

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

