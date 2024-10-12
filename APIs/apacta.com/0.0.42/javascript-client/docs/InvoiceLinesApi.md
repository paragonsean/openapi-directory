# Apacta.InvoiceLinesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoiceLineTextsInvoiceLineTextIdPost**](InvoiceLinesApi.md#invoiceLineTextsInvoiceLineTextIdPost) | **POST** /invoice_line_texts/{invoice_line_text_id} | Edit invoice line text
[**invoiceLineTextsPost**](InvoiceLinesApi.md#invoiceLineTextsPost) | **POST** /invoice_line_texts/ | Add invoice line text
[**invoiceLinesGet**](InvoiceLinesApi.md#invoiceLinesGet) | **GET** /invoice_lines | View list of invoice lines
[**invoiceLinesInvoiceLineIdDelete**](InvoiceLinesApi.md#invoiceLinesInvoiceLineIdDelete) | **DELETE** /invoice_lines/{invoice_line_id} | Delete invoice line
[**invoiceLinesInvoiceLineIdGet**](InvoiceLinesApi.md#invoiceLinesInvoiceLineIdGet) | **GET** /invoice_lines/{invoice_line_id} | View invoice line
[**invoiceLinesInvoiceLineIdPut**](InvoiceLinesApi.md#invoiceLinesInvoiceLineIdPut) | **PUT** /invoice_lines/{invoice_line_id} | Edit invoice line
[**invoiceLinesPost**](InvoiceLinesApi.md#invoiceLinesPost) | **POST** /invoice_lines | Add invoice line



## invoiceLineTextsInvoiceLineTextIdPost

> EmptySuccessResponse invoiceLineTextsInvoiceLineTextIdPost(invoiceLineTextId, html, opts)

Edit invoice line text

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

let apiInstance = new Apacta.InvoiceLinesApi();
let invoiceLineTextId = "invoiceLineTextId_example"; // String | Automatically added
let html = "html_example"; // String | 
let opts = {
  'image': "/path/to/file" // File | 
};
apiInstance.invoiceLineTextsInvoiceLineTextIdPost(invoiceLineTextId, html, opts, (error, data, response) => {
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
 **invoiceLineTextId** | **String**| Automatically added | 
 **html** | **String**|  | 
 **image** | **File**|  | [optional] 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## invoiceLineTextsPost

> CreateSuccessResponse invoiceLineTextsPost(html, invoiceId, opts)

Add invoice line text

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

let apiInstance = new Apacta.InvoiceLinesApi();
let html = "html_example"; // String | 
let invoiceId = "invoiceId_example"; // String | 
let opts = {
  'image': "/path/to/file", // File | 
  'placement': 56 // Number | 
};
apiInstance.invoiceLineTextsPost(html, invoiceId, opts, (error, data, response) => {
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
 **html** | **String**|  | 
 **invoiceId** | **String**|  | 
 **image** | **File**|  | [optional] 
 **placement** | **Number**|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## invoiceLinesGet

> InvoiceLinesGet200Response invoiceLinesGet(opts)

View list of invoice lines

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

let apiInstance = new Apacta.InvoiceLinesApi();
let opts = {
  'invoiceId': "invoiceId_example", // String | 
  'productId': "productId_example", // String | 
  'userId': "userId_example", // String | 
  'name': "name_example", // String | 
  'discountText': "discountText_example" // String | 
};
apiInstance.invoiceLinesGet(opts, (error, data, response) => {
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
 **invoiceId** | **String**|  | [optional] 
 **productId** | **String**|  | [optional] 
 **userId** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **discountText** | **String**|  | [optional] 

### Return type

[**InvoiceLinesGet200Response**](InvoiceLinesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceLinesInvoiceLineIdDelete

> ClockingRecordsClockingRecordIdPut200Response invoiceLinesInvoiceLineIdDelete(invoiceLineId)

Delete invoice line

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

let apiInstance = new Apacta.InvoiceLinesApi();
let invoiceLineId = "invoiceLineId_example"; // String | 
apiInstance.invoiceLinesInvoiceLineIdDelete(invoiceLineId, (error, data, response) => {
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
 **invoiceLineId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceLinesInvoiceLineIdGet

> InvoiceLinesInvoiceLineIdGet200Response invoiceLinesInvoiceLineIdGet(invoiceLineId)

View invoice line

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

let apiInstance = new Apacta.InvoiceLinesApi();
let invoiceLineId = "invoiceLineId_example"; // String | 
apiInstance.invoiceLinesInvoiceLineIdGet(invoiceLineId, (error, data, response) => {
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
 **invoiceLineId** | **String**|  | 

### Return type

[**InvoiceLinesInvoiceLineIdGet200Response**](InvoiceLinesInvoiceLineIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceLinesInvoiceLineIdPut

> ClockingRecordsClockingRecordIdPut200Response invoiceLinesInvoiceLineIdPut(invoiceLineId, opts)

Edit invoice line

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

let apiInstance = new Apacta.InvoiceLinesApi();
let invoiceLineId = "invoiceLineId_example"; // String | 
let opts = {
  'invoiceLinesInvoiceLineIdPutRequest': new Apacta.InvoiceLinesInvoiceLineIdPutRequest() // InvoiceLinesInvoiceLineIdPutRequest | 
};
apiInstance.invoiceLinesInvoiceLineIdPut(invoiceLineId, opts, (error, data, response) => {
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
 **invoiceLineId** | **String**|  | 
 **invoiceLinesInvoiceLineIdPutRequest** | [**InvoiceLinesInvoiceLineIdPutRequest**](InvoiceLinesInvoiceLineIdPutRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invoiceLinesPost

> ClockingRecordsPost201Response invoiceLinesPost(opts)

Add invoice line

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

let apiInstance = new Apacta.InvoiceLinesApi();
let opts = {
  'invoiceLinesPostRequest': new Apacta.InvoiceLinesPostRequest() // InvoiceLinesPostRequest | 
};
apiInstance.invoiceLinesPost(opts, (error, data, response) => {
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
 **invoiceLinesPostRequest** | [**InvoiceLinesPostRequest**](InvoiceLinesPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

