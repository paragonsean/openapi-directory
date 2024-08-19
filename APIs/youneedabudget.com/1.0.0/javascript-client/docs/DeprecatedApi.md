# YnabApiEndpoints.DeprecatedApi

All URIs are relative to *https://api.ynab.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkCreateTransactions**](DeprecatedApi.md#bulkCreateTransactions) | **POST** /budgets/{budget_id}/transactions/bulk | Bulk create transactions



## bulkCreateTransactions

> BulkResponse bulkCreateTransactions(budgetId, bulkTransactions)

Bulk create transactions

Creates multiple transactions.  Although this endpoint is still supported, it is recommended to use &#39;POST /budgets/{budget_id}/transactions&#39; to create multiple transactions.

### Example

```javascript
import YnabApiEndpoints from 'ynab_api_endpoints';
let defaultClient = YnabApiEndpoints.ApiClient.instance;
// Configure API key authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//bearer.apiKeyPrefix = 'Token';

let apiInstance = new YnabApiEndpoints.DeprecatedApi();
let budgetId = "budgetId_example"; // String | The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).
let bulkTransactions = new YnabApiEndpoints.BulkTransactions(); // BulkTransactions | The list of transactions to create
apiInstance.bulkCreateTransactions(budgetId, bulkTransactions, (error, data, response) => {
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
 **budgetId** | **String**| The id of the budget. \&quot;last-used\&quot; can be used to specify the last used budget and \&quot;default\&quot; can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget). | 
 **bulkTransactions** | [**BulkTransactions**](BulkTransactions.md)| The list of transactions to create | 

### Return type

[**BulkResponse**](BulkResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

