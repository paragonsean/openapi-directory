# BillbeeApi.InvoiceApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orderApiCreateInvoice_0**](InvoiceApi.md#orderApiCreateInvoice_0) | **POST** /api/v1/orders/CreateInvoice/{id} | Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.
[**orderApiGetInvoiceList_0**](InvoiceApi.md#orderApiGetInvoiceList_0) | **GET** /api/v1/orders/invoices | Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate



## orderApiCreateInvoice_0

> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice orderApiCreateInvoice_0(id, opts)

Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.InvoiceApi();
let id = 789; // Number | The internal billbee id of the order
let opts = {
  'includeInvoicePdf': true, // Boolean | If true, the PDF is included in the response as base64 encoded string
  'templateId': 789, // Number | You can pass the id of an invoice template to overwrite the assigned template for invoice creation
  'sendToCloudId': 789 // Number | You can pass the id of a connected cloud printer/storage to send the invoice to it
};
apiInstance.orderApiCreateInvoice_0(id, opts, (error, data, response) => {
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
 **id** | **Number**| The internal billbee id of the order | 
 **includeInvoicePdf** | **Boolean**| If true, the PDF is included in the response as base64 encoded string | [optional] 
 **templateId** | **Number**| You can pass the id of an invoice template to overwrite the assigned template for invoice creation | [optional] 
 **sendToCloudId** | **Number**| You can pass the id of a connected cloud printer/storage to send the invoice to it | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## orderApiGetInvoiceList_0

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel orderApiGetInvoiceList_0(opts)

Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.InvoiceApi();
let opts = {
  'minInvoiceDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Specifies the oldest invoice date to include
  'maxInvoiceDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Specifies the newest invoice date to include
  'page': 56, // Number | Specifies the page to request
  'pageSize': 56, // Number | Specifies the pagesize. Defaults to 50, max value is 250
  'shopId': [null], // [Number] | Specifies a list of shop ids for which invoices should be included
  'orderStateId': [null], // [Number] | Specifies a list of state ids to include in the response
  'tag': ["null"], // [String] | 
  'minPayDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'maxPayDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'includePositions': true, // Boolean | 
  'excludeTags': true // Boolean | If true the list of tags passed to the call are used to filter orders to not include these tags
};
apiInstance.orderApiGetInvoiceList_0(opts, (error, data, response) => {
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
 **minInvoiceDate** | **Date**| Specifies the oldest invoice date to include | [optional] 
 **maxInvoiceDate** | **Date**| Specifies the newest invoice date to include | [optional] 
 **page** | **Number**| Specifies the page to request | [optional] 
 **pageSize** | **Number**| Specifies the pagesize. Defaults to 50, max value is 250 | [optional] 
 **shopId** | [**[Number]**](Number.md)| Specifies a list of shop ids for which invoices should be included | [optional] 
 **orderStateId** | [**[Number]**](Number.md)| Specifies a list of state ids to include in the response | [optional] 
 **tag** | [**[String]**](String.md)|  | [optional] 
 **minPayDate** | **Date**|  | [optional] 
 **maxPayDate** | **Date**|  | [optional] 
 **includePositions** | **Boolean**|  | [optional] 
 **excludeTags** | **Boolean**| If true the list of tags passed to the call are used to filter orders to not include these tags | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

