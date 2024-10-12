# Apacta.ExpenseOIOUBLFilesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expensesExpenseIdOriginalFilesFileIdGet**](ExpenseOIOUBLFilesApi.md#expensesExpenseIdOriginalFilesFileIdGet) | **GET** /expenses/{expense_id}/original_files/{file_id} | Show OIOUBL file
[**expensesExpenseIdOriginalFilesGet**](ExpenseOIOUBLFilesApi.md#expensesExpenseIdOriginalFilesGet) | **GET** /expenses/{expense_id}/original_files | Show list of all OIOUBL files for the expense



## expensesExpenseIdOriginalFilesFileIdGet

> ClockingRecordsCheckoutPost201Response expensesExpenseIdOriginalFilesFileIdGet(expenseId, fileId)

Show OIOUBL file

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

let apiInstance = new Apacta.ExpenseOIOUBLFilesApi();
let expenseId = "expenseId_example"; // String | 
let fileId = "fileId_example"; // String | 
apiInstance.expensesExpenseIdOriginalFilesFileIdGet(expenseId, fileId, (error, data, response) => {
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
 **expenseId** | **String**|  | 
 **fileId** | **String**|  | 

### Return type

[**ClockingRecordsCheckoutPost201Response**](ClockingRecordsCheckoutPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expensesExpenseIdOriginalFilesGet

> ClockingRecordsCheckoutPost201Response expensesExpenseIdOriginalFilesGet(expenseId)

Show list of all OIOUBL files for the expense

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

let apiInstance = new Apacta.ExpenseOIOUBLFilesApi();
let expenseId = "expenseId_example"; // String | 
apiInstance.expensesExpenseIdOriginalFilesGet(expenseId, (error, data, response) => {
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
 **expenseId** | **String**|  | 

### Return type

[**ClockingRecordsCheckoutPost201Response**](ClockingRecordsCheckoutPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

