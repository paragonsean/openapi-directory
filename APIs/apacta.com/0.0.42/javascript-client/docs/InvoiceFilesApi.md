# Apacta.InvoiceFilesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInvoiceFile**](InvoiceFilesApi.md#createInvoiceFile) | **POST** /invoices/{invoice_id}/files | Create a new invoice file
[**getInvoiceFiles**](InvoiceFilesApi.md#getInvoiceFiles) | **GET** /invoices/{invoice_id}/files | Get list of invoice files
[**getOneInvoiceFiles**](InvoiceFilesApi.md#getOneInvoiceFiles) | **GET** /invoices/{invoice_id}/files/{file_id} | Get an invoice files
[**invoicesInvoiceIdFilesFileIdDelete**](InvoiceFilesApi.md#invoicesInvoiceIdFilesFileIdDelete) | **DELETE** /invoices/{invoice_id}/files/{file_id} | Delete invoice file



## createInvoiceFile

> CreateSuccessResponse createInvoiceFile(invoiceId, fileId, invoiceId2, opts)

Create a new invoice file

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.InvoiceFilesApi();
let invoiceId = "invoiceId_example"; // String | 
let fileId = "fileId_example"; // String | 
let invoiceId2 = "invoiceId_example"; // String | 
let opts = {
  'type': "type_example" // String | 
};
apiInstance.createInvoiceFile(invoiceId, fileId, invoiceId2, opts, (error, data, response) => {
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
 **invoiceId** | **String**|  | 
 **fileId** | **String**|  | 
 **invoiceId2** | **String**|  | 
 **type** | **String**|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getInvoiceFiles

> GetInvoiceFiles200Response getInvoiceFiles(invoiceId)

Get list of invoice files

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.InvoiceFilesApi();
let invoiceId = "invoiceId_example"; // String | 
apiInstance.getInvoiceFiles(invoiceId, (error, data, response) => {
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
 **invoiceId** | **String**|  | 

### Return type

[**GetInvoiceFiles200Response**](GetInvoiceFiles200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOneInvoiceFiles

> GetOneInvoiceFiles200Response getOneInvoiceFiles(invoiceId, fileId)

Get an invoice files

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.InvoiceFilesApi();
let invoiceId = "invoiceId_example"; // String | 
let fileId = "fileId_example"; // String | 
apiInstance.getOneInvoiceFiles(invoiceId, fileId, (error, data, response) => {
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
 **invoiceId** | **String**|  | 
 **fileId** | **String**|  | 

### Return type

[**GetOneInvoiceFiles200Response**](GetOneInvoiceFiles200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesInvoiceIdFilesFileIdDelete

> ClockingRecordsClockingRecordIdPut200Response invoicesInvoiceIdFilesFileIdDelete(invoiceId, fileId)

Delete invoice file

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

let apiInstance = new Apacta.InvoiceFilesApi();
let invoiceId = "invoiceId_example"; // String | 
let fileId = "fileId_example"; // String | 
apiInstance.invoicesInvoiceIdFilesFileIdDelete(invoiceId, fileId, (error, data, response) => {
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
 **invoiceId** | **String**|  | 
 **fileId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

