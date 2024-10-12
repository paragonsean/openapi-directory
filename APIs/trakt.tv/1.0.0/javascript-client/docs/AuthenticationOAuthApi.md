# TraktApi.AuthenticationOAuthApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizeApplication**](AuthenticationOAuthApi.md#authorizeApplication) | **GET** /oauth/authorize | Authorize Application
[**exchangeRefreshTokenForAccessToken**](AuthenticationOAuthApi.md#exchangeRefreshTokenForAccessToken) | **POST** /oauth/token | Exchange refresh_token for access_token
[**revokeAnAccessToken**](AuthenticationOAuthApi.md#revokeAnAccessToken) | **POST** /oauth/revoke | Revoke an access_token



## authorizeApplication

> authorizeApplication(responseType, clientId, redirectUri, opts)

Authorize Application

Construct then redirect to this URL. The Trakt website will request permissions for your app, which the user needs to approve. If the user isn&#39;t signed into Trakt, it will ask them to do so. Send &#x60;signup&#x3D;true&#x60; if you prefer the account sign up page to be the default.  **Note:** You should use the normal **https://trakt.tv** hostname when creating this URL and not the API URL.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.AuthenticationOAuthApi();
let responseType = "code"; // String | Must be set to code.
let clientId = " "; // String | Get this from your app settings.
let redirectUri = " "; // String | URI specified in your app settings.
let opts = {
  'state': " ", // String | State variable for CSRF purposes.
  'body': "body_example" // String | Default to the sign up page.
};
apiInstance.authorizeApplication(responseType, clientId, redirectUri, opts, (error, data, response) => {
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
 **responseType** | **String**| Must be set to code. | 
 **clientId** | **String**| Get this from your app settings. | 
 **redirectUri** | **String**| URI specified in your app settings. | 
 **state** | **String**| State variable for CSRF purposes. | [optional] 
 **body** | **String**| Default to the sign up page. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## exchangeRefreshTokenForAccessToken

> exchangeRefreshTokenForAccessToken(opts)

Exchange refresh_token for access_token

Use the &#x60;refresh_token&#x60; to get a new &#x60;access_token&#x60; without asking the user to re-authenticate. The &#x60;access_token&#x60; is valid for 3 months before it needs to be refreshed again.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;refresh_token&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Saved from the initial token method. | | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;client_secret&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;redirect_uri&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | URI specified in your app settings. | | &#x60;grant_type&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;* &lt;/a&gt; | string | &#x60;refresh_token&#x60; |

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.AuthenticationOAuthApi();
let opts = {
  'exchangeRefreshTokenForAccessTokenRequest': new TraktApi.ExchangeRefreshTokenForAccessTokenRequest() // ExchangeRefreshTokenForAccessTokenRequest | 
};
apiInstance.exchangeRefreshTokenForAccessToken(opts, (error, data, response) => {
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
 **exchangeRefreshTokenForAccessTokenRequest** | [**ExchangeRefreshTokenForAccessTokenRequest**](ExchangeRefreshTokenForAccessTokenRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokeAnAccessToken

> revokeAnAccessToken(opts)

Revoke an access_token

An &#x60;access_token&#x60; can be revoked when a user signs out of their Trakt account in your app. This is not required, but might improve the user experience so the user doesn&#39;t have an unused app connection hanging around.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;token&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | A valid OAuth &#x60;access_token&#x60;. | | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;client_secret&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. |

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.AuthenticationOAuthApi();
let opts = {
  'revokeAnAccessTokenRequest': new TraktApi.RevokeAnAccessTokenRequest() // RevokeAnAccessTokenRequest | 
};
apiInstance.revokeAnAccessToken(opts, (error, data, response) => {
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
 **revokeAnAccessTokenRequest** | [**RevokeAnAccessTokenRequest**](RevokeAnAccessTokenRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

