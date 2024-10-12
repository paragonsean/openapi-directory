# MerakiDashboardApi.VideoApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceCameraVideoSettings_1**](VideoApi.md#getDeviceCameraVideoSettings_1) | **GET** /devices/{serial}/camera/video/settings | Returns video settings for the given camera
[**updateDeviceCameraVideoSettings_1**](VideoApi.md#updateDeviceCameraVideoSettings_1) | **PUT** /devices/{serial}/camera/video/settings | Update video settings for the given camera



## getDeviceCameraVideoSettings_1

> Object getDeviceCameraVideoSettings_1(serial)

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

let apiInstance = new MerakiDashboardApi.VideoApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraVideoSettings_1(serial, (error, data, response) => {
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


## updateDeviceCameraVideoSettings_1

> Object updateDeviceCameraVideoSettings_1(serial, opts)

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

let apiInstance = new MerakiDashboardApi.VideoApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCameraVideoSettingsRequest': new MerakiDashboardApi.UpdateDeviceCameraVideoSettingsRequest() // UpdateDeviceCameraVideoSettingsRequest | 
};
apiInstance.updateDeviceCameraVideoSettings_1(serial, opts, (error, data, response) => {
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

