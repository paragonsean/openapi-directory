# AvazaApiDocumentation.PaymentApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentGet**](PaymentApi.md#paymentGet) | **GET** /api/Payment | Gets list of Payments
[**paymentGetByID**](PaymentApi.md#paymentGetByID) | **GET** /api/Payment/{id} | Gets Payment by Payment Transaction ID
[**paymentPost**](PaymentApi.md#paymentPost) | **POST** /api/Payment | Create new Payment and optionally assign payment allocations to Invoices



## paymentGet

> PaymentList paymentGet(opts)

Gets list of Payments

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.PaymentApi();
let opts = {
  'invoiceTransactionID': 789, // Number | Filter for Payments that have at least one allocation against a given Invoice Transaction ID
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter for Payments updated after a given date
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56 // Number | Page to display. Starts from 1.
};
apiInstance.paymentGet(opts, (error, data, response) => {
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
 **invoiceTransactionID** | **Number**| Filter for Payments that have at least one allocation against a given Invoice Transaction ID | [optional] 
 **updatedAfter** | **Date**| Filter for Payments updated after a given date | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 

### Return type

[**PaymentList**](PaymentList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## paymentGetByID

> Payment paymentGetByID(id)

Gets Payment by Payment Transaction ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.PaymentApi();
let id = 789; // Number | Invoice Transaction ID Number
apiInstance.paymentGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Invoice Transaction ID Number | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## paymentPost

> Payment paymentPost(model)

Create new Payment and optionally assign payment allocations to Invoices

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.PaymentApi();
let model = new AvazaApiDocumentation.NewPayment(); // NewPayment | 
apiInstance.paymentPost(model, (error, data, response) => {
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
 **model** | [**NewPayment**](NewPayment.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

