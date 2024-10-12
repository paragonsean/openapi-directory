# CodatExpenseApi.SyncStatusApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLastSuccessfulSync**](SyncStatusApi.md#getLastSuccessfulSync) | **GET** /companies/{companyId}/sync/expenses/syncs/lastSuccessful/status | Last successful sync
[**getLatestSync**](SyncStatusApi.md#getLatestSync) | **GET** /companies/{companyId}/sync/expenses/syncs/latest/status | Latest sync status
[**getSyncById**](SyncStatusApi.md#getSyncById) | **GET** /companies/{companyId}/sync/expenses/syncs/{syncId}/status | Get Sync status
[**listSyncs**](SyncStatusApi.md#listSyncs) | **GET** /companies/{companyId}/sync/expenses/syncs/list/status | List sync statuses



## getLastSuccessfulSync

> CompanySyncStatus getLastSuccessfulSync(companyId)

Last successful sync

Gets the status of the last successfull sync

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.SyncStatusApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
apiInstance.getLastSuccessfulSync(companyId, (error, data, response) => {
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

### Return type

[**CompanySyncStatus**](CompanySyncStatus.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLatestSync

> CompanySyncStatus getLatestSync(companyId)

Latest sync status

Gets the latest sync status

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.SyncStatusApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
apiInstance.getLatestSync(companyId, (error, data, response) => {
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

### Return type

[**CompanySyncStatus**](CompanySyncStatus.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSyncById

> CompanySyncStatus getSyncById(companyId, syncId)

Get Sync status

Get the sync status for a specified sync

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.SyncStatusApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
let syncId = "6fb40d5e-b13e-11ed-afa1-0242ac120002"; // String | Unique identifier for a sync.
apiInstance.getSyncById(companyId, syncId, (error, data, response) => {
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
 **syncId** | **String**| Unique identifier for a sync. | 

### Return type

[**CompanySyncStatus**](CompanySyncStatus.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncs

> [CompanySyncStatus] listSyncs(companyId)

List sync statuses

Gets a list of sync statuses

### Example

```javascript
import CodatExpenseApi from 'codat_expense_api';
let defaultClient = CodatExpenseApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CodatExpenseApi.SyncStatusApi();
let companyId = "8a210b68-6988-11ed-a1eb-0242ac120002"; // String | 
apiInstance.listSyncs(companyId, (error, data, response) => {
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

### Return type

[**[CompanySyncStatus]**](CompanySyncStatus.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

