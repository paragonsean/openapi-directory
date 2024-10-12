# DeveloperDocumentation.AccountsApi

All URIs are relative to *https://api.journy.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addUserToAccount**](AccountsApi.md#addUserToAccount) | **POST** /accounts/users/add | Add users to an account
[**deleteAccount**](AccountsApi.md#deleteAccount) | **DELETE** /accounts | Delete account
[**removeUserFromAccount**](AccountsApi.md#removeUserFromAccount) | **POST** /accounts/users/remove | Remove user from account
[**upsertAccount**](AccountsApi.md#upsertAccount) | **POST** /accounts/upsert | Create or update account



## addUserToAccount

> DeleteAccount202Response addUserToAccount(addUserToAccountRequest)

Add users to an account

You can add up to 100 users to an account.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.AccountsApi();
let addUserToAccountRequest = new DeveloperDocumentation.AddUserToAccountRequest(); // AddUserToAccountRequest | 
apiInstance.addUserToAccount(addUserToAccountRequest, (error, data, response) => {
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
 **addUserToAccountRequest** | [**AddUserToAccountRequest**](AddUserToAccountRequest.md)|  | 

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccount

> DeleteAccount202Response deleteAccount(deleteAccountRequest)

Delete account

Endpoint used to delete an account.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.AccountsApi();
let deleteAccountRequest = new DeveloperDocumentation.DeleteAccountRequest(); // DeleteAccountRequest | 
apiInstance.deleteAccount(deleteAccountRequest, (error, data, response) => {
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
 **deleteAccountRequest** | [**DeleteAccountRequest**](DeleteAccountRequest.md)|  | 

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeUserFromAccount

> DeleteAccount202Response removeUserFromAccount(addUserToAccountRequest)

Remove user from account

You can remove up to 100 users from an account.  When removing a user, the user will still be stored in journy.io, but marked as \&quot;removed\&quot;. 

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.AccountsApi();
let addUserToAccountRequest = new DeveloperDocumentation.AddUserToAccountRequest(); // AddUserToAccountRequest | 
apiInstance.removeUserFromAccount(addUserToAccountRequest, (error, data, response) => {
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
 **addUserToAccountRequest** | [**AddUserToAccountRequest**](AddUserToAccountRequest.md)|  | 

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upsertAccount

> UpsertAccount201Response upsertAccount(upsertAccountRequest)

Create or update account

Endpoint used to create or update an account.

### Example

```javascript
import DeveloperDocumentation from 'developer_documentation';

let apiInstance = new DeveloperDocumentation.AccountsApi();
let upsertAccountRequest = new DeveloperDocumentation.UpsertAccountRequest(); // UpsertAccountRequest | 
apiInstance.upsertAccount(upsertAccountRequest, (error, data, response) => {
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
 **upsertAccountRequest** | [**UpsertAccountRequest**](UpsertAccountRequest.md)|  | 

### Return type

[**UpsertAccount201Response**](UpsertAccount201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

