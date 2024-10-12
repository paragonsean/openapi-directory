# ApiVideo.AuthenticationApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pOSTAuthApiKey**](AuthenticationApi.md#pOSTAuthApiKey) | **POST** /auth/api-key | Authenticate
[**pOSTAuthRefresh**](AuthenticationApi.md#pOSTAuthRefresh) | **POST** /auth/refresh | Refresh token



## pOSTAuthApiKey

> AccessToken pOSTAuthApiKey(opts)

Authenticate

To get started, submit your API key in the body of your request. api.video returns an access token that is valid for one hour (3600 seconds). A refresh token is also returned. View a [tutorial](https://api.video/blog/tutorials/authentication-tutorial) on authentication. All tutorials using the [authentication endpoint](https://api.video/blog/endpoints/authenticate)

### Example

```javascript
import ApiVideo from 'api_video';

let apiInstance = new ApiVideo.AuthenticationApi();
let opts = {
  'authenticatePayload': new ApiVideo.AuthenticatePayload() // AuthenticatePayload | 
};
apiInstance.pOSTAuthApiKey(opts, (error, data, response) => {
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
 **authenticatePayload** | [**AuthenticatePayload**](AuthenticatePayload.md)|  | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pOSTAuthRefresh

> AccessToken pOSTAuthRefresh(opts)

Refresh token

Use the refresh endpoint with the refresh token you received when you first authenticated using the api-key endpoint. Send the refresh token in the body of your request. The api.video API returns a new access token that is valid for one hour (3600 seconds) and a new refresh token.  

### Example

```javascript
import ApiVideo from 'api_video';

let apiInstance = new ApiVideo.AuthenticationApi();
let opts = {
  'refreshTokenPayload': new ApiVideo.RefreshTokenPayload() // RefreshTokenPayload | 
};
apiInstance.pOSTAuthRefresh(opts, (error, data, response) => {
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
 **refreshTokenPayload** | [**RefreshTokenPayload**](RefreshTokenPayload.md)|  | [optional] 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

