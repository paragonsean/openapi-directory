# FireFinancialServicesBusinessApi.PayeeBankAccountsApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPayees**](PayeeBankAccountsApi.md#getPayees) | **GET** /v1/payees | List all Payee Bank Accounts



## getPayees

> PayeeBankAccounts getPayees()

List all Payee Bank Accounts

Returns all your payee bank accounts.   Ordered by payee name ascending.   Can be paginated. 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.PayeeBankAccountsApi();
apiInstance.getPayees((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PayeeBankAccounts**](PayeeBankAccounts.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

