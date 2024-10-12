# CustomerCreditApi.InvoicesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelInvoice**](InvoicesApi.md#cancelInvoice) | **DELETE** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId} | Cancel Invoice
[**changeInvoice**](InvoicesApi.md#changeInvoice) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId} | Change Invoice
[**markaninvoiceasPaid**](InvoicesApi.md#markaninvoiceasPaid) | **POST** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId}/payments | Mark an invoice as Paid
[**postponeaninvoice**](InvoicesApi.md#postponeaninvoice) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId}/postponement | Postpone an invoice
[**retrieveInvoicebyId**](InvoicesApi.md#retrieveInvoicebyId) | **GET** /api/creditcontrol/accounts/{creditAccountId}/invoices/{invoiceId} | Retrieve Invoice by Id
[**searchallinvoices**](InvoicesApi.md#searchallinvoices) | **GET** /api/creditcontrol/invoices | Search all invoices
[**searchallinvoicesofaAccount**](InvoicesApi.md#searchallinvoicesofaAccount) | **GET** /api/creditcontrol/accounts/{creditAccountId}/invoices | Retrieve invoice by creditAccountId



## cancelInvoice

> Object cancelInvoice(contentType, accept, creditAccountId, invoiceId)

Cancel Invoice

Changes invoice&#39;s status from ancells invoice by specified Id.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.InvoicesApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let invoiceId = "'insert identifier here'"; // String | 
apiInstance.cancelInvoice(contentType, accept, creditAccountId, invoiceId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **invoiceId** | **String**|  | [default to &#39;insert identifier here&#39;]

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## changeInvoice

> Object changeInvoice(creditAccountId, invoiceId, accept, contentType, changeInvoiceRequest1, opts)

Change Invoice

Updates invoice&#39;s attributes &#x60;status&#x60;, &#x60;paymentLink&#x60; and &#x60;observation&#x60;.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.InvoicesApi();
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let invoiceId = "'insert identifier here'"; // String | 
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let changeInvoiceRequest1 = {"observation":"string (optional)","paymentLink":"string (URL) (optional)","status":"string"}; // ChangeInvoiceRequest1 | 
let opts = {
  'friendlyId': "'insert identifier here'" // String | Invoice's identification
};
apiInstance.changeInvoice(creditAccountId, invoiceId, accept, contentType, changeInvoiceRequest1, opts, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **invoiceId** | **String**|  | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **changeInvoiceRequest1** | [**ChangeInvoiceRequest1**](ChangeInvoiceRequest1.md)|  | 
 **friendlyId** | **String**| Invoice&#39;s identification | [optional] [default to &#39;insert identifier here&#39;]

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## markaninvoiceasPaid

> String markaninvoiceasPaid(creditAccountId, invoiceId, accept, contentType, markaninvoiceasPaidRequest1)

Mark an invoice as Paid

Pay an invoice.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.InvoicesApi();
let creditAccountId = "'isert indentifier here'"; // String | Credit account's identification
let invoiceId = "'insert identifier here'"; // String | 
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let markaninvoiceasPaidRequest1 = {"value":"number (FULL invoice value [deprecated])"}; // MarkaninvoiceasPaidRequest1 | 
apiInstance.markaninvoiceasPaid(creditAccountId, invoiceId, accept, contentType, markaninvoiceasPaidRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;isert indentifier here&#39;]
 **invoiceId** | **String**|  | [default to &#39;insert identifier here&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **markaninvoiceasPaidRequest1** | [**MarkaninvoiceasPaidRequest1**](MarkaninvoiceasPaidRequest1.md)|  | 

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## postponeaninvoice

> Object postponeaninvoice(creditAccountId, invoiceId, accept, contentType, postponeaninvoiceRequest1)

Postpone an invoice

Postpone an invoice.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.InvoicesApi();
let creditAccountId = "creditAccountId_example"; // String | Credit account's identification
let invoiceId = "invoiceId_example"; // String | 
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let postponeaninvoiceRequest1 = {"dueDays":"number (integer)"}; // PostponeaninvoiceRequest1 | 
apiInstance.postponeaninvoice(creditAccountId, invoiceId, accept, contentType, postponeaninvoiceRequest1, (error, data, response) => {
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
 **creditAccountId** | **String**| Credit account&#39;s identification | 
 **invoiceId** | **String**|  | 
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **postponeaninvoiceRequest1** | [**PostponeaninvoiceRequest1**](PostponeaninvoiceRequest1.md)|  | 

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## retrieveInvoicebyId

> Retrievedinvoice1 retrieveInvoicebyId(contentType, accept, creditAccountId, invoiceId)

Retrieve Invoice by Id

Returns associated data for the specified Invoice Id, like status  and value, for example.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.InvoicesApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let creditAccountId = "'insert identifier here'"; // String | Credit account's identification
let invoiceId = "'insert identifier here'"; // String | 
apiInstance.retrieveInvoicebyId(contentType, accept, creditAccountId, invoiceId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **creditAccountId** | **String**| Credit account&#39;s identification | [default to &#39;insert identifier here&#39;]
 **invoiceId** | **String**|  | [default to &#39;insert identifier here&#39;]

### Return type

[**Retrievedinvoice1**](Retrievedinvoice1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## searchallinvoices

> Paidinvoices1 searchallinvoices(contentType, accept, opts)

Search all invoices

Returns all invoices according to the informed query params in the request.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.InvoicesApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let opts = {
  'from': "''", // String | 
  'to': "''", // String | 
  'createdDateFrom': "", // String | 
  'createdDateTo': "", // String | 
  'value': 3.4, // Number | Invoice's value. It must be completed with a decimal value.
  'status': "'Paid'", // String | Invoice's status. It must be completed with \"Paid\", \"Cancelled\" or \"Open\" value.
  'friendlyId': "'insert identifier here'", // String | Invoice's identifier
  'creditAccountId': "'B75F0'" // String | Credit account's identifier
};
apiInstance.searchallinvoices(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **from** | **String**|  | [optional] [default to &#39;&#39;]
 **to** | **String**|  | [optional] [default to &#39;&#39;]
 **createdDateFrom** | **String**|  | [optional] 
 **createdDateTo** | **String**|  | [optional] 
 **value** | **Number**| Invoice&#39;s value. It must be completed with a decimal value. | [optional] 
 **status** | **String**| Invoice&#39;s status. It must be completed with \&quot;Paid\&quot;, \&quot;Cancelled\&quot; or \&quot;Open\&quot; value. | [optional] [default to &#39;Paid&#39;]
 **friendlyId** | **String**| Invoice&#39;s identifier | [optional] [default to &#39;insert identifier here&#39;]
 **creditAccountId** | **String**| Credit account&#39;s identifier | [optional] [default to &#39;B75F0&#39;]

### Return type

[**Paidinvoices1**](Paidinvoices1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## searchallinvoicesofaAccount

> Getinvoicesfromacheckingaccount1 searchallinvoicesofaAccount(contentType, accept, creditAccountId)

Retrieve invoice by creditAccountId

Returns associated invoices by specified creditAccountId, the param that identifies a client in VTEX&#39;s system.

### Example

```javascript
import CustomerCreditApi from 'customer_credit_api';
let defaultClient = CustomerCreditApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CustomerCreditApi.InvoicesApi();
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let creditAccountId = "'insert identifier here'"; // String | 
apiInstance.searchallinvoicesofaAccount(contentType, accept, creditAccountId, (error, data, response) => {
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
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **creditAccountId** | **String**|  | [default to &#39;insert identifier here&#39;]

### Return type

[**Getinvoicesfromacheckingaccount1**](Getinvoicesfromacheckingaccount1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

