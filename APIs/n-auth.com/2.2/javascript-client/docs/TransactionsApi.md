# NextAuthApi.TransactionsApi

All URIs are relative to *https://api.nextauth.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTransaction**](TransactionsApi.md#createTransaction) | **POST** /servers/{serverid}/sessions/transactions | Create a transaction to be approved within the current session.
[**getTransactionResult**](TransactionsApi.md#getTransactionResult) | **GET** /servers/{serverid}/transactions/{transactionid} | Get transaction result for a given transaction.



## createTransaction

> TransactionId createTransaction(serverid, xNonce, msg)

Create a transaction to be approved within the current session.

Create a transaction for approval within the current session. Required permission: &#39;sessions&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.TransactionsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
let msg = new NextAuthApi.Transaction(); // Transaction | 
apiInstance.createTransaction(serverid, xNonce, msg, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **xNonce** | **String**| Nonce to identify the browser/webserver session | 
 **msg** | [**Transaction**](Transaction.md)|  | 

### Return type

[**TransactionId**](TransactionId.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionResult

> TransactionResult getTransactionResult(serverid, transactionid)

Get transaction result for a given transaction.

Get transaction result for a given transaction id. Required permission: &#39;sessions&#39;.

### Example

```javascript
import NextAuthApi from 'next_auth_api';
let defaultClient = NextAuthApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: role_id
let role_id = defaultClient.authentications['role_id'];
role_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//role_id.apiKeyPrefix = 'Token';

let apiInstance = new NextAuthApi.TransactionsApi();
let serverid = "serverid_example"; // String | Base64 encoded server id
let transactionid = "transactionid_example"; // String | Base64 encoded transaction id
apiInstance.getTransactionResult(serverid, transactionid, (error, data, response) => {
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
 **serverid** | **String**| Base64 encoded server id | 
 **transactionid** | **String**| Base64 encoded transaction id | 

### Return type

[**TransactionResult**](TransactionResult.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

