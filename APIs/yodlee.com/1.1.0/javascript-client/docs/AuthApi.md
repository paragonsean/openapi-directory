# YodleeCoreApis.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteApiKey**](AuthApi.md#deleteApiKey) | **DELETE** /auth/apiKey/{key} | Delete API Key
[**deleteToken**](AuthApi.md#deleteToken) | **DELETE** /auth/token | Delete Token
[**generateAccessToken**](AuthApi.md#generateAccessToken) | **POST** /auth/token | Generate Access Token
[**generateApiKey**](AuthApi.md#generateApiKey) | **POST** /auth/apiKey | Generate API Key
[**getApiKeys**](AuthApi.md#getApiKeys) | **GET** /auth/apiKey | Get API Keys



## deleteApiKey

> deleteApiKey(key)

Delete API Key

This endpoint allows an existing API key to be deleted.&lt;br&gt;You can use one of the following authorization methods to access this API:&lt;br&gt;&lt;ol&gt;&lt;li&gt;cobsession&lt;/li&gt;&lt;li&gt;JWT token&lt;/li&gt;&lt;/ol&gt; &lt;b&gt;Notes:&lt;/b&gt; &lt;li&gt;This service is not available in developer sandbox environment and will be made availablefor testing in your dedicated environment. 

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.AuthApi();
let key = "key_example"; // String | key
apiInstance.deleteApiKey(key, (error, data, response) => {
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
 **key** | **String**| key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## deleteToken

> deleteToken()

Delete Token

This endpoint revokes the token passed in the Authorization header. This service is applicable for JWT-based (and all API key-based) authentication and also client credential (clientId and secret) based authentication. This service does not return a response body. The HTTP response code is 204 (success with no content). &lt;br&gt;Tokens generally have limited lifetime of up to 30 minutes. You will call this service when you finish working with one user, and you want to delete the valid token rather than simply letting it expire.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;Revoking an access token (either type, admin or a user token) can take up to 2 minutes, as the tokens are stored on a distributed system.&lt;br/&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.AuthApi();
apiInstance.deleteToken((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## generateAccessToken

> ClientCredentialTokenResponse generateAccessToken()

Generate Access Token

&lt;b&gt;Generate Access Token using client credential authentication.&lt;/b&gt;&lt;br&gt;This service returns access tokens required to access Yodlee 1.1 APIs. These tokens are the simplest and easiest of several alternatives for authenticating with Yodlee servers.&lt;br&gt;The most commonly used services obtain data specific to an end user (your customer). For these services, you need a &lt;b&gt;user access token&lt;/b&gt;. These are simply tokens created with the user name parameter (&lt;b&gt;loginName&lt;/b&gt;) set to the id of your end user.  &lt;i&gt;&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; You determine this id and you must ensure it&#39;s unique among all your customers.&lt;/i&gt; &lt;br&gt;&lt;br&gt;Each token issued has an associated user. The token passed in the http headers explicitly names the user referenced in that API call.&lt;br&gt;&lt;br&gt;Some of the APIs do administrative work, and don&#39;t reference an end user. &lt;br/&gt;One example of administrative work is key management. Another example is registering a new user explicitly, with &lt;b&gt;POST /user/register&lt;/b&gt; call or subscribe to webhook, with &lt;b&gt;POST /config/notifications/events/{eventName}&lt;/b&gt;. &lt;br/&gt;To invoke these, you need an &lt;b&gt;admin access token&lt;/b&gt;. Create this by passing in your admin user login name in place of a regular user name.&lt;br&gt;&lt;br&gt;This service also allows for simplified registration of new users. Any time you pass in a user name not already in use, the system will automatically implicitly create a new user for you. &lt;br&gt;This user will naturally have very few associated details. You can later provide additional user information by calling the &lt;b&gt;PUT user/register service&lt;/b&gt;.&lt;br&gt;&lt;br&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;The content type has to be passed as application/x-www-form-urlencoded.&lt;li&gt;Upgrading to client credential authentication requires infrastructure reconfiguration. &lt;li&gt;Customers wishing to switch from another authentication scheme to client credential authentication, please contact Yodlee Client Services.&lt;/li&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.AuthApi();
apiInstance.generateAccessToken((error, data, response) => {
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

[**ClientCredentialTokenResponse**](ClientCredentialTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## generateApiKey

> ApiKeyResponse generateApiKey(apiKeyRequest)

Generate API Key

This endpoint is used to generate an API key. The RSA public key you provide should be in 2048 bit PKCS#8 encoded format. &lt;br&gt;A public key is a mandatory input for generating the API key.&lt;br/&gt;The public key should be a unique key. The apiKeyId you get in the response is what you should use to generate the JWT token.&lt;br&gt; You can use one of the following authorization methods to access&lt;br/&gt;this API:&lt;br&gt;&lt;ol&gt;&lt;li&gt;cobsession&lt;/li&gt;&lt;li&gt;JWT token&lt;/li&gt;&lt;/ol&gt; Alternatively, you can use base 64 encoded cobrandLogin and cobrandPassword in the Authorization header (Format: Authorization: Basic &lt;encoded value of cobrandLogin: cobrandPassword&gt;)&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;&lt;li&gt;This service is not available in developer sandbox environment and will be made available for testing in your dedicated environment. The content type has to be passed as application/json for the body parameter.&lt;/li&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.AuthApi();
let apiKeyRequest = new YodleeCoreApis.ApiKeyRequest(); // ApiKeyRequest | apiKeyRequest
apiInstance.generateApiKey(apiKeyRequest, (error, data, response) => {
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
 **apiKeyRequest** | [**ApiKeyRequest**](ApiKeyRequest.md)| apiKeyRequest | 

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8


## getApiKeys

> ApiKeyResponse getApiKeys()

Get API Keys

This endpoint provides the list of API keys that exist for a customer.&lt;br&gt;You can use one of the following authorization methods to access this API:&lt;br&gt;&lt;ol&gt;&lt;li&gt;cobsession&lt;/li&gt;&lt;li&gt;JWT token&lt;/li&gt;&lt;/ol&gt;&lt;b&gt;Notes:&lt;/b&gt;&lt;li&gt;This service is not available in developer sandbox environment and will be made available for testing in your dedicated environment. 

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.AuthApi();
apiInstance.getApiKeys((error, data, response) => {
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

[**ApiKeyResponse**](ApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

