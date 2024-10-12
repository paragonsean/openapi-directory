# MastodonApiSpecificationHttpsGithubComMastodonMastodon.OauthApi

All URIs are relative to *http://mastodon.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauthAuthorizeGet**](OauthApi.md#oauthAuthorizeGet) | **GET** /oauth/authorize | 
[**oauthRevokePost**](OauthApi.md#oauthRevokePost) | **POST** /oauth/revoke | 
[**oauthTokenPost**](OauthApi.md#oauthTokenPost) | **POST** /oauth/token | 



## oauthAuthorizeGet

> oauthAuthorizeGet(responseType, clientId, redirectUri, opts)



Displays an authorization form to the user. If approved, it will create and return an authorization code, then redirect to the desired redirect_uri, or show the authorization code if urn:ietf:wg:oauth:2.0:oob was requested. The authorization code can be used while requesting a token to obtain access to user-level methods.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.OauthApi();
let responseType = "responseType_example"; // String | Should be set equal to code.
let clientId = "clientId_example"; // String | Client ID, obtained during app registration.
let redirectUri = "redirectUri_example"; // String | Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration.
let opts = {
  'scope': "scope_example", // String | List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read.
  'forceLogin': true // Boolean | Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance.
};
apiInstance.oauthAuthorizeGet(responseType, clientId, redirectUri, opts, (error, data, response) => {
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
 **responseType** | **String**| Should be set equal to code. | 
 **clientId** | **String**| Client ID, obtained during app registration. | 
 **redirectUri** | **String**| Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the authorization code will be shown instead. Must match one of the redirect URIs declared during app registration. | 
 **scope** | **String**| List of requested OAuth scopes, separated by spaces (or by pluses, if using query parameters). Must be a subset of scopes declared during app registration. If not provided, defaults to read. | [optional] 
 **forceLogin** | **Boolean**| Added in 2.6.0. Forces the user to re-login, which is necessary for authorizing with multiple accounts from the same instance. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## oauthRevokePost

> oauthRevokePost(opts)



Revoke an access token to make it no longer valid for use.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.OauthApi();
let opts = {
  'oauthRevokePostRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.OauthRevokePostRequest() // OauthRevokePostRequest | 
};
apiInstance.oauthRevokePost(opts, (error, data, response) => {
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
 **oauthRevokePostRequest** | [**OauthRevokePostRequest**](OauthRevokePostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: application/json


## oauthTokenPost

> OauthTokenPost200Response oauthTokenPost(opts)



Returns an access token, to be used during API calls that are not public.

### Example

```javascript
import MastodonApiSpecificationHttpsGithubComMastodonMastodon from 'mastodon_api_specification__https__github_com_mastodon_mastodon';

let apiInstance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.OauthApi();
let opts = {
  'oauthTokenPostRequest': new MastodonApiSpecificationHttpsGithubComMastodonMastodon.OauthTokenPostRequest() // OauthTokenPostRequest | 
};
apiInstance.oauthTokenPost(opts, (error, data, response) => {
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
 **oauthTokenPostRequest** | [**OauthTokenPostRequest**](OauthTokenPostRequest.md)|  | [optional] 

### Return type

[**OauthTokenPost200Response**](OauthTokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/form-data
- **Accept**: application/json

