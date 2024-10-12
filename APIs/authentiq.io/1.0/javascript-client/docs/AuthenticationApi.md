# AuthentiqConnectApi.AuthenticationApi

All URIs are relative to *https://connect.authentiq.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize**](AuthenticationApi.md#authorize) | **GET** /authorize | Authenticate a user
[**token**](AuthenticationApi.md#token) | **POST** /token | Obtain an ID Token
[**userInfo**](AuthenticationApi.md#userInfo) | **GET** /userinfo | Retrieve a user profile



## authorize

> authorize(clientId, responseType, scope, redirectUri, state, opts)

Authenticate a user

Start a session with Authentiq Connect to authenticate a user.  &#x60;&#x60;&#x60; GET https://connect.authentiq.io/authorize?client_id&#x3D;&lt;your-client-id&gt;&amp;response_type&#x3D;code+id_token&amp;scope&#x3D;openid+email&amp;redirect_uri&#x3D;&lt;your-redirect-uri&gt;&amp;state&#x3D;0123456789 &#x60;&#x60;&#x60;  This endpoint also supports the POST method. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';

let apiInstance = new AuthentiqConnectApi.AuthenticationApi();
let clientId = "clientId_example"; // String | A client ID obtained from the [Dashboard](https://dashboard.authentiq.com/). 
let responseType = "responseType_example"; // String | The OIDC response type to use for this authentication flow. Valid choices are `code`, `id_token`, `token`, `token id_token`, `code id_token` `code token` and `code token id_token`, but a client can be configured with a more restricted set. 
let scope = "scope_example"; // String | The space-separated identity claims to request from the end-user. Always include `openid` as a scope for compatibility with OIDC. 
let redirectUri = "redirectUri_example"; // String | The location to redirect to after (un)successful authentication. See OIDC for the parameters passed in the query string (`response_mode=query`) or as fragments (`response_mode=fragment`). Unless the client is in test-mode this must be one of the registered redirect URLs. 
let state = "state_example"; // String | An opaque string that will be passed back to the redirect URL and therefore can be used to communicate client side state and prevent CSRF attacks. 
let opts = {
  'responseMode': "responseMode_example", // String | Whether to append parameters to the redirect URL in the query string (`query`) or as fragments (`fragment`). This option usually has a sensible default for each of the response types. 
  'nonce': "nonce_example", // String | An nonce provided by the client (and opaque to Authentiq Connect) that will be included in any ID Token generated for this session. Clients should use the nonce to mitigate replay attacks. 
  'display': "'page'", // String | The authentication display mode, which can be one of `page`, `popup` or `modal`. Defaults to `page`. 
  'prompt': "'login'", // String | Space-delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for reauthentication and consent. The supported values are: `none`, `login`, `consent`. If `consent` the end-user is asked to (re)confirm what claims they share. Use `none` to check for an active session. 
  'maxAge': 0, // Number | Specifies the allowable elapsed time in seconds since the last time the end-user was actively authenticated. 
  'uiLocales': "uiLocales_example" // String | Specifies the preferred language to use on the authorization page, as a space-separated list of BCP47 language tags. Ignored at the moment. 
};
apiInstance.authorize(clientId, responseType, scope, redirectUri, state, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientId** | **String**| A client ID obtained from the [Dashboard](https://dashboard.authentiq.com/).  | 
 **responseType** | **String**| The OIDC response type to use for this authentication flow. Valid choices are &#x60;code&#x60;, &#x60;id_token&#x60;, &#x60;token&#x60;, &#x60;token id_token&#x60;, &#x60;code id_token&#x60; &#x60;code token&#x60; and &#x60;code token id_token&#x60;, but a client can be configured with a more restricted set.  | 
 **scope** | **String**| The space-separated identity claims to request from the end-user. Always include &#x60;openid&#x60; as a scope for compatibility with OIDC.  | 
 **redirectUri** | **String**| The location to redirect to after (un)successful authentication. See OIDC for the parameters passed in the query string (&#x60;response_mode&#x3D;query&#x60;) or as fragments (&#x60;response_mode&#x3D;fragment&#x60;). Unless the client is in test-mode this must be one of the registered redirect URLs.  | 
 **state** | **String**| An opaque string that will be passed back to the redirect URL and therefore can be used to communicate client side state and prevent CSRF attacks.  | 
 **responseMode** | **String**| Whether to append parameters to the redirect URL in the query string (&#x60;query&#x60;) or as fragments (&#x60;fragment&#x60;). This option usually has a sensible default for each of the response types.  | [optional] 
 **nonce** | **String**| An nonce provided by the client (and opaque to Authentiq Connect) that will be included in any ID Token generated for this session. Clients should use the nonce to mitigate replay attacks.  | [optional] 
 **display** | **String**| The authentication display mode, which can be one of &#x60;page&#x60;, &#x60;popup&#x60; or &#x60;modal&#x60;. Defaults to &#x60;page&#x60;.  | [optional] [default to &#39;page&#39;]
 **prompt** | **String**| Space-delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for reauthentication and consent. The supported values are: &#x60;none&#x60;, &#x60;login&#x60;, &#x60;consent&#x60;. If &#x60;consent&#x60; the end-user is asked to (re)confirm what claims they share. Use &#x60;none&#x60; to check for an active session.  | [optional] [default to &#39;login&#39;]
 **maxAge** | **Number**| Specifies the allowable elapsed time in seconds since the last time the end-user was actively authenticated.  | [optional] [default to 0]
 **uiLocales** | **String**| Specifies the preferred language to use on the authorization page, as a space-separated list of BCP47 language tags. Ignored at the moment.  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## token

> Token token(clientId, clientSecret, code, grantType, redirectUri, opts)

Obtain an ID Token

Exchange en authorization code for an ID Token or Access Token.  This endpoint supports both &#x60;client_secret_basic&#x60; (default) and &#x60;client_secret_basic&#x60; authentication methods, as specified by the client&#39;s &#x60;token_endpoint_auth_method&#x60;. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';

let apiInstance = new AuthentiqConnectApi.AuthenticationApi();
let clientId = "clientId_example"; // String | The registered client ID. 
let clientSecret = "clientSecret_example"; // String | The registered client ID secret. 
let code = "code_example"; // String | The authorization code previously obtained from the Authentication endpoint. 
let grantType = "grantType_example"; // String | The authorization grant type, must be `authorization_code`. 
let redirectUri = "redirectUri_example"; // String | The redirect URL that was used previously with the Authentication endpoint. 
let opts = {
  'authorization': "authorization_example" // String | HTTP Basic authorization header. 
};
apiInstance.token(clientId, clientSecret, code, grantType, redirectUri, opts, (error, data, response) => {
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
 **clientId** | **String**| The registered client ID.  | 
 **clientSecret** | **String**| The registered client ID secret.  | 
 **code** | **String**| The authorization code previously obtained from the Authentication endpoint.  | 
 **grantType** | **String**| The authorization grant type, must be &#x60;authorization_code&#x60;.  | 
 **redirectUri** | **String**| The redirect URL that was used previously with the Authentication endpoint.  | 
 **authorization** | **String**| HTTP Basic authorization header.  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html


## userInfo

> UserInfo userInfo()

Retrieve a user profile

Use this endpoint to retrieve a user&#39;s profile in case you are unable to parse an ID Token or you&#39;ve not already obtained enough details from the ID Token via the Token Endpoint. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';
let defaultClient = AuthentiqConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_code
let oauth_code = defaultClient.authentications['oauth_code'];
oauth_code.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth_implicit
let oauth_implicit = defaultClient.authentications['oauth_implicit'];
oauth_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthentiqConnectApi.AuthenticationApi();
apiInstance.userInfo((error, data, response) => {
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

[**UserInfo**](UserInfo.md)

### Authorization

[oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html

