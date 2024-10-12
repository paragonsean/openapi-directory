# IllumiDesk.AuthApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authJwtTokenAuth**](AuthApi.md#authJwtTokenAuth) | **POST** /auth/jwt-token-auth/ | Create JSON Web Token (JWT)
[**authJwtTokenRefresh**](AuthApi.md#authJwtTokenRefresh) | **POST** /auth/jwt-token-refresh/ | Refresh a JSON Web Token (JWT)
[**authJwtTokenVerify**](AuthApi.md#authJwtTokenVerify) | **POST** /auth/jwt-token-verify/ | Validate JSON Web Token (JWT)
[**authRegister**](AuthApi.md#authRegister) | **POST** /auth/register/ | Register a user
[**oauthLogin**](AuthApi.md#oauthLogin) | **GET** /auth/login/{provider}/ | 



## authJwtTokenAuth

> JWT authJwtTokenAuth(opts)

Create JSON Web Token (JWT)

### Example

```javascript
import IllumiDesk from 'illumi_desk';

let apiInstance = new IllumiDesk.AuthApi();
let opts = {
  'jwtData': new IllumiDesk.JWTData() // JWTData | 
};
apiInstance.authJwtTokenAuth(opts, (error, data, response) => {
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
 **jwtData** | [**JWTData**](JWTData.md)|  | [optional] 

### Return type

[**JWT**](JWT.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## authJwtTokenRefresh

> RefreshJSONWebToken authJwtTokenRefresh(opts)

Refresh a JSON Web Token (JWT)

Obtains a new JSON Web Token using existing user credentials.

### Example

```javascript
import IllumiDesk from 'illumi_desk';

let apiInstance = new IllumiDesk.AuthApi();
let opts = {
  'refreshjwtData': new IllumiDesk.RefreshJSONWebTokenData() // RefreshJSONWebTokenData | 
};
apiInstance.authJwtTokenRefresh(opts, (error, data, response) => {
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
 **refreshjwtData** | [**RefreshJSONWebTokenData**](RefreshJSONWebTokenData.md)|  | [optional] 

### Return type

[**RefreshJSONWebToken**](RefreshJSONWebToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## authJwtTokenVerify

> VerifyJSONWebToken authJwtTokenVerify(opts)

Validate JSON Web Token (JWT)

Checks veraciy of token.

### Example

```javascript
import IllumiDesk from 'illumi_desk';

let apiInstance = new IllumiDesk.AuthApi();
let opts = {
  'verifyjwtData': new IllumiDesk.VerifyJSONWebTokenData() // VerifyJSONWebTokenData | 
};
apiInstance.authJwtTokenVerify(opts, (error, data, response) => {
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
 **verifyjwtData** | [**VerifyJSONWebTokenData**](VerifyJSONWebTokenData.md)|  | [optional] 

### Return type

[**VerifyJSONWebToken**](VerifyJSONWebToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## authRegister

> User authRegister(opts)

Register a user

User registration requires confirming email address to activate user.

### Example

```javascript
import IllumiDesk from 'illumi_desk';

let apiInstance = new IllumiDesk.AuthApi();
let opts = {
  'userData': new IllumiDesk.UserData() // UserData | 
};
apiInstance.authRegister(opts, (error, data, response) => {
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
 **userData** | [**UserData**](UserData.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## oauthLogin

> oauthLogin(provider)



### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.AuthApi();
let provider = "provider_example"; // String | OAuth2 provider
apiInstance.oauthLogin(provider, (error, data, response) => {
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
 **provider** | **String**| OAuth2 provider | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

