# CambaseIo.RecordersApi

All URIs are relative to *http://api.cambase.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1RecordersCreate**](RecordersApi.md#apiV1RecordersCreate) | **POST** /api/v1/recorders.json | Creates a new Recorder
[**apiV1RecordersIdJsonPatch**](RecordersApi.md#apiV1RecordersIdJsonPatch) | **PATCH** /api/v1/recorders/{id}.json | Updates an existing Recorder
[**apiV1RecordersIdJsonPut**](RecordersApi.md#apiV1RecordersIdJsonPut) | **PUT** /api/v1/recorders/{id}.json | Updates an existing Recorder
[**apiV1RecordersIndex**](RecordersApi.md#apiV1RecordersIndex) | **GET** /api/v1/recorders.json | Fetches all Recorders
[**apiV1RecordersSearch**](RecordersApi.md#apiV1RecordersSearch) | **GET** /api/v1/recorders/search.json | Searches all Recorders
[**apiV1RecordersShow**](RecordersApi.md#apiV1RecordersShow) | **GET** /api/v1/recorders/{id}.json | Fetches a single Recorder



## apiV1RecordersCreate

> apiV1RecordersCreate(vendorId, recorderModel, recorderName, recorderRecorderType, opts)

Creates a new Recorder

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.RecordersApi();
let vendorId = "vendorId_example"; // String | Vendor ID
let recorderModel = "recorderModel_example"; // String | Model
let recorderName = "recorderName_example"; // String | Name
let recorderRecorderType = "recorderRecorderType_example"; // String | Type
let opts = {
  'recorderResolution': "recorderResolution_example", // String | Resolution
  'recorderOnvif': "recorderOnvif_example", // String | ONVIF
  'recorderPsia': "recorderPsia_example", // String | PSIA
  'recorderPtz': "recorderPtz_example", // String | PTZ
  'recorderDiscontinued': "recorderDiscontinued_example", // String | Discontinued
  'recorderSupport3rdparty': "recorderSupport3rdparty_example", // String | 3rd pparty Camera Support
  'recorderSdCard': "recorderSdCard_example", // String | SD Card
  'recorderUpnp': "recorderUpnp_example", // String | UPnP
  'recorderHotSwap': "recorderHotSwap_example", // String | Hot Swap
  'recorderHdmi': "recorderHdmi_example", // String | HDMI Support
  'recorderDigitalIo': "recorderDigitalIo_example", // String | Digital I/O
  'recorderAudioIn': "recorderAudioIn_example", // String | Audio In
  'recorderAudioOut': "recorderAudioOut_example", // String | Audio Out
  'recorderInputChannels': "recorderInputChannels_example", // String | Input Channels
  'recorderPlaybackChannels': "recorderPlaybackChannels_example", // String | Playback Channels
  'recorderUsb': "recorderUsb_example", // String | USB Ports
  'recorderSdhc': "recorderSdhc_example", // String | SD Card (GB)
  'recorderMobileAccess': "recorderMobileAccess_example", // String | Mobile Access
  'recorderAlarms': "recorderAlarms_example", // String | Alarms
  'recorderRaidSupport': "recorderRaidSupport_example", // String | Raid Support
  'recorderStorage': "recorderStorage_example", // String | Internal Storage
  'recorderAdditionalInformation': "recorderAdditionalInformation_example", // String | Additional Information
  'recorderDefaultUsername': "recorderDefaultUsername_example", // String | Default Username
  'recorderDefaultPassword': "recorderDefaultPassword_example", // String | Default Password
  'recorderJpegUrl': "recorderJpegUrl_example", // String | JPEG URL
  'recorderH264Url': "recorderH264Url_example", // String | H264 URL
  'recorderMjpegUrl': "recorderMjpegUrl_example", // String | MJPEG URL
  'recorderOfficialUrl': "recorderOfficialUrl_example" // String | Official URL
};
apiInstance.apiV1RecordersCreate(vendorId, recorderModel, recorderName, recorderRecorderType, opts, (error, data, response) => {
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
 **recorderModel** | **String**| Model | 
 **recorderName** | **String**| Name | 
 **recorderRecorderType** | **String**| Type | 
 **recorderResolution** | **String**| Resolution | [optional] 
 **recorderOnvif** | **String**| ONVIF | [optional] 
 **recorderPsia** | **String**| PSIA | [optional] 
 **recorderPtz** | **String**| PTZ | [optional] 
 **recorderDiscontinued** | **String**| Discontinued | [optional] 
 **recorderSupport3rdparty** | **String**| 3rd pparty Camera Support | [optional] 
 **recorderSdCard** | **String**| SD Card | [optional] 
 **recorderUpnp** | **String**| UPnP | [optional] 
 **recorderHotSwap** | **String**| Hot Swap | [optional] 
 **recorderHdmi** | **String**| HDMI Support | [optional] 
 **recorderDigitalIo** | **String**| Digital I/O | [optional] 
 **recorderAudioIn** | **String**| Audio In | [optional] 
 **recorderAudioOut** | **String**| Audio Out | [optional] 
 **recorderInputChannels** | **String**| Input Channels | [optional] 
 **recorderPlaybackChannels** | **String**| Playback Channels | [optional] 
 **recorderUsb** | **String**| USB Ports | [optional] 
 **recorderSdhc** | **String**| SD Card (GB) | [optional] 
 **recorderMobileAccess** | **String**| Mobile Access | [optional] 
 **recorderAlarms** | **String**| Alarms | [optional] 
 **recorderRaidSupport** | **String**| Raid Support | [optional] 
 **recorderStorage** | **String**| Internal Storage | [optional] 
 **recorderAdditionalInformation** | **String**| Additional Information | [optional] 
 **recorderDefaultUsername** | **String**| Default Username | [optional] 
 **recorderDefaultPassword** | **String**| Default Password | [optional] 
 **recorderJpegUrl** | **String**| JPEG URL | [optional] 
 **recorderH264Url** | **String**| H264 URL | [optional] 
 **recorderMjpegUrl** | **String**| MJPEG URL | [optional] 
 **recorderOfficialUrl** | **String**| Official URL | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1RecordersIdJsonPatch

> apiV1RecordersIdJsonPatch(id, vendorId, recorderModel, recorderName, recorderRecorderType, opts)

Updates an existing Recorder

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.RecordersApi();
let id = "id_example"; // String | Recorder ID
let vendorId = "vendorId_example"; // String | Vendor ID
let recorderModel = "recorderModel_example"; // String | Model
let recorderName = "recorderName_example"; // String | Name
let recorderRecorderType = "recorderRecorderType_example"; // String | Type
let opts = {
  'recorderResolution': "recorderResolution_example", // String | Resolution
  'recorderOnvif': "recorderOnvif_example", // String | ONVIF
  'recorderPsia': "recorderPsia_example", // String | PSIA
  'recorderPtz': "recorderPtz_example", // String | PTZ
  'recorderDiscontinued': "recorderDiscontinued_example", // String | Discontinued
  'recorderSupport3rdparty': "recorderSupport3rdparty_example", // String | 3rd pparty Camera Support
  'recorderSdCard': "recorderSdCard_example", // String | SD Card
  'recorderUpnp': "recorderUpnp_example", // String | UPnP
  'recorderHotSwap': "recorderHotSwap_example", // String | Hot Swap
  'recorderHdmi': "recorderHdmi_example", // String | HDMI Support
  'recorderDigitalIo': "recorderDigitalIo_example", // String | Digital I/O
  'recorderAudioIn': "recorderAudioIn_example", // String | Audio In
  'recorderAudioOut': "recorderAudioOut_example", // String | Audio Out
  'recorderInputChannels': "recorderInputChannels_example", // String | Input Channels
  'recorderPlaybackChannels': "recorderPlaybackChannels_example", // String | Playback Channels
  'recorderUsb': "recorderUsb_example", // String | USB Ports
  'recorderSdhc': "recorderSdhc_example", // String | SD Card (GB)
  'recorderMobileAccess': "recorderMobileAccess_example", // String | Mobile Access
  'recorderAlarms': "recorderAlarms_example", // String | Alarms
  'recorderRaidSupport': "recorderRaidSupport_example", // String | Raid Support
  'recorderStorage': "recorderStorage_example", // String | Internal Storage
  'recorderAdditionalInformation': "recorderAdditionalInformation_example", // String | Additional Information
  'recorderDefaultUsername': "recorderDefaultUsername_example", // String | Default Username
  'recorderDefaultPassword': "recorderDefaultPassword_example", // String | Default Password
  'recorderJpegUrl': "recorderJpegUrl_example", // String | JPEG URL
  'recorderH264Url': "recorderH264Url_example", // String | H264 URL
  'recorderMjpegUrl': "recorderMjpegUrl_example", // String | MJPEG URL
  'recorderOfficialUrl': "recorderOfficialUrl_example" // String | Official URL
};
apiInstance.apiV1RecordersIdJsonPatch(id, vendorId, recorderModel, recorderName, recorderRecorderType, opts, (error, data, response) => {
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
 **id** | **String**| Recorder ID | 
 **vendorId** | **String**| Vendor ID | 
 **recorderModel** | **String**| Model | 
 **recorderName** | **String**| Name | 
 **recorderRecorderType** | **String**| Type | 
 **recorderResolution** | **String**| Resolution | [optional] 
 **recorderOnvif** | **String**| ONVIF | [optional] 
 **recorderPsia** | **String**| PSIA | [optional] 
 **recorderPtz** | **String**| PTZ | [optional] 
 **recorderDiscontinued** | **String**| Discontinued | [optional] 
 **recorderSupport3rdparty** | **String**| 3rd pparty Camera Support | [optional] 
 **recorderSdCard** | **String**| SD Card | [optional] 
 **recorderUpnp** | **String**| UPnP | [optional] 
 **recorderHotSwap** | **String**| Hot Swap | [optional] 
 **recorderHdmi** | **String**| HDMI Support | [optional] 
 **recorderDigitalIo** | **String**| Digital I/O | [optional] 
 **recorderAudioIn** | **String**| Audio In | [optional] 
 **recorderAudioOut** | **String**| Audio Out | [optional] 
 **recorderInputChannels** | **String**| Input Channels | [optional] 
 **recorderPlaybackChannels** | **String**| Playback Channels | [optional] 
 **recorderUsb** | **String**| USB Ports | [optional] 
 **recorderSdhc** | **String**| SD Card (GB) | [optional] 
 **recorderMobileAccess** | **String**| Mobile Access | [optional] 
 **recorderAlarms** | **String**| Alarms | [optional] 
 **recorderRaidSupport** | **String**| Raid Support | [optional] 
 **recorderStorage** | **String**| Internal Storage | [optional] 
 **recorderAdditionalInformation** | **String**| Additional Information | [optional] 
 **recorderDefaultUsername** | **String**| Default Username | [optional] 
 **recorderDefaultPassword** | **String**| Default Password | [optional] 
 **recorderJpegUrl** | **String**| JPEG URL | [optional] 
 **recorderH264Url** | **String**| H264 URL | [optional] 
 **recorderMjpegUrl** | **String**| MJPEG URL | [optional] 
 **recorderOfficialUrl** | **String**| Official URL | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1RecordersIdJsonPut

> apiV1RecordersIdJsonPut(id, vendorId, recorderModel, recorderName, recorderRecorderType, opts)

Updates an existing Recorder

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.RecordersApi();
let id = "id_example"; // String | Recorder ID
let vendorId = "vendorId_example"; // String | Vendor ID
let recorderModel = "recorderModel_example"; // String | Model
let recorderName = "recorderName_example"; // String | Name
let recorderRecorderType = "recorderRecorderType_example"; // String | Type
let opts = {
  'recorderResolution': "recorderResolution_example", // String | Resolution
  'recorderOnvif': "recorderOnvif_example", // String | ONVIF
  'recorderPsia': "recorderPsia_example", // String | PSIA
  'recorderPtz': "recorderPtz_example", // String | PTZ
  'recorderDiscontinued': "recorderDiscontinued_example", // String | Discontinued
  'recorderSupport3rdparty': "recorderSupport3rdparty_example", // String | 3rd pparty Camera Support
  'recorderSdCard': "recorderSdCard_example", // String | SD Card
  'recorderUpnp': "recorderUpnp_example", // String | UPnP
  'recorderHotSwap': "recorderHotSwap_example", // String | Hot Swap
  'recorderHdmi': "recorderHdmi_example", // String | HDMI Support
  'recorderDigitalIo': "recorderDigitalIo_example", // String | Digital I/O
  'recorderAudioIn': "recorderAudioIn_example", // String | Audio In
  'recorderAudioOut': "recorderAudioOut_example", // String | Audio Out
  'recorderInputChannels': "recorderInputChannels_example", // String | Input Channels
  'recorderPlaybackChannels': "recorderPlaybackChannels_example", // String | Playback Channels
  'recorderUsb': "recorderUsb_example", // String | USB Ports
  'recorderSdhc': "recorderSdhc_example", // String | SD Card (GB)
  'recorderMobileAccess': "recorderMobileAccess_example", // String | Mobile Access
  'recorderAlarms': "recorderAlarms_example", // String | Alarms
  'recorderRaidSupport': "recorderRaidSupport_example", // String | Raid Support
  'recorderStorage': "recorderStorage_example", // String | Internal Storage
  'recorderAdditionalInformation': "recorderAdditionalInformation_example", // String | Additional Information
  'recorderDefaultUsername': "recorderDefaultUsername_example", // String | Default Username
  'recorderDefaultPassword': "recorderDefaultPassword_example", // String | Default Password
  'recorderJpegUrl': "recorderJpegUrl_example", // String | JPEG URL
  'recorderH264Url': "recorderH264Url_example", // String | H264 URL
  'recorderMjpegUrl': "recorderMjpegUrl_example", // String | MJPEG URL
  'recorderOfficialUrl': "recorderOfficialUrl_example" // String | Official URL
};
apiInstance.apiV1RecordersIdJsonPut(id, vendorId, recorderModel, recorderName, recorderRecorderType, opts, (error, data, response) => {
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
 **id** | **String**| Recorder ID | 
 **vendorId** | **String**| Vendor ID | 
 **recorderModel** | **String**| Model | 
 **recorderName** | **String**| Name | 
 **recorderRecorderType** | **String**| Type | 
 **recorderResolution** | **String**| Resolution | [optional] 
 **recorderOnvif** | **String**| ONVIF | [optional] 
 **recorderPsia** | **String**| PSIA | [optional] 
 **recorderPtz** | **String**| PTZ | [optional] 
 **recorderDiscontinued** | **String**| Discontinued | [optional] 
 **recorderSupport3rdparty** | **String**| 3rd pparty Camera Support | [optional] 
 **recorderSdCard** | **String**| SD Card | [optional] 
 **recorderUpnp** | **String**| UPnP | [optional] 
 **recorderHotSwap** | **String**| Hot Swap | [optional] 
 **recorderHdmi** | **String**| HDMI Support | [optional] 
 **recorderDigitalIo** | **String**| Digital I/O | [optional] 
 **recorderAudioIn** | **String**| Audio In | [optional] 
 **recorderAudioOut** | **String**| Audio Out | [optional] 
 **recorderInputChannels** | **String**| Input Channels | [optional] 
 **recorderPlaybackChannels** | **String**| Playback Channels | [optional] 
 **recorderUsb** | **String**| USB Ports | [optional] 
 **recorderSdhc** | **String**| SD Card (GB) | [optional] 
 **recorderMobileAccess** | **String**| Mobile Access | [optional] 
 **recorderAlarms** | **String**| Alarms | [optional] 
 **recorderRaidSupport** | **String**| Raid Support | [optional] 
 **recorderStorage** | **String**| Internal Storage | [optional] 
 **recorderAdditionalInformation** | **String**| Additional Information | [optional] 
 **recorderDefaultUsername** | **String**| Default Username | [optional] 
 **recorderDefaultPassword** | **String**| Default Password | [optional] 
 **recorderJpegUrl** | **String**| JPEG URL | [optional] 
 **recorderH264Url** | **String**| H264 URL | [optional] 
 **recorderMjpegUrl** | **String**| MJPEG URL | [optional] 
 **recorderOfficialUrl** | **String**| Official URL | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## apiV1RecordersIndex

> apiV1RecordersIndex(opts)

Fetches all Recorders

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.RecordersApi();
let opts = {
  'page': 56, // Number | Page number
  'order': "order_example" // String | Sort order
};
apiInstance.apiV1RecordersIndex(opts, (error, data, response) => {
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


## apiV1RecordersSearch

> apiV1RecordersSearch(opts)

Searches all Recorders

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.RecordersApi();
let opts = {
  'page': 56, // Number | Page number
  'qModelCont': "qModelCont_example", // String | Model
  'qVendorNameCont': "qVendorNameCont_example", // String | Vendor
  'qSdhcEq': "qSdhcEq_example", // String | SD Card (GB)
  'qTypeEq': "qTypeEq_example", // String | Type
  'qResolutionEq': "qResolutionEq_example", // String | Resolution
  'qInputChannelsEq': "qInputChannelsEq_example", // String | Input Channels
  'qPlaybackChannelsEq': "qPlaybackChannelsEq_example", // String | Playback Channels
  'qOnvifTrue': "qOnvifTrue_example", // String | ONVIF
  'qPsiaTrue': "qPsiaTrue_example", // String | PSIA
  'qPtzTrue': "qPtzTrue_example", // String | PTZ
  'qSdCardTrue': "qSdCardTrue_example", // String | SD Card
  'qUpnpTrue': "qUpnpTrue_example", // String | UPnP
  'qAudioInTrue': "qAudioInTrue_example", // String | Audio In
  'qAudioOutTrue': "qAudioOutTrue_example", // String | Audio Out
  'qHdmiTrue': "qHdmiTrue_example", // String | HDMI Support
  'qHotSwapTrue': "qHotSwapTrue_example", // String | Hot Swap
  'qSupport3rdpartyTrue': "qSupport3rdpartyTrue_example", // String | 3rd pparty Camera Support
  'qDigitalIoTrue': "qDigitalIoTrue_example" // String | Digital I/O
};
apiInstance.apiV1RecordersSearch(opts, (error, data, response) => {
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
 **qVendorNameCont** | **String**| Vendor | [optional] 
 **qSdhcEq** | **String**| SD Card (GB) | [optional] 
 **qTypeEq** | **String**| Type | [optional] 
 **qResolutionEq** | **String**| Resolution | [optional] 
 **qInputChannelsEq** | **String**| Input Channels | [optional] 
 **qPlaybackChannelsEq** | **String**| Playback Channels | [optional] 
 **qOnvifTrue** | **String**| ONVIF | [optional] 
 **qPsiaTrue** | **String**| PSIA | [optional] 
 **qPtzTrue** | **String**| PTZ | [optional] 
 **qSdCardTrue** | **String**| SD Card | [optional] 
 **qUpnpTrue** | **String**| UPnP | [optional] 
 **qAudioInTrue** | **String**| Audio In | [optional] 
 **qAudioOutTrue** | **String**| Audio Out | [optional] 
 **qHdmiTrue** | **String**| HDMI Support | [optional] 
 **qHotSwapTrue** | **String**| Hot Swap | [optional] 
 **qSupport3rdpartyTrue** | **String**| 3rd pparty Camera Support | [optional] 
 **qDigitalIoTrue** | **String**| Digital I/O | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1RecordersShow

> apiV1RecordersShow(id)

Fetches a single Recorder

### Example

```javascript
import CambaseIo from 'cambase_io';

let apiInstance = new CambaseIo.RecordersApi();
let id = 56; // Number | Recorder ID
apiInstance.apiV1RecordersShow(id, (error, data, response) => {
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
 **id** | **Number**| Recorder ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

