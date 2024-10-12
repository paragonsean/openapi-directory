# BillingoApiV3.DocumentApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelDocument**](DocumentApi.md#cancelDocument) | **POST** /documents/{id}/cancel | Cancel a document
[**createDocument**](DocumentApi.md#createDocument) | **POST** /documents | Create a document
[**createDocumentFromProforma**](DocumentApi.md#createDocumentFromProforma) | **POST** /documents/{id}/create-from-proforma | Create a document from proforma.
[**deletePayment**](DocumentApi.md#deletePayment) | **DELETE** /documents/{id}/payments | Delete all payment history on document
[**downloadDocument**](DocumentApi.md#downloadDocument) | **GET** /documents/{id}/download | Download a document in PDF format.
[**getDocument**](DocumentApi.md#getDocument) | **GET** /documents/{id} | Retrieve a document
[**getOnlineSzamlaStatus**](DocumentApi.md#getOnlineSzamlaStatus) | **GET** /documents/{id}/online-szamla | Retrieve a document Online Számla status
[**getPayment**](DocumentApi.md#getPayment) | **GET** /documents/{id}/payments | Retrieve a payment histroy
[**getPublicUrl**](DocumentApi.md#getPublicUrl) | **GET** /documents/{id}/public-url | Retrieve a document download public url.
[**listDocument**](DocumentApi.md#listDocument) | **GET** /documents | List all documents
[**sendDocument**](DocumentApi.md#sendDocument) | **POST** /documents/{id}/send | Send invoice to given email adresses.
[**updatePayment**](DocumentApi.md#updatePayment) | **PUT** /documents/{id}/payments | Update payment history



## cancelDocument

> Document cancelDocument(id)

Cancel a document

Cancel a document. Returns a cancellation document object if the cancellation is succeded.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
apiInstance.cancelDocument(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDocument

> Document createDocument(documentInsert)

Create a document

Create a new document. Returns a document object if the create is succeded.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let documentInsert = new BillingoApiV3.DocumentInsert(); // DocumentInsert | DocumentInsert object that you would like to store.
apiInstance.createDocument(documentInsert, (error, data, response) => {
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
 **documentInsert** | [**DocumentInsert**](DocumentInsert.md)| DocumentInsert object that you would like to store. | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDocumentFromProforma

> Document createDocumentFromProforma(id)

Create a document from proforma.

Create a new document from proforma. Returns a document object if the create is succeded.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
apiInstance.createDocumentFromProforma(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePayment

> [PaymentHistory] deletePayment(id)

Delete all payment history on document

Delete all exist payment history on document.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
apiInstance.deletePayment(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**[PaymentHistory]**](PaymentHistory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## downloadDocument

> File downloadDocument(id)

Download a document in PDF format.

Download a document. Returns a document in PDF format.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
apiInstance.downloadDocument(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

**File**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json


## getDocument

> Document getDocument(id)

Retrieve a document

Retrieves the details of an existing document.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
apiInstance.getDocument(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOnlineSzamlaStatus

> OnlineSzamlaStatus getOnlineSzamlaStatus(id)

Retrieve a document Online Számla status

Retrieves the details of an existing document status.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
apiInstance.getOnlineSzamlaStatus(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**OnlineSzamlaStatus**](OnlineSzamlaStatus.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayment

> [PaymentHistory] getPayment(id)

Retrieve a payment histroy

Retrieves the details of payment history an existing document.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
apiInstance.getPayment(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**[PaymentHistory]**](PaymentHistory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicUrl

> DocumentPublicUrl getPublicUrl(id)

Retrieve a document download public url.

Retrieves public url to download an existing document.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
apiInstance.getPublicUrl(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**DocumentPublicUrl**](DocumentPublicUrl.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDocument

> DocumentList listDocument(opts)

List all documents

Returns a list of your documents. The documents are returned sorted by creation date, with the most recent documents appearing first.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let opts = {
  'page': 56, // Number | 
  'perPage': 25, // Number | 
  'blockId': 56, // Number | Filter documents by the identifier of your DocumentBlock.
  'partnerId': 56, // Number | Filter documents by the identifier of your Partner.
  'paymentMethod': new BillingoApiV3.PaymentMethod(), // PaymentMethod | Filter documents by PaymentMethod value.
  'paymentStatus': new BillingoApiV3.PaymentStatus(), // PaymentStatus | Filter documents by PaymentStatus value.
  'startDate': new Date("2020-05-15"), // Date | Filter documents by date.
  'endDate': new Date("2020-05-15"), // Date | Filter documents by date.
  'startNumber': 1, // Number | Starting number of the document, should not contain year or any other formatting. Required if `start_year` given
  'endNumber': 10, // Number | Ending number of the document, should not contain year or any other formatting. Required if `end_year` given
  'startYear': 2020, // Number | Year for `start_number` parameter. Required if `start_number` given.
  'endYear': 2020 // Number | Year for `end_number` parameter. Required if `end_number` given.
};
apiInstance.listDocument(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] [default to 25]
 **blockId** | **Number**| Filter documents by the identifier of your DocumentBlock. | [optional] 
 **partnerId** | **Number**| Filter documents by the identifier of your Partner. | [optional] 
 **paymentMethod** | [**PaymentMethod**](.md)| Filter documents by PaymentMethod value. | [optional] 
 **paymentStatus** | [**PaymentStatus**](.md)| Filter documents by PaymentStatus value. | [optional] 
 **startDate** | **Date**| Filter documents by date. | [optional] 
 **endDate** | **Date**| Filter documents by date. | [optional] 
 **startNumber** | **Number**| Starting number of the document, should not contain year or any other formatting. Required if &#x60;start_year&#x60; given | [optional] 
 **endNumber** | **Number**| Ending number of the document, should not contain year or any other formatting. Required if &#x60;end_year&#x60; given | [optional] 
 **startYear** | **Number**| Year for &#x60;start_number&#x60; parameter. Required if &#x60;start_number&#x60; given. | [optional] 
 **endYear** | **Number**| Year for &#x60;end_number&#x60; parameter. Required if &#x60;end_number&#x60; given. | [optional] 

### Return type

[**DocumentList**](DocumentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendDocument

> SendDocument sendDocument(id, opts)

Send invoice to given email adresses.

Returns a list of emails, where the invoice is sent.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
let opts = {
  'sendDocument': new BillingoApiV3.SendDocument() // SendDocument | List of email-s where you want to send the invoice.
};
apiInstance.sendDocument(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **sendDocument** | [**SendDocument**](SendDocument.md)| List of email-s where you want to send the invoice. | [optional] 

### Return type

[**SendDocument**](SendDocument.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePayment

> [PaymentHistory] updatePayment(id, paymentHistory)

Update payment history

Update payment history an existing document. Returns a payment history object if the update is succeded.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.DocumentApi();
let id = 56; // Number | 
let paymentHistory = [new BillingoApiV3.PaymentHistory()]; // [PaymentHistory] | Payment history object that you would like to update.
apiInstance.updatePayment(id, paymentHistory, (error, data, response) => {
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
 **id** | **Number**|  | 
 **paymentHistory** | [**[PaymentHistory]**](PaymentHistory.md)| Payment history object that you would like to update. | 

### Return type

[**[PaymentHistory]**](PaymentHistory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

