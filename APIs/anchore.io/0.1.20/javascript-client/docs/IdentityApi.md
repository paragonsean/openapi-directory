# AnchoreEngineApiServer.IdentityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCredential**](IdentityApi.md#addCredential) | **POST** /user/credentials | add/replace credential
[**getCredentials**](IdentityApi.md#getCredentials) | **GET** /user/credentials | Get current credential summary
[**getUser**](IdentityApi.md#getUser) | **GET** /user | List authenticated user info
[**getUsersAccount**](IdentityApi.md#getUsersAccount) | **GET** /account | List the account for the authenticated user



## addCredential

> User addCredential(accessCredential)

add/replace credential

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.IdentityApi();
let accessCredential = new AnchoreEngineApiServer.AccessCredential(); // AccessCredential | 
apiInstance.addCredential(accessCredential, (error, data, response) => {
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
 **accessCredential** | [**AccessCredential**](AccessCredential.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCredentials

> [AccessCredential] getCredentials()

Get current credential summary

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.IdentityApi();
apiInstance.getCredentials((error, data, response) => {
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

[**[AccessCredential]**](AccessCredential.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> User getUser()

List authenticated user info

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.IdentityApi();
apiInstance.getUser((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersAccount

> Account getUsersAccount()

List the account for the authenticated user

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.IdentityApi();
apiInstance.getUsersAccount((error, data, response) => {
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

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

