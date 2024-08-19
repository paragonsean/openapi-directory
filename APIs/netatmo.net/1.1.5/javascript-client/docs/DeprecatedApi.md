# Netatmo.DeprecatedApi

All URIs are relative to *https://api.netatmo.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicelist**](DeprecatedApi.md#devicelist) | **GET** /devicelist | 
[**getthermstate**](DeprecatedApi.md#getthermstate) | **GET** /getthermstate | 
[**getuser**](DeprecatedApi.md#getuser) | **GET** /getuser | 



## devicelist

> NADeviceListResponse devicelist(opts)



The method devicelist returns the list of devices owned by the user, and their modules. A device is identified by its _id (which is its mac address) and each device may have one, several or no modules, also identified by an _id. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.DeprecatedApi();
let opts = {
  'appType': "appType_example", // String | Defines which device type will be returned by devicelist. It could be app_thermostat or app_station (by default if not provided)
  'deviceId': "deviceId_example", // String | Specify a device_id if you want to retrieve only this device informations.
  'getFavorites': false // Boolean | When set to \"true\", the favorite devices of the user are returned. This flag is available only if the devices requested are Weather Stations.
};
apiInstance.devicelist(opts, (error, data, response) => {
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
 **appType** | **String**| Defines which device type will be returned by devicelist. It could be app_thermostat or app_station (by default if not provided) | [optional] 
 **deviceId** | **String**| Specify a device_id if you want to retrieve only this device informations. | [optional] 
 **getFavorites** | **Boolean**| When set to \&quot;true\&quot;, the favorite devices of the user are returned. This flag is available only if the devices requested are Weather Stations. | [optional] [default to false]

### Return type

[**NADeviceListResponse**](NADeviceListResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getthermstate

> NAThermStateResponse getthermstate(deviceId, moduleId)



The method getthermstate returns the last Thermostat measurements, its current weekly schedule, and, if present, its current manual temperature setpoint.

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.DeprecatedApi();
let deviceId = "deviceId_example"; // String | The relay id
let moduleId = "moduleId_example"; // String | The thermostat id
apiInstance.getthermstate(deviceId, moduleId, (error, data, response) => {
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
 **deviceId** | **String**| The relay id | 
 **moduleId** | **String**| The thermostat id | 

### Return type

[**NAThermStateResponse**](NAThermStateResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getuser

> NAUserResponse getuser()



The method getuser returns information about a user such as prefered language, prefered units, and list of devices. 

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.DeprecatedApi();
apiInstance.getuser((error, data, response) => {
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

[**NAUserResponse**](NAUserResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

