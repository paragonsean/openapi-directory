# FireFinancialServicesBusinessApi.AccountsApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addAccount**](AccountsApi.md#addAccount) | **POST** /v1/accounts | Add a new account
[**getAccountById**](AccountsApi.md#getAccountById) | **GET** /v1/accounts/{ican} | Retrieve the details of a fire.com Account
[**getAccounts**](AccountsApi.md#getAccounts) | **GET** /v1/accounts | List all fire.com Accounts



## addAccount

> Account addAccount(newAccount)

Add a new account

Creates a new fire.com account.  **Please note there is a charge associated with creating a new account.** 

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.AccountsApi();
let newAccount = new FireFinancialServicesBusinessApi.NewAccount(); // NewAccount | Details of the new account
apiInstance.addAccount(newAccount, (error, data, response) => {
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
 **newAccount** | [**NewAccount**](NewAccount.md)| Details of the new account | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccountById

> Account getAccountById(ican)

Retrieve the details of a fire.com Account

You can retrieve the details of a fire.com Account by its &#x60;ican&#x60;.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.AccountsApi();
let ican = 789; // Number | 
apiInstance.getAccountById(ican, (error, data, response) => {
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

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccounts

> Accounts getAccounts()

List all fire.com Accounts

Returns all your fire.com Accounts. Ordered by Alias ascending. Can be paginated.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.AccountsApi();
apiInstance.getAccounts((error, data, response) => {
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

[**Accounts**](Accounts.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

