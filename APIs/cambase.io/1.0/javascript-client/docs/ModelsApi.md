# CambaseIo.ModelsApi

All URIs are relative to *http://api.cambase.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1ModelsCreate**](ModelsApi.md#apiV1ModelsCreate) | **POST** /api/v1/models.json | Creates a new Model
[**apiV1ModelsIdJsonPatch**](ModelsApi.md#apiV1ModelsIdJsonPatch) | **PATCH** /api/v1/models/{id}.json | Updates an existing Model
[**apiV1ModelsIdJsonPut**](ModelsApi.md#apiV1ModelsIdJsonPut) | **PUT** /api/v1/models/{id}.json | Updates an existing Model
[**apiV1ModelsIndex**](ModelsApi.md#apiV1ModelsIndex) | **GET** /api/v1/models.json | Fetches all Models
[**apiV1ModelsSearch**](ModelsApi.md#apiV1ModelsSearch) | **GET** /api/v1/models/search.json | Searches all Models
[**apiV1ModelsShow**](ModelsApi.md#apiV1ModelsShow) | **GET** /api/v1/models/{id}.json | Fetches a single Model



## apiV1ModelsCreate

> apiV1ModelsCreate(vendorId, modelModel, opts)

Creates a new Model

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.ModelsApi();
let vendorId = "vendorId_example"; // String | Vendor ID
let modelModel = "modelModel_example"; // String | Model
let opts = {
  'modelShape': "modelShape_example", // String | Shape
  'modelResolution': "modelResolution_example", // String | Resolution
  'modelOnvif': "modelOnvif_example", // String | ONVIF
  'modelPsia': "modelPsia_example", // String | PSIA
  'modelPtz': "modelPtz_example", // String | PTZ
  'modelInfrared': "modelInfrared_example", // String | Infrared
  'modelVarifocal': "modelVarifocal_example", // String | Varifocal
  'modelSdCard': "modelSdCard_example", // String | SD Card
  'modelUpnp': "modelUpnp_example", // String | UPnP
  'modelAudioIn': "modelAudioIn_example", // String | UPnP
  'modelAudioOut': "modelAudioOut_example", // String | UPnP
  'modelDefaultUsername': "modelDefaultUsername_example", // String | Default Username
  'modelDefaultPassword': "modelDefaultPassword_example", // String | Default Password
  'modelJpegUrl': "modelJpegUrl_example", // String | JPEG URL
  'modelH264Url': "modelH264Url_example", // String | H264 URL
  'modelMjpegUrl': "modelMjpegUrl_example" // String | MJPEG URL
};
apiInstance.apiV1ModelsCreate(vendorId, modelModel, opts, (error, data, response) => {
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
 **vendorId** | **String**| Vendor ID | 
 **modelModel** | **String**| Model | 
 **modelShape** | **String**| Shape | [optional] 
 **modelResolution** | **String**| Resolution | [optional] 
 **modelOnvif** | **String**| ONVIF | [optional] 
 **modelPsia** | **String**| PSIA | [optional] 
 **modelPtz** | **String**| PTZ | [optional] 
 **modelInfrared** | **String**| Infrared | [optional] 
 **modelVarifocal** | **String**| Varifocal | [optional] 
 **modelSdCard** | **String**| SD Card | [optional] 
 **modelUpnp** | **String**| UPnP | [optional] 
 **modelAudioIn** | **String**| UPnP | [optional] 
 **modelAudioOut** | **String**| UPnP | [optional] 
 **modelDefaultUsername** | **String**| Default Username | [optional] 
 **modelDefaultPassword** | **String**| Default Password | [optional] 
 **modelJpegUrl** | **String**| JPEG URL | [optional] 
 **modelH264Url** | **String**| H264 URL | [optional] 
 **modelMjpegUrl** | **String**| MJPEG URL | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1ModelsIdJsonPatch

> apiV1ModelsIdJsonPatch(id, vendorId, opts)

Updates an existing Model

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.ModelsApi();
let id = "id_example"; // String | Model ID
let vendorId = "vendorId_example"; // String | Vendor ID
let opts = {
  'modelModel': "modelModel_example", // String | Model
  'modelShape': "modelShape_example", // String | Shape
  'modelResolution': "modelResolution_example", // String | Resolution
  'modelOnvif': "modelOnvif_example", // String | ONVIF
  'modelPsia': "modelPsia_example", // String | PSIA
  'modelPtz': "modelPtz_example", // String | PTZ
  'modelInfrared': "modelInfrared_example", // String | Infrared
  'modelVarifocal': "modelVarifocal_example", // String | Varifocal
  'modelSdCard': "modelSdCard_example", // String | SD Card
  'modelUpnp': "modelUpnp_example", // String | UPnP
  'modelAudioIn': "modelAudioIn_example", // String | Audio In
  'modelAudioOut': "modelAudioOut_example", // String | Audio Out
  'modelDefaultUsername': "modelDefaultUsername_example", // String | Default Username
  'modelDefaultPassword': "modelDefaultPassword_example", // String | Default Password
  'modelJpegUrl': "modelJpegUrl_example", // String | JPEG URL
  'modelH264Url': "modelH264Url_example", // String | H264 URL
  'modelMjpegUrl': "modelMjpegUrl_example" // String | MJPEG URL
};
apiInstance.apiV1ModelsIdJsonPatch(id, vendorId, opts, (error, data, response) => {
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
 **id** | **String**| Model ID | 
 **vendorId** | **String**| Vendor ID | 
 **modelModel** | **String**| Model | [optional] 
 **modelShape** | **String**| Shape | [optional] 
 **modelResolution** | **String**| Resolution | [optional] 
 **modelOnvif** | **String**| ONVIF | [optional] 
 **modelPsia** | **String**| PSIA | [optional] 
 **modelPtz** | **String**| PTZ | [optional] 
 **modelInfrared** | **String**| Infrared | [optional] 
 **modelVarifocal** | **String**| Varifocal | [optional] 
 **modelSdCard** | **String**| SD Card | [optional] 
 **modelUpnp** | **String**| UPnP | [optional] 
 **modelAudioIn** | **String**| Audio In | [optional] 
 **modelAudioOut** | **String**| Audio Out | [optional] 
 **modelDefaultUsername** | **String**| Default Username | [optional] 
 **modelDefaultPassword** | **String**| Default Password | [optional] 
 **modelJpegUrl** | **String**| JPEG URL | [optional] 
 **modelH264Url** | **String**| H264 URL | [optional] 
 **modelMjpegUrl** | **String**| MJPEG URL | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1ModelsIdJsonPut

> apiV1ModelsIdJsonPut(id, vendorId, opts)

Updates an existing Model

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.ModelsApi();
let id = "id_example"; // String | Model ID
let vendorId = "vendorId_example"; // String | Vendor ID
let opts = {
  'modelModel': "modelModel_example", // String | Model
  'modelShape': "modelShape_example", // String | Shape
  'modelResolution': "modelResolution_example", // String | Resolution
  'modelOnvif': "modelOnvif_example", // String | ONVIF
  'modelPsia': "modelPsia_example", // String | PSIA
  'modelPtz': "modelPtz_example", // String | PTZ
  'modelInfrared': "modelInfrared_example", // String | Infrared
  'modelVarifocal': "modelVarifocal_example", // String | Varifocal
  'modelSdCard': "modelSdCard_example", // String | SD Card
  'modelUpnp': "modelUpnp_example", // String | UPnP
  'modelAudioIn': "modelAudioIn_example", // String | Audio In
  'modelAudioOut': "modelAudioOut_example", // String | Audio Out
  'modelDefaultUsername': "modelDefaultUsername_example", // String | Default Username
  'modelDefaultPassword': "modelDefaultPassword_example", // String | Default Password
  'modelJpegUrl': "modelJpegUrl_example", // String | JPEG URL
  'modelH264Url': "modelH264Url_example", // String | H264 URL
  'modelMjpegUrl': "modelMjpegUrl_example" // String | MJPEG URL
};
apiInstance.apiV1ModelsIdJsonPut(id, vendorId, opts, (error, data, response) => {
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
 **id** | **String**| Model ID | 
 **vendorId** | **String**| Vendor ID | 
 **modelModel** | **String**| Model | [optional] 
 **modelShape** | **String**| Shape | [optional] 
 **modelResolution** | **String**| Resolution | [optional] 
 **modelOnvif** | **String**| ONVIF | [optional] 
 **modelPsia** | **String**| PSIA | [optional] 
 **modelPtz** | **String**| PTZ | [optional] 
 **modelInfrared** | **String**| Infrared | [optional] 
 **modelVarifocal** | **String**| Varifocal | [optional] 
 **modelSdCard** | **String**| SD Card | [optional] 
 **modelUpnp** | **String**| UPnP | [optional] 
 **modelAudioIn** | **String**| Audio In | [optional] 
 **modelAudioOut** | **String**| Audio Out | [optional] 
 **modelDefaultUsername** | **String**| Default Username | [optional] 
 **modelDefaultPassword** | **String**| Default Password | [optional] 
 **modelJpegUrl** | **String**| JPEG URL | [optional] 
 **modelH264Url** | **String**| H264 URL | [optional] 
 **modelMjpegUrl** | **String**| MJPEG URL | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1ModelsIndex

> apiV1ModelsIndex(opts)

Fetches all Models

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.ModelsApi();
let opts = {
  'page': 56, // Number | Page number
  'order': "order_example" // String | Sort order
};
apiInstance.apiV1ModelsIndex(opts, (error, data, response) => {
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
 **page** | **Number**| Page number | [optional] 
 **order** | **String**| Sort order | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ModelsSearch

> apiV1ModelsSearch(opts)

Searches all Models

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.ModelsApi();
let opts = {
  'page': 56, // Number | Page number
  'qModelCont': "qModelCont_example", // String | Model
  'qManufacturerNameCont': "qManufacturerNameCont_example", // String | Vendor
  'qShapeEq': "qShapeEq_example", // String | Shape
  'qResolutionEq': "qResolutionEq_example", // String | Resolution
  'qOnvifTrue': "qOnvifTrue_example", // String | ONVIF
  'qPsiaTrue': "qPsiaTrue_example", // String | PSIA
  'qPtzTrue': "qPtzTrue_example", // String | PTZ
  'qInfraredTrue': "qInfraredTrue_example", // String | Infrared
  'qVarifocalTrue': "qVarifocalTrue_example", // String | Varifocal
  'qSdCardTrue': "qSdCardTrue_example", // String | SD Card
  'qUpnpTrue': "qUpnpTrue_example", // String | UPnP
  'qAudioInTrue': "qAudioInTrue_example", // String | Audio In
  'qAudioOutTrue': "qAudioOutTrue_example" // String | Audio Out
};
apiInstance.apiV1ModelsSearch(opts, (error, data, response) => {
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
 **page** | **Number**| Page number | [optional] 
 **qModelCont** | **String**| Model | [optional] 
 **qManufacturerNameCont** | **String**| Vendor | [optional] 
 **qShapeEq** | **String**| Shape | [optional] 
 **qResolutionEq** | **String**| Resolution | [optional] 
 **qOnvifTrue** | **String**| ONVIF | [optional] 
 **qPsiaTrue** | **String**| PSIA | [optional] 
 **qPtzTrue** | **String**| PTZ | [optional] 
 **qInfraredTrue** | **String**| Infrared | [optional] 
 **qVarifocalTrue** | **String**| Varifocal | [optional] 
 **qSdCardTrue** | **String**| SD Card | [optional] 
 **qUpnpTrue** | **String**| UPnP | [optional] 
 **qAudioInTrue** | **String**| Audio In | [optional] 
 **qAudioOutTrue** | **String**| Audio Out | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1ModelsShow

> apiV1ModelsShow(id)

Fetches a single Model

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.ModelsApi();
let id = 56; // Number | Model ID
apiInstance.apiV1ModelsShow(id, (error, data, response) => {
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
 **id** | **Number**| Model ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

