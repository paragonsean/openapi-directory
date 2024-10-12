# RedirectionIo.UserApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirmNewEmailUserItem**](UserApi.md#confirmNewEmailUserItem) | **GET** /users/{id}/confirm-new-email/{newEmailToken} | Retrieves a User resource.
[**deleteUserItem**](UserApi.md#deleteUserItem) | **DELETE** /users/{id} | Removes the User resource.
[**editEmailUserItem**](UserApi.md#editEmailUserItem) | **PUT** /users/{id}/edit-email | Replaces the User resource.
[**editInfoUserItem**](UserApi.md#editInfoUserItem) | **PUT** /users/{id}/edit-info | Replaces the User resource.
[**editPasswordUserItem**](UserApi.md#editPasswordUserItem) | **PUT** /users/{id}/edit-password | Replaces the User resource.
[**forgotPasswordUserItem**](UserApi.md#forgotPasswordUserItem) | **PUT** /users/forgot-password/{resetToken} | Replaces the User resource.
[**getUserCollection**](UserApi.md#getUserCollection) | **GET** /users | Retrieves the collection of User resources.
[**getUserItem**](UserApi.md#getUserItem) | **GET** /users/{id} | Retrieves a User resource.
[**postUserCollection**](UserApi.md#postUserCollection) | **POST** /users | Creates a User resource.



## confirmNewEmailUserItem

> UserRead confirmNewEmailUserItem(id, newEmailToken)

Retrieves a User resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let id = "id_example"; // String | 
let newEmailToken = "newEmailToken_example"; // String | 
apiInstance.confirmNewEmailUserItem(id, newEmailToken, (error, data, response) => {
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
 **id** | **String**|  | 
 **newEmailToken** | **String**|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## deleteUserItem

> deleteUserItem(id)

Removes the User resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let id = "id_example"; // String | 
apiInstance.deleteUserItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## editEmailUserItem

> UserRead editEmailUserItem(id, opts)

Replaces the User resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let id = "id_example"; // String | 
let opts = {
  'user': new RedirectionIo.UserEditInfo() // UserEditInfo | The updated User resource
};
apiInstance.editEmailUserItem(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **user** | [**UserEditInfo**](UserEditInfo.md)| The updated User resource | [optional] 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## editInfoUserItem

> UserRead editInfoUserItem(id, opts)

Replaces the User resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let id = "id_example"; // String | 
let opts = {
  'user': new RedirectionIo.UserEditInfo() // UserEditInfo | The updated User resource
};
apiInstance.editInfoUserItem(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **user** | [**UserEditInfo**](UserEditInfo.md)| The updated User resource | [optional] 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## editPasswordUserItem

> UserRead editPasswordUserItem(id, opts)

Replaces the User resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let id = "id_example"; // String | 
let opts = {
  'user': new RedirectionIo.UserEditInfo() // UserEditInfo | The updated User resource
};
apiInstance.editPasswordUserItem(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **user** | [**UserEditInfo**](UserEditInfo.md)| The updated User resource | [optional] 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## forgotPasswordUserItem

> UserRead forgotPasswordUserItem(resetToken, opts)

Replaces the User resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let resetToken = "resetToken_example"; // String | 
let opts = {
  'user': new RedirectionIo.UserPassword() // UserPassword | The updated User resource
};
apiInstance.forgotPasswordUserItem(resetToken, opts, (error, data, response) => {
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
 **resetToken** | **String**|  | 
 **user** | [**UserPassword**](UserPassword.md)| The updated User resource | [optional] 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getUserCollection

> [UserList] getUserCollection(organizationId, opts)

Retrieves the collection of User resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'search': "search_example" // String | 
};
apiInstance.getUserCollection(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **search** | **String**|  | [optional] 

### Return type

[**[UserList]**](UserList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getUserItem

> UserRead getUserItem(id)

Retrieves a User resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let id = "id_example"; // String | 
apiInstance.getUserItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## postUserCollection

> UserRead postUserCollection(opts)

Creates a User resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.UserApi();
let opts = {
  'user': new RedirectionIo.UserCreationWrite() // UserCreationWrite | The new User resource
};
apiInstance.postUserCollection(opts, (error, data, response) => {
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
 **user** | [**UserCreationWrite**](UserCreationWrite.md)| The new User resource | [optional] 

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/ld+json, application/json, text/html, text/csv
- **Accept**: application/ld+json, application/json, text/html, text/csv

