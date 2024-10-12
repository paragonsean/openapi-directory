# CodatExpenseApi.SyncApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**intiateSync**](SyncApi.md#intiateSync) | **POST** /companies/{companyId}/sync/expenses/syncs | Initiate sync



## intiateSync

> SyncInitiated intiateSync(companyId, opts)

Initiate sync

Initiate sync of pending transactions.

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.SyncApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let opts = {
  'postSync': new CodatExpenseApi.PostSync() // PostSync | 
};
apiInstance.intiateSync(companyId, opts, (error, data, response) => {
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
 **postSync** | [**PostSync**](PostSync.md)|  | [optional] 

### Return type

[**SyncInitiated**](SyncInitiated.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

