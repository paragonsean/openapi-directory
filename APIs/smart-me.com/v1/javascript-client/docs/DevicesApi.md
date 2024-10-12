# SmartMe.DevicesApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDevicesIdGet**](DevicesApi.md#apiDevicesIdGet) | **GET** /api/Devices/{id} | Gets a Device by it&#39;s ID
[**devicesGet**](DevicesApi.md#devicesGet) | **GET** /api/Devices | Gets all Devices
[**devicesPost**](DevicesApi.md#devicesPost) | **POST** /api/Devices | Creates or updates a Device or updates it&#39;s values.
[**devicesPut**](DevicesApi.md#devicesPut) | **PUT** /api/Devices/{id} | Updates the On/Off Switch on a device.               For new implementations please use the \&quot;actions\&quot; command



## apiDevicesIdGet

> Device apiDevicesIdGet(id)

Gets a Device by it&#39;s ID

Gets a Device by it&#39;s ID

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.DevicesApi();
let id = "id_example"; // String | The ID of the device
apiInstance.apiDevicesIdGet(id, (error, data, response) => {
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
 **id** | **String**| The ID of the device | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## devicesGet

> [Device] devicesGet()

Gets all Devices

Gets all Devices

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.DevicesApi();
apiInstance.devicesGet((error, data, response) => {
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

[**[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## devicesPost

> DeviceToPost devicesPost(deviceToPost)

Creates or updates a Device or updates it&#39;s values.

Creates or updates a Device or updates it&#39;s values.               For a new device leave the ID empty. To create a device you have to set the DeviceEnergyType.              To update values, add the ID of the device and the values you like to set.  (See the Data Type Model for more Information)

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.DevicesApi();
let deviceToPost = new SmartMe.DeviceToPost(); // DeviceToPost | Device object with all the data
apiInstance.devicesPost(deviceToPost, (error, data, response) => {
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
 **deviceToPost** | [**DeviceToPost**](DeviceToPost.md)| Device object with all the data | 

### Return type

[**DeviceToPost**](DeviceToPost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## devicesPut

> Object devicesPut(id, switchState, opts)

Updates the On/Off Switch on a device.               For new implementations please use the \&quot;actions\&quot; command

Updates the On/Off Switch on a device              For new implementations please use the \&quot;actions\&quot; command

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.DevicesApi();
let id = "id_example"; // String | The ID of the device
let switchState = true; // Boolean | The new state of the switch
let opts = {
  'switchNumber': 56 // Number | The number of the switch if there are multiple (1 for L1, 3 for L3)
};
apiInstance.devicesPut(id, switchState, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the device | 
 **switchState** | **Boolean**| The new state of the switch | 
 **switchNumber** | **Number**| The number of the switch if there are multiple (1 for L1, 3 for L3) | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

