# BillbeeApi.OrdersApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layoutApiGetList**](OrdersApi.md#layoutApiGetList) | **GET** /api/v1/layouts | 
[**orderApiAddShipment**](OrdersApi.md#orderApiAddShipment) | **POST** /api/v1/orders/{id}/shipment | Add a shipment to a given order
[**orderApiCreateDeliveryNote**](OrdersApi.md#orderApiCreateDeliveryNote) | **POST** /api/v1/orders/CreateDeliveryNote/{id} | Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.
[**orderApiCreateInvoice**](OrdersApi.md#orderApiCreateInvoice) | **POST** /api/v1/orders/CreateInvoice/{id} | Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.
[**orderApiFind**](OrdersApi.md#orderApiFind) | **GET** /api/v1/orders/find/{id}/{partner} | Find a single order by its external id (order number)
[**orderApiGet**](OrdersApi.md#orderApiGet) | **GET** /api/v1/orders/{id} | Get a single order by its internal billbee id. This request is throttled to 6 calls per order in one minute
[**orderApiGetByExtRef**](OrdersApi.md#orderApiGetByExtRef) | **GET** /api/v1/orders/findbyextref/{extRef} | Get a single order by its external order number
[**orderApiGetInvoiceList**](OrdersApi.md#orderApiGetInvoiceList) | **GET** /api/v1/orders/invoices | Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate
[**orderApiGetList**](OrdersApi.md#orderApiGetList) | **GET** /api/v1/orders | Get a list of all orders optionally filtered by date
[**orderApiGetPatchableFields**](OrdersApi.md#orderApiGetPatchableFields) | **GET** /api/v1/orders/PatchableFields | Returns a list of fields which can be updated with the orders/{id} patch call
[**orderApiParsePlaceholders**](OrdersApi.md#orderApiParsePlaceholders) | **POST** /api/v1/orders/{id}/parse-placeholders | Parses a text and replaces all placeholders
[**orderApiPatchOrder**](OrdersApi.md#orderApiPatchOrder) | **PATCH** /api/v1/orders/{id} | Updates one or more fields of an order
[**orderApiPostNewOrder**](OrdersApi.md#orderApiPostNewOrder) | **POST** /api/v1/orders | Creates a new order in the Billbee account
[**orderApiSendMessage**](OrdersApi.md#orderApiSendMessage) | **POST** /api/v1/orders/{id}/send-message | Sends a message to the buyer
[**orderApiTagsCreate**](OrdersApi.md#orderApiTagsCreate) | **POST** /api/v1/orders/{id}/tags | Attach one or more tags to an order
[**orderApiTagsUpdate**](OrdersApi.md#orderApiTagsUpdate) | **PUT** /api/v1/orders/{id}/tags | Sets the tags attached to an order
[**orderApiTriggerEvent**](OrdersApi.md#orderApiTriggerEvent) | **POST** /api/v1/orders/{id}/trigger-event | Triggers a rule event
[**orderApiUpdateState**](OrdersApi.md#orderApiUpdateState) | **PUT** /api/v1/orders/{id}/orderstate | Changes the main state of a single order
[**searchSearch_1**](OrdersApi.md#searchSearch_1) | **POST** /api/v1/search | Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax



## layoutApiGetList

> RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate layoutApiGetList()



### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
apiInstance.layoutApiGetList((error, data, response) => {
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

[**RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate**](RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## orderApiAddShipment

> Object orderApiAddShipment(id, rechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel)

Add a shipment to a given order

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The internal billbee id of the order
let rechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel = new BillbeeApi.RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel(); // RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel | The shipment data to create the shipment
apiInstance.orderApiAddShipment(id, rechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel, (error, data, response) => {
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
 **rechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel** | [**RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel**](RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel.md)| The shipment data to create the shipment | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## orderApiCreateDeliveryNote

> Object orderApiCreateDeliveryNote(id, opts)

Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The internal billbee id of the order
let opts = {
  'includePdf': true, // Boolean | If true, the PDF is included in the response as base64 encoded string
  'sendToCloudId': 789 // Number | Optionally specify the id of a billbee connected cloud device to send the pdf to
};
apiInstance.orderApiCreateDeliveryNote(id, opts, (error, data, response) => {
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


## orderApiCreateInvoice

> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice orderApiCreateInvoice(id, opts)

Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The internal billbee id of the order
let opts = {
  'includeInvoicePdf': true, // Boolean | If true, the PDF is included in the response as base64 encoded string
  'templateId': 789, // Number | You can pass the id of an invoice template to overwrite the assigned template for invoice creation
  'sendToCloudId': 789 // Number | You can pass the id of a connected cloud printer/storage to send the invoice to it
};
apiInstance.orderApiCreateInvoice(id, opts, (error, data, response) => {
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


## orderApiFind

> Object orderApiFind(id, partner)

Find a single order by its external id (order number)

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = "id_example"; // String | The order id from the external system
let partner = "partner_example"; // String | Optional the name of the shop/marketplace the order was imported from
apiInstance.orderApiFind(id, partner, (error, data, response) => {
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
 **id** | **String**| The order id from the external system | 
 **partner** | **String**| Optional the name of the shop/marketplace the order was imported from | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## orderApiGet

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder orderApiGet(id, opts)

Get a single order by its internal billbee id. This request is throttled to 6 calls per order in one minute

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The internal billbee id of the order
let opts = {
  'articleTitleSource': 56 // Number | The source field for the article title. 0 = Order Position (default), 1 = Article Title, 2 = Article Invoice Text
};
apiInstance.orderApiGet(id, opts, (error, data, response) => {
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
 **articleTitleSource** | **Number**| The source field for the article title. 0 &#x3D; Order Position (default), 1 &#x3D; Article Title, 2 &#x3D; Article Invoice Text | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## orderApiGetByExtRef

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder orderApiGetByExtRef(extRef)

Get a single order by its external order number

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let extRef = "extRef_example"; // String | The extern order number of the order
apiInstance.orderApiGetByExtRef(extRef, (error, data, response) => {
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
 **extRef** | **String**| The extern order number of the order | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## orderApiGetInvoiceList

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel orderApiGetInvoiceList(opts)

Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
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
apiInstance.orderApiGetInvoiceList(opts, (error, data, response) => {
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


## orderApiGetList

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder orderApiGetList(opts)

Get a list of all orders optionally filtered by date

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let opts = {
  'minOrderDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Specifies the oldest order date to include in the response
  'maxOrderDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Specifies the newest order date to include in the response
  'page': 56, // Number | Specifies the page to request
  'pageSize': 56, // Number | Specifies the pagesize. Defaults to 50, max value is 250
  'shopId': [null], // [Number] | Specifies a list of shop ids for which invoices should be included
  'orderStateId': [null], // [Number] | Specifies a list of state ids to include in the response
  'tag': ["null"], // [String] | Specifies a list of tags the order must have attached to be included in the response
  'minimumBillBeeOrderId': 789, // Number | If given, all delivered orders have an Id greater than or equal to the given minimumOrderId
  'modifiedAtMin': new Date("2013-10-20T19:20:30+01:00"), // Date | If given, the last modification has to be newer than the given date
  'modifiedAtMax': new Date("2013-10-20T19:20:30+01:00"), // Date | If given, the last modification has to be older or equal than the given date.
  'articleTitleSource': 56, // Number | The source field for the article title. 0 = Order Position (default), 1 = Article Title, 2 = Article Invoice Text
  'excludeTags': true // Boolean | If true the list of tags passed to the call are used to filter orders to not include these tags
};
apiInstance.orderApiGetList(opts, (error, data, response) => {
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
 **minOrderDate** | **Date**| Specifies the oldest order date to include in the response | [optional] 
 **maxOrderDate** | **Date**| Specifies the newest order date to include in the response | [optional] 
 **page** | **Number**| Specifies the page to request | [optional] 
 **pageSize** | **Number**| Specifies the pagesize. Defaults to 50, max value is 250 | [optional] 
 **shopId** | [**[Number]**](Number.md)| Specifies a list of shop ids for which invoices should be included | [optional] 
 **orderStateId** | [**[Number]**](Number.md)| Specifies a list of state ids to include in the response | [optional] 
 **tag** | [**[String]**](String.md)| Specifies a list of tags the order must have attached to be included in the response | [optional] 
 **minimumBillBeeOrderId** | **Number**| If given, all delivered orders have an Id greater than or equal to the given minimumOrderId | [optional] 
 **modifiedAtMin** | **Date**| If given, the last modification has to be newer than the given date | [optional] 
 **modifiedAtMax** | **Date**| If given, the last modification has to be older or equal than the given date. | [optional] 
 **articleTitleSource** | **Number**| The source field for the article title. 0 &#x3D; Order Position (default), 1 &#x3D; Article Title, 2 &#x3D; Article Invoice Text | [optional] 
 **excludeTags** | **Boolean**| If true the list of tags passed to the call are used to filter orders to not include these tags | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## orderApiGetPatchableFields

> Object orderApiGetPatchableFields()

Returns a list of fields which can be updated with the orders/{id} patch call

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
apiInstance.orderApiGetPatchableFields((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## orderApiParsePlaceholders

> Object orderApiParsePlaceholders(id, rechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer)

Parses a text and replaces all placeholders

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The id of the order
let rechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer = new BillbeeApi.RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer(); // RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer | 
apiInstance.orderApiParsePlaceholders(id, rechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer, (error, data, response) => {
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
 **id** | **Number**| The id of the order | 
 **rechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer** | [**RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer**](RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## orderApiPatchOrder

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder orderApiPatchOrder(id, body)

Updates one or more fields of an order

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | 
let body = {key: null}; // Object | 
apiInstance.orderApiPatchOrder(id, body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml


## orderApiPostNewOrder

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder orderApiPostNewOrder(billbeeInterfacesBillbeeAPIModelOrder, opts)

Creates a new order in the Billbee account

To create an order POST an JSON object to the orders endpoint with the shown properties.  Not all properties are required.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let billbeeInterfacesBillbeeAPIModelOrder = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelOrder(); // BillbeeInterfacesBillbeeAPIModelOrder | 
let opts = {
  'shopId': 789 // Number | Deprecated, if orderData.ApiAccountId is set, it will be used instead of 'shopId'
};
apiInstance.orderApiPostNewOrder(billbeeInterfacesBillbeeAPIModelOrder, opts, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelOrder** | [**BillbeeInterfacesBillbeeAPIModelOrder**](BillbeeInterfacesBillbeeAPIModelOrder.md)|  | 
 **shopId** | **Number**| Deprecated, if orderData.ApiAccountId is set, it will be used instead of &#39;shopId&#39; | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## orderApiSendMessage

> Object orderApiSendMessage(id, rechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel)

Sends a message to the buyer

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The id of the order
let rechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel = new BillbeeApi.RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel(); // RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel | The message model
apiInstance.orderApiSendMessage(id, rechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel, (error, data, response) => {
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
 **id** | **Number**| The id of the order | 
 **rechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel** | [**RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel**](RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel.md)| The message model | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## orderApiTagsCreate

> Object orderApiTagsCreate(id, rechnungsdruckWebAppControllersApiOrderTagCreate)

Attach one or more tags to an order

When a tag is already attached, it is ignored. Tags are not case sensitive. All given tags are added to the existing tags.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The internal id of the order
let rechnungsdruckWebAppControllersApiOrderTagCreate = new BillbeeApi.RechnungsdruckWebAppControllersApiOrderTagCreate(); // RechnungsdruckWebAppControllersApiOrderTagCreate | Tags to attach
apiInstance.orderApiTagsCreate(id, rechnungsdruckWebAppControllersApiOrderTagCreate, (error, data, response) => {
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
 **id** | **Number**| The internal id of the order | 
 **rechnungsdruckWebAppControllersApiOrderTagCreate** | [**RechnungsdruckWebAppControllersApiOrderTagCreate**](RechnungsdruckWebAppControllersApiOrderTagCreate.md)| Tags to attach | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## orderApiTagsUpdate

> Object orderApiTagsUpdate(id, rechnungsdruckWebAppControllersApiOrderTagCreate)

Sets the tags attached to an order

All existing tags will be replaced by the given list of new tags. To just add tags, use POST method.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The internal id of the order
let rechnungsdruckWebAppControllersApiOrderTagCreate = new BillbeeApi.RechnungsdruckWebAppControllersApiOrderTagCreate(); // RechnungsdruckWebAppControllersApiOrderTagCreate | Tags to attach
apiInstance.orderApiTagsUpdate(id, rechnungsdruckWebAppControllersApiOrderTagCreate, (error, data, response) => {
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
 **id** | **Number**| The internal id of the order | 
 **rechnungsdruckWebAppControllersApiOrderTagCreate** | [**RechnungsdruckWebAppControllersApiOrderTagCreate**](RechnungsdruckWebAppControllersApiOrderTagCreate.md)| Tags to attach | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## orderApiTriggerEvent

> Object orderApiTriggerEvent(id, rechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer)

Triggers a rule event

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The id of the order
let rechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer = new BillbeeApi.RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer(); // RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer | 
apiInstance.orderApiTriggerEvent(id, rechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer, (error, data, response) => {
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
 **id** | **Number**| The id of the order | 
 **rechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer** | [**RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer**](RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## orderApiUpdateState

> Object orderApiUpdateState(id, rechnungsdruckWebAppControllersApiOrderStateUpdate)

Changes the main state of a single order

### REMARKS ###  Use this call to change the state of an order to i.e. paid or sent.    The state is transfered to the external shop/marketplace if configured.  This is the list of known states:  - 1: ordered  - 2: confirmed  - 3: paid  - 4: shipped  - 5: reclamation  - 6: deleted  - 7: closed  - 8: canceled  - 9: archived  - 10: not used  - 11: demand note 1  - 12: demand note 2  - 13: packed  - 14: offered  - 15: payment reminder  - 16: fulfilling

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let id = 789; // Number | The internal id of the order
let rechnungsdruckWebAppControllersApiOrderStateUpdate = new BillbeeApi.RechnungsdruckWebAppControllersApiOrderStateUpdate(); // RechnungsdruckWebAppControllersApiOrderStateUpdate | The data used to change the state
apiInstance.orderApiUpdateState(id, rechnungsdruckWebAppControllersApiOrderStateUpdate, (error, data, response) => {
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
 **id** | **Number**| The internal id of the order | 
 **rechnungsdruckWebAppControllersApiOrderStateUpdate** | [**RechnungsdruckWebAppControllersApiOrderStateUpdate**](RechnungsdruckWebAppControllersApiOrderStateUpdate.md)| The data used to change the state | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## searchSearch_1

> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel searchSearch_1(rechnungsdruckWebAppControllersApiSearchControllerSearchModel)

Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.OrdersApi();
let rechnungsdruckWebAppControllersApiSearchControllerSearchModel = new BillbeeApi.RechnungsdruckWebAppControllersApiSearchControllerSearchModel(); // RechnungsdruckWebAppControllersApiSearchControllerSearchModel | 
apiInstance.searchSearch_1(rechnungsdruckWebAppControllersApiSearchControllerSearchModel, (error, data, response) => {
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
 **rechnungsdruckWebAppControllersApiSearchControllerSearchModel** | [**RechnungsdruckWebAppControllersApiSearchControllerSearchModel**](RechnungsdruckWebAppControllersApiSearchControllerSearchModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

