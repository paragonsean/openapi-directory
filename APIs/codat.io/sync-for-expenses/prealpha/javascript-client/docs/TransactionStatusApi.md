# CodatExpenseApi.TransactionStatusApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSyncTransaction**](TransactionStatusApi.md#getSyncTransaction) | **GET** /companies/{companyId}/sync/expenses/syncs/{syncId}/transactions/{transactionId} | Get Sync Transaction
[**listSyncTransactions**](TransactionStatusApi.md#listSyncTransactions) | **GET** /companies/{companyId}/sync/expenses/syncs/{syncId}/transactions | Get Sync transactions



## getSyncTransaction

> [TransactionMetadata] getSyncTransaction(companyId, syncId, transactionId)

Get Sync Transaction

Gets the status of a transaction for a sync

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.TransactionStatusApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let syncId = "6fb40d5e-b13e-11ed-afa1-0242ac120002"; // String | Unique identifier for a sync.
let transactionId = "336694d8-2dca-4cb5-a28d-3ccb83e55eee"; // String | The unique identifier for your SMB's transaction.
apiInstance.getSyncTransaction(companyId, syncId, transactionId, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **syncId** | **String**| Unique identifier for a sync. | 
 **transactionId** | **String**| The unique identifier for your SMB&#39;s transaction. | 

### Return type

[**[TransactionMetadata]**](TransactionMetadata.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncTransactions

> TransactionMetadataList listSyncTransactions(companyId, syncId, page, opts)

Get Sync transactions

Get&#39;s the transactions and status for a sync

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.TransactionStatusApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let syncId = "6fb40d5e-b13e-11ed-afa1-0242ac120002"; // String | Unique identifier for a sync.
let page = 1; // Number | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
let opts = {
  'pageSize': 100 // Number | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
};
apiInstance.listSyncTransactions(companyId, syncId, page, opts, (error, data, response) => {
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
 **companyId** | **String**|  | 
 **syncId** | **String**| Unique identifier for a sync. | 
 **page** | **Number**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1]
 **pageSize** | **Number**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]

### Return type

[**TransactionMetadataList**](TransactionMetadataList.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

