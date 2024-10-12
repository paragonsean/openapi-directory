# Apacta.InvoicesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteInvoices**](InvoicesApi.md#bulkDeleteInvoices) | **DELETE** /invoices/bulkDelete | Bulk delete invoices
[**invoicesGet**](InvoicesApi.md#invoicesGet) | **GET** /invoices | View list of invoices
[**invoicesInvoiceIdCopyPost**](InvoicesApi.md#invoicesInvoiceIdCopyPost) | **POST** /invoices/{invoice_id}/copy | Create a copy of an invoice
[**invoicesInvoiceIdDelete**](InvoicesApi.md#invoicesInvoiceIdDelete) | **DELETE** /invoices/{invoice_id} | Delete invoice
[**invoicesInvoiceIdGet**](InvoicesApi.md#invoicesInvoiceIdGet) | **GET** /invoices/{invoice_id} | View invoice
[**invoicesInvoiceIdLinkProjectPdfPost**](InvoicesApi.md#invoicesInvoiceIdLinkProjectPdfPost) | **POST** /invoices/{invoice_id}/linkProjectPdf | Creates an invoice file containing the project&#39;s pdf overview
[**invoicesInvoiceIdPut**](InvoicesApi.md#invoicesInvoiceIdPut) | **PUT** /invoices/{invoice_id} | Edit invoice
[**invoicesInvoiceIdUnlinkProjectPdfPost**](InvoicesApi.md#invoicesInvoiceIdUnlinkProjectPdfPost) | **POST** /invoices/{invoice_id}/unlinkProjectPdf | Deletes the linked project overview pdf
[**invoicesPost**](InvoicesApi.md#invoicesPost) | **POST** /invoices | Add invoice
[**invoicesVatOptionsGet**](InvoicesApi.md#invoicesVatOptionsGet) | **GET** /invoices/vatOptions | List VAT options



## bulkDeleteInvoices

> EmptySuccessResponse bulkDeleteInvoices(bulkActionRequestBody)

Bulk delete invoices

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

let apiInstance = new Apacta.InvoicesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Invoices ids
apiInstance.bulkDeleteInvoices(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Invoices ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invoicesGet

> InvoicesGet200Response invoicesGet(opts)

View list of invoices

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

let apiInstance = new Apacta.InvoicesApi();
let opts = {
  'contactId': "contactId_example", // String | Used to filter on the `contact_id` of the invoices
  'projectId': "projectId_example", // String | Used to filter on the `project_id` of the invoices
  'invoiceNumber': "invoiceNumber_example", // String | Used to filter on the `invoice_number` of the invoices
  'offerNumber': "offerNumber_example", // String | 
  'isDraft': 56, // Number | 
  'isOffer': 56, // Number | 
  'isLocked': 56, // Number | 
  'isFixedPrice': 56, // Number | 
  'dateFrom': new Date("2013-10-20"), // Date | 
  'dateTo': new Date("2013-10-20"), // Date | 
  'issuedDate': new Date("2013-10-20"), // Date | 
  'sentAsDraft': 56 // Number | Used to filter invoices which are sent as draft to integration
};
apiInstance.invoicesGet(opts, (error, data, response) => {
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
 **contactId** | **String**| Used to filter on the &#x60;contact_id&#x60; of the invoices | [optional] 
 **projectId** | **String**| Used to filter on the &#x60;project_id&#x60; of the invoices | [optional] 
 **invoiceNumber** | **String**| Used to filter on the &#x60;invoice_number&#x60; of the invoices | [optional] 
 **offerNumber** | **String**|  | [optional] 
 **isDraft** | **Number**|  | [optional] 
 **isOffer** | **Number**|  | [optional] 
 **isLocked** | **Number**|  | [optional] 
 **isFixedPrice** | **Number**|  | [optional] 
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 
 **issuedDate** | **Date**|  | [optional] 
 **sentAsDraft** | **Number**| Used to filter invoices which are sent as draft to integration | [optional] 

### Return type

[**InvoicesGet200Response**](InvoicesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesInvoiceIdCopyPost

> CreateSuccessResponse invoicesInvoiceIdCopyPost(invoiceId, opts)

Create a copy of an invoice

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

let apiInstance = new Apacta.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | 
let opts = {
  'projectId': "projectId_example", // String | 
  'contactId': "contactId_example" // String | 
};
apiInstance.invoicesInvoiceIdCopyPost(invoiceId, opts, (error, data, response) => {
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
 **projectId** | **String**|  | [optional] 
 **contactId** | **String**|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesInvoiceIdDelete

> ClockingRecordsClockingRecordIdPut200Response invoicesInvoiceIdDelete(invoiceId)

Delete invoice

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

let apiInstance = new Apacta.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | 
apiInstance.invoicesInvoiceIdDelete(invoiceId, (error, data, response) => {
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

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesInvoiceIdGet

> InvoicesInvoiceIdGet200Response invoicesInvoiceIdGet(invoiceId)

View invoice

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

let apiInstance = new Apacta.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | 
apiInstance.invoicesInvoiceIdGet(invoiceId, (error, data, response) => {
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

[**InvoicesInvoiceIdGet200Response**](InvoicesInvoiceIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesInvoiceIdLinkProjectPdfPost

> EmptySuccessResponse invoicesInvoiceIdLinkProjectPdfPost(invoiceId)

Creates an invoice file containing the project&#39;s pdf overview

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

let apiInstance = new Apacta.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | 
apiInstance.invoicesInvoiceIdLinkProjectPdfPost(invoiceId, (error, data, response) => {
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

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesInvoiceIdPut

> ClockingRecordsClockingRecordIdPut200Response invoicesInvoiceIdPut(invoiceId, opts)

Edit invoice

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

let apiInstance = new Apacta.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | 
let opts = {
  'invoicesInvoiceIdPutRequest': new Apacta.InvoicesInvoiceIdPutRequest() // InvoicesInvoiceIdPutRequest | 
};
apiInstance.invoicesInvoiceIdPut(invoiceId, opts, (error, data, response) => {
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
 **invoicesInvoiceIdPutRequest** | [**InvoicesInvoiceIdPutRequest**](InvoicesInvoiceIdPutRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invoicesInvoiceIdUnlinkProjectPdfPost

> EmptySuccessResponse invoicesInvoiceIdUnlinkProjectPdfPost(invoiceId)

Deletes the linked project overview pdf

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

let apiInstance = new Apacta.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | 
apiInstance.invoicesInvoiceIdUnlinkProjectPdfPost(invoiceId, (error, data, response) => {
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

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesPost

> ClockingRecordsPost201Response invoicesPost(opts)

Add invoice

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

let apiInstance = new Apacta.InvoicesApi();
let opts = {
  'invoicesPostRequest': new Apacta.InvoicesPostRequest() // InvoicesPostRequest | 
};
apiInstance.invoicesPost(opts, (error, data, response) => {
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
 **invoicesPostRequest** | [**InvoicesPostRequest**](InvoicesPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invoicesVatOptionsGet

> IntegrationsProductsSyncGet200Response invoicesVatOptionsGet()

List VAT options

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

let apiInstance = new Apacta.InvoicesApi();
apiInstance.invoicesVatOptionsGet((error, data, response) => {
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

[**IntegrationsProductsSyncGet200Response**](IntegrationsProductsSyncGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

