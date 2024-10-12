# TurbineLabsApi.UserManagementApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminUserSelfAccessTokenAccessTokenKeyDelete**](UserManagementApi.md#adminUserSelfAccessTokenAccessTokenKeyDelete) | **DELETE** /admin/user/self/access_token/{access-token-key} | Delete the specified access token.
[**adminUserSelfAccessTokensGet**](UserManagementApi.md#adminUserSelfAccessTokensGet) | **GET** /admin/user/self/access_tokens | Lists Access Tokens that are configured for the authenticated user.
[**adminUserSelfAccessTokensPost**](UserManagementApi.md#adminUserSelfAccessTokensPost) | **POST** /admin/user/self/access_tokens | Creates a new Access Token and associates it with the authenticated user.
[**adminUserSelfGet**](UserManagementApi.md#adminUserSelfGet) | **GET** /admin/user/self | Returns the user object for the account authorized and making this request.



## adminUserSelfAccessTokenAccessTokenKeyDelete

> adminUserSelfAccessTokenAccessTokenKeyDelete(accessTokenKey, checksum)

Delete the specified access token.

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.UserManagementApi();
let accessTokenKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the key of the Access Token that should be deleted
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the user to be modified
apiInstance.adminUserSelfAccessTokenAccessTokenKeyDelete(accessTokenKey, checksum, (error, data, response) => {
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
 **accessTokenKey** | **String**| the key of the Access Token that should be deleted | 
 **checksum** | **String**| the current checksum of the user to be modified | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminUserSelfAccessTokensGet

> MultiAccessTokens adminUserSelfAccessTokensGet()

Lists Access Tokens that are configured for the authenticated user.

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.UserManagementApi();
apiInstance.adminUserSelfAccessTokensGet((error, data, response) => {
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

[**MultiAccessTokens**](MultiAccessTokens.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminUserSelfAccessTokensPost

> AccessToken adminUserSelfAccessTokensPost(description)

Creates a new Access Token and associates it with the authenticated user.

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.UserManagementApi();
let description = new TurbineLabsApi.AccessTokenDescription(); // AccessTokenDescription | A short string (<255 characters) describing the expected use of the token.
apiInstance.adminUserSelfAccessTokensPost(description, (error, data, response) => {
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
 **description** | [**AccessTokenDescription**](AccessTokenDescription.md)| A short string (&lt;255 characters) describing the expected use of the token. | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adminUserSelfGet

> User adminUserSelfGet()

Returns the user object for the account authorized and making this request.

Request the user object for an authorized requesting account.

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.UserManagementApi();
apiInstance.adminUserSelfGet((error, data, response) => {
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

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

