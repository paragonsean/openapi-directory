# EnodeApi.UserManagementApi

All URIs are relative to *https://api.test.enode.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUsersUserid**](UserManagementApi.md#deleteUsersUserid) | **DELETE** /users/{userId} | Unlink User
[**deleteUsersUseridAuthorization**](UserManagementApi.md#deleteUsersUseridAuthorization) | **DELETE** /users/{userId}/authorization | Deauthorize User
[**postUsersUseridLink**](UserManagementApi.md#postUsersUseridLink) | **POST** /users/{userId}/link | Link User



## deleteUsersUserid

> deleteUsersUserid(userId)

Unlink User

Deletes a User and all of their data permanently, and invalidates any associated sessions, authorization codes, and access/refresh tokens

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ClientAccessToken
let ClientAccessToken = defaultClient.authentications['ClientAccessToken'];
ClientAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.UserManagementApi();
let userId = "userId_example"; // String | ID of the User
apiInstance.deleteUsersUserid(userId, (error, data, response) => {
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
 **userId** | **String**| ID of the User | 

### Return type

null (empty response body)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUsersUseridAuthorization

> deleteUsersUseridAuthorization(userId)

Deauthorize User

Deletes the User&#39;s stored vendor authorizations and credentials, invalidates any associated sessions, authorization codes, and access/refresh tokens.  All other User data is retained, and if the User is sent through the Link User flow in the future their account will be just as they left it.  No webhook events will be generated for a deauthorized user.

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ClientAccessToken
let ClientAccessToken = defaultClient.authentications['ClientAccessToken'];
ClientAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.UserManagementApi();
let userId = "userId_example"; // String | ID of the User
apiInstance.deleteUsersUseridAuthorization(userId, (error, data, response) => {
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
 **userId** | **String**| ID of the User | 

### Return type

null (empty response body)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUsersUseridLink

> PostUsersUseridLink200Response postUsersUseridLink(userId, opts)

Link User

Creates an Enode Link session attached to the provided User ID. If this User does not exist, it will be created. The returned &#x60;linkState&#x60; gives the user short-lived access to Enode Link.

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ClientAccessToken
let ClientAccessToken = defaultClient.authentications['ClientAccessToken'];
ClientAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.UserManagementApi();
let userId = "userId_example"; // String | ID of the User
let opts = {
  'postUsersUseridLinkRequest': new EnodeApi.PostUsersUseridLinkRequest() // PostUsersUseridLinkRequest | 
};
apiInstance.postUsersUseridLink(userId, opts, (error, data, response) => {
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
 **userId** | **String**| ID of the User | 
 **postUsersUseridLinkRequest** | [**PostUsersUseridLinkRequest**](PostUsersUseridLinkRequest.md)|  | [optional] 

### Return type

[**PostUsersUseridLink200Response**](PostUsersUseridLink200Response.md)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

