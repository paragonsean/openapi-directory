# NooshApiApplication.ShipmentApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getShipment**](ShipmentApi.md#getShipment) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/shipments/{shipment_id} | Get a specific shipment.
[**getShipmentList**](ShipmentApi.md#getShipmentList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/shipments | List shipments of project
[**postShipment**](ShipmentApi.md#postShipment) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/shipments | Create a shipment
[**putShipmentLocation**](ShipmentApi.md#putShipmentLocation) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/shipments/{shipment_id}/locations/{location_id} | Update a specific shipment location



## getShipment

> ShipmentExpandVO getShipment(workgroupId, projectId, shipmentId)

Get a specific shipment.

Get a specific shipment.

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ShipmentApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let shipmentId = "shipmentId_example"; // String | 
apiInstance.getShipment(workgroupId, projectId, shipmentId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **shipmentId** | **String**|  | 

### Return type

[**ShipmentExpandVO**](ShipmentExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getShipmentList

> ShipmentListVO getShipmentList(workgroupId, projectId)

List shipments of project

List shipments of project

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ShipmentApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getShipmentList(workgroupId, projectId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**ShipmentListVO**](ShipmentListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postShipment

> ShipmentLocationsPOSTResultVO postShipment(workgroupId, projectId, opts)

Create a shipment

Create a shipment

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ShipmentApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'shipmentLocationPostPersistVO': new NooshApiApplication.ShipmentLocationPostPersistVO() // ShipmentLocationPostPersistVO | 
};
apiInstance.postShipment(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **shipmentLocationPostPersistVO** | [**ShipmentLocationPostPersistVO**](ShipmentLocationPostPersistVO.md)|  | [optional] 

### Return type

[**ShipmentLocationsPOSTResultVO**](ShipmentLocationsPOSTResultVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## putShipmentLocation

> HTTPStatusVO putShipmentLocation(workgroupId, projectId, shipmentId, locationId, opts)

Update a specific shipment location

Update a specific shipment location

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ShipmentApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let shipmentId = "shipmentId_example"; // String | 
let locationId = "locationId_example"; // String | 
let opts = {
  'shipmentLocationPersistVO': new NooshApiApplication.ShipmentLocationPersistVO() // ShipmentLocationPersistVO | 
};
apiInstance.putShipmentLocation(workgroupId, projectId, shipmentId, locationId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **shipmentId** | **String**|  | 
 **locationId** | **String**|  | 
 **shipmentLocationPersistVO** | [**ShipmentLocationPersistVO**](ShipmentLocationPersistVO.md)|  | [optional] 

### Return type

[**HTTPStatusVO**](HTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

