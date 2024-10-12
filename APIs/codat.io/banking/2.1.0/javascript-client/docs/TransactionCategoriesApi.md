# BankingApi.TransactionCategoriesApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listTransactionCategories**](TransactionCategoriesApi.md#listTransactionCategories) | **GET** /companies/{companyId}/connections/{connectionId}/data/banking-transactionCategories | List all transaction categories



## listTransactionCategories

> TransactionCategories listTransactionCategories(page, opts)

List all transaction categories

Gets a list of hierarchical categories associated with a transaction for greater contextual meaning to transactionactivity.

### Example

```javascript
import BankingApi from 'banking_api';
let defaultClient = BankingApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new BankingApi.TransactionCategoriesApi();
let page = 1; // Number | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
let opts = {
  'pageSize': 100, // Number | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
  'query': "query_example", // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
  'orderBy': "-modifiedDate" // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
};
apiInstance.listTransactionCategories(page, opts, (error, data, response) => {
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
 **page** | **Number**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1]
 **pageSize** | **Number**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | **String**| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **orderBy** | **String**| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**TransactionCategories**](TransactionCategories.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

