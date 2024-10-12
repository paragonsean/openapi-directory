# XtrfHomePortalApi.ClientInvoicesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create1**](ClientInvoicesApi.md#create1) | **POST** /accounting/customers/invoices | Creates a new invoice.
[**createPayment**](ClientInvoicesApi.md#createPayment) | **POST** /accounting/customers/invoices/{invoiceId}/payments | Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated.
[**delete1**](ClientInvoicesApi.md#delete1) | **DELETE** /accounting/customers/invoices/{invoiceId} | Removes a client invoice.
[**delete2**](ClientInvoicesApi.md#delete2) | **DELETE** /accounting/customers/payments/{paymentId} | Removes a customer payment.
[**downloadDocuments**](ClientInvoicesApi.md#downloadDocuments) | **POST** /accounting/customers/invoices/documents | Generates client invoices&#39; documents.
[**duplicate**](ClientInvoicesApi.md#duplicate) | **POST** /accounting/customers/invoices/{invoiceId}/duplicate | Duplicate client invoice.
[**duplicateAsProForma**](ClientInvoicesApi.md#duplicateAsProForma) | **POST** /accounting/customers/invoices/{invoiceId}/duplicate/proForma | Duplicate client invoice as pro forma.
[**getAll**](ClientInvoicesApi.md#getAll) | **GET** /accounting/customers/invoices | Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date.
[**getAllIds**](ClientInvoicesApi.md#getAllIds) | **GET** /accounting/customers/invoices/ids | Returns client invoices&#39; internal identifiers.
[**getById**](ClientInvoicesApi.md#getById) | **GET** /accounting/customers/invoices/{invoiceId} | Returns client invoice details.
[**getDates**](ClientInvoicesApi.md#getDates) | **GET** /accounting/customers/invoices/{invoiceId}/dates | Returns dates of a given client invoice.
[**getDocument**](ClientInvoicesApi.md#getDocument) | **GET** /accounting/customers/invoices/{invoiceId}/document | Generates client invoice document (PDF).
[**getPaymentTerms**](ClientInvoicesApi.md#getPaymentTerms) | **GET** /accounting/customers/invoices/{invoiceId}/paymentTerms | Returns payment terms of a given client invoice.
[**getPayments**](ClientInvoicesApi.md#getPayments) | **GET** /accounting/customers/invoices/{invoiceId}/payments | Returns all payments for the client invoice.
[**sendReminder**](ClientInvoicesApi.md#sendReminder) | **POST** /accounting/customers/invoices/{invoiceId}/sendReminder | Sends reminder.
[**sendReminders**](ClientInvoicesApi.md#sendReminders) | **POST** /accounting/customers/invoices/sendReminders | Sends reminders. Returns number of sent e-mails.



## create1

> CustomerInvoiceCreateResultDTO create1(customerInvoiceCreateDTO)

Creates a new invoice.

Creates a new invoice from tasks. Tasks are grouped by client and currency, therefore multiple invoices can be created.If any of the tasks cannot be invoiced (ie. it is already invoiced, not invoiceable, not associated with a project) then an error is reported.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let customerInvoiceCreateDTO = /home-api/assets/examples/accounting/customers/invoices/createMultipleFromTasks.json#requestBody; // CustomerInvoiceCreateDTO | Created new invoice.
apiInstance.create1(customerInvoiceCreateDTO, (error, data, response) => {
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
 **customerInvoiceCreateDTO** | [**CustomerInvoiceCreateDTO**](CustomerInvoiceCreateDTO.md)| Created new invoice. | 

### Return type

[**CustomerInvoiceCreateResultDTO**](CustomerInvoiceCreateResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## createPayment

> createPayment(invoiceId, paymentDTO)

Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated.

Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
let paymentDTO = /home-api/assets/examples/accounting/customers/invoices/createPayment.json#requestBody; // PaymentDTO | New payment.
apiInstance.createPayment(invoiceId, paymentDTO, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 
 **paymentDTO** | [**PaymentDTO**](PaymentDTO.md)| New payment. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: Not defined


## delete1

> delete1(invoiceId)

Removes a client invoice.

Removes a client invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
apiInstance.delete1(invoiceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delete2

> delete2(paymentId)

Removes a customer payment.

Removes a customer payment.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let paymentId = 789; // Number | customer payment's internal identifier
apiInstance.delete2(paymentId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentId** | **Number**| customer payment&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## downloadDocuments

> UrlResultDTO downloadDocuments(downloadDocumentsRequestDTO)

Generates client invoices&#39; documents.

Generates client invoices&#39; documents.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let downloadDocumentsRequestDTO = /home-api/assets/examples/accounting/customers/invoices/downloadDocuments.json#requestBody; // DownloadDocumentsRequestDTO | Generated client invoices documents.
apiInstance.downloadDocuments(downloadDocumentsRequestDTO, (error, data, response) => {
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
 **downloadDocumentsRequestDTO** | [**DownloadDocumentsRequestDTO**](DownloadDocumentsRequestDTO.md)| Generated client invoices documents. | 

### Return type

[**UrlResultDTO**](UrlResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## duplicate

> CustomerInvoiceDTO duplicate(invoiceId)

Duplicate client invoice.

Duplicate client invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
apiInstance.duplicate(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 

### Return type

[**CustomerInvoiceDTO**](CustomerInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## duplicateAsProForma

> CustomerInvoiceDTO duplicateAsProForma(invoiceId)

Duplicate client invoice as pro forma.

Duplicate client invoice as pro forma.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
apiInstance.duplicateAsProForma(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 

### Return type

[**CustomerInvoiceDTO**](CustomerInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getAll

> [CustomerInvoiceDTO] getAll(opts)

Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let opts = {
  'updatedSince': 789 // Number | only client invoices modified since this timestamp
};
apiInstance.getAll(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only client invoices modified since this timestamp | [optional] 

### Return type

[**[CustomerInvoiceDTO]**](CustomerInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getAllIds

> [Number] getAllIds(opts)

Returns client invoices&#39; internal identifiers.

Returns client invoices&#39; internal identifiers.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let opts = {
  'updatedSince': 789 // Number | only client invoices modified since this timestamp
};
apiInstance.getAllIds(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only client invoices modified since this timestamp | [optional] 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getById

> CustomerInvoiceDTO getById(invoiceId, opts)

Returns client invoice details.

Returns client invoice details.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
let opts = {
  'embed': "embed_example" // String | list of adittional fields which should be embedded in the response (ie. tasks)
};
apiInstance.getById(invoiceId, opts, (error, data, response) => {
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
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 
 **embed** | **String**| list of adittional fields which should be embedded in the response (ie. tasks) | [optional] 

### Return type

[**CustomerInvoiceDTO**](CustomerInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getDates

> CustomerInvoiceDatesDTO getDates(invoiceId)

Returns dates of a given client invoice.

Returns dates of a given client invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
apiInstance.getDates(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 

### Return type

[**CustomerInvoiceDatesDTO**](CustomerInvoiceDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getDocument

> UrlResultDTO getDocument(invoiceId)

Generates client invoice document (PDF).

Generates client invoice document (PDF).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
apiInstance.getDocument(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 

### Return type

[**UrlResultDTO**](UrlResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getPaymentTerms

> PaymentTermsDTO getPaymentTerms(invoiceId)

Returns payment terms of a given client invoice.

Returns payment terms of a given client invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
apiInstance.getPaymentTerms(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 

### Return type

[**PaymentTermsDTO**](PaymentTermsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getPayments

> [PaymentDTO] getPayments(invoiceId)

Returns all payments for the client invoice.

Returns all payments for the client invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
apiInstance.getPayments(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 

### Return type

[**[PaymentDTO]**](PaymentDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## sendReminder

> sendReminder(invoiceId)

Sends reminder.

Sends reminder.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let invoiceId = 789; // Number | client invoice's internal identifier
apiInstance.sendReminder(invoiceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoiceId** | **Number**| client invoice&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sendReminders

> SendRemindersResponseDTO sendReminders(sendRemindersRequestDTO)

Sends reminders. Returns number of sent e-mails.

Sends reminders. Returns number of sent e-mails.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientInvoicesApi();
let sendRemindersRequestDTO = /home-api/assets/examples/accounting/customers/invoices/sendReminders.json#requestBody; // SendRemindersRequestDTO | Number of sent e-mails.
apiInstance.sendReminders(sendRemindersRequestDTO, (error, data, response) => {
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
 **sendRemindersRequestDTO** | [**SendRemindersRequestDTO**](SendRemindersRequestDTO.md)| Number of sent e-mails. | 

### Return type

[**SendRemindersResponseDTO**](SendRemindersResponseDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

