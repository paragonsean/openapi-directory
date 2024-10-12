# BillbeeApi.ShipmentsApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipmentGetList**](ShipmentsApi.md#shipmentGetList) | **GET** /api/v1/shipment/shipments | Get a list of all shipments optionally filtered by date. All parameters are optional.
[**shipmentGetPing**](ShipmentsApi.md#shipmentGetPing) | **GET** /api/v1/shipment/ping | 
[**shipmentGetShippingCarrier**](ShipmentsApi.md#shipmentGetShippingCarrier) | **GET** /api/v1/shipment/shippingcarriers | Queries the currently available shipping carriers.
[**shipmentGetShippingproviders**](ShipmentsApi.md#shipmentGetShippingproviders) | **GET** /api/v1/shipment/shippingproviders | Query all defined shipping providers
[**shipmentPostShipment**](ShipmentsApi.md#shipmentPostShipment) | **POST** /api/v1/shipment/shipment | Creates a new shipment with the selected Shippingprovider
[**shipmentShipWithLabel**](ShipmentsApi.md#shipmentShipWithLabel) | **POST** /api/v1/shipment/shipwithlabel | Creates a shipment for an order in billbee



## shipmentGetList

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment shipmentGetList(opts)

Get a list of all shipments optionally filtered by date. All parameters are optional.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ShipmentsApi();
let opts = {
  'page': 56, // Number | Specifies the page to request.
  'pageSize': 56, // Number | Specifies the pagesize. Defaults to 50, max value is 250
  'createdAtMin': new Date("2013-10-20T19:20:30+01:00"), // Date | Specifies the oldest shipment date to include in the response
  'createdAtMax': new Date("2013-10-20T19:20:30+01:00"), // Date | Specifies the newest shipment date to include in the response
  'orderId': 789, // Number | Get shipments for this order only.
  'minimumShipmentId': 789, // Number | Get Shipments with a shipment greater or equal than this id. New shipments have a greater id than older shipments.
  'shippingProviderId': 789 // Number | Get Shippings for the specified shipping provider only. <seealso cref=\"M:Rechnungsdruck.WebApp.Controllers.Api.ShipmentController.GetShippingproviders\" />
};
apiInstance.shipmentGetList(opts, (error, data, response) => {
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
 **page** | **Number**| Specifies the page to request. | [optional] 
 **pageSize** | **Number**| Specifies the pagesize. Defaults to 50, max value is 250 | [optional] 
 **createdAtMin** | **Date**| Specifies the oldest shipment date to include in the response | [optional] 
 **createdAtMax** | **Date**| Specifies the newest shipment date to include in the response | [optional] 
 **orderId** | **Number**| Get shipments for this order only. | [optional] 
 **minimumShipmentId** | **Number**| Get Shipments with a shipment greater or equal than this id. New shipments have a greater id than older shipments. | [optional] 
 **shippingProviderId** | **Number**| Get Shippings for the specified shipping provider only. &lt;seealso cref&#x3D;\&quot;M:Rechnungsdruck.WebApp.Controllers.Api.ShipmentController.GetShippingproviders\&quot; /&gt; | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## shipmentGetPing

> Object shipmentGetPing()



### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ShipmentsApi();
apiInstance.shipmentGetPing((error, data, response) => {
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


## shipmentGetShippingCarrier

> Object shipmentGetShippingCarrier()

Queries the currently available shipping carriers.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ShipmentsApi();
apiInstance.shipmentGetShippingCarrier((error, data, response) => {
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


## shipmentGetShippingproviders

> Object shipmentGetShippingproviders()

Query all defined shipping providers

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ShipmentsApi();
apiInstance.shipmentGetShippingproviders((error, data, response) => {
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


## shipmentPostShipment

> Object shipmentPostShipment(billbeeInterfacesBillbeeAPIModelCreateShipmentApiModel)

Creates a new shipment with the selected Shippingprovider

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ShipmentsApi();
let billbeeInterfacesBillbeeAPIModelCreateShipmentApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel(); // BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel | Data to specify shipment parameters
apiInstance.shipmentPostShipment(billbeeInterfacesBillbeeAPIModelCreateShipmentApiModel, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelCreateShipmentApiModel** | [**BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel**](BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel.md)| Data to specify shipment parameters | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## shipmentShipWithLabel

> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult shipmentShipWithLabel(rechnungsdruckWebAppControllersApiShipmentWithLabel)

Creates a shipment for an order in billbee

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ShipmentsApi();
let rechnungsdruckWebAppControllersApiShipmentWithLabel = new BillbeeApi.RechnungsdruckWebAppControllersApiShipmentWithLabel(); // RechnungsdruckWebAppControllersApiShipmentWithLabel | Details on the order and the shipping methods, that should be used.
apiInstance.shipmentShipWithLabel(rechnungsdruckWebAppControllersApiShipmentWithLabel, (error, data, response) => {
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
 **rechnungsdruckWebAppControllersApiShipmentWithLabel** | [**RechnungsdruckWebAppControllersApiShipmentWithLabel**](RechnungsdruckWebAppControllersApiShipmentWithLabel.md)| Details on the order and the shipping methods, that should be used. | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

