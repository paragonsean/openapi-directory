# AvazaApiDocumentation.InvoiceApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoiceGet**](InvoiceApi.md#invoiceGet) | **GET** /api/Invoice | Gets list of Invoices
[**invoiceGetByID**](InvoiceApi.md#invoiceGetByID) | **GET** /api/Invoice/{id} | Gets Invoice by Invoice ID
[**invoicePost**](InvoiceApi.md#invoicePost) | **POST** /api/Invoice | Create a new draft invoice



## invoiceGet

> InvoiceList invoiceGet(opts)

Gets list of Invoices

TransactionStatusCode values are: \&quot;Draft\&quot;, \&quot;Sent\&quot;, \&quot;Late\&quot;, \&quot;Paid\&quot;, \&quot;Partial\&quot;, \&quot;Void\&quot;

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.InvoiceApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'sort': "sort_example", // String | 
  'companyIDFK': 56 // Number | 
};
apiInstance.invoiceGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**|  | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **sort** | **String**|  | [optional] 
 **companyIDFK** | **Number**|  | [optional] 

### Return type

[**InvoiceList**](InvoiceList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## invoiceGetByID

> invoiceGetByID(id)

Gets Invoice by Invoice ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.InvoiceApi();
let id = 789; // Number | Invoice Transaction ID number
apiInstance.invoiceGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Invoice Transaction ID number | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## invoicePost

> Invoice invoicePost(model)

Create a new draft invoice

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.InvoiceApi();
let model = new AvazaApiDocumentation.NewInvoice(); // NewInvoice | 
apiInstance.invoicePost(model, (error, data, response) => {
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
 **model** | [**NewInvoice**](NewInvoice.md)|  | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

