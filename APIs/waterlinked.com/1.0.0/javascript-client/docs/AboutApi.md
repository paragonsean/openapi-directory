# TheWaterLinkedUnderwaterGpsApi.AboutApi

All URIs are relative to *http://demo.waterlinked.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aboutApiVersion**](AboutApi.md#aboutApiVersion) | **GET** /api/ | ApiVersion about
[**aboutFactoryReset**](AboutApi.md#aboutFactoryReset) | **POST** /api/v1/about/factoryreset | FactoryReset about
[**aboutGet**](AboutApi.md#aboutGet) | **GET** /api/v1/about | Get about
[**aboutLED**](AboutApi.md#aboutLED) | **GET** /api/v1/about/led | LED about
[**aboutStatus**](AboutApi.md#aboutStatus) | **GET** /api/v1/about/status | Status about
[**aboutTemperature**](AboutApi.md#aboutTemperature) | **GET** /api/v1/about/temperature | Temperature about



## aboutApiVersion

> WupdaterApiversion aboutApiVersion()

ApiVersion about

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.AboutApi();
apiInstance.aboutApiVersion((error, data, response) => {
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

[**WupdaterApiversion**](WupdaterApiversion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.wupdater.apiversion


## aboutFactoryReset

> WaterlinkedOperationResponse aboutFactoryReset()

FactoryReset about

Reset all settings on master electronics

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.AboutApi();
apiInstance.aboutFactoryReset((error, data, response) => {
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

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.operation_response+json


## aboutGet

> WaterlinkedAbout aboutGet()

Get about

Get about information

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.AboutApi();
apiInstance.aboutGet((error, data, response) => {
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

[**WaterlinkedAbout**](WaterlinkedAbout.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.about+json


## aboutLED

> aboutLED()

LED about

Flash LED1 on master electronics

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.AboutApi();
apiInstance.aboutLED((error, data, response) => {
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


## aboutStatus

> WaterlinkedStatus aboutStatus()

Status about

Get current IMU and GPS status

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.AboutApi();
apiInstance.aboutStatus((error, data, response) => {
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

[**WaterlinkedStatus**](WaterlinkedStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.status+json


## aboutTemperature

> WaterlinkedTemperature aboutTemperature()

Temperature about

Get board temperature

### Example

```javascript
import TheWaterLinkedUnderwaterGpsApi from 'the_water_linked_underwater_gps_api';

let apiInstance = new TheWaterLinkedUnderwaterGpsApi.AboutApi();
apiInstance.aboutTemperature((error, data, response) => {
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

[**WaterlinkedTemperature**](WaterlinkedTemperature.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.waterlinked.temperature+json

