# AccountApi.AccountsApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Account/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCloseAccount**](AccountsApi.md#postCloseAccount) | **POST** /closeAccount | Close an account
[**postCreateAccount**](AccountsApi.md#postCreateAccount) | **POST** /createAccount | Create an account
[**postUpdateAccount**](AccountsApi.md#postUpdateAccount) | **POST** /updateAccount | Update an account



## postCloseAccount

> CloseAccountResponse postCloseAccount(opts)

Close an account

Closes an account. If an account is closed, you cannot process transactions, pay out its funds, or reopen it. If payments are made to a closed account, the payments are sent to your liable account.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountsApi();
let opts = {
  'closeAccountRequest': new AccountApi.CloseAccountRequest() // CloseAccountRequest | 
};
apiInstance.postCloseAccount(opts, (error, data, response) => {
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
 **closeAccountRequest** | [**CloseAccountRequest**](CloseAccountRequest.md)|  | [optional] 

### Return type

[**CloseAccountResponse**](CloseAccountResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCreateAccount

> CreateAccountResponse postCreateAccount(opts)

Create an account

Creates an account under an account holder. An account holder can have [multiple accounts](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#create-additional-accounts).

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountsApi();
let opts = {
  'createAccountRequest': new AccountApi.CreateAccountRequest() // CreateAccountRequest | 
};
apiInstance.postCreateAccount(opts, (error, data, response) => {
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
 **createAccountRequest** | [**CreateAccountRequest**](CreateAccountRequest.md)|  | [optional] 

### Return type

[**CreateAccountResponse**](CreateAccountResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postUpdateAccount

> UpdateAccountResponse postUpdateAccount(opts)

Update an account

Updates the description or payout schedule of an account.

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AccountApi.AccountsApi();
let opts = {
  'updateAccountRequest': new AccountApi.UpdateAccountRequest() // UpdateAccountRequest | 
};
apiInstance.postUpdateAccount(opts, (error, data, response) => {
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
 **updateAccountRequest** | [**UpdateAccountRequest**](UpdateAccountRequest.md)|  | [optional] 

### Return type

[**UpdateAccountResponse**](UpdateAccountResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

