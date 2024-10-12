# Apacta.ExpenseFilesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenseFilesExpenseFileIdDelete**](ExpenseFilesApi.md#expenseFilesExpenseFileIdDelete) | **DELETE** /expense_files/{expense_file_id} | Delete file
[**expenseFilesExpenseFileIdGet**](ExpenseFilesApi.md#expenseFilesExpenseFileIdGet) | **GET** /expense_files/{expense_file_id} | Show file
[**expenseFilesExpenseFileIdPut**](ExpenseFilesApi.md#expenseFilesExpenseFileIdPut) | **PUT** /expense_files/{expense_file_id} | Edit file
[**expenseFilesGet**](ExpenseFilesApi.md#expenseFilesGet) | **GET** /expense_files | Show list of expense files
[**expenseFilesPost**](ExpenseFilesApi.md#expenseFilesPost) | **POST** /expense_files | Add file to expense



## expenseFilesExpenseFileIdDelete

> ExpenseFilesExpenseFileIdGet200Response expenseFilesExpenseFileIdDelete(expenseFileId)

Delete file

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

let apiInstance = new Apacta.ExpenseFilesApi();
let expenseFileId = "expenseFileId_example"; // String | 
apiInstance.expenseFilesExpenseFileIdDelete(expenseFileId, (error, data, response) => {
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
 **expenseFileId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdGet200Response**](ExpenseFilesExpenseFileIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenseFilesExpenseFileIdGet

> ExpenseFilesExpenseFileIdGet200Response expenseFilesExpenseFileIdGet(expenseFileId)

Show file

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

let apiInstance = new Apacta.ExpenseFilesApi();
let expenseFileId = "expenseFileId_example"; // String | 
apiInstance.expenseFilesExpenseFileIdGet(expenseFileId, (error, data, response) => {
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
 **expenseFileId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdGet200Response**](ExpenseFilesExpenseFileIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenseFilesExpenseFileIdPut

> ExpenseFilesExpenseFileIdPut200Response expenseFilesExpenseFileIdPut(expenseFileId)

Edit file

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

let apiInstance = new Apacta.ExpenseFilesApi();
let expenseFileId = "expenseFileId_example"; // String | 
apiInstance.expenseFilesExpenseFileIdPut(expenseFileId, (error, data, response) => {
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
 **expenseFileId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenseFilesGet

> ExpenseFilesGet200Response expenseFilesGet(opts)

Show list of expense files

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

let apiInstance = new Apacta.ExpenseFilesApi();
let opts = {
  'createdById': "createdById_example", // String | 
  'expenseId': "expenseId_example" // String | 
};
apiInstance.expenseFilesGet(opts, (error, data, response) => {
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
 **expenseId** | **String**|  | [optional] 

### Return type

[**ExpenseFilesGet200Response**](ExpenseFilesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expenseFilesPost

> ClockingRecordsPost201Response expenseFilesPost(file, opts)

Add file to expense

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

let apiInstance = new Apacta.ExpenseFilesApi();
let file = "/path/to/file"; // File | 
let opts = {
  'description': "description_example" // String | 
};
apiInstance.expenseFilesPost(file, opts, (error, data, response) => {
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
 **file** | **File**|  | 
 **description** | **String**|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

