# PocketSmith.TransactionsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsIdTransactionsGet**](TransactionsApi.md#accountsIdTransactionsGet) | **GET** /accounts/{id}/transactions | List transactions in account
[**categoriesIdTransactionsGet**](TransactionsApi.md#categoriesIdTransactionsGet) | **GET** /categories/{id}/transactions | List transactions in categories
[**transactionAccountsIdTransactionsGet**](TransactionsApi.md#transactionAccountsIdTransactionsGet) | **GET** /transaction_accounts/{id}/transactions | List transactions in transaction account
[**transactionAccountsIdTransactionsPost**](TransactionsApi.md#transactionAccountsIdTransactionsPost) | **POST** /transaction_accounts/{id}/transactions | Create a transaction in transaction account
[**transactionsIdDelete**](TransactionsApi.md#transactionsIdDelete) | **DELETE** /transactions/{id} | Delete transaction
[**transactionsIdGet**](TransactionsApi.md#transactionsIdGet) | **GET** /transactions/{id} | Get a transaction
[**transactionsIdPut**](TransactionsApi.md#transactionsIdPut) | **PUT** /transactions/{id} | Update a transaction
[**usersIdTransactionsGet**](TransactionsApi.md#usersIdTransactionsGet) | **GET** /users/{id}/transactions | List transactions in user



## accountsIdTransactionsGet

> [Transaction] accountsIdTransactionsGet(id, opts)

List transactions in account

Lists transactions belonging to an account by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionsApi();
let id = 42; // Number | The unique identifier of the account.
let opts = {
  'startDate': "2016-11-01", // String | Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user's subscription.
  'endDate': "2016-11-30", // String | Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today's date.
  'updatedSince': "2020-10-14T09:20:33+13:00", // String | Limit to transactions updated since an ISO 8601 timestamp.
  'uncategorised': 1, // Number | Limit to uncategorised transactions.
  'type': "debit", // String | Limit to transactions of this type.
  'needsReview': 1, // Number | Limit to transactions that need to be reviewed.
  'search': "Paypal", // String | Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format.
  'page': 3 // Number | Choose a particular page of the results.
};
apiInstance.accountsIdTransactionsGet(id, opts, (error, data, response) => {
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
 **startDate** | **String**| Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user&#39;s subscription. | [optional] 
 **endDate** | **String**| Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today&#39;s date. | [optional] 
 **updatedSince** | **String**| Limit to transactions updated since an ISO 8601 timestamp. | [optional] 
 **uncategorised** | **Number**| Limit to uncategorised transactions. | [optional] 
 **type** | **String**| Limit to transactions of this type. | [optional] 
 **needsReview** | **Number**| Limit to transactions that need to be reviewed. | [optional] 
 **search** | **String**| Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format. | [optional] 
 **page** | **Number**| Choose a particular page of the results. | [optional] 

### Return type

[**[Transaction]**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesIdTransactionsGet

> [Transaction] categoriesIdTransactionsGet(id, opts)

List transactions in categories

Lists transactions belonging to one or more categories by their IDs.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionsApi();
let id = "42,43"; // String | A comma-separated list of category IDs.
let opts = {
  'startDate': "2016-11-01", // String | Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user's subscription.
  'endDate': "2016-11-30", // String | Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today's date.
  'updatedSince': "2020-10-14T09:20:33+13:00", // String | Limit to transactions updated since an ISO 8601 timestamp.
  'uncategorised': 1, // Number | Limit to uncategorised transactions.
  'type': "debit", // String | Limit to transactions of this type.
  'needsReview': 1, // Number | Limit to transactions that need to be reviewed.
  'search': "Paypal", // String | Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format.
  'page': 3 // Number | Choose a particular page of the results.
};
apiInstance.categoriesIdTransactionsGet(id, opts, (error, data, response) => {
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
 **id** | **String**| A comma-separated list of category IDs. | 
 **startDate** | **String**| Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user&#39;s subscription. | [optional] 
 **endDate** | **String**| Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today&#39;s date. | [optional] 
 **updatedSince** | **String**| Limit to transactions updated since an ISO 8601 timestamp. | [optional] 
 **uncategorised** | **Number**| Limit to uncategorised transactions. | [optional] 
 **type** | **String**| Limit to transactions of this type. | [optional] 
 **needsReview** | **Number**| Limit to transactions that need to be reviewed. | [optional] 
 **search** | **String**| Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format. | [optional] 
 **page** | **Number**| Choose a particular page of the results. | [optional] 

### Return type

[**[Transaction]**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionAccountsIdTransactionsGet

> [Transaction] transactionAccountsIdTransactionsGet(id, opts)

List transactions in transaction account

Lists transactions belonging to a transaction account by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionsApi();
let id = 42; // Number | The unique identifier of the transaction account.
let opts = {
  'startDate': "2016-11-01", // String | Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user's subscription.
  'endDate': "2016-11-30", // String | Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today's date.
  'updatedSince': "2020-10-14T09:20:33+13:00", // String | Limit to transactions updated since an ISO 8601 timestamp.
  'uncategorised': 1, // Number | Limit to uncategorised transactions.
  'type': "debit", // String | Limit to transactions of this type.
  'needsReview': 1, // Number | Limit to transactions that need to be reviewed.
  'search': "Paypal", // String | Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format.
  'page': 3 // Number | Choose a particular page of the results.
};
apiInstance.transactionAccountsIdTransactionsGet(id, opts, (error, data, response) => {
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
 **startDate** | **String**| Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user&#39;s subscription. | [optional] 
 **endDate** | **String**| Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today&#39;s date. | [optional] 
 **updatedSince** | **String**| Limit to transactions updated since an ISO 8601 timestamp. | [optional] 
 **uncategorised** | **Number**| Limit to uncategorised transactions. | [optional] 
 **type** | **String**| Limit to transactions of this type. | [optional] 
 **needsReview** | **Number**| Limit to transactions that need to be reviewed. | [optional] 
 **search** | **String**| Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format. | [optional] 
 **page** | **Number**| Choose a particular page of the results. | [optional] 

### Return type

[**[Transaction]**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionAccountsIdTransactionsPost

> Transaction transactionAccountsIdTransactionsPost(id, opts)

Create a transaction in transaction account

Creates a transaction in a transaction account by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionsApi();
let id = 42; // Number | The unique identifier of the transaction account.
let opts = {
  'transactionAccountsIdTransactionsPostRequest': new PocketSmith.TransactionAccountsIdTransactionsPostRequest() // TransactionAccountsIdTransactionsPostRequest | 
};
apiInstance.transactionAccountsIdTransactionsPost(id, opts, (error, data, response) => {
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
 **transactionAccountsIdTransactionsPostRequest** | [**TransactionAccountsIdTransactionsPostRequest**](TransactionAccountsIdTransactionsPostRequest.md)|  | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsIdDelete

> transactionsIdDelete(id)

Delete transaction

Deletes a transaction and all its data by ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionsApi();
let id = 42; // Number | The unique identifier of the transaction.
apiInstance.transactionsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the transaction. | 

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsIdGet

> Transaction transactionsIdGet(id)

Get a transaction

Gets a transaction by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionsApi();
let id = 42; // Number | The unique identifier of the transaction.
apiInstance.transactionsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the transaction. | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsIdPut

> Transaction transactionsIdPut(id, opts)

Update a transaction

Updates a transaction by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionsApi();
let id = 42; // Number | The unique identifier of the transaction.
let opts = {
  'transactionsIdPutRequest': new PocketSmith.TransactionsIdPutRequest() // TransactionsIdPutRequest | 
};
apiInstance.transactionsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the transaction. | 
 **transactionsIdPutRequest** | [**TransactionsIdPutRequest**](TransactionsIdPutRequest.md)|  | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersIdTransactionsGet

> [Transaction] usersIdTransactionsGet(id, opts)

List transactions in user

Lists transactions belonging to a user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.TransactionsApi();
let id = 42; // Number | The unique identifier of the account.
let opts = {
  'startDate': "2016-11-01", // String | Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user's subscription.
  'endDate': "2016-11-30", // String | Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today's date.
  'updatedSince': "2020-10-14T09:20:33+13:00", // String | Limit to transactions updated since an ISO 8601 timestamp.
  'uncategorised': 1, // Number | Limit to uncategorised transactions.
  'type': "debit", // String | Limit to transactions of this type.
  'needsReview': 1, // Number | Limit to transactions that need to be reviewed.
  'search': "Paypal", // String | Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format.
  'page': 3 // Number | Choose a particular page of the results.
};
apiInstance.usersIdTransactionsGet(id, opts, (error, data, response) => {
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
 **startDate** | **String**| Limit to transactions on or after this date. Required if end_date is provided. If not provided, defaults to the furtherest date allowed by the user&#39;s subscription. | [optional] 
 **endDate** | **String**| Limit to transactions on or before this date. Required if start_date is provided. If not provided, defaults to today&#39;s date. | [optional] 
 **updatedSince** | **String**| Limit to transactions updated since an ISO 8601 timestamp. | [optional] 
 **uncategorised** | **Number**| Limit to uncategorised transactions. | [optional] 
 **type** | **String**| Limit to transactions of this type. | [optional] 
 **needsReview** | **Number**| Limit to transactions that need to be reviewed. | [optional] 
 **search** | **String**| Limit to transactions matching a keyword search string. The provided string is matched against the transaction amount, account name, payee, category title, note, labels, and the date in ISO 8601 format. | [optional] 
 **page** | **Number**| Choose a particular page of the results. | [optional] 

### Return type

[**[Transaction]**](Transaction.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

