# MerakiDashboardApi.SenseApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceCameraSenseObjectDetectionModels_1**](SenseApi.md#getDeviceCameraSenseObjectDetectionModels_1) | **GET** /devices/{serial}/camera/sense/objectDetectionModels | Returns the MV Sense object detection model list for the given camera
[**getDeviceCameraSense_1**](SenseApi.md#getDeviceCameraSense_1) | **GET** /devices/{serial}/camera/sense | Returns sense settings for a given camera
[**updateDeviceCameraSense_1**](SenseApi.md#updateDeviceCameraSense_1) | **PUT** /devices/{serial}/camera/sense | Update sense settings for the given camera



## getDeviceCameraSenseObjectDetectionModels_1

> [Object] getDeviceCameraSenseObjectDetectionModels_1(serial)

Returns the MV Sense object detection model list for the given camera

Returns the MV Sense object detection model list for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SenseApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraSenseObjectDetectionModels_1(serial, (error, data, response) => {
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

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceCameraSense_1

> Object getDeviceCameraSense_1(serial)

Returns sense settings for a given camera

Returns sense settings for a given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SenseApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraSense_1(serial, (error, data, response) => {
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


## updateDeviceCameraSense_1

> Object updateDeviceCameraSense_1(serial, opts)

Update sense settings for the given camera

Update sense settings for the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SenseApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceCameraSenseRequest': new MerakiDashboardApi.UpdateDeviceCameraSenseRequest() // UpdateDeviceCameraSenseRequest | 
};
apiInstance.updateDeviceCameraSense_1(serial, opts, (error, data, response) => {
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
 **updateDeviceCameraSenseRequest** | [**UpdateDeviceCameraSenseRequest**](UpdateDeviceCameraSenseRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

