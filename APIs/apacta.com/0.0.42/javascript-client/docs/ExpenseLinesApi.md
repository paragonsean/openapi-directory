# Apacta.ExpenseLinesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenseLinesExpenseLineIdDelete**](ExpenseLinesApi.md#expenseLinesExpenseLineIdDelete) | **DELETE** /expense_lines/{expense_line_id} | Delete expense line
[**expenseLinesExpenseLineIdGet**](ExpenseLinesApi.md#expenseLinesExpenseLineIdGet) | **GET** /expense_lines/{expense_line_id} | Show expense line
[**expenseLinesExpenseLineIdPut**](ExpenseLinesApi.md#expenseLinesExpenseLineIdPut) | **PUT** /expense_lines/{expense_line_id} | Edit expense line
[**expenseLinesGet**](ExpenseLinesApi.md#expenseLinesGet) | **GET** /expense_lines | Show list of expense lines
[**expenseLinesPost**](ExpenseLinesApi.md#expenseLinesPost) | **POST** /expense_lines | Add line to expense



## expenseLinesExpenseLineIdDelete

> ExpenseLinesExpenseLineIdGet200Response expenseLinesExpenseLineIdDelete(expenseLineId)

Delete expense line

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ExpenseLinesApi();
let expenseLineId = "expenseLineId_example"; // String | 
apiInstance.expenseLinesExpenseLineIdDelete(expenseLineId, (error, data, response) => {
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
 **expenseLineId** | **String**|  | 

### Return type

[**ExpenseLinesExpenseLineIdGet200Response**](ExpenseLinesExpenseLineIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenseLinesExpenseLineIdGet

> ExpenseLinesExpenseLineIdGet200Response expenseLinesExpenseLineIdGet(expenseLineId)

Show expense line

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ExpenseLinesApi();
let expenseLineId = "expenseLineId_example"; // String | 
apiInstance.expenseLinesExpenseLineIdGet(expenseLineId, (error, data, response) => {
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
 **expenseLineId** | **String**|  | 

### Return type

[**ExpenseLinesExpenseLineIdGet200Response**](ExpenseLinesExpenseLineIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenseLinesExpenseLineIdPut

> ExpenseLinesExpenseLineIdGet200Response expenseLinesExpenseLineIdPut(expenseLineId)

Edit expense line

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ExpenseLinesApi();
let expenseLineId = "expenseLineId_example"; // String | 
apiInstance.expenseLinesExpenseLineIdPut(expenseLineId, (error, data, response) => {
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
 **expenseLineId** | **String**|  | 

### Return type

[**ExpenseLinesExpenseLineIdGet200Response**](ExpenseLinesExpenseLineIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenseLinesGet

> ExpenseLinesGet200Response expenseLinesGet(opts)

Show list of expense lines

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ExpenseLinesApi();
let opts = {
  'createdById': "createdById_example", // String | 
  'currencyId': "currencyId_example", // String | 
  'expenseId': "expenseId_example" // String | 
};
apiInstance.expenseLinesGet(opts, (error, data, response) => {
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
 **createdById** | **String**|  | [optional] 
 **currencyId** | **String**|  | [optional] 
 **expenseId** | **String**|  | [optional] 

### Return type

[**ExpenseLinesGet200Response**](ExpenseLinesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenseLinesPost

> ClockingRecordsPost201Response expenseLinesPost(opts)

Add line to expense

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.ExpenseLinesApi();
let opts = {
  'expenseLinesPostRequest': new Apacta.ExpenseLinesPostRequest() // ExpenseLinesPostRequest | 
};
apiInstance.expenseLinesPost(opts, (error, data, response) => {
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
 **expenseLinesPostRequest** | [**ExpenseLinesPostRequest**](ExpenseLinesPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

