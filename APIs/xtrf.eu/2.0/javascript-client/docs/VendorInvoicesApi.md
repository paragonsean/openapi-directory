# XtrfHomePortalApi.VendorInvoicesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create4**](VendorInvoicesApi.md#create4) | **POST** /accounting/providers/invoices | Creates a new invoice.
[**createPayment1**](VendorInvoicesApi.md#createPayment1) | **POST** /accounting/providers/invoices/{invoiceId}/payments | Creates a new payment on the vendor account and assigns the payment to the invoice.
[**delete6**](VendorInvoicesApi.md#delete6) | **DELETE** /accounting/providers/invoices/{invoiceId} | Removes a provider invoice.
[**delete7**](VendorInvoicesApi.md#delete7) | **DELETE** /accounting/providers/payments/{paymentId} | Removes a provider payment.
[**getAll2**](VendorInvoicesApi.md#getAll2) | **GET** /accounting/providers/invoices | Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date.
[**getAllIds3**](VendorInvoicesApi.md#getAllIds3) | **GET** /accounting/providers/invoices/ids | Returns vendor invoices&#39; internal identifiers.
[**getById3**](VendorInvoicesApi.md#getById3) | **GET** /accounting/providers/invoices/{invoiceId} | Returns provider invoice details.
[**getDocument1**](VendorInvoicesApi.md#getDocument1) | **GET** /accounting/providers/invoices/{invoiceId}/document | Generates provider invoice document (PDF).
[**getPayments1**](VendorInvoicesApi.md#getPayments1) | **GET** /accounting/providers/invoices/{invoiceId}/payments | Returns all payments for the vendor invoice.
[**send**](VendorInvoicesApi.md#send) | **POST** /accounting/providers/invoices/{invoiceId}/send | Sends a provider invoice.
[**setStatus**](VendorInvoicesApi.md#setStatus) | **POST** /accounting/providers/invoices/{invoiceId}/status | Changes invoice status to given status.



## create4

> ProviderInvoiceCreateResultDTO create4(providerInvoiceCreateDTO)

Creates a new invoice.

Creates a new invoice from jobs. Jobs are grouped by provider and currency, therefore multiple invoices can be created.If any of the jobs cannot be invoiced (ie. it is already invoiced) then an error is reported.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let providerInvoiceCreateDTO = /home-api/assets/examples/accounting/providers/invoices/createSingleFromJobs.json#requestBody; // ProviderInvoiceCreateDTO | Created new invoice.
apiInstance.create4(providerInvoiceCreateDTO, (error, data, response) => {
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
 **providerInvoiceCreateDTO** | [**ProviderInvoiceCreateDTO**](ProviderInvoiceCreateDTO.md)| Created new invoice. | 

### Return type

[**ProviderInvoiceCreateResultDTO**](ProviderInvoiceCreateResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## createPayment1

> createPayment1(invoiceId, paymentDTO)

Creates a new payment on the vendor account and assigns the payment to the invoice.

Creates a new payment on the vendor account and assigns the payment to the invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let invoiceId = 789; // Number | vendor invoice's internal identifier
let paymentDTO = /home-api/assets/examples/accounting/providers/invoices/createPayment.json#requestBody; // PaymentDTO | New payment.
apiInstance.createPayment1(invoiceId, paymentDTO, (error, data, response) => {
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
 **invoiceId** | **Number**| vendor invoice&#39;s internal identifier | 
 **paymentDTO** | [**PaymentDTO**](PaymentDTO.md)| New payment. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: Not defined


## delete6

> delete6(invoiceId)

Removes a provider invoice.

Removes a provider invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let invoiceId = 789; // Number | provider invoice's internal identifier
apiInstance.delete6(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| provider invoice&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delete7

> delete7(paymentId)

Removes a provider payment.

Removes a provider payment.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let paymentId = 789; // Number | provider payment's internal identifier
apiInstance.delete7(paymentId, (error, data, response) => {
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
 **paymentId** | **Number**| provider payment&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAll2

> [ProviderInvoiceDTO] getAll2(opts)

Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let opts = {
  'updatedSince': 789 // Number | only vendor invoices modified since this timestamp
};
apiInstance.getAll2(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only vendor invoices modified since this timestamp | [optional] 

### Return type

[**[ProviderInvoiceDTO]**](ProviderInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getAllIds3

> [Number] getAllIds3(opts)

Returns vendor invoices&#39; internal identifiers.

Returns vendor invoices&#39; internal identifiers.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let opts = {
  'updatedSince': 789 // Number | only vendor invoices modified since this timestamp
};
apiInstance.getAllIds3(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only vendor invoices modified since this timestamp | [optional] 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getById3

> ProviderInvoiceDTO getById3(invoiceId)

Returns provider invoice details.

Returns provider invoice details.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let invoiceId = 789; // Number | provider invoice's internal identifier
apiInstance.getById3(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| provider invoice&#39;s internal identifier | 

### Return type

[**ProviderInvoiceDTO**](ProviderInvoiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getDocument1

> UrlResultDTO getDocument1(invoiceId)

Generates provider invoice document (PDF).

Generates provider invoice document (PDF).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let invoiceId = 789; // Number | provider invoice's internal identifier
apiInstance.getDocument1(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| provider invoice&#39;s internal identifier | 

### Return type

[**UrlResultDTO**](UrlResultDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getPayments1

> [PaymentDTO] getPayments1(invoiceId)

Returns all payments for the vendor invoice.

Returns all payments for the vendor invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let invoiceId = 789; // Number | vendor invoice's internal identifier
apiInstance.getPayments1(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| vendor invoice&#39;s internal identifier | 

### Return type

[**[PaymentDTO]**](PaymentDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## send

> send(invoiceId)

Sends a provider invoice.

Sends a provider invoice.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let invoiceId = 789; // Number | provider invoice's internal identifier
apiInstance.send(invoiceId, (error, data, response) => {
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
 **invoiceId** | **Number**| provider invoice&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setStatus

> setStatus(invoiceId, statusRequestDTO)

Changes invoice status to given status.

Changes invoice status to given status.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.VendorInvoicesApi();
let invoiceId = 789; // Number | provider invoice's internal identifier
let statusRequestDTO = /home-api/assets/examples/accounting/providers/invoices/setStatus.json#requestBody; // StatusRequestDTO | Changed invoice status to given status.
apiInstance.setStatus(invoiceId, statusRequestDTO, (error, data, response) => {
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
 **invoiceId** | **Number**| provider invoice&#39;s internal identifier | 
 **statusRequestDTO** | [**StatusRequestDTO**](StatusRequestDTO.md)| Changed invoice status to given status. | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

