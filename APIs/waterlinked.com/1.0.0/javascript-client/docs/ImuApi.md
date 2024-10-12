# TheWaterLinkedUnderwaterGpsApi.ImuApi

All URIs are relative to *http://demo.waterlinked.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imuCalibrate**](ImuApi.md#imuCalibrate) | **POST** /api/v1/imu/calibrate | Calibrate imu
[**imuGet**](ImuApi.md#imuGet) | **GET** /api/v1/imu/calibrate | Get imu
[**imuResetGyro**](ImuApi.md#imuResetGyro) | **POST** /api/v1/imu/resetgyros | ResetGyro imu
[**imuSetNorth**](ImuApi.md#imuSetNorth) | **POST** /api/v1/imu/setnorth | SetNorth imu



## imuCalibrate

> imuCalibrate(payload)

Calibrate imu

[DEPRECATED]Start calibration

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ImuApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.CalibrateImuPayload(); // CalibrateImuPayload | IMU calibration action
apiInstance.imuCalibrate(payload, (error, data, response) => {
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
 **payload** | [**CalibrateImuPayload**](CalibrateImuPayload.md)| IMU calibration action | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## imuGet

> WaterlinkedImu imuGet()

Get imu

Get IMU status and orientation

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ImuApi();
apiInstance.imuGet((error, data, response) => {
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

[**WaterlinkedImu**](WaterlinkedImu.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.imu+json


## imuResetGyro

> imuResetGyro()

ResetGyro imu

Reset Gyro

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ImuApi();
apiInstance.imuResetGyro((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## imuSetNorth

> imuSetNorth(payload)

SetNorth imu

Set north point

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.ImuApi();
let payload = new TheWaterLinkedUnderwaterGpsApi.SetNorthImuPayload(); // SetNorthImuPayload | IMU set north
apiInstance.imuSetNorth(payload, (error, data, response) => {
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
 **payload** | [**SetNorthImuPayload**](SetNorthImuPayload.md)| IMU set north | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

