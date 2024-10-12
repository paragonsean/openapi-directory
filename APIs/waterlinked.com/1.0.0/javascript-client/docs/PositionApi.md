# TheWaterLinkedUnderwaterGpsApi.PositionApi

All URIs are relative to *http://demo.waterlinked.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**positionAcousticFiltered**](PositionApi.md#positionAcousticFiltered) | **GET** /api/v1/position/acoustic/filtered | AcousticFiltered position
[**positionAcousticRaw**](PositionApi.md#positionAcousticRaw) | **GET** /api/v1/position/acoustic/raw | AcousticRaw position
[**positionGet**](PositionApi.md#positionGet) | **GET** /api/v1/position/global | Get position
[**positionGetMaster**](PositionApi.md#positionGetMaster) | **GET** /api/v1/position/master | GetMaster position



## positionAcousticFiltered

> WaterlinkedAccousticPosition positionAcousticFiltered()

AcousticFiltered position

Get current Kalman filtered acoustic position relative to master acoustics. Expected update frequency: 4 Hz

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PositionApi();
apiInstance.positionAcousticFiltered((error, data, response) => {
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

[**WaterlinkedAccousticPosition**](WaterlinkedAccousticPosition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.accoustic.position+json


## positionAcousticRaw

> WaterlinkedAccousticPosition positionAcousticRaw()

AcousticRaw position

Get current unfiltered acoustic position relative to master acoustics. Expected update frequency: 4 Hz

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PositionApi();
apiInstance.positionAcousticRaw((error, data, response) => {
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

[**WaterlinkedAccousticPosition**](WaterlinkedAccousticPosition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.accoustic.position+json


## positionGet

> WlSatellitePosition positionGet()

Get position

Get current global position of locator. Locator position is calculated from the current acoustic position and the global position of the master electronics. Expected update frequency: 4 Hz

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PositionApi();
apiInstance.positionGet((error, data, response) => {
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

[**WlSatellitePosition**](WlSatellitePosition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.wl.satellite.position+json


## positionGetMaster

> WlSatellitePosition positionGetMaster()

GetMaster position

Get current global position of master electronics. Expected update frequency: 1 Hz

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.PositionApi();
apiInstance.positionGetMaster((error, data, response) => {
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

[**WlSatellitePosition**](WlSatellitePosition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.wl.satellite.position+json

