# SquareConnectApi.OAuthApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**obtainToken**](OAuthApi.md#obtainToken) | **POST** /oauth2/token | ObtainToken
[**renewToken**](OAuthApi.md#renewToken) | **POST** /oauth2/clients/{client_id}/access-token/renew | RenewToken
[**revokeToken**](OAuthApi.md#revokeToken) | **POST** /oauth2/revoke | RevokeToken



## obtainToken

> ObtainTokenResponse obtainToken(obtainTokenRequest)

ObtainToken

Returns an OAuth access token.  The endpoint supports distinct methods of obtaining OAuth access tokens. Applications specify a method by adding the &#x60;grant_type&#x60; parameter in the request and also provide relevant information.  __Note:__ Regardless of the method application specified, the endpoint always returns two items; an OAuth access token and a refresh token in the response.  __OAuth tokens should only live on secure servers. Application clients should never interact directly with OAuth tokens__.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';

let apiInstance = new SquareConnectApi.OAuthApi();
let obtainTokenRequest = new SquareConnectApi.ObtainTokenRequest(); // ObtainTokenRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.obtainToken(obtainTokenRequest, (error, data, response) => {
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
 **obtainTokenRequest** | [**ObtainTokenRequest**](ObtainTokenRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**ObtainTokenResponse**](ObtainTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## renewToken

> RenewTokenResponse renewToken(clientId, renewTokenRequest)

RenewToken

&#x60;RenewToken&#x60; is deprecated. For information about refreshing OAuth access tokens, see [Migrate from Renew to Refresh OAuth Tokens](https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens).   Renews an OAuth access token before it expires.  OAuth access tokens besides your application&#39;s personal access token expire after __30 days__. You can also renew expired tokens within __15 days__ of their expiration. You cannot renew an access token that has been expired for more than 15 days. Instead, the associated user must re-complete the OAuth flow from the beginning.  __Important:__ The &#x60;Authorization&#x60; header for this endpoint must have the following format:  &#x60;&#x60;&#x60; Authorization: Client APPLICATION_SECRET &#x60;&#x60;&#x60;  Replace &#x60;APPLICATION_SECRET&#x60; with the application secret on the Credentials page in the [developer dashboard](https://developer.squareup.com/apps).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure API key authorization: oauth2ClientSecret
let oauth2ClientSecret = defaultClient.authentications['oauth2ClientSecret'];
oauth2ClientSecret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//oauth2ClientSecret.apiKeyPrefix = 'Token';

let apiInstance = new SquareConnectApi.OAuthApi();
let clientId = "clientId_example"; // String | Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps).
let renewTokenRequest = new SquareConnectApi.RenewTokenRequest(); // RenewTokenRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.renewToken(clientId, renewTokenRequest, (error, data, response) => {
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
 **clientId** | **String**| Your application ID, available from the [developer dashboard](https://developer.squareup.com/apps). | 
 **renewTokenRequest** | [**RenewTokenRequest**](RenewTokenRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**RenewTokenResponse**](RenewTokenResponse.md)

### Authorization

[oauth2ClientSecret](../README.md#oauth2ClientSecret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokeToken

> RevokeTokenResponse revokeToken(revokeTokenRequest)

RevokeToken

Revokes an access token generated with the OAuth flow.  If an account has more than one OAuth access token for your application, this endpoint revokes all of them, regardless of which token you specify. When an OAuth access token is revoked, all of the active subscriptions associated with that OAuth token are canceled immediately.  __Important:__ The &#x60;Authorization&#x60; header for this endpoint must have the following format:  &#x60;&#x60;&#x60; Authorization: Client APPLICATION_SECRET &#x60;&#x60;&#x60;  Replace &#x60;APPLICATION_SECRET&#x60; with the application secret on the OAuth page in the [developer dashboard](https://developer.squareup.com/apps).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure API key authorization: oauth2ClientSecret
let oauth2ClientSecret = defaultClient.authentications['oauth2ClientSecret'];
oauth2ClientSecret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//oauth2ClientSecret.apiKeyPrefix = 'Token';

let apiInstance = new SquareConnectApi.OAuthApi();
let revokeTokenRequest = new SquareConnectApi.RevokeTokenRequest(); // RevokeTokenRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.revokeToken(revokeTokenRequest, (error, data, response) => {
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
 **revokeTokenRequest** | [**RevokeTokenRequest**](RevokeTokenRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**RevokeTokenResponse**](RevokeTokenResponse.md)

### Authorization

[oauth2ClientSecret](../README.md#oauth2ClientSecret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

