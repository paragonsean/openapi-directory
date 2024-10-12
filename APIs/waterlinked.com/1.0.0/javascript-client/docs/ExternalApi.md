# TheWaterLinkedUnderwaterGpsApi.ExternalApi

All URIs are relative to *http://demo.waterlinked.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**externalGetOrientation**](ExternalApi.md#externalGetOrientation) | **GET** /api/v1/external/orientation | GetOrientation external
[**externalGetVehicleIMU**](ExternalApi.md#externalGetVehicleIMU) | **GET** /api/v1/external/imu | GetVehicleIMU external
[**externalSetDepth**](ExternalApi.md#externalSetDepth) | **PUT** /api/v1/external/depth | SetDepth external
[**externalSetMaster**](ExternalApi.md#externalSetMaster) | **PUT** /api/v1/external/master | SetMaster external
[**externalSetOrientation**](ExternalApi.md#externalSetOrientation) | **PUT** /api/v1/external/orientation | SetOrientation external
[**externalSetVehicleIMU**](ExternalApi.md#externalSetVehicleIMU) | **PUT** /api/v1/external/imu | SetVehicleIMU external



## externalGetOrientation

> WlExternalLocatorOrientation externalGetOrientation()

GetOrientation external

Get orientation of Vehicle/ROV/Locator set by SetOrientation

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ExternalApi();
apiInstance.externalGetOrientation((error, data, response) => {
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

[**WlExternalLocatorOrientation**](WlExternalLocatorOrientation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.operation_response+json, application/vnd.wl.external.locator.orientation+json


## externalGetVehicleIMU

> WlExternalVehicleImu externalGetVehicleIMU()

GetVehicleIMU external

[DEPRECATED]Get rotation and acceleration of vehicle Locator is mounted on which was previously set

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ExternalApi();
apiInstance.externalGetVehicleIMU((error, data, response) => {
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

[**WlExternalVehicleImu**](WlExternalVehicleImu.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.wl.external.vehicle.imu+json


## externalSetDepth

> WaterlinkedOperationResponse externalSetDepth(payload)

SetDepth external

Set depth from external source. If Locator A1 is used, this is required to get a position

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ExternalApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.SetDepthExternalPayload(); // SetDepthExternalPayload | Current locator depth and temperature
apiInstance.externalSetDepth(payload, (error, data, response) => {
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
 **payload** | [**SetDepthExternalPayload**](SetDepthExternalPayload.md)| Current locator depth and temperature | 

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.waterlinked.operation_response+json


## externalSetMaster

> WaterlinkedOperationResponse externalSetMaster(payload)

SetMaster external

Set current global position of master electronics from external source. Values are only used if GPS mode is set to use external GPS

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ExternalApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.SetMasterExternalPayload(); // SetMasterExternalPayload | Global master position from external source
apiInstance.externalSetMaster(payload, (error, data, response) => {
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
 **payload** | [**SetMasterExternalPayload**](SetMasterExternalPayload.md)| Global master position from external source | 

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.waterlinked.operation_response+json


## externalSetOrientation

> WaterlinkedOperationResponse externalSetOrientation(payload)

SetOrientation external

Set orientation/compass heading of Vehicle/ROV/Locator. This is used only for visualization in GUI

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ExternalApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.SetOrientationExternalPayload(); // SetOrientationExternalPayload | Set current compass heading of ROV/locator
apiInstance.externalSetOrientation(payload, (error, data, response) => {
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
 **payload** | [**SetOrientationExternalPayload**](SetOrientationExternalPayload.md)| Set current compass heading of ROV/locator | 

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.waterlinked.operation_response+json


## externalSetVehicleIMU

> WaterlinkedOperationResponse externalSetVehicleIMU(payload)

SetVehicleIMU external

[DEPRECATED]Set rotation and acceleration of vehicle Locator is mounted on. This is used to improve positioning of vehicle

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ExternalApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.SetVehicleIMUExternalPayload(); // SetVehicleIMUExternalPayload | Set current rotation and acceleration of vehicle
apiInstance.externalSetVehicleIMU(payload, (error, data, response) => {
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
 **payload** | [**SetVehicleIMUExternalPayload**](SetVehicleIMUExternalPayload.md)| Set current rotation and acceleration of vehicle | 

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.waterlinked.operation_response+json

