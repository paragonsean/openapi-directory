# AnchoreEngineApiServer.UserManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccount**](UserManagementApi.md#createAccount) | **POST** /accounts | Create a new user. Only avaialble to admin user.
[**createUser**](UserManagementApi.md#createUser) | **POST** /accounts/{accountname}/users | Create a new user
[**createUserCredential**](UserManagementApi.md#createUserCredential) | **POST** /accounts/{accountname}/users/{username}/credentials | add/replace credential
[**deleteAccount**](UserManagementApi.md#deleteAccount) | **DELETE** /accounts/{accountname} | Delete the specified account, only allowed if the account is in the disabled state. All users will be deleted along with the account and all resources will be garbage collected
[**deleteUser**](UserManagementApi.md#deleteUser) | **DELETE** /accounts/{accountname}/users/{username} | Delete a specific user credential by username of the credential. Cannot be the credential used to authenticate the request.
[**deleteUserCredential**](UserManagementApi.md#deleteUserCredential) | **DELETE** /accounts/{accountname}/users/{username}/credentials | Delete a credential by type
[**getAccount**](UserManagementApi.md#getAccount) | **GET** /accounts/{accountname} | Get info about an user. Only available to admin user. Uses the main user Id, not a username.
[**getAccountUser**](UserManagementApi.md#getAccountUser) | **GET** /accounts/{accountname}/users/{username} | Get a specific user in the specified account
[**listAccounts**](UserManagementApi.md#listAccounts) | **GET** /accounts | List user summaries. Only available to the system admin user.
[**listUserCredentials**](UserManagementApi.md#listUserCredentials) | **GET** /accounts/{accountname}/users/{username}/credentials | Get current credential summary
[**listUsers**](UserManagementApi.md#listUsers) | **GET** /accounts/{accountname}/users | List accounts for the user
[**updateAccountState**](UserManagementApi.md#updateAccountState) | **PUT** /accounts/{accountname}/state | Update the state of an account to either enabled or disabled. For deletion use the DELETE route



## createAccount

> Account createAccount(accountCreationRequest)

Create a new user. Only avaialble to admin user.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountCreationRequest = new AnchoreEngineApiServer.AccountCreationRequest(); // AccountCreationRequest | 
apiInstance.createAccount(accountCreationRequest, (error, data, response) => {
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
 **accountCreationRequest** | [**AccountCreationRequest**](AccountCreationRequest.md)|  | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUser

> User createUser(accountname, userCreationRequest)

Create a new user

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
let userCreationRequest = new AnchoreEngineApiServer.UserCreationRequest(); // UserCreationRequest | 
apiInstance.createUser(accountname, userCreationRequest, (error, data, response) => {
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
 **accountname** | **String**|  | 
 **userCreationRequest** | [**UserCreationRequest**](UserCreationRequest.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUserCredential

> User createUserCredential(accountname, username, accessCredential)

add/replace credential

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
let username = "username_example"; // String | 
let accessCredential = new AnchoreEngineApiServer.AccessCredential(); // AccessCredential | 
apiInstance.createUserCredential(accountname, username, accessCredential, (error, data, response) => {
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
 **accountname** | **String**|  | 
 **username** | **String**|  | 
 **accessCredential** | [**AccessCredential**](AccessCredential.md)|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccount

> deleteAccount(accountname)

Delete the specified account, only allowed if the account is in the disabled state. All users will be deleted along with the account and all resources will be garbage collected

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
apiInstance.deleteAccount(accountname, (error, data, response) => {
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
 **accountname** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUser

> deleteUser(accountname, username)

Delete a specific user credential by username of the credential. Cannot be the credential used to authenticate the request.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
let username = "username_example"; // String | 
apiInstance.deleteUser(accountname, username, (error, data, response) => {
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
 **accountname** | **String**|  | 
 **username** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUserCredential

> deleteUserCredential(accountname, username, credentialType)

Delete a credential by type

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
let username = "username_example"; // String | 
let credentialType = "credentialType_example"; // String | 
apiInstance.deleteUserCredential(accountname, username, credentialType, (error, data, response) => {
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
 **accountname** | **String**|  | 
 **username** | **String**|  | 
 **credentialType** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccount

> Account getAccount(accountname)

Get info about an user. Only available to admin user. Uses the main user Id, not a username.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
apiInstance.getAccount(accountname, (error, data, response) => {
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
 **accountname** | **String**|  | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountUser

> User getAccountUser(accountname, username)

Get a specific user in the specified account

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
let username = "username_example"; // String | 
apiInstance.getAccountUser(accountname, username, (error, data, response) => {
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
 **accountname** | **String**|  | 
 **username** | **String**|  | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccounts

> [Account] listAccounts(opts)

List user summaries. Only available to the system admin user.

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let opts = {
  'state': "state_example" // String | Filter accounts by state
};
apiInstance.listAccounts(opts, (error, data, response) => {
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
 **state** | **String**| Filter accounts by state | [optional] 

### Return type

[**[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserCredentials

> [AccessCredential] listUserCredentials(accountname, username)

Get current credential summary

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
let username = "username_example"; // String | 
apiInstance.listUserCredentials(accountname, username, (error, data, response) => {
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
 **accountname** | **String**|  | 
 **username** | **String**|  | 

### Return type

[**[AccessCredential]**](AccessCredential.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsers

> [User] listUsers(accountname)

List accounts for the user

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
apiInstance.listUsers(accountname, (error, data, response) => {
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
 **accountname** | **String**|  | 

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccountState

> AccountStatus updateAccountState(accountname, accountStatus)

Update the state of an account to either enabled or disabled. For deletion use the DELETE route

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.UserManagementApi();
let accountname = "accountname_example"; // String | 
let accountStatus = new AnchoreEngineApiServer.AccountStatus(); // AccountStatus | 
apiInstance.updateAccountState(accountname, accountStatus, (error, data, response) => {
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
 **accountname** | **String**|  | 
 **accountStatus** | [**AccountStatus**](AccountStatus.md)|  | 

### Return type

[**AccountStatus**](AccountStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

