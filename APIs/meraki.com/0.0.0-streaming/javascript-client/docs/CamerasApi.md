# MerakiDashboardApi.CamerasApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generateNetworkCameraSnapshot**](CamerasApi.md#generateNetworkCameraSnapshot) | **POST** /networks/{networkId}/cameras/{serial}/snapshot | Generate a snapshot of what the camera sees at the specified time and return a link to that image.
[**getDeviceCameraVideoSettings**](CamerasApi.md#getDeviceCameraVideoSettings) | **GET** /devices/{serial}/camera/video/settings | Returns video settings for the given camera
[**getNetworkCameraSchedules**](CamerasApi.md#getNetworkCameraSchedules) | **GET** /networks/{networkId}/camera/schedules | Returns a list of all camera recording schedules.
[**getNetworkCameraVideoLink**](CamerasApi.md#getNetworkCameraVideoLink) | **GET** /networks/{networkId}/cameras/{serial}/videoLink | Returns video link to the specified camera
[**updateDeviceCameraVideoSettings**](CamerasApi.md#updateDeviceCameraVideoSettings) | **PUT** /devices/{serial}/camera/video/settings | Update video settings for the given camera



## generateNetworkCameraSnapshot

> Object generateNetworkCameraSnapshot(networkId, serial, opts)

Generate a snapshot of what the camera sees at the specified time and return a link to that image.

Generate a snapshot of what the camera sees at the specified time and return a link to that image.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CamerasApi();
let networkId = "networkId_example"; // String | 
let serial = "serial_example"; // String | 
let opts = {
  'generateNetworkCameraSnapshotRequest': new MerakiDashboardApi.GenerateNetworkCameraSnapshotRequest() // GenerateNetworkCameraSnapshotRequest | 
};
apiInstance.generateNetworkCameraSnapshot(networkId, serial, opts, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **serial** | **String**|  | 
 **generateNetworkCameraSnapshotRequest** | [**GenerateNetworkCameraSnapshotRequest**](GenerateNetworkCameraSnapshotRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDeviceCameraVideoSettings

> Object getDeviceCameraVideoSettings(serial)

Returns video settings for the given camera

Returns video settings for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CamerasApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraVideoSettings(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraSchedules

> [Object] getNetworkCameraSchedules(networkId)

Returns a list of all camera recording schedules.

Returns a list of all camera recording schedules.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CamerasApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCameraSchedules(networkId, (error, data, response) => {
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
 **networkId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraVideoLink

> Object getNetworkCameraVideoLink(networkId, serial, opts)

Returns video link to the specified camera

Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CamerasApi();
let networkId = "networkId_example"; // String | 
let serial = "serial_example"; // String | 
let opts = {
  'timestamp': "timestamp_example" // String | [optional] The video link will start at this timestamp. The timestamp is in UNIX Epoch time (milliseconds). If no timestamp is specified, we will assume current time.
};
apiInstance.getNetworkCameraVideoLink(networkId, serial, opts, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **serial** | **String**|  | 
 **timestamp** | **String**| [optional] The video link will start at this timestamp. The timestamp is in UNIX Epoch time (milliseconds). If no timestamp is specified, we will assume current time. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceCameraVideoSettings

> Object updateDeviceCameraVideoSettings(serial, opts)

Update video settings for the given camera

Update video settings for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.CamerasApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCameraVideoSettingsRequest': new MerakiDashboardApi.UpdateDeviceCameraVideoSettingsRequest() // UpdateDeviceCameraVideoSettingsRequest | 
};
apiInstance.updateDeviceCameraVideoSettings(serial, opts, (error, data, response) => {
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
 **serial** | **String**|  | 
 **updateDeviceCameraVideoSettingsRequest** | [**UpdateDeviceCameraVideoSettingsRequest**](UpdateDeviceCameraVideoSettingsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

