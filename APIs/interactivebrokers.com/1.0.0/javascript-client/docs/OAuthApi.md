# Ibkr3rdPartyWebApi.OAuthApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauthAccessTokenPost**](OAuthApi.md#oauthAccessTokenPost) | **POST** /oauth/access_token | Obtain a access token
[**oauthLiveSessionTokenPost**](OAuthApi.md#oauthLiveSessionTokenPost) | **POST** /oauth/live_session_token | Obtain a live session token
[**oauthRequestTokenPost**](OAuthApi.md#oauthRequestTokenPost) | **POST** /oauth/request_token | Obtain a request token



## oauthAccessTokenPost

> OauthAccessTokenPost200Response oauthAccessTokenPost(oauthAccessTokenPostRequest)

Obtain a access token

Obtain an access token using the request token and the verification code you received after the user provided authorization. See section 6.3 of the OAuth v1.0a specification for more details.  

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OAuthApi();
let oauthAccessTokenPostRequest = new Ibkr3rdPartyWebApi.OauthAccessTokenPostRequest(); // OauthAccessTokenPostRequest | OAuth Parameters
apiInstance.oauthAccessTokenPost(oauthAccessTokenPostRequest, (error, data, response) => {
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
 **oauthAccessTokenPostRequest** | [**OauthAccessTokenPostRequest**](OauthAccessTokenPostRequest.md)| OAuth Parameters | 

### Return type

[**OauthAccessTokenPost200Response**](OauthAccessTokenPost200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## oauthLiveSessionTokenPost

> OauthLiveSessionTokenPost200Response oauthLiveSessionTokenPost(oauthLiveSessionTokenPostRequest)

Obtain a live session token

In order to access protected IB resources, a live session token is required. This endpoint allows consumers to obtain a live session token to access these resources using an OAuth access token and the Diffie-Hellman prime and generator supplied during the registration process. Note this is an additional IB-specific step, and not part of the OAuth v1.0a specification. Please refer to the \&quot;OAuth at Interactive Brokers\&quot; document for more details.  https://www.interactivebrokers.com/webtradingapi/oauth.pdf 

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OAuthApi();
let oauthLiveSessionTokenPostRequest = new Ibkr3rdPartyWebApi.OauthLiveSessionTokenPostRequest(); // OauthLiveSessionTokenPostRequest | OAuth Parameters
apiInstance.oauthLiveSessionTokenPost(oauthLiveSessionTokenPostRequest, (error, data, response) => {
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
 **oauthLiveSessionTokenPostRequest** | [**OauthLiveSessionTokenPostRequest**](OauthLiveSessionTokenPostRequest.md)| OAuth Parameters | 

### Return type

[**OauthLiveSessionTokenPost200Response**](OauthLiveSessionTokenPost200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## oauthRequestTokenPost

> OauthRequestTokenPost200Response oauthRequestTokenPost(oauthRequestTokenPostRequest)

Obtain a request token

Obtain a request token. See section 6.1 of the OAuth v1.0a specification for more information. http://oauth.net/core/1.0a/#auth_step1  Note we do not return an oauth_token_secret in the response as we are using RSA signatures rather than PLAINTEXT authentication.  

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OAuthApi();
let oauthRequestTokenPostRequest = new Ibkr3rdPartyWebApi.OauthRequestTokenPostRequest(); // OauthRequestTokenPostRequest | OAuth Parameters
apiInstance.oauthRequestTokenPost(oauthRequestTokenPostRequest, (error, data, response) => {
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
 **oauthRequestTokenPostRequest** | [**OauthRequestTokenPostRequest**](OauthRequestTokenPostRequest.md)| OAuth Parameters | 

### Return type

[**OauthRequestTokenPost200Response**](OauthRequestTokenPost200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

