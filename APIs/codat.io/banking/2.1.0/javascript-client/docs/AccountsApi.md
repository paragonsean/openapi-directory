# BankingApi.AccountsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listAccounts**](AccountsApi.md#listAccounts) | **GET** /companies/{companyId}/connections/{connectionId}/data/banking-accounts | List accounts



## listAccounts

> Accounts listAccounts(companyId, connectionId, page, opts)

List accounts

Gets a list of all bank accounts of the SMB, with rich data like balances, account numbers and institutions holdingthe accounts.

### Example

```javascript
import BankingApi from 'banking_api';
let defaultClient = BankingApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new BankingApi.AccountsApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let connectionId = "2e9d2c44-f675-40ba-8049-353bfcb5e171"; // String | 
let page = 1; // Number | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
let opts = {
  'pageSize': 100, // Number | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
  'query': "query_example", // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
  'orderBy': "-modifiedDate" // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
};
apiInstance.listAccounts(companyId, connectionId, page, opts, (error, data, response) => {
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
 **connectionId** | **String**|  | 
 **page** | **Number**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1]
 **pageSize** | **Number**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | **String**| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **orderBy** | **String**| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

