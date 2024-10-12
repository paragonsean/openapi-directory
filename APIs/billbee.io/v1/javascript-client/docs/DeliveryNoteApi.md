# BillbeeApi.DeliveryNoteApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orderApiCreateDeliveryNote_0**](DeliveryNoteApi.md#orderApiCreateDeliveryNote_0) | **POST** /api/v1/orders/CreateDeliveryNote/{id} | Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.



## orderApiCreateDeliveryNote_0

> Object orderApiCreateDeliveryNote_0(id, opts)

Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.DeliveryNoteApi();
let id = 789; // Number | The internal billbee id of the order
let opts = {
  'includePdf': true, // Boolean | If true, the PDF is included in the response as base64 encoded string
  'sendToCloudId': 789 // Number | Optionally specify the id of a billbee connected cloud device to send the pdf to
};
apiInstance.orderApiCreateDeliveryNote_0(id, opts, (error, data, response) => {
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
 **includePdf** | **Boolean**| If true, the PDF is included in the response as base64 encoded string | [optional] 
 **sendToCloudId** | **Number**| Optionally specify the id of a billbee connected cloud device to send the pdf to | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

