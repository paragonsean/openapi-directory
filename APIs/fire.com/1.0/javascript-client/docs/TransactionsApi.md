# FireFinancialServicesBusinessApi.TransactionsApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTransactionsByAccountIdFiltered**](TransactionsApi.md#getTransactionsByAccountIdFiltered) | **GET** /v1/accounts/{ican}/transactions/filter | Filtered list of transactions for an account (v1)
[**getTransactionsByAccountIdv1**](TransactionsApi.md#getTransactionsByAccountIdv1) | **GET** /v1/accounts/{ican}/transactions | List transactions for an account (v1)
[**getTransactionsByAccountIdv3**](TransactionsApi.md#getTransactionsByAccountIdv3) | **GET** /v3/accounts/{ican}/transactions | List transactions for an account (v3)



## getTransactionsByAccountIdFiltered

> CardTransactionsv1 getTransactionsByAccountIdFiltered(ican, dateRangeFrom, dateRangeTo, searchKeyword, transactionTypes, offset)

Filtered list of transactions for an account (v1)

Retrieve a filtered list of transactions against an account. Recommended to use the v3 endpoint instead. * &#x60;dateRangeFrom&#x60; - A millisecond epoch time specifying the date range start date. * &#x60;dateRangeTo&#x60; - A millisecond epoch time specifying the date range end date. * &#x60;searchKeyword&#x60; - Search term to filter by from the reference field (&#x60;myRef&#x60;). * &#x60;transactionTypes&#x60; - One or more of the transaction types above. This field can be repeated multiple times to allow for multiple transaction types. * &#x60;offset&#x60; - The page offset. Defaults to 0. This is the record number that the returned list will start at. E.g. offset &#x3D; 40 and limit &#x3D; 20 will return records 40 to 59. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.TransactionsApi();
let ican = 789; // Number | 
let dateRangeFrom = 789; // Number | 
let dateRangeTo = 789; // Number | 
let searchKeyword = "searchKeyword_example"; // String | 
let transactionTypes = ["null"]; // [String] | 
let offset = 789; // Number | 
apiInstance.getTransactionsByAccountIdFiltered(ican, dateRangeFrom, dateRangeTo, searchKeyword, transactionTypes, offset, (error, data, response) => {
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
 **ican** | **Number**|  | 
 **dateRangeFrom** | **Number**|  | 
 **dateRangeTo** | **Number**|  | 
 **searchKeyword** | **String**|  | 
 **transactionTypes** | [**[String]**](String.md)|  | 
 **offset** | **Number**|  | 

### Return type

[**CardTransactionsv1**](CardTransactionsv1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionsByAccountIdv1

> CardTransactionsv1 getTransactionsByAccountIdv1(ican, limit, offset)

List transactions for an account (v1)

Retrieve a list of transactions against an account. Recommended to use the v3 endpoint instead.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.TransactionsApi();
let ican = 789; // Number | 
let limit = 789; // Number | 
let offset = 789; // Number | 
apiInstance.getTransactionsByAccountIdv1(ican, limit, offset, (error, data, response) => {
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
 **ican** | **Number**|  | 
 **limit** | **Number**|  | 
 **offset** | **Number**|  | 

### Return type

[**CardTransactionsv1**](CardTransactionsv1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionsByAccountIdv3

> CardTransactionsv3 getTransactionsByAccountIdv3(ican, opts)

List transactions for an account (v3)

Retrieve a list of transactions against an account. Initially, use the optional &#x60;limit&#x60;, &#x60;dateRangeFrom&#x60; and &#x60;dateRangeTo&#x60; query params to limit your query, then use the embedded &#x60;next&#x60; or &#x60;prev&#x60; links in the response to get newer or older pages. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.TransactionsApi();
let ican = 789; // Number | 
let opts = {
  'limit': 789, // Number | 
  'dateRangeFrom': 789, // Number | 
  'dateRangeTo': 789, // Number | 
  'startAfter': "startAfter_example" // String | 
};
apiInstance.getTransactionsByAccountIdv3(ican, opts, (error, data, response) => {
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
 **ican** | **Number**|  | 
 **limit** | **Number**|  | [optional] 
 **dateRangeFrom** | **Number**|  | [optional] 
 **dateRangeTo** | **Number**|  | [optional] 
 **startAfter** | **String**|  | [optional] 

### Return type

[**CardTransactionsv3**](CardTransactionsv3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

