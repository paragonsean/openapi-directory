# OpenChannelMarketApi.TransactionsFindPaymentsAndRefundsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactionsGet**](TransactionsFindPaymentsAndRefundsApi.md#transactionsGet) | **GET** /transactions | Returns a paginated list of transactions
[**transactionsTransactionIdDelete**](TransactionsFindPaymentsAndRefundsApi.md#transactionsTransactionIdDelete) | **DELETE** /transactions/{transactionId} | Deleted a transaction
[**transactionsTransactionIdGet**](TransactionsFindPaymentsAndRefundsApi.md#transactionsTransactionIdGet) | **GET** /transactions/{transactionId} | Returns a transaction
[**transactionsTransactionIdPost**](TransactionsFindPaymentsAndRefundsApi.md#transactionsTransactionIdPost) | **POST** /transactions/{transactionId} | Updates a transaction



## transactionsGet

> TransactionPages transactionsGet(opts)

Returns a paginated list of transactions

- Results are paginated and the default is value is 100 if no limit is provided 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.TransactionsFindPaymentsAndRefundsApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'userId':'1'} matches all the transactions that have the userId '1'.
  'sort': "sort_example", // String | A sort document. Example: {'date':1} sorts the results by total in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56 // Number | The maximum number of results to return per page
};
apiInstance.transactionsGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;userId&#39;:&#39;1&#39;} matches all the transactions that have the userId &#39;1&#39;. | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;date&#39;:1} sorts the results by total in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 

### Return type

[**TransactionPages**](TransactionPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## transactionsTransactionIdDelete

> transactionsTransactionIdDelete(transactionId)

Deleted a transaction

- Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.TransactionsFindPaymentsAndRefundsApi();
let transactionId = "transactionId_example"; // String | The id of the transaction to be deleted
apiInstance.transactionsTransactionIdDelete(transactionId, (error, data, response) => {
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
 **transactionId** | **String**| The id of the transaction to be deleted | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## transactionsTransactionIdGet

> transactionsTransactionIdGet(transactionId)

Returns a transaction

- Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.TransactionsFindPaymentsAndRefundsApi();
let transactionId = "transactionId_example"; // String | The id of the transaction to return
apiInstance.transactionsTransactionIdGet(transactionId, (error, data, response) => {
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
 **transactionId** | **String**| The id of the transaction to return | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## transactionsTransactionIdPost

> Transaction transactionsTransactionIdPost(transactionId, opts)

Updates a transaction

- Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.TransactionsFindPaymentsAndRefundsApi();
let transactionId = "transactionId_example"; // String | The id of the transaction to be updated
let opts = {
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.transactionsTransactionIdPost(transactionId, opts, (error, data, response) => {
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
 **transactionId** | **String**| The id of the transaction to be updated | 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

