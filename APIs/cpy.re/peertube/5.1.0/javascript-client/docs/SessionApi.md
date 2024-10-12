# PeerTube.SessionApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOAuthClient**](SessionApi.md#getOAuthClient) | **GET** /api/v1/oauth-clients/local | Login prerequisite
[**getOAuthToken**](SessionApi.md#getOAuthToken) | **POST** /api/v1/users/token | Login
[**revokeOAuthToken**](SessionApi.md#revokeOAuthToken) | **POST** /api/v1/users/revoke-token | Logout



## getOAuthClient

> OAuthClient getOAuthClient()

Login prerequisite

You need to retrieve a client id and secret before [logging in](#operation/getOAuthToken).

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.SessionApi();
apiInstance.getOAuthClient((error, data, response) => {
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

[**OAuthClient**](OAuthClient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOAuthToken

> GetOAuthToken200Response getOAuthToken(opts)

Login

With your [client id and secret](#operation/getOAuthClient), you can retrieve an access and refresh tokens.

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.SessionApi();
let opts = {
  'clientId': "clientId_example", // String | 
  'clientSecret': "clientSecret_example", // String | 
  'grantType': "'password'", // String | 
  'password': "password_example", // String | 
  'username': "username_example", // String | immutable name of the user, used to find or mention its actor
  'refreshToken': "refreshToken_example" // String | 
};
apiInstance.getOAuthToken(opts, (error, data, response) => {
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
 **clientId** | **String**|  | [optional] 
 **clientSecret** | **String**|  | [optional] 
 **grantType** | **String**|  | [optional] [default to &#39;password&#39;]
 **password** | **String**|  | [optional] 
 **username** | **String**| immutable name of the user, used to find or mention its actor | [optional] 
 **refreshToken** | **String**|  | [optional] 

### Return type

[**GetOAuthToken200Response**](GetOAuthToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## revokeOAuthToken

> revokeOAuthToken()

Logout

Revokes your access token and its associated refresh token, destroying your current session.

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.SessionApi();
apiInstance.revokeOAuthToken((error, data, response) => {
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

