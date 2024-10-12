# SquareConnectApi.InvoicesApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelInvoice**](InvoicesApi.md#cancelInvoice) | **POST** /v2/invoices/{invoice_id}/cancel | CancelInvoice
[**createInvoice**](InvoicesApi.md#createInvoice) | **POST** /v2/invoices | CreateInvoice
[**deleteInvoice**](InvoicesApi.md#deleteInvoice) | **DELETE** /v2/invoices/{invoice_id} | DeleteInvoice
[**getInvoice**](InvoicesApi.md#getInvoice) | **GET** /v2/invoices/{invoice_id} | GetInvoice
[**listInvoices**](InvoicesApi.md#listInvoices) | **GET** /v2/invoices | ListInvoices
[**publishInvoice**](InvoicesApi.md#publishInvoice) | **POST** /v2/invoices/{invoice_id}/publish | PublishInvoice
[**searchInvoices**](InvoicesApi.md#searchInvoices) | **POST** /v2/invoices/search | SearchInvoices
[**updateInvoice**](InvoicesApi.md#updateInvoice) | **PUT** /v2/invoices/{invoice_id} | UpdateInvoice



## cancelInvoice

> CancelInvoiceResponse cancelInvoice(invoiceId, cancelInvoiceRequest)

CancelInvoice

Cancels an invoice. The seller cannot collect payments for  the canceled invoice.  You cannot cancel an invoice in the &#x60;DRAFT&#x60; state or in a terminal state: &#x60;PAID&#x60;, &#x60;REFUNDED&#x60;, &#x60;CANCELED&#x60;, or &#x60;FAILED&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | The ID of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel.
let cancelInvoiceRequest = new SquareConnectApi.CancelInvoiceRequest(); // CancelInvoiceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.cancelInvoice(invoiceId, cancelInvoiceRequest, (error, data, response) => {
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
 **invoiceId** | **String**| The ID of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to cancel. | 
 **cancelInvoiceRequest** | [**CancelInvoiceRequest**](CancelInvoiceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CancelInvoiceResponse**](CancelInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInvoice

> CreateInvoiceResponse createInvoice(createInvoiceRequest)

CreateInvoice

Creates a draft [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice)  for an order created using the Orders API.  A draft invoice remains in your account and no action is taken.  You must publish the invoice before Square can process it (send it to the customer&#39;s email address or charge the customer’s card on file).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.InvoicesApi();
let createInvoiceRequest = new SquareConnectApi.CreateInvoiceRequest(); // CreateInvoiceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createInvoice(createInvoiceRequest, (error, data, response) => {
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
 **createInvoiceRequest** | [**CreateInvoiceRequest**](CreateInvoiceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateInvoiceResponse**](CreateInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteInvoice

> DeleteInvoiceResponse deleteInvoice(invoiceId, opts)

DeleteInvoice

Deletes the specified invoice. When an invoice is deleted, the  associated order status changes to CANCELED. You can only delete a draft  invoice (you cannot delete a published invoice, including one that is scheduled for processing).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | The ID of the invoice to delete.
let opts = {
  'version': 56 // Number | The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete. If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or  [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices).
};
apiInstance.deleteInvoice(invoiceId, opts, (error, data, response) => {
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
 **invoiceId** | **String**| The ID of the invoice to delete. | 
 **version** | **Number**| The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to delete. If you do not know the version, you can call [GetInvoice](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/get-invoice) or  [ListInvoices](https://developer.squareup.com/reference/square_2021-08-18/invoices-api/list-invoices). | [optional] 

### Return type

[**DeleteInvoiceResponse**](DeleteInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoice

> GetInvoiceResponse getInvoice(invoiceId)

GetInvoice

Retrieves an invoice by invoice ID.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | The ID of the invoice to retrieve.
apiInstance.getInvoice(invoiceId, (error, data, response) => {
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
 **invoiceId** | **String**| The ID of the invoice to retrieve. | 

### Return type

[**GetInvoiceResponse**](GetInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInvoices

> ListInvoicesResponse listInvoices(locationId, opts)

ListInvoices

Returns a list of invoices for a given location. The response  is paginated. If truncated, the response includes a &#x60;cursor&#x60; that you     use in a subsequent request to retrieve the next set of invoices.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.InvoicesApi();
let locationId = "locationId_example"; // String | The ID of the location for which to list invoices.
let opts = {
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint.  Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
  'limit': 56 // Number | The maximum number of invoices to return (200 is the maximum `limit`).  If not provided, the server uses a default limit of 100 invoices.
};
apiInstance.listInvoices(locationId, opts, (error, data, response) => {
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
 **locationId** | **String**| The ID of the location for which to list invoices. | 
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint.  Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 
 **limit** | **Number**| The maximum number of invoices to return (200 is the maximum &#x60;limit&#x60;).  If not provided, the server uses a default limit of 100 invoices. | [optional] 

### Return type

[**ListInvoicesResponse**](ListInvoicesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishInvoice

> PublishInvoiceResponse publishInvoice(invoiceId, publishInvoiceRequest)

PublishInvoice

Publishes the specified draft invoice.   After an invoice is published, Square  follows up based on the invoice configuration. For example, Square  sends the invoice to the customer&#39;s email address, charges the customer&#39;s card on file, or does  nothing. Square also makes the invoice available on a Square-hosted invoice page.   The invoice &#x60;status&#x60; also changes from &#x60;DRAFT&#x60; to a status  based on the invoice configuration. For example, the status changes to &#x60;UNPAID&#x60; if  Square emails the invoice or &#x60;PARTIALLY_PAID&#x60; if Square charge a card on file for a portion of the  invoice amount.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | The ID of the invoice to publish.
let publishInvoiceRequest = new SquareConnectApi.PublishInvoiceRequest(); // PublishInvoiceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.publishInvoice(invoiceId, publishInvoiceRequest, (error, data, response) => {
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
 **invoiceId** | **String**| The ID of the invoice to publish. | 
 **publishInvoiceRequest** | [**PublishInvoiceRequest**](PublishInvoiceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**PublishInvoiceResponse**](PublishInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchInvoices

> SearchInvoicesResponse searchInvoices(searchInvoicesRequest)

SearchInvoices

Searches for invoices from a location specified in  the filter. You can optionally specify customers in the filter for whom to  retrieve invoices. In the current implementation, you can only specify one location and  optionally one customer.  The response is paginated. If truncated, the response includes a &#x60;cursor&#x60;  that you use in a subsequent request to retrieve the next set of invoices.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.InvoicesApi();
let searchInvoicesRequest = new SquareConnectApi.SearchInvoicesRequest(); // SearchInvoicesRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchInvoices(searchInvoicesRequest, (error, data, response) => {
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
 **searchInvoicesRequest** | [**SearchInvoicesRequest**](SearchInvoicesRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchInvoicesResponse**](SearchInvoicesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInvoice

> UpdateInvoiceResponse updateInvoice(invoiceId, updateInvoiceRequest)

UpdateInvoice

Updates an invoice by modifying fields, clearing fields, or both. For most updates, you can use a sparse  &#x60;Invoice&#x60; object to add fields or change values and use the &#x60;fields_to_clear&#x60; field to specify fields to clear.  However, some restrictions apply. For example, you cannot change the &#x60;order_id&#x60; or &#x60;location_id&#x60; field and you  must provide the complete &#x60;custom_fields&#x60; list to update a custom field. Published invoices have additional restrictions.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.InvoicesApi();
let invoiceId = "invoiceId_example"; // String | The ID of the invoice to update.
let updateInvoiceRequest = new SquareConnectApi.UpdateInvoiceRequest(); // UpdateInvoiceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateInvoice(invoiceId, updateInvoiceRequest, (error, data, response) => {
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
 **invoiceId** | **String**| The ID of the invoice to update. | 
 **updateInvoiceRequest** | [**UpdateInvoiceRequest**](UpdateInvoiceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateInvoiceResponse**](UpdateInvoiceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

