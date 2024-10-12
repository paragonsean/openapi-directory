# PocketSmith.TransactionAccountsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactionAccountsIdGet**](TransactionAccountsApi.md#transactionAccountsIdGet) | **GET** /transaction_accounts/{id} | Get transaction account
[**transactionAccountsIdPut**](TransactionAccountsApi.md#transactionAccountsIdPut) | **PUT** /transaction_accounts/{id} | Update transaction account
[**usersIdTransactionAccountsGet**](TransactionAccountsApi.md#usersIdTransactionAccountsGet) | **GET** /users/{id}/transaction_accounts | List transaction accounts in user



## transactionAccountsIdGet

> TransactionAccount transactionAccountsIdGet(id)

Get transaction account

Gets a transaction account by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionAccountsApi();
let id = 42; // Number | The unique identifier of the transaction account.
apiInstance.transactionAccountsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the transaction account. | 

### Return type

[**TransactionAccount**](TransactionAccount.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionAccountsIdPut

> TransactionAccount transactionAccountsIdPut(id, opts)

Update transaction account

Updates the transaction account by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionAccountsApi();
let id = 42; // Number | The unique identifier of the transaction account.
let opts = {
  'transactionAccountsIdPutRequest': new PocketSmith.TransactionAccountsIdPutRequest() // TransactionAccountsIdPutRequest | 
};
apiInstance.transactionAccountsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the transaction account. | 
 **transactionAccountsIdPutRequest** | [**TransactionAccountsIdPutRequest**](TransactionAccountsIdPutRequest.md)|  | [optional] 

### Return type

[**TransactionAccount**](TransactionAccount.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersIdTransactionAccountsGet

> [TransactionAccount] usersIdTransactionAccountsGet(id)

List transaction accounts in user

List all transaction accounts belonging to a user.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionAccountsApi();
let id = 42; // Number | The unique identifier of the user.
apiInstance.usersIdTransactionAccountsGet(id, (error, data, response) => {
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

[**[TransactionAccount]**](TransactionAccount.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

