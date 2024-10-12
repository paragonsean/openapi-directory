# BhagavadGitaApi.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authOauthTokenPost**](AuthApi.md#authOauthTokenPost) | **POST** /auth/oauth/token | Send client credentials and get an access token.



## authOauthTokenPost

> authOauthTokenPost(clientId, clientSecret, grantType, scope)

Send client credentials and get an access token.

### Example

```javascript
import BhagavadGitaApi from 'bhagavad_gita_api';

let apiInstance = new BhagavadGitaApi.AuthApi();
let clientId = "clientId_example"; // String | Your app's client_id. Get from API dashboard.
let clientSecret = "clientSecret_example"; // String | Your app's client_secret. Get from API dashboard.
let grantType = "'client_credentials'"; // String | Grant Type.
let scope = "'verse chapter'"; // String | The resources that you would like to access.
apiInstance.authOauthTokenPost(clientId, clientSecret, grantType, scope, (error, data, response) => {
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
 **clientId** | **String**| Your app&#39;s client_id. Get from API dashboard. | 
 **clientSecret** | **String**| Your app&#39;s client_secret. Get from API dashboard. | 
 **grantType** | **String**| Grant Type. | [default to &#39;client_credentials&#39;]
 **scope** | **String**| The resources that you would like to access. | [default to &#39;verse chapter&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

