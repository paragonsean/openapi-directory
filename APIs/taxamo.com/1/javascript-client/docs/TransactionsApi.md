# Taxamo.TransactionsApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelTransaction**](TransactionsApi.md#cancelTransaction) | **DELETE** /api/v1/transactions/{key} | Delete transaction
[**confirmTransaction**](TransactionsApi.md#confirmTransaction) | **POST** /api/v1/transactions/{key}/confirm | Confirm transaction
[**createTransaction**](TransactionsApi.md#createTransaction) | **POST** /api/v1/transactions | Store transaction
[**getTransaction**](TransactionsApi.md#getTransaction) | **GET** /api/v1/transactions/{key} | Retrieve transaction data.
[**listTransactions**](TransactionsApi.md#listTransactions) | **GET** /api/v1/transactions | Browse transactions
[**unconfirmTransaction**](TransactionsApi.md#unconfirmTransaction) | **POST** /api/v1/transactions/{key}/unconfirm | Un-confirm the transaction
[**updateTransaction**](TransactionsApi.md#updateTransaction) | **PUT** /api/v1/transactions/{key} | Update transaction



## cancelTransaction

> CancelTransactionOut cancelTransaction(key)

Delete transaction

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TransactionsApi();
let key = "key_example"; // String | Transaction key
apiInstance.cancelTransaction(key, (error, data, response) => {
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
 **key** | **String**| Transaction key | 

### Return type

[**CancelTransactionOut**](CancelTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## confirmTransaction

> ConfirmTransactionOut confirmTransaction(key, input)

Confirm transaction

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TransactionsApi();
let key = "key_example"; // String | Transaction key.
let input = new Taxamo.ConfirmTransactionIn(); // ConfirmTransactionIn | Input
apiInstance.confirmTransaction(key, input, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 
 **input** | [**ConfirmTransactionIn**](ConfirmTransactionIn.md)| Input | 

### Return type

[**ConfirmTransactionOut**](ConfirmTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTransaction

> CreateTransactionOut createTransaction(input)

Store transaction

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TransactionsApi();
let input = new Taxamo.CreateTransactionIn(); // CreateTransactionIn | Input
apiInstance.createTransaction(input, (error, data, response) => {
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
 **input** | [**CreateTransactionIn**](CreateTransactionIn.md)| Input | 

### Return type

[**CreateTransactionOut**](CreateTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTransaction

> GetTransactionOut getTransaction(key)

Retrieve transaction data.

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TransactionsApi();
let key = "key_example"; // String | Transaction key
apiInstance.getTransaction(key, (error, data, response) => {
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
 **key** | **String**| Transaction key | 

### Return type

[**GetTransactionOut**](GetTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTransactions

> ListTransactionsOut listTransactions(opts)

Browse transactions

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TransactionsApi();
let opts = {
  'filterText': "filterText_example", // String | Filtering expression
  'offset': 56, // Number | Offset
  'hasNote': true, // Boolean | Return only transactions with a note field set.
  'keyOrCustomId': "keyOrCustomId_example", // String | Taxamo provided transaction key or custom id
  'currencyCode': "currencyCode_example", // String | Three letter ISO currency code.
  'orderDateTo': "orderDateTo_example", // String | Order date to in yyyy-MM-dd format.
  'sortReverse': true, // Boolean | If true, results are sorted in descending order.
  'limit': 56, // Number | Limit (no more than 1000, defaults to 100).
  'invoiceNumber': "invoiceNumber_example", // String | Transaction invoice number.
  'taxCountryCodes': "taxCountryCodes_example", // String | Comma separated list of two letter ISO tax country codes.
  'statuses': "statuses_example", // String | Comma separated list of of transaction statuses. 'N' - unconfirmed transaction, 'C' - confirmed transaction.
  'originalTransactionKey': "originalTransactionKey_example", // String | Taxamo provided original transaction key
  'orderDateFrom': "orderDateFrom_example", // String | Order date from in yyyy-MM-dd format.
  'totalAmountGreaterThan': "totalAmountGreaterThan_example", // String | Return only transactions with total amount greater than given number. Transactions with total amount equal to a given number (e.g. 0) are not returned.
  'format': "format_example", // String | Output format - supports 'csv' value for this operation.
  'totalAmountLessThan': "totalAmountLessThan_example", // String | Return only transactions with total amount less than a given number. Transactions with total amount equal to a given number (e.g. 1) are not returned.
  'taxCountryCode': "taxCountryCode_example" // String | Two letter ISO tax country code.
};
apiInstance.listTransactions(opts, (error, data, response) => {
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
 **filterText** | **String**| Filtering expression | [optional] 
 **offset** | **Number**| Offset | [optional] 
 **hasNote** | **Boolean**| Return only transactions with a note field set. | [optional] 
 **keyOrCustomId** | **String**| Taxamo provided transaction key or custom id | [optional] 
 **currencyCode** | **String**| Three letter ISO currency code. | [optional] 
 **orderDateTo** | **String**| Order date to in yyyy-MM-dd format. | [optional] 
 **sortReverse** | **Boolean**| If true, results are sorted in descending order. | [optional] 
 **limit** | **Number**| Limit (no more than 1000, defaults to 100). | [optional] 
 **invoiceNumber** | **String**| Transaction invoice number. | [optional] 
 **taxCountryCodes** | **String**| Comma separated list of two letter ISO tax country codes. | [optional] 
 **statuses** | **String**| Comma separated list of of transaction statuses. &#39;N&#39; - unconfirmed transaction, &#39;C&#39; - confirmed transaction. | [optional] 
 **originalTransactionKey** | **String**| Taxamo provided original transaction key | [optional] 
 **orderDateFrom** | **String**| Order date from in yyyy-MM-dd format. | [optional] 
 **totalAmountGreaterThan** | **String**| Return only transactions with total amount greater than given number. Transactions with total amount equal to a given number (e.g. 0) are not returned. | [optional] 
 **format** | **String**| Output format - supports &#39;csv&#39; value for this operation. | [optional] 
 **totalAmountLessThan** | **String**| Return only transactions with total amount less than a given number. Transactions with total amount equal to a given number (e.g. 1) are not returned. | [optional] 
 **taxCountryCode** | **String**| Two letter ISO tax country code. | [optional] 

### Return type

[**ListTransactionsOut**](ListTransactionsOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unconfirmTransaction

> UnconfirmTransactionOut unconfirmTransaction(key, input)

Un-confirm the transaction

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TransactionsApi();
let key = "key_example"; // String | Transaction key.
let input = new Taxamo.UnconfirmTransactionIn(); // UnconfirmTransactionIn | Input
apiInstance.unconfirmTransaction(key, input, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 
 **input** | [**UnconfirmTransactionIn**](UnconfirmTransactionIn.md)| Input | 

### Return type

[**UnconfirmTransactionOut**](UnconfirmTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTransaction

> UpdateTransactionOut updateTransaction(key, input)

Update transaction

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.TransactionsApi();
let key = "key_example"; // String | Transaction key.
let input = new Taxamo.UpdateTransactionIn(); // UpdateTransactionIn | Input
apiInstance.updateTransaction(key, input, (error, data, response) => {
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
 **key** | **String**| Transaction key. | 
 **input** | [**UpdateTransactionIn**](UpdateTransactionIn.md)| Input | 

### Return type

[**UpdateTransactionOut**](UpdateTransactionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

