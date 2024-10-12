# PocketSmith.AccountsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsIdDelete**](AccountsApi.md#accountsIdDelete) | **DELETE** /accounts/{id} | Delete account
[**accountsIdGet**](AccountsApi.md#accountsIdGet) | **GET** /accounts/{id} | Get account
[**accountsIdPut**](AccountsApi.md#accountsIdPut) | **PUT** /accounts/{id} | Update account
[**institutionsIdAccountsGet**](AccountsApi.md#institutionsIdAccountsGet) | **GET** /institutions/{id}/accounts | List accounts in institution
[**usersIdAccountsGet**](AccountsApi.md#usersIdAccountsGet) | **GET** /users/{id}/accounts | List accounts in user
[**usersIdAccountsPost**](AccountsApi.md#usersIdAccountsPost) | **POST** /users/{id}/accounts | Create an account in user
[**usersIdAccountsPut**](AccountsApi.md#usersIdAccountsPut) | **PUT** /users/{id}/accounts | Update the display order of accounts in user



## accountsIdDelete

> accountsIdDelete(id)

Delete account

Deletes an account and all its data by ID, optionally merge scenarios into another account.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AccountsApi();
let id = 42; // Number | The unique identifier of the account.
apiInstance.accountsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the account. | 

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsIdGet

> Account accountsIdGet(id)

Get account

Gets an account by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AccountsApi();
let id = 42; // Number | The unique identifier of the account.
apiInstance.accountsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the account. | 

### Return type

[**Account**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsIdPut

> Account accountsIdPut(id, opts)

Update account

Updates and returns an account by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AccountsApi();
let id = 42; // Number | The unique identifier of the account.
let opts = {
  'accountsIdPutRequest': new PocketSmith.AccountsIdPutRequest() // AccountsIdPutRequest | 
};
apiInstance.accountsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the account. | 
 **accountsIdPutRequest** | [**AccountsIdPutRequest**](AccountsIdPutRequest.md)|  | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## institutionsIdAccountsGet

> [Account] institutionsIdAccountsGet(id)

List accounts in institution

Lists accounts belonging to an institution by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AccountsApi();
let id = 42; // Number | The unique identifier of the institution.
apiInstance.institutionsIdAccountsGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the institution. | 

### Return type

[**[Account]**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdAccountsGet

> [Account] usersIdAccountsGet(id)

List accounts in user

Lists all accounts belonging to the user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AccountsApi();
let id = 42; // Number | The unique identifier of the user.
apiInstance.usersIdAccountsGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 

### Return type

[**[Account]**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdAccountsPost

> Account usersIdAccountsPost(id, opts)

Create an account in user

Creates and returns an account belonging to the user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AccountsApi();
let id = 42; // Number | The unique identifier of the user.
let opts = {
  'usersIdAccountsPostRequest': new PocketSmith.UsersIdAccountsPostRequest() // UsersIdAccountsPostRequest | 
};
apiInstance.usersIdAccountsPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 
 **usersIdAccountsPostRequest** | [**UsersIdAccountsPostRequest**](UsersIdAccountsPostRequest.md)|  | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersIdAccountsPut

> [Account] usersIdAccountsPut(id, opts)

Update the display order of accounts in user

Updates the display order of accounts belonging to the user, by accepting an array of accounts in their new display order.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.AccountsApi();
let id = 42; // Number | The unique identifier of the user.
let opts = {
  'usersIdAccountsPutRequest': new PocketSmith.UsersIdAccountsPutRequest() // UsersIdAccountsPutRequest | 
};
apiInstance.usersIdAccountsPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 
 **usersIdAccountsPutRequest** | [**UsersIdAccountsPutRequest**](UsersIdAccountsPutRequest.md)|  | [optional] 

### Return type

[**[Account]**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

