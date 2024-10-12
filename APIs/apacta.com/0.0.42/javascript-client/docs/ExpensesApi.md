# Apacta.ExpensesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteExpenses**](ExpensesApi.md#bulkDeleteExpenses) | **DELETE** /expenses/bulkDelete | Bulk delete expenses
[**expensesExpenseIdDelete**](ExpensesApi.md#expensesExpenseIdDelete) | **DELETE** /expenses/{expense_id} | Delete expense
[**expensesExpenseIdGet**](ExpensesApi.md#expensesExpenseIdGet) | **GET** /expenses/{expense_id} | Show expense
[**expensesExpenseIdPut**](ExpensesApi.md#expensesExpenseIdPut) | **PUT** /expenses/{expense_id} | Edit expense
[**expensesGet**](ExpensesApi.md#expensesGet) | **GET** /expenses | Show list of expenses
[**expensesHighestAmountGet**](ExpensesApi.md#expensesHighestAmountGet) | **GET** /expenses/highest_amount | Show highest Expense amount(&#x60;total_selling_price&#x60;)
[**expensesPost**](ExpensesApi.md#expensesPost) | **POST** /expenses | Add line to expense
[**sendEmailsExpenses**](ExpensesApi.md#sendEmailsExpenses) | **DELETE** /expenses/sendEmails | Bulk delete expenses



## bulkDeleteExpenses

> EmptySuccessResponse bulkDeleteExpenses(bulkActionRequestBody)

Bulk delete expenses

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

let apiInstance = new Apacta.ExpensesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | expense ids
apiInstance.bulkDeleteExpenses(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| expense ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expensesExpenseIdDelete

> ExpensesExpenseIdGet200Response expensesExpenseIdDelete(expenseId)

Delete expense

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

let apiInstance = new Apacta.ExpensesApi();
let expenseId = "expenseId_example"; // String | 
apiInstance.expensesExpenseIdDelete(expenseId, (error, data, response) => {
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

[**ExpensesExpenseIdGet200Response**](ExpensesExpenseIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expensesExpenseIdGet

> ExpensesExpenseIdGet200Response expensesExpenseIdGet(expenseId)

Show expense

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

let apiInstance = new Apacta.ExpensesApi();
let expenseId = "expenseId_example"; // String | 
apiInstance.expensesExpenseIdGet(expenseId, (error, data, response) => {
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

[**ExpensesExpenseIdGet200Response**](ExpensesExpenseIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expensesExpenseIdPut

> ExpensesExpenseIdGet200Response expensesExpenseIdPut(expenseId)

Edit expense

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

let apiInstance = new Apacta.ExpensesApi();
let expenseId = "expenseId_example"; // String | 
apiInstance.expensesExpenseIdPut(expenseId, (error, data, response) => {
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

[**ExpensesExpenseIdGet200Response**](ExpensesExpenseIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expensesGet

> ExpensesGet200Response expensesGet(opts)

Show list of expenses

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

let apiInstance = new Apacta.ExpensesApi();
let opts = {
  'createdById': "createdById_example", // String | 
  'companyId': "companyId_example", // String | 
  'contactId': "contactId_example", // String | 
  'projectId': "projectId_example", // String | 
  'dueDate': "dueDate_example", // String | Filter by [valid=records in future including today], [exceeded=records in past] or [null=all records]
  'gtCreated': new Date("2013-10-20"), // Date | Created after date
  'ltCreated': new Date("2013-10-20"), // Date | Created before date
  'status': "status_example", // String | Filter by status identifier. [null=all records]
  'isImported': true, // Boolean | 
  'minAmount': 3.4, // Number | Expenses `total_selling_price` > `min_amount`
  'maxAmount': 3.4, // Number | Expenses `total_selling_price` < `max_amount`
  'projects': "projects_example" // String | You can select `all projects`, `no projects` or select `multiple projects`
};
apiInstance.expensesGet(opts, (error, data, response) => {
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
 **companyId** | **String**|  | [optional] 
 **contactId** | **String**|  | [optional] 
 **projectId** | **String**|  | [optional] 
 **dueDate** | **String**| Filter by [valid&#x3D;records in future including today], [exceeded&#x3D;records in past] or [null&#x3D;all records] | [optional] 
 **gtCreated** | **Date**| Created after date | [optional] 
 **ltCreated** | **Date**| Created before date | [optional] 
 **status** | **String**| Filter by status identifier. [null&#x3D;all records] | [optional] 
 **isImported** | **Boolean**|  | [optional] [default to true]
 **minAmount** | **Number**| Expenses &#x60;total_selling_price&#x60; &gt; &#x60;min_amount&#x60; | [optional] 
 **maxAmount** | **Number**| Expenses &#x60;total_selling_price&#x60; &lt; &#x60;max_amount&#x60; | [optional] 
 **projects** | **String**| You can select &#x60;all projects&#x60;, &#x60;no projects&#x60; or select &#x60;multiple projects&#x60; | [optional] 

### Return type

[**ExpensesGet200Response**](ExpensesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expensesHighestAmountGet

> ExpensesHighestAmountGet200Response expensesHighestAmountGet(gtCreated, ltCreated)

Show highest Expense amount(&#x60;total_selling_price&#x60;)

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

let apiInstance = new Apacta.ExpensesApi();
let gtCreated = new Date("2013-10-20"); // Date | Used to filter time range
let ltCreated = new Date("2013-10-20"); // Date | Used to filter time range
apiInstance.expensesHighestAmountGet(gtCreated, ltCreated, (error, data, response) => {
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
 **gtCreated** | **Date**| Used to filter time range | 
 **ltCreated** | **Date**| Used to filter time range | 

### Return type

[**ExpensesHighestAmountGet200Response**](ExpensesHighestAmountGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expensesPost

> ClockingRecordsPost201Response expensesPost(opts)

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

let apiInstance = new Apacta.ExpensesApi();
let opts = {
  'expensesPostRequest': new Apacta.ExpensesPostRequest() // ExpensesPostRequest | 
};
apiInstance.expensesPost(opts, (error, data, response) => {
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
 **expensesPostRequest** | [**ExpensesPostRequest**](ExpensesPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendEmailsExpenses

> EmptySuccessResponse sendEmailsExpenses(bulkActionRequestBody)

Bulk delete expenses

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

let apiInstance = new Apacta.ExpensesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | expense ids
apiInstance.sendEmailsExpenses(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| expense ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

