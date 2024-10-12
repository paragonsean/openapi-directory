# BillingoApiV3.BankAccountApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBankAccount**](BankAccountApi.md#createBankAccount) | **POST** /bank-accounts | Create a bank account
[**deleteBankAccount**](BankAccountApi.md#deleteBankAccount) | **DELETE** /bank-accounts/{id} | Delete a bank account
[**getBankAccount**](BankAccountApi.md#getBankAccount) | **GET** /bank-accounts/{id} | Retrieve a bank account
[**listBankAccount**](BankAccountApi.md#listBankAccount) | **GET** /bank-accounts | List all bank account
[**updateBankAccount**](BankAccountApi.md#updateBankAccount) | **PUT** /bank-accounts/{id} | Update a bank account



## createBankAccount

> BankAccount createBankAccount(bankAccount)

Create a bank account

Create a new bank account. Returns a bank account object if the create is succeded.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.BankAccountApi();
let bankAccount = new BillingoApiV3.BankAccount(); // BankAccount | BankAccount object that you would like to store.
apiInstance.createBankAccount(bankAccount, (error, data, response) => {
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
 **bankAccount** | [**BankAccount**](BankAccount.md)| BankAccount object that you would like to store. | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBankAccount

> deleteBankAccount(id)

Delete a bank account

Delete an existing bank account.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.BankAccountApi();
let id = 56; // Number | 
apiInstance.deleteBankAccount(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankAccount

> BankAccount getBankAccount(id)

Retrieve a bank account

Retrieves the details of an existing bank account.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.BankAccountApi();
let id = 56; // Number | 
apiInstance.getBankAccount(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBankAccount

> BankAccountList listBankAccount(opts)

List all bank account

Returns a list of your bank accounts. The bank accounts are returned sorted by creation date, with the most recent bank account appearing first.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.BankAccountApi();
let opts = {
  'page': 56, // Number | 
  'perPage': 25 // Number | 
};
apiInstance.listBankAccount(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] [default to 25]

### Return type

[**BankAccountList**](BankAccountList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBankAccount

> BankAccount updateBankAccount(id, bankAccount)

Update a bank account

Update an existing bank accounts. Returns a bank account object if the update is succeded.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.BankAccountApi();
let id = 56; // Number | 
let bankAccount = new BillingoApiV3.BankAccount(); // BankAccount | Bank account object that you would like to update.
apiInstance.updateBankAccount(id, bankAccount, (error, data, response) => {
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
 **id** | **Number**|  | 
 **bankAccount** | [**BankAccount**](BankAccount.md)| Bank account object that you would like to update. | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

