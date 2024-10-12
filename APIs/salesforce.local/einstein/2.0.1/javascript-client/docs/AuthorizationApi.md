# EinsteinVisionAndEinsteinLanguage.AuthorizationApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateTokenV2**](AuthorizationApi.md#generateTokenV2) | **POST** /v2/oauth2/token | Generate an OAuth Token
[**revokeRefreshTokenV2**](AuthorizationApi.md#revokeRefreshTokenV2) | **DELETE** /v2/oauth2/tokens/{token} | Delete a Refresh Token



## generateTokenV2

> GenerateAccessTokenResponse generateTokenV2(opts)

Generate an OAuth Token

Returns an OAuth access token or a refresh token. You must pass a valid access token in the header of each API call.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';

let apiInstance = new EinsteinVisionAndEinsteinLanguage.AuthorizationApi();
let opts = {
  'assertion': "assertion_example", // String | encrypted payload to identify yourself
  'grantType': "grantType_example", // String | specify the authentication method desired
  'refreshToken': "refreshToken_example", // String | The refresh token you created previously.
  'scope': "scope_example", // String | set to `offline` to generate a refresh token
  'validFor': 60 // Number | Number of seconds until the access token expires. Default is 60 seconds. Maximum value is 30 days
};
apiInstance.generateTokenV2(opts, (error, data, response) => {
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
 **assertion** | **String**| encrypted payload to identify yourself | [optional] 
 **grantType** | **String**| specify the authentication method desired | [optional] 
 **refreshToken** | **String**| The refresh token you created previously. | [optional] 
 **scope** | **String**| set to &#x60;offline&#x60; to generate a refresh token | [optional] 
 **validFor** | **Number**| Number of seconds until the access token expires. Default is 60 seconds. Maximum value is 30 days | [optional] [default to 60]

### Return type

[**GenerateAccessTokenResponse**](GenerateAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## revokeRefreshTokenV2

> revokeRefreshTokenV2(token)

Delete a Refresh Token

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.AuthorizationApi();
let token = "SOME_REFRESH_TOKEN"; // String | the token to revoke
apiInstance.revokeRefreshTokenV2(token, (error, data, response) => {
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
 **token** | **String**| the token to revoke | 

### Return type

null (empty response body)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

