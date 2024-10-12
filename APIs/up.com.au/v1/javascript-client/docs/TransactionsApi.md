# UpApi.TransactionsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsAccountIdTransactionsGet**](TransactionsApi.md#accountsAccountIdTransactionsGet) | **GET** /accounts/{accountId}/transactions | List transactions by account
[**transactionsGet**](TransactionsApi.md#transactionsGet) | **GET** /transactions | List transactions
[**transactionsIdGet**](TransactionsApi.md#transactionsIdGet) | **GET** /transactions/{id} | Retrieve transaction



## accountsAccountIdTransactionsGet

> ListTransactionsResponse accountsAccountIdTransactionsGet(accountId, opts)

List transactions by account

Retrieve a list of all transactions for a specific account. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. To narrow the results to a specific date range pass one or both of &#x60;filter[since]&#x60; and &#x60;filter[until]&#x60; in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.TransactionsApi();
let accountId = "b5544658-4bbd-4eb1-8f63-a9909e0f564b"; // String | The unique identifier for the account. 
let opts = {
  'pageSize': 30, // Number | The number of records to return in each page. 
  'filterStatus': new UpApi.TransactionStatusEnum(), // TransactionStatusEnum | The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`. 
  'filterSince': new Date("2020-01-01T01:02:03+10:00"), // Date | The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
  'filterUntil': new Date("2020-02-01T01:02:03+10:00"), // Date | The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
  'filterCategory': "good-life", // String | The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response. 
  'filterTag': "Holiday" // String | A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given. 
};
apiInstance.accountsAccountIdTransactionsGet(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**| The unique identifier for the account.  | 
 **pageSize** | **Number**| The number of records to return in each page.  | [optional] 
 **filterStatus** | [**TransactionStatusEnum**](.md)| The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;.  | [optional] 
 **filterSince** | **Date**| The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filterUntil** | **Date**| The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filterCategory** | **String**| The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 
 **filterTag** | **String**| A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  | [optional] 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsGet

> ListTransactionsResponse transactionsGet(opts)

List transactions

Retrieve a list of all transactions across all accounts for the currently authenticated user. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. To narrow the results to a specific date range pass one or both of &#x60;filter[since]&#x60; and &#x60;filter[until]&#x60; in the query string. These filter parameters **should not** be used for pagination. Results are ordered newest first to oldest last. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.TransactionsApi();
let opts = {
  'pageSize': 30, // Number | The number of records to return in each page. 
  'filterStatus': new UpApi.TransactionStatusEnum(), // TransactionStatusEnum | The transaction status for which to return records. This can be used to filter `HELD` transactions from those that are `SETTLED`. 
  'filterSince': new Date("2020-01-01T01:02:03+10:00"), // Date | The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
  'filterUntil': new Date("2020-02-01T01:02:03+10:00"), // Date | The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes. 
  'filterCategory': "good-life", // String | The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a `404` response. 
  'filterTag': "Holiday" // String | A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given. 
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
 **pageSize** | **Number**| The number of records to return in each page.  | [optional] 
 **filterStatus** | [**TransactionStatusEnum**](.md)| The transaction status for which to return records. This can be used to filter &#x60;HELD&#x60; transactions from those that are &#x60;SETTLED&#x60;.  | [optional] 
 **filterSince** | **Date**| The start date-time from which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filterUntil** | **Date**| The end date-time up to which to return records, formatted according to rfc-3339. Not to be used for pagination purposes.  | [optional] 
 **filterCategory** | **String**| The category identifier for which to filter transactions. Both parent and child categories can be filtered through this parameter. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 
 **filterTag** | **String**| A transaction tag to filter for which to return records. If the tag does not exist, zero records are returned and a success response is given.  | [optional] 

### Return type

[**ListTransactionsResponse**](ListTransactionsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsIdGet

> GetTransactionResponse transactionsIdGet(id)

Retrieve transaction

Retrieve a specific transaction by providing its unique identifier. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.TransactionsApi();
let id = "7a9d19f9-106c-4e29-8591-52fc5d8f09c5"; // String | The unique identifier for the transaction. 
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
 **id** | **String**| The unique identifier for the transaction.  | 

### Return type

[**GetTransactionResponse**](GetTransactionResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

