# StorecoveApi.InvoiceSubmissionsApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInvoiceSubmission**](InvoiceSubmissionsApi.md#createInvoiceSubmission) | **POST** /invoice_submissions | Submit a new invoice
[**preflightInvoiceRecipient**](InvoiceSubmissionsApi.md#preflightInvoiceRecipient) | **POST** /invoice_submissions/preflight | DEPRECATED. Preflight an invoice recipient
[**showInvoiceSubmissionEvidence**](InvoiceSubmissionsApi.md#showInvoiceSubmissionEvidence) | **GET** /invoice_submissions/{guid}/evidence | DEPRECATED. Get InvoiceSubmission Evidence



## createInvoiceSubmission

> InvoiceSubmissionResult createInvoiceSubmission(invoiceSubmission)

Submit a new invoice

DEPRECATED. Use the new /document_submissions endpoint. Submit an invoice for delivery.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.InvoiceSubmissionsApi();
let invoiceSubmission = new StorecoveApi.InvoiceSubmission(); // InvoiceSubmission | Invoice to submit
apiInstance.createInvoiceSubmission(invoiceSubmission, (error, data, response) => {
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
 **invoiceSubmission** | [**InvoiceSubmission**](InvoiceSubmission.md)| Invoice to submit | 

### Return type

[**InvoiceSubmissionResult**](InvoiceSubmissionResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## preflightInvoiceRecipient

> PreflightInvoiceRecipientResult preflightInvoiceRecipient(invoiceRecipientPreflight)

DEPRECATED. Preflight an invoice recipient

Deprecated. Use the new /discovery endpoint. Check whether Storecove can deliver an invoice for a list of ids.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.InvoiceSubmissionsApi();
let invoiceRecipientPreflight = new StorecoveApi.InvoiceRecipientPreflight(); // InvoiceRecipientPreflight | The invoice recipient to preflight
apiInstance.preflightInvoiceRecipient(invoiceRecipientPreflight, (error, data, response) => {
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
 **invoiceRecipientPreflight** | [**InvoiceRecipientPreflight**](InvoiceRecipientPreflight.md)| The invoice recipient to preflight | 

### Return type

[**PreflightInvoiceRecipientResult**](PreflightInvoiceRecipientResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## showInvoiceSubmissionEvidence

> InvoiceSubmissionEvidence showInvoiceSubmissionEvidence(guid)

DEPRECATED. Get InvoiceSubmission Evidence

Deprecated. Use the new /document_submissions/{guid}/evidence endpoint. Get evidence for an InvoiceSubmission by GUID with corresponding status

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.InvoiceSubmissionsApi();
let guid = "guid_example"; // String | InvoiceSubmission GUID
apiInstance.showInvoiceSubmissionEvidence(guid, (error, data, response) => {
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
 **guid** | **String**| InvoiceSubmission GUID | 

### Return type

[**InvoiceSubmissionEvidence**](InvoiceSubmissionEvidence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

