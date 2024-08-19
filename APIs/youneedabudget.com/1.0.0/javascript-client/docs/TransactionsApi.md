# YnabApiEndpoints.TransactionsApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTransaction**](TransactionsApi.md#createTransaction) | **POST** /budgets/{budget_id}/transactions | Create a single transaction or multiple transactions
[**deleteTransaction**](TransactionsApi.md#deleteTransaction) | **DELETE** /budgets/{budget_id}/transactions/{transaction_id} | Deletes an existing transaction
[**getTransactionById**](TransactionsApi.md#getTransactionById) | **GET** /budgets/{budget_id}/transactions/{transaction_id} | Single transaction
[**getTransactions**](TransactionsApi.md#getTransactions) | **GET** /budgets/{budget_id}/transactions | List transactions
[**getTransactionsByAccount**](TransactionsApi.md#getTransactionsByAccount) | **GET** /budgets/{budget_id}/accounts/{account_id}/transactions | List account transactions
[**getTransactionsByCategory**](TransactionsApi.md#getTransactionsByCategory) | **GET** /budgets/{budget_id}/categories/{category_id}/transactions | List category transactions
[**getTransactionsByPayee**](TransactionsApi.md#getTransactionsByPayee) | **GET** /budgets/{budget_id}/payees/{payee_id}/transactions | List payee transactions
[**importTransactions**](TransactionsApi.md#importTransactions) | **POST** /budgets/{budget_id}/transactions/import | Import transactions
[**updateTransaction**](TransactionsApi.md#updateTransaction) | **PUT** /budgets/{budget_id}/transactions/{transaction_id} | Updates an existing transaction
[**updateTransactions**](TransactionsApi.md#updateTransactions) | **PATCH** /budgets/{budget_id}/transactions | Update multiple transactions



## createTransaction

> SaveTransactionsResponse createTransaction(budgetId, postTransactionsWrapper)

Create a single transaction or multiple transactions

Creates a single transaction or multiple transactions.  If you provide a body containing a &#x60;transaction&#x60; object, a single transaction will be created and if you provide a body containing a &#x60;transactions&#x60; array, multiple transactions will be created.  Scheduled transactions cannot be created on this endpoint.

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let postTransactionsWrapper = new YnabApiEndpoints.PostTransactionsWrapper(); // PostTransactionsWrapper | The transaction or transactions to create.  To create a single transaction you can specify a value for the `transaction` object and to create multiple transactions you can specify an array of `transactions`.  It is expected that you will only provide a value for one of these objects.
apiInstance.createTransaction(budgetId, postTransactionsWrapper, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **postTransactionsWrapper** | [**PostTransactionsWrapper**](PostTransactionsWrapper.md)| The transaction or transactions to create.  To create a single transaction you can specify a value for the &#x60;transaction&#x60; object and to create multiple transactions you can specify an array of &#x60;transactions&#x60;.  It is expected that you will only provide a value for one of these objects. | 

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTransaction

> TransactionResponse deleteTransaction(budgetId, transactionId)

Deletes an existing transaction

Deletes a transaction

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let transactionId = "transactionId_example"; // String | The id of the transaction
apiInstance.deleteTransaction(budgetId, transactionId, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **transactionId** | **String**| The id of the transaction | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionById

> TransactionResponse getTransactionById(budgetId, transactionId)

Single transaction

Returns a single transaction

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let transactionId = "transactionId_example"; // String | The id of the transaction
apiInstance.getTransactionById(budgetId, transactionId, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **transactionId** | **String**| The id of the transaction | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactions

> TransactionsResponse getTransactions(budgetId, opts)

List transactions

Returns budget transactions

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let opts = {
  'sinceDate': new Date("2013-10-20"), // Date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).
  'type': "type_example", // String | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported.
  'lastKnowledgeOfServer': 789 // Number | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
};
apiInstance.getTransactions(budgetId, opts, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **sinceDate** | **Date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **String**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **lastKnowledgeOfServer** | **Number**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionsByAccount

> TransactionsResponse getTransactionsByAccount(budgetId, accountId, opts)

List account transactions

Returns all transactions for a specified account

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let accountId = "accountId_example"; // String | The id of the account
let opts = {
  'sinceDate': new Date("2013-10-20"), // Date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).
  'type': "type_example", // String | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported.
  'lastKnowledgeOfServer': 789 // Number | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
};
apiInstance.getTransactionsByAccount(budgetId, accountId, opts, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **accountId** | **String**| The id of the account | 
 **sinceDate** | **Date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **String**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **lastKnowledgeOfServer** | **Number**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionsByCategory

> HybridTransactionsResponse getTransactionsByCategory(budgetId, categoryId, opts)

List category transactions

Returns all transactions for a specified category

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let categoryId = "categoryId_example"; // String | The id of the category
let opts = {
  'sinceDate': new Date("2013-10-20"), // Date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).
  'type': "type_example", // String | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported.
  'lastKnowledgeOfServer': 789 // Number | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
};
apiInstance.getTransactionsByCategory(budgetId, categoryId, opts, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **categoryId** | **String**| The id of the category | 
 **sinceDate** | **Date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **String**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **lastKnowledgeOfServer** | **Number**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionsByPayee

> HybridTransactionsResponse getTransactionsByPayee(budgetId, payeeId, opts)

List payee transactions

Returns all transactions for a specified payee

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let payeeId = "payeeId_example"; // String | The id of the payee
let opts = {
  'sinceDate': new Date("2013-10-20"), // Date | If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).
  'type': "type_example", // String | If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported.
  'lastKnowledgeOfServer': 789 // Number | The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.
};
apiInstance.getTransactionsByPayee(budgetId, payeeId, opts, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **payeeId** | **String**| The id of the payee | 
 **sinceDate** | **Date**| If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). | [optional] 
 **type** | **String**| If specified, only transactions of the specified type will be included. \&quot;uncategorized\&quot; and \&quot;unapproved\&quot; are currently supported. | [optional] 
 **lastKnowledgeOfServer** | **Number**| The starting server knowledge.  If provided, only entities that have changed since &#x60;last_knowledge_of_server&#x60; will be included. | [optional] 

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importTransactions

> TransactionsImportResponse importTransactions(budgetId)

Import transactions

Imports available transactions on all linked accounts for the given budget.  Linked accounts allow transactions to be imported directly from a specified financial institution and this endpoint initiates that import.  Sending a request to this endpoint is the equivalent of clicking \&quot;Import\&quot; on each account in the web application or tapping the \&quot;New Transactions\&quot; banner in the mobile applications.  The response for this endpoint contains the transaction ids that have been imported.

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
apiInstance.importTransactions(budgetId, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 

### Return type

[**TransactionsImportResponse**](TransactionsImportResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTransaction

> TransactionResponse updateTransaction(budgetId, transactionId, putTransactionWrapper)

Updates an existing transaction

Updates a single transaction

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let transactionId = "transactionId_example"; // String | The id of the transaction
let putTransactionWrapper = new YnabApiEndpoints.PutTransactionWrapper(); // PutTransactionWrapper | The transaction to update
apiInstance.updateTransaction(budgetId, transactionId, putTransactionWrapper, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **transactionId** | **String**| The id of the transaction | 
 **putTransactionWrapper** | [**PutTransactionWrapper**](PutTransactionWrapper.md)| The transaction to update | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTransactions

> SaveTransactionsResponse updateTransactions(budgetId, patchTransactionsWrapper)

Update multiple transactions

Updates multiple transactions, by &#x60;id&#x60; or &#x60;import_id&#x60;.

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.TransactionsApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let patchTransactionsWrapper = new YnabApiEndpoints.PatchTransactionsWrapper(); // PatchTransactionsWrapper | The transactions to update. Each transaction must have either an `id` or `import_id` specified. If `id` is specified as null an `import_id` value can be provided which will allow transaction(s) to be updated by their `import_id`. If an `id` is specified, it will always be used for lookup.
apiInstance.updateTransactions(budgetId, patchTransactionsWrapper, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **patchTransactionsWrapper** | [**PatchTransactionsWrapper**](PatchTransactionsWrapper.md)| The transactions to update. Each transaction must have either an &#x60;id&#x60; or &#x60;import_id&#x60; specified. If &#x60;id&#x60; is specified as null an &#x60;import_id&#x60; value can be provided which will allow transaction(s) to be updated by their &#x60;import_id&#x60;. If an &#x60;id&#x60; is specified, it will always be used for lookup. | 

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

