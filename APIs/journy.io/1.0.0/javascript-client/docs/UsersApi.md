# DeveloperDocumentation.UsersApi

All URIs are relative to *https://api.journy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /users | Delete user
[**link**](UsersApi.md#link) | **POST** /link | Link web activity to user
[**upsertUser**](UsersApi.md#upsertUser) | **POST** /users/upsert | Create or update user



## deleteUser

> DeleteAccount202Response deleteUser(deleteUserRequest)

Delete user

Endpoint to delete a user.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.UsersApi();
let deleteUserRequest = new DeveloperDocumentation.DeleteUserRequest(); // DeleteUserRequest | 
apiInstance.deleteUser(deleteUserRequest, (error, data, response) => {
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
 **deleteUserRequest** | [**DeleteUserRequest**](DeleteUserRequest.md)|  | 

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## link

> DeleteAccount202Response link(linkRequest)

Link web activity to user

💡 You don&#39;t need to use this endpoint if you use our JavaScript snippet in your application.  This endpoint is used to link web activity to a user in your application. This will help you discover which channels and campaigns work best.  When our JavaScript snippet is embedded on your website, blog or landing pages, a cookie named \&quot;__journey\&quot; will be set.  This will only work if your website and application are under the same top level domain.  Website, blog or landing pages * www.my-domain.tld * blog.my-domain.tld * landing-page.my-domain.tld  Application * app.my-domain.tld  The cookie on my-domain.tld will also be send to your app domain.  You should call this endpoint after the user succesfully logged in (so that you know the user&#39;s ID). Use the value of the cookie as device ID.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.UsersApi();
let linkRequest = new DeveloperDocumentation.LinkRequest(); // LinkRequest | 
apiInstance.link(linkRequest, (error, data, response) => {
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
 **linkRequest** | [**LinkRequest**](LinkRequest.md)|  | 

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upsertUser

> UpsertUser201Response upsertUser(upsertUserRequest)

Create or update user

Endpoint to create or update a user.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.UsersApi();
let upsertUserRequest = new DeveloperDocumentation.UpsertUserRequest(); // UpsertUserRequest | 
apiInstance.upsertUser(upsertUserRequest, (error, data, response) => {
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
 **upsertUserRequest** | [**UpsertUserRequest**](UpsertUserRequest.md)|  | 

### Return type

[**UpsertUser201Response**](UpsertUser201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

