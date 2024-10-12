# FilesComApi.PaymentsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPayments**](PaymentsApi.md#getPayments) | **GET** /payments | List Payments
[**getPaymentsId**](PaymentsApi.md#getPaymentsId) | **GET** /payments/{id} | Show Payment



## getPayments

> [AccountLineItemEntity] getPayments(opts)

List Payments

List Payments

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PaymentsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getPayments(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[AccountLineItemEntity]**](AccountLineItemEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentsId

> AccountLineItemEntity getPaymentsId(id)

Show Payment

Show Payment

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.PaymentsApi();
let id = 56; // Number | Payment ID.
apiInstance.getPaymentsId(id, (error, data, response) => {
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
 **id** | **Number**| Payment ID. | 

### Return type

[**AccountLineItemEntity**](AccountLineItemEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

