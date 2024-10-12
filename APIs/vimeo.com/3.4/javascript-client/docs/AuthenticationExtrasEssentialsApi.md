# Vimeo.AuthenticationExtrasEssentialsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clientAuth**](AuthenticationExtrasEssentialsApi.md#clientAuth) | **POST** /oauth/authorize/client | Authorize a client with OAuth
[**convertAccessToken**](AuthenticationExtrasEssentialsApi.md#convertAccessToken) | **POST** /oauth/authorize/vimeo_oauth1 | Convert OAuth 1 access tokens to OAuth 2 access tokens
[**deleteToken**](AuthenticationExtrasEssentialsApi.md#deleteToken) | **DELETE** /tokens | Revoke the current access token
[**exchangeAuthCode**](AuthenticationExtrasEssentialsApi.md#exchangeAuthCode) | **POST** /oauth/access_token | Exchange an authorization code for an access token
[**verifyToken**](AuthenticationExtrasEssentialsApi.md#verifyToken) | **GET** /oauth/verify | Verify an OAuth 2 token



## clientAuth

> Auth clientAuth(clientAuthRequest)

Authorize a client with OAuth

For information on utilizing OAuth client authorization, see our [authentication](/api/authentication#generate-unauthenticated-tokens) documentation or the [Client Credentials Grant](https://tools.ietf.org/html/draft-ietf-oauth-v2-31#section-4.4) section of the [OAuth spec](https://tools.ietf.org/html/draft-ietf-oauth-v2-31.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AuthenticationExtrasEssentialsApi();
let clientAuthRequest = new Vimeo.ClientAuthRequest(); // ClientAuthRequest | 
apiInstance.clientAuth(clientAuthRequest, (error, data, response) => {
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
 **clientAuthRequest** | [**ClientAuthRequest**](ClientAuthRequest.md)|  | 

### Return type

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.auth+json
- **Accept**: application/vnd.vimeo.auth+json


## convertAccessToken

> Auth convertAccessToken(convertAccessTokenRequest)

Convert OAuth 1 access tokens to OAuth 2 access tokens

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AuthenticationExtrasEssentialsApi();
let convertAccessTokenRequest = new Vimeo.ConvertAccessTokenRequest(); // ConvertAccessTokenRequest | 
apiInstance.convertAccessToken(convertAccessTokenRequest, (error, data, response) => {
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
 **convertAccessTokenRequest** | [**ConvertAccessTokenRequest**](ConvertAccessTokenRequest.md)|  | 

### Return type

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.auth+json
- **Accept**: application/vnd.vimeo.auth+json


## deleteToken

> Auth deleteToken()

Revoke the current access token

This method enables an app to notify the API that it is done with a token and that the token can be discarded.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AuthenticationExtrasEssentialsApi();
apiInstance.deleteToken((error, data, response) => {
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

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.auth+json


## exchangeAuthCode

> Auth exchangeAuthCode(exchangeAuthCodeRequest)

Exchange an authorization code for an access token

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AuthenticationExtrasEssentialsApi();
let exchangeAuthCodeRequest = new Vimeo.ExchangeAuthCodeRequest(); // ExchangeAuthCodeRequest | 
apiInstance.exchangeAuthCode(exchangeAuthCodeRequest, (error, data, response) => {
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
 **exchangeAuthCodeRequest** | [**ExchangeAuthCodeRequest**](ExchangeAuthCodeRequest.md)|  | 

### Return type

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.auth+json
- **Accept**: application/vnd.vimeo.auth+json


## verifyToken

> Auth verifyToken()

Verify an OAuth 2 token

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AuthenticationExtrasEssentialsApi();
apiInstance.verifyToken((error, data, response) => {
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

[**Auth**](Auth.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.auth+json

