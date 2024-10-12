# BigRedCloudApi.BankAccountsApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bankAccountsDelete**](BankAccountsApi.md#bankAccountsDelete) | **DELETE** /v1/bankAccounts/{id} | Removes an existing Bank Account.
[**bankAccountsGet**](BankAccountsApi.md#bankAccountsGet) | **GET** /v1/bankAccounts | Returns a list of company&#39;s Bank Account. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;acCode\&quot; fields.
[**bankAccountsPost**](BankAccountsApi.md#bankAccountsPost) | **POST** /v1/bankAccounts | Creates a new Bank Account.
[**bankAccountsProcessBatch**](BankAccountsApi.md#bankAccountsProcessBatch) | **PUT** /v1/bankAccounts/batch | Processes a batch of Bank Accounts.
[**bankAccountsPut**](BankAccountsApi.md#bankAccountsPut) | **PUT** /v1/bankAccounts/{id} | Updates an existing Bank Account.
[**v1BankAccountsIdGet**](BankAccountsApi.md#v1BankAccountsIdGet) | **GET** /v1/bankAccounts/{id} | Returns information about a single Bank Account.



## bankAccountsDelete

> Object bankAccountsDelete(id, timestamp)

Removes an existing Bank Account.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.BankAccountsApi();
let id = 789; // Number | Id of Bank Account to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Bank Account to remove. Should be encoded in Base64.
apiInstance.bankAccountsDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Bank Account to remove. | 
 **timestamp** | **String**| Timestamp of Bank Account to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bankAccountsGet

> PageResultBankAccountQueryDto bankAccountsGet()

Returns a list of company&#39;s Bank Account. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;acCode\&quot; fields.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.BankAccountsApi();
apiInstance.bankAccountsGet((error, data, response) => {
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

[**PageResultBankAccountQueryDto**](PageResultBankAccountQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bankAccountsPost

> Object bankAccountsPost(bankAccountDto)

Creates a new Bank Account.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.BankAccountsApi();
let bankAccountDto = new BigRedCloudApi.BankAccountDto(); // BankAccountDto | Information of Bank Account to create.
apiInstance.bankAccountsPost(bankAccountDto, (error, data, response) => {
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
 **bankAccountDto** | [**BankAccountDto**](BankAccountDto.md)| Information of Bank Account to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankAccountsProcessBatch

> Object bankAccountsProcessBatch(batchItemBankAccountDto)

Processes a batch of Bank Accounts.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.BankAccountsApi();
let batchItemBankAccountDto = [new BigRedCloudApi.BatchItemBankAccountDto()]; // [BatchItemBankAccountDto] | Batch of Bank Accounts to process.
apiInstance.bankAccountsProcessBatch(batchItemBankAccountDto, (error, data, response) => {
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
 **batchItemBankAccountDto** | [**[BatchItemBankAccountDto]**](BatchItemBankAccountDto.md)| Batch of Bank Accounts to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankAccountsPut

> Object bankAccountsPut(id, bankAccountDto)

Updates an existing Bank Account.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.BankAccountsApi();
let id = 789; // Number | Id of Bank Account to update.
let bankAccountDto = new BigRedCloudApi.BankAccountDto(); // BankAccountDto | Information of Bank Account to update.
apiInstance.bankAccountsPut(id, bankAccountDto, (error, data, response) => {
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
 **id** | **Number**| Id of Bank Account to update. | 
 **bankAccountDto** | [**BankAccountDto**](BankAccountDto.md)| Information of Bank Account to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1BankAccountsIdGet

> BankAccountDto v1BankAccountsIdGet(id)

Returns information about a single Bank Account.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.BankAccountsApi();
let id = 789; // Number | Id of Bank Account to return.
apiInstance.v1BankAccountsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of Bank Account to return. | 

### Return type

[**BankAccountDto**](BankAccountDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

