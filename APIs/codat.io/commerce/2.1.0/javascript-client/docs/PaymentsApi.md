# CommerceApi.PaymentsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listPaymentMethods**](PaymentsApi.md#listPaymentMethods) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-paymentMethods | List payment methods
[**listPayments**](PaymentsApi.md#listPayments) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-payments | List payments



## listPaymentMethods

> PaymentMethods listPaymentMethods(page, opts)

List payment methods

Retrieve a list of payment methods, such as card, cash or other online payment methods, as held in the linked commerce platform.

### Example

```javascript
import CommerceApi from 'commerce_api';
let defaultClient = CommerceApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CommerceApi.PaymentsApi();
let page = 1; // Number | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
let opts = {
  'pageSize': 100, // Number | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
  'query': "query_example", // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
  'orderBy': "-modifiedDate" // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
};
apiInstance.listPaymentMethods(page, opts, (error, data, response) => {
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

[**PaymentMethods**](PaymentMethods.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPayments

> Payments listPayments(page, opts)

List payments

List commerce payments for the given company &amp; data connection.

### Example

```javascript
import CommerceApi from 'commerce_api';
let defaultClient = CommerceApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CommerceApi.PaymentsApi();
let page = 1; // Number | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
let opts = {
  'pageSize': 100, // Number | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
  'query': "query_example", // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
  'orderBy': "-modifiedDate" // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
};
apiInstance.listPayments(page, opts, (error, data, response) => {
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

[**Payments**](Payments.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

