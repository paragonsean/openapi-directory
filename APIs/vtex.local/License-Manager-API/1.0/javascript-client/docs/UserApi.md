# LicenseManagerApi.UserApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUser**](UserApi.md#createUser) | **POST** /api/license-manager/users | Create User
[**getListUsers**](UserApi.md#getListUsers) | **GET** /api/license-manager/site/pvt/logins/list/paged | Get List of Users
[**getUser**](UserApi.md#getUser) | **GET** /api/license-manager/users/{userId} | Get User



## createUser

> CreateUser200Response createUser(createUserRequest)

Create User

Allows you to create a user by providing an email (mandatory) and name (optional). The email must be in a valid format. The success response will contain the generated &#x60;userId&#x60; for that user.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LicenseManagerApi.UserApi();
let createUserRequest = {"email":"mynewuser@mydomain.com","name":"My New User Name"}; // CreateUserRequest | 
apiInstance.createUser(createUserRequest, (error, data, response) => {
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
 **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | 

### Return type

[**CreateUser200Response**](CreateUser200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getListUsers

> ListUsersResponse getListUsers(contentType, opts)

Get List of Users

Returns a list of registered users. The response is divided in pages. The query parameter &#x60;numItems&#x60; defines the number of items in each page, and consequently the amount of pages for the whole list.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LicenseManagerApi.UserApi();
let contentType = "'application/json'"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
let opts = {
  'numItems': 10, // Number | Number of items in the returned page
  'pageNumber': 1, // Number | Which page from the whole list will be returned
  'sort': "'name'", // String | Chooses the field that the list will be sorted by
  'sortType': "'ASC'" // String | Defines the sorting order. `ASC` is used for ascendant order. `DSC` is used for descendant order
};
apiInstance.getListUsers(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | [default to &#39;application/json&#39;]
 **numItems** | **Number**| Number of items in the returned page | [optional] [default to 10]
 **pageNumber** | **Number**| Which page from the whole list will be returned | [optional] [default to 1]
 **sort** | **String**| Chooses the field that the list will be sorted by | [optional] [default to &#39;name&#39;]
 **sortType** | **String**| Defines the sorting order. &#x60;ASC&#x60; is used for ascendant order. &#x60;DSC&#x60; is used for descendant order | [optional] [default to &#39;ASC&#39;]

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> CreateUser200Response getUser(contentType, userId)

Get User

Allows you to get a user from the database, using the &#x60;userId&#x60; as the identifier.

### Example

```javascript
import LicenseManagerApi from 'license_manager_api';
let defaultClient = LicenseManagerApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LicenseManagerApi.UserApi();
let contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
let userId = "userId_example"; // String | ID from queried user.
apiInstance.getUser(contentType, userId, (error, data, response) => {
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
 **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | 
 **userId** | **String**| ID from queried user. | 

### Return type

[**CreateUser200Response**](CreateUser200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

