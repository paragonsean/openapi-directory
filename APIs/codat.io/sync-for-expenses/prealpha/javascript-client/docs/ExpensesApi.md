# CodatExpenseApi.ExpensesApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createExpenseDataset**](ExpensesApi.md#createExpenseDataset) | **POST** /companies/{companyId}/sync/expenses/data/expense-transactions | Create expense-transactions
[**uploadAttachment**](ExpensesApi.md#uploadAttachment) | **POST** /companies/{companyId}/sync/expenses/syncs/{syncId}/transactions/{transactionId}/attachments | Upload attachment



## createExpenseDataset

> CreateExpenseResponse createExpenseDataset(companyId, opts)

Create expense-transactions

Create an expense transaction

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.ExpensesApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let opts = {
  'createExpenseRequest': {"items":[{"currency":"GBP","currencyRate":1.18,"id":"4d7c6929-7770-412b-91bb-44d3bc71d111","issueDate":"2021-05-21T00:00:00+00:00","lines":[{"accountRef":{"id":"9aa5b894-1be9-4f97-96cd-ffde90766b3e"},"netAmount":110.42,"taxAmount":14.43,"taxRateRef":{"id":"77a32ee2-60c7-4ab9-917a-bd82e2e43a26"},"trackingRefs":[{"id":"dde5b35f-5d33-40bd-a34f-ee529f4c785c"}]}],"merchantName":"Amazon UK","notes":"APPLE.COM/BILL - 09001077498 - Card Ending: 4590","type":"Payment"}]} // CreateExpenseRequest | 
};
apiInstance.createExpenseDataset(companyId, opts, (error, data, response) => {
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
 **createExpenseRequest** | [**CreateExpenseRequest**](CreateExpenseRequest.md)|  | [optional] 

### Return type

[**CreateExpenseResponse**](CreateExpenseResponse.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadAttachment

> Attachment uploadAttachment(companyId, transactionId, syncId)

Upload attachment

Creates an attachment in the accounting software against the given transactionId

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.ExpensesApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let transactionId = "336694d8-2dca-4cb5-a28d-3ccb83e55eee"; // String | The unique identifier for your SMB's transaction.
let syncId = "6fb40d5e-b13e-11ed-afa1-0242ac120002"; // String | Unique identifier for a sync.
apiInstance.uploadAttachment(companyId, transactionId, syncId, (error, data, response) => {
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
 **transactionId** | **String**| The unique identifier for your SMB&#39;s transaction. | 
 **syncId** | **String**| Unique identifier for a sync. | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

