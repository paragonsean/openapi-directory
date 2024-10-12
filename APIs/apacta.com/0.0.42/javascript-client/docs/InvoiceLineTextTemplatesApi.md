# Apacta.InvoiceLineTextTemplatesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoiceLineTextTemplateGet**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateGet) | **GET** /invoice_line_text_template | Get a list of invoice line text templates
[**invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete) | **DELETE** /invoice_line_text_template/{invoice_line_text_template_id} | Delete an invoice line text template
[**invoiceLineTextTemplateInvoiceLineTextTemplateIdGet**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdGet) | **GET** /invoice_line_text_template/{invoice_line_text_template_id} | Get a single invoice line text template
[**invoiceLineTextTemplateInvoiceLineTextTemplateIdPost**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdPost) | **POST** /invoice_line_text_template/{invoice_line_text_template_id} | Edit an invoice line text template
[**invoiceLineTextTemplatePost**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplatePost) | **POST** /invoice_line_text_template | Add a new invoice line text template



## invoiceLineTextTemplateGet

> InvoiceLineTextTemplateGet200Response invoiceLineTextTemplateGet()

Get a list of invoice line text templates

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

let apiInstance = new Apacta.InvoiceLineTextTemplatesApi();
apiInstance.invoiceLineTextTemplateGet((error, data, response) => {
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

[**InvoiceLineTextTemplateGet200Response**](InvoiceLineTextTemplateGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete

> EmptySuccessResponse invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete(invoiceLineTextTemplateId)

Delete an invoice line text template

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

let apiInstance = new Apacta.InvoiceLineTextTemplatesApi();
let invoiceLineTextTemplateId = "invoiceLineTextTemplateId_example"; // String | 
apiInstance.invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete(invoiceLineTextTemplateId, (error, data, response) => {
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
 **invoiceLineTextTemplateId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceLineTextTemplateInvoiceLineTextTemplateIdGet

> InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response invoiceLineTextTemplateInvoiceLineTextTemplateIdGet(invoiceLineTextTemplateId)

Get a single invoice line text template

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

let apiInstance = new Apacta.InvoiceLineTextTemplatesApi();
let invoiceLineTextTemplateId = "invoiceLineTextTemplateId_example"; // String | 
apiInstance.invoiceLineTextTemplateInvoiceLineTextTemplateIdGet(invoiceLineTextTemplateId, (error, data, response) => {
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
 **invoiceLineTextTemplateId** | **String**|  | 

### Return type

[**InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response**](InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceLineTextTemplateInvoiceLineTextTemplateIdPost

> EmptySuccessResponse invoiceLineTextTemplateInvoiceLineTextTemplateIdPost(invoiceLineTextTemplateId, html, opts)

Edit an invoice line text template

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

let apiInstance = new Apacta.InvoiceLineTextTemplatesApi();
let invoiceLineTextTemplateId = "invoiceLineTextTemplateId_example"; // String | 
let html = "html_example"; // String | 
let opts = {
  'image': "/path/to/file" // File | 
};
apiInstance.invoiceLineTextTemplateInvoiceLineTextTemplateIdPost(invoiceLineTextTemplateId, html, opts, (error, data, response) => {
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
 **invoiceLineTextTemplateId** | **String**|  | 
 **html** | **String**|  | 
 **image** | **File**|  | [optional] 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## invoiceLineTextTemplatePost

> CreateSuccessResponse invoiceLineTextTemplatePost(html, opts)

Add a new invoice line text template

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.InvoiceLineTextTemplatesApi();
let html = "html_example"; // String | 
let opts = {
  'image': "/path/to/file" // File | 
};
apiInstance.invoiceLineTextTemplatePost(html, opts, (error, data, response) => {
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
 **image** | **File**|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

