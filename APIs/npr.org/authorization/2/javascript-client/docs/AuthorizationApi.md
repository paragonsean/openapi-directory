# NprAuthorizationService.AuthorizationApi

All URIs are relative to *https://authorization.api.npr.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createToken**](AuthorizationApi.md#createToken) | **POST** /v2/token | Create a new OAuth2 access token
[**generateDeviceCode**](AuthorizationApi.md#generateDeviceCode) | **POST** /v2/device | Initiate an OAuth2 login flow for limited input devices
[**revokeToken**](AuthorizationApi.md#revokeToken) | **POST** /v2/token/revoke | Revoke an existing OAuth2 access token



## createToken

> AccessTokenData createToken(grantType, clientId, clientSecret, opts)

Create a new OAuth2 access token

Please be aware that the required parameters are contingent on the &#x60;grant_type&#x60; that you select.  For the &#x60;authorization_code&#x60; grant type, you are **required** to pass in the &#x60;code&#x60; and &#x60;redirect_uri&#x60; parameters. &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  For the &#x60;client_credentials&#x60; grant type, you do not need to pass in any additional parameters beyond the basic requirements. &#x60;code&#x60;, &#x60;redirect_uri&#x60;, &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  For the &#x60;device_code&#x60; grant type, you are **required** to pass in the &#x60;code&#x60; parameter. If you are a third-party developer, you are also required to provide the &#x60;scope&#x60; parameter; see the documentation for &#x60;GET /v2/authorize&#x60; for possible values. &#x60;redirect_uri&#x60;, &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  For the &#x60;password&#x60; grant type, you are **required** to pass in the &#x60;username&#x60; and &#x60;password&#x60; parameters. The &#x60;code&#x60; and &#x60;redirect_uri&#x60; parameters are ignored. Third-party developers do not have access to this grant type.  For the &#x60;refresh_token&#x60; grant type, you are **required** to pass in the &#x60;refresh_token&#x60; parameter. The &#x60;scope&#x60; parameter can optionally be used to request a different set of scopes than were used in the original request, but it **cannot** contain any scopes that were not previously requested. If not specified, then &#x60;scope&#x60; will be set to whichever scopes were used for the original access token request. If trading in an old non-expiring access token for a refresh-enabled token, set the value of &#x60;refresh_token&#x60; to the access token value and &#x60;token_type_hint&#x60; must be set to &#x60;access_token&#x60;. &#x60;code&#x60;, &#x60;redirect_uri&#x60;, &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  The &#x60;anonymous_user&#x60; grant type is a custom grant type created by NPR to suit our needs for functionality such as our &amp;quot;try-before-you-buy&amp;quot; experience. If you are a third-party developer, you will not have access to this grant type unless we have explicitly given you permission within our system. For this grant type, if you are a third-party developer, you are required to provide the &#x60;scope&#x60; parameter; see the documentation for &#x60;GET /v2/authorize&#x60; for possible values. &#x60;code&#x60;, &#x60;redirect_uri&#x60;, &#x60;service&#x60;, &#x60;username&#x60; and &#x60;password&#x60; parameters will be ignored.  The &#x60;third_party&#x60; grant type is another custom grant type created by NPR to handle login via third-party providers such as Facebook and Google. If you are a third-party developer, you will not have access to this grant types unless we have explicitly given you permission within our system. For this grant type, you are **required** to pass in the &#x60;service&#x60; and &#x60;token&#x60; parameters. If you are a third-party developer, you are also required to provide the &#x60;scope&#x60; parameter; see the documentation for &#x60;GET /v2/authorize&#x60; for possible values. The &#x60;code&#x60; and &#x60;redirect_uri&#x60; parameters are ignored.  If you are unsure of which grant type to select, assume that &#x60;authorization_code&#x60; is the one you want.  Note that at this time, refresh tokens are an opt-in feature; however, in the future, they will gradually transition to being opt-out, and ultimately required for all clients. Our general guidance at this time is that if this endpoint starts returning refresh tokens for you, you are responsible for implementing the code to handle them appropriately in accordance with the OAuth 2.0 spec. For more information about our gradual rollout of this feature, please contact the NPR One API team.

### Example

```javascript
import NprAuthorizationService from 'npr_authorization_service';

let apiInstance = new NprAuthorizationService.AuthorizationApi();
let grantType = "grantType_example"; // String | The type of grant the client is requesting
let clientId = "clientId_example"; // String | The client's ID, required for all grant types.
let clientSecret = "clientSecret_example"; // String | The client's secret, required for all grant types.
let opts = {
  'code': "code_example", // String | Required for `authorization_code` and `device_code` grant types. The authorization code from a successful call to `/v2/authorize`, or a device code from a successful call to `/v2/device`.
  'redirectUri': "redirectUri_example", // String | Required for `authorization_code` grant type. The requested redirect_uri.
  'username': "username_example", // String | Required for `password` grant type. The email address of an NPR user.
  'password': "password_example", // String | Required for `password` grant type. The password that matches the user specified with the username parameter.
  'service': "service_example", // String | Required for `third_party` grant type. The name of the third-party login provider.
  'refreshToken': "refreshToken_example", // String | Required for `refresh_token` grant type. A valid refresh token from a previous successful call to `POST /v2/token`.
  'scope': "scope_example", // String | Required for third-party developers using the `device_code` and `third_party` grant types. Optionally used by the `refresh_token` grant type. A space-separated list of scope(s) requested by the application.
  'tokenTypeHint': "tokenTypeHint_example" // String | A hint about the type of the token submitted for a new access and refresh token. If unspecified, the default value is assumed to be `refresh_token`.
};
apiInstance.createToken(grantType, clientId, clientSecret, opts, (error, data, response) => {
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
 **grantType** | **String**| The type of grant the client is requesting | 
 **clientId** | **String**| The client&#39;s ID, required for all grant types. | 
 **clientSecret** | **String**| The client&#39;s secret, required for all grant types. | 
 **code** | **String**| Required for &#x60;authorization_code&#x60; and &#x60;device_code&#x60; grant types. The authorization code from a successful call to &#x60;/v2/authorize&#x60;, or a device code from a successful call to &#x60;/v2/device&#x60;. | [optional] 
 **redirectUri** | **String**| Required for &#x60;authorization_code&#x60; grant type. The requested redirect_uri. | [optional] 
 **username** | **String**| Required for &#x60;password&#x60; grant type. The email address of an NPR user. | [optional] 
 **password** | **String**| Required for &#x60;password&#x60; grant type. The password that matches the user specified with the username parameter. | [optional] 
 **service** | **String**| Required for &#x60;third_party&#x60; grant type. The name of the third-party login provider. | [optional] 
 **refreshToken** | **String**| Required for &#x60;refresh_token&#x60; grant type. A valid refresh token from a previous successful call to &#x60;POST /v2/token&#x60;. | [optional] 
 **scope** | **String**| Required for third-party developers using the &#x60;device_code&#x60; and &#x60;third_party&#x60; grant types. Optionally used by the &#x60;refresh_token&#x60; grant type. A space-separated list of scope(s) requested by the application. | [optional] 
 **tokenTypeHint** | **String**| A hint about the type of the token submitted for a new access and refresh token. If unspecified, the default value is assumed to be &#x60;refresh_token&#x60;. | [optional] 

### Return type

[**AccessTokenData**](AccessTokenData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## generateDeviceCode

> DeviceCodeData generateDeviceCode(clientId, clientSecret, opts)

Initiate an OAuth2 login flow for limited input devices

This flow should only be used by clients who cannot show a native webview or do not have advanced input controls. It is an alternative to &#x60;GET /v2/authorize&#x60;.  Third-party clients will need to use one or the other of these two endpoints, but they will generally not use both.

### Example

```javascript
import NprAuthorizationService from 'npr_authorization_service';

let apiInstance = new NprAuthorizationService.AuthorizationApi();
let clientId = "clientId_example"; // String | The client's ID
let clientSecret = "clientSecret_example"; // String | The client's secret key
let opts = {
  'scope': "scope_example" // String | A space-separated list of scope(s) requested by the application. Required for all untrusted clients; will be ignored for trusted clients.
};
apiInstance.generateDeviceCode(clientId, clientSecret, opts, (error, data, response) => {
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
 **clientId** | **String**| The client&#39;s ID | 
 **clientSecret** | **String**| The client&#39;s secret key | 
 **scope** | **String**| A space-separated list of scope(s) requested by the application. Required for all untrusted clients; will be ignored for trusted clients. | [optional] 

### Return type

[**DeviceCodeData**](DeviceCodeData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## revokeToken

> Object revokeToken(authorization, token, opts)

Revoke an existing OAuth2 access token

Our implementation follows the proposed IETF specification [RFC-7009](https://tools.ietf.org/html/rfc7009).  If your client application offers the ability to for a logged-in user to log out, and you have access to a long-lived &#x60;client_credentials&#x60; token (i.e. you have generated one that you are storing securely for the lifetime of the entire app install), we suggest (but do not require) that you call this endpoint and revoke the access token belonging to the logged-in user as part of your logout process. If you do not already have a long-lived &#x60;client_credentials&#x60; token, please don&#39;t generate one just for the purposes of calling this endpoint.  If you are building a prototype application, we also recommend that you use this endpoint to clean up access tokens that you generate during the testing of your app and do not intend to reuse.  Note that revoking an access token will automatically revoke any refresh tokens associated with it, and vice-versa.

### Example

```javascript
import NprAuthorizationService from 'npr_authorization_service';

let apiInstance = new NprAuthorizationService.AuthorizationApi();
let authorization = "authorization_example"; // String | A `client_credentials` access token from the same client application as the token being revoked. Should start with `Bearer`, followed by a space, followed by the token.
let token = "token_example"; // String | The access token or refresh token that the client wants to have revoked.
let opts = {
  'tokenTypeHint': "tokenTypeHint_example" // String | A hint about the type of the token submitted for revocation. If unspecified, the default value is assumed to be `access_token`.
};
apiInstance.revokeToken(authorization, token, opts, (error, data, response) => {
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
 **authorization** | **String**| A &#x60;client_credentials&#x60; access token from the same client application as the token being revoked. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | 
 **token** | **String**| The access token or refresh token that the client wants to have revoked. | 
 **tokenTypeHint** | **String**| A hint about the type of the token submitted for revocation. If unspecified, the default value is assumed to be &#x60;access_token&#x60;. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

