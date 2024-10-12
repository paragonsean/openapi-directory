# Contribly.AuthApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credentialsGet**](AuthApi.md#credentialsGet) | **GET** /credentials | List the credentials associated with the authenticated user.
[**scopesGet**](AuthApi.md#scopesGet) | **GET** /scopes | Scopes
[**verifyPost**](AuthApi.md#verifyPost) | **POST** /verify | Verify token and return details of the owning user



## credentialsGet

> [Credential] credentialsGet()

List the credentials associated with the authenticated user.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.AuthApi();
apiInstance.credentialsGet((error, data, response) => {
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

[**[Credential]**](Credential.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scopesGet

> [String] scopesGet()

Scopes

List available token scopes

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.AuthApi();
apiInstance.scopesGet((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## verifyPost

> Authority verifyPost()

Verify token and return details of the owning user

### Example

```javascript
import Contribly from 'contribly';
let defaultClient = Contribly.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Contribly.AuthApi();
apiInstance.verifyPost((error, data, response) => {
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

[**Authority**](Authority.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

