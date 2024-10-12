# MerakiDashboardApi.SMApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSmBypassActivationLockAttempt**](SMApi.md#createNetworkSmBypassActivationLockAttempt) | **POST** /networks/{networkId}/sm/bypassActivationLockAttempts | Bypass activation lock attempt
[**getNetworkSmBypassActivationLockAttempt**](SMApi.md#getNetworkSmBypassActivationLockAttempt) | **GET** /networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId} | Bypass activation lock attempt status
[**getNetworkSmCellularUsageHistory**](SMApi.md#getNetworkSmCellularUsageHistory) | **GET** /networks/{networkId}/sm/{deviceId}/cellularUsageHistory | Return the client&#39;s daily cellular data usage history
[**getNetworkSmCerts**](SMApi.md#getNetworkSmCerts) | **GET** /networks/{networkId}/sm/{deviceId}/certs | List the certs on a device
[**getNetworkSmConnectivity**](SMApi.md#getNetworkSmConnectivity) | **GET** /networks/{network_id}/sm/{id}/connectivity | Returns historical connectivity data (whether a device is regularly checking in to Dashboard).
[**getNetworkSmDesktopLogs**](SMApi.md#getNetworkSmDesktopLogs) | **GET** /networks/{network_id}/sm/{id}/desktopLogs | Return historical records of various Systems Manager network connection details for desktop devices.
[**getNetworkSmDeviceCommandLogs**](SMApi.md#getNetworkSmDeviceCommandLogs) | **GET** /networks/{network_id}/sm/{id}/deviceCommandLogs | Return historical records of commands sent to Systems Manager devices
[**getNetworkSmDeviceProfiles**](SMApi.md#getNetworkSmDeviceProfiles) | **GET** /networks/{networkId}/sm/{deviceId}/deviceProfiles | Get the profiles associated with a device
[**getNetworkSmDevices**](SMApi.md#getNetworkSmDevices) | **GET** /networks/{networkId}/sm/devices | List the devices enrolled in an SM network with various specified fields and filters
[**getNetworkSmNetworkAdapters**](SMApi.md#getNetworkSmNetworkAdapters) | **GET** /networks/{networkId}/sm/{deviceId}/networkAdapters | List the network adapters of a device
[**getNetworkSmPerformanceHistory**](SMApi.md#getNetworkSmPerformanceHistory) | **GET** /networks/{network_id}/sm/{id}/performanceHistory | Return historical records of various Systems Manager client metrics for desktop devices.
[**getNetworkSmProfiles**](SMApi.md#getNetworkSmProfiles) | **GET** /networks/{networkId}/sm/profiles | List all the profiles in the network
[**getNetworkSmRestrictions**](SMApi.md#getNetworkSmRestrictions) | **GET** /networks/{networkId}/sm/{deviceId}/restrictions | List the restrictions on a device
[**getNetworkSmSecurityCenters**](SMApi.md#getNetworkSmSecurityCenters) | **GET** /networks/{networkId}/sm/{deviceId}/securityCenters | List the security centers on a device
[**getNetworkSmSoftwares**](SMApi.md#getNetworkSmSoftwares) | **GET** /networks/{networkId}/sm/{deviceId}/softwares | Get a list of softwares associated with a device
[**getNetworkSmUserDeviceProfiles**](SMApi.md#getNetworkSmUserDeviceProfiles) | **GET** /networks/{networkId}/sm/user/{userId}/deviceProfiles | Get the profiles associated with a user
[**getNetworkSmUserSoftwares**](SMApi.md#getNetworkSmUserSoftwares) | **GET** /networks/{networkId}/sm/user/{userId}/softwares | Get a list of softwares associated with a user
[**getNetworkSmUsers**](SMApi.md#getNetworkSmUsers) | **GET** /networks/{networkId}/sm/users | List the owners in an SM network with various specified fields and filters
[**getNetworkSmWlanLists**](SMApi.md#getNetworkSmWlanLists) | **GET** /networks/{networkId}/sm/{deviceId}/wlanLists | List the saved SSID names on a device
[**lockNetworkSmDevices**](SMApi.md#lockNetworkSmDevices) | **PUT** /networks/{network_id}/sm/devices/lock | Lock a set of devices
[**refreshNetworkSmDeviceDetails**](SMApi.md#refreshNetworkSmDeviceDetails) | **POST** /networks/{networkId}/sm/device/{deviceId}/refreshDetails | Refresh the details of a device
[**unenrollNetworkSmDevice**](SMApi.md#unenrollNetworkSmDevice) | **POST** /networks/{networkId}/sm/devices/{deviceId}/unenroll | Unenroll a device
[**updateNetworkSmDeviceFields**](SMApi.md#updateNetworkSmDeviceFields) | **PUT** /networks/{networkId}/sm/device/fields | Modify the fields of a device
[**updateNetworkSmDevicesTags**](SMApi.md#updateNetworkSmDevicesTags) | **PUT** /networks/{networkId}/sm/devices/tags | Add, delete, or update the tags of a set of devices
[**wipeNetworkSmDevice**](SMApi.md#wipeNetworkSmDevice) | **PUT** /networks/{networkId}/sm/device/wipe | Wipe a device



## createNetworkSmBypassActivationLockAttempt

> Object createNetworkSmBypassActivationLockAttempt(networkId, createNetworkSmBypassActivationLockAttemptRequest)

Bypass activation lock attempt

Bypass activation lock attempt

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let createNetworkSmBypassActivationLockAttemptRequest = new MerakiDashboardApi.CreateNetworkSmBypassActivationLockAttemptRequest(); // CreateNetworkSmBypassActivationLockAttemptRequest | 
apiInstance.createNetworkSmBypassActivationLockAttempt(networkId, createNetworkSmBypassActivationLockAttemptRequest, (error, data, response) => {
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
 **createNetworkSmBypassActivationLockAttemptRequest** | [**CreateNetworkSmBypassActivationLockAttemptRequest**](CreateNetworkSmBypassActivationLockAttemptRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getNetworkSmBypassActivationLockAttempt

> Object getNetworkSmBypassActivationLockAttempt(networkId, attemptId)

Bypass activation lock attempt status

Bypass activation lock attempt status

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let attemptId = "attemptId_example"; // String | 
apiInstance.getNetworkSmBypassActivationLockAttempt(networkId, attemptId, (error, data, response) => {
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
 **attemptId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmCellularUsageHistory

> [Object] getNetworkSmCellularUsageHistory(networkId, deviceId)

Return the client&#39;s daily cellular data usage history

Return the client&#39;s daily cellular data usage history. Usage data is in kilobytes.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmCellularUsageHistory(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmCerts

> [Object] getNetworkSmCerts(networkId, deviceId)

List the certs on a device

List the certs on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmCerts(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmConnectivity

> [Object] getNetworkSmConnectivity(networkId, id, opts)

Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSmConnectivity(networkId, id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDesktopLogs

> [Object] getNetworkSmDesktopLogs(networkId, id, opts)

Return historical records of various Systems Manager network connection details for desktop devices.

Return historical records of various Systems Manager network connection details for desktop devices.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSmDesktopLogs(networkId, id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceCommandLogs

> [Object] getNetworkSmDeviceCommandLogs(networkId, id, opts)

Return historical records of commands sent to Systems Manager devices

Return historical records of commands sent to Systems Manager devices. Note that this will include the name of the Dashboard user who initiated the command if it was generated by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out of any reports.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSmDeviceCommandLogs(networkId, id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDeviceProfiles

> [Object] getNetworkSmDeviceProfiles(networkId, deviceId)

Get the profiles associated with a device

Get the profiles associated with a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmDeviceProfiles(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmDevices

> Object getNetworkSmDevices(networkId, opts)

List the devices enrolled in an SM network with various specified fields and filters

List the devices enrolled in an SM network with various specified fields and filters

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'fields': "fields_example", // String | Additional fields that will be displayed for each device. Multiple fields can be passed in as comma separated values.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, and androidSecurityPatchVersion.
  'wifiMacs': "wifiMacs_example", // String | Filter devices by wifi mac(s). Multiple wifi macs can be passed in as comma separated values.
  'serials': "serials_example", // String | Filter devices by serial(s). Multiple serials can be passed in as comma separated values.
  'ids': "ids_example", // String | Filter devices by id(s). Multiple ids can be passed in as comma separated values.
  'scope': "scope_example", // String | Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags as comma separated values.
  'batchSize': 56, // Number | Number of devices to return, 1000 is the default as well as the max.
  'batchToken': "batchToken_example" // String | If the network has more devices than the batch size, a batch token will be returned     as a part of the device list. To see the remainder of the devices, pass in the batchToken as a parameter in the next request.     Requests made with the batchToken do not require additional parameters as the batchToken includes the parameters passed in     with the original request. Additional parameters passed in with the batchToken will be ignored.
};
apiInstance.getNetworkSmDevices(networkId, opts, (error, data, response) => {
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
 **fields** | **String**| Additional fields that will be displayed for each device. Multiple fields can be passed in as comma separated values.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, and androidSecurityPatchVersion. | [optional] 
 **wifiMacs** | **String**| Filter devices by wifi mac(s). Multiple wifi macs can be passed in as comma separated values. | [optional] 
 **serials** | **String**| Filter devices by serial(s). Multiple serials can be passed in as comma separated values. | [optional] 
 **ids** | **String**| Filter devices by id(s). Multiple ids can be passed in as comma separated values. | [optional] 
 **scope** | **String**| Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags as comma separated values. | [optional] 
 **batchSize** | **Number**| Number of devices to return, 1000 is the default as well as the max. | [optional] 
 **batchToken** | **String**| If the network has more devices than the batch size, a batch token will be returned     as a part of the device list. To see the remainder of the devices, pass in the batchToken as a parameter in the next request.     Requests made with the batchToken do not require additional parameters as the batchToken includes the parameters passed in     with the original request. Additional parameters passed in with the batchToken will be ignored. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmNetworkAdapters

> [Object] getNetworkSmNetworkAdapters(networkId, deviceId)

List the network adapters of a device

List the network adapters of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmNetworkAdapters(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmPerformanceHistory

> [Object] getNetworkSmPerformanceHistory(networkId, id, opts)

Return historical records of various Systems Manager client metrics for desktop devices.

Return historical records of various Systems Manager client metrics for desktop devices.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getNetworkSmPerformanceHistory(networkId, id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmProfiles

> Object getNetworkSmProfiles(networkId)

List all the profiles in the network

List all the profiles in the network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSmProfiles(networkId, (error, data, response) => {
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmRestrictions

> [Object] getNetworkSmRestrictions(networkId, deviceId)

List the restrictions on a device

List the restrictions on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmRestrictions(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmSecurityCenters

> [Object] getNetworkSmSecurityCenters(networkId, deviceId)

List the security centers on a device

List the security centers on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmSecurityCenters(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmSoftwares

> [Object] getNetworkSmSoftwares(networkId, deviceId)

Get a list of softwares associated with a device

Get a list of softwares associated with a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmSoftwares(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUserDeviceProfiles

> [Object] getNetworkSmUserDeviceProfiles(networkId, userId)

Get the profiles associated with a user

Get the profiles associated with a user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getNetworkSmUserDeviceProfiles(networkId, userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUserSoftwares

> [Object] getNetworkSmUserSoftwares(networkId, userId)

Get a list of softwares associated with a user

Get a list of softwares associated with a user

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getNetworkSmUserSoftwares(networkId, userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmUsers

> [Object] getNetworkSmUsers(networkId, opts)

List the owners in an SM network with various specified fields and filters

List the owners in an SM network with various specified fields and filters

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'ids': "ids_example", // String | Filter users by id(s). Multiple ids can be passed in as comma separated values.
  'usernames': "usernames_example", // String | Filter users by username(s). Multiple usernames can be passed in as comma separated values.
  'emails': "emails_example", // String | Filter users by email(s). Multiple emails can be passed in as comma separated values.
  'scope': "scope_example" // String | Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags as comma separated values.
};
apiInstance.getNetworkSmUsers(networkId, opts, (error, data, response) => {
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
 **ids** | **String**| Filter users by id(s). Multiple ids can be passed in as comma separated values. | [optional] 
 **usernames** | **String**| Filter users by username(s). Multiple usernames can be passed in as comma separated values. | [optional] 
 **emails** | **String**| Filter users by email(s). Multiple emails can be passed in as comma separated values. | [optional] 
 **scope** | **String**| Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags as comma separated values. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmWlanLists

> [Object] getNetworkSmWlanLists(networkId, deviceId)

List the saved SSID names on a device

List the saved SSID names on a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.getNetworkSmWlanLists(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lockNetworkSmDevices

> Object lockNetworkSmDevices(networkId, opts)

Lock a set of devices

Lock a set of devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'lockNetworkSmDevicesRequest': new MerakiDashboardApi.LockNetworkSmDevicesRequest() // LockNetworkSmDevicesRequest | 
};
apiInstance.lockNetworkSmDevices(networkId, opts, (error, data, response) => {
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
 **lockNetworkSmDevicesRequest** | [**LockNetworkSmDevicesRequest**](LockNetworkSmDevicesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## refreshNetworkSmDeviceDetails

> refreshNetworkSmDeviceDetails(networkId, deviceId)

Refresh the details of a device

Refresh the details of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.refreshNetworkSmDeviceDetails(networkId, deviceId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **deviceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## unenrollNetworkSmDevice

> Object unenrollNetworkSmDevice(networkId, deviceId)

Unenroll a device

Unenroll a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let deviceId = "deviceId_example"; // String | 
apiInstance.unenrollNetworkSmDevice(networkId, deviceId, (error, data, response) => {
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
 **deviceId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSmDeviceFields

> Object updateNetworkSmDeviceFields(networkId, updateNetworkSmDeviceFieldsRequest)

Modify the fields of a device

Modify the fields of a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSmDeviceFieldsRequest = new MerakiDashboardApi.UpdateNetworkSmDeviceFieldsRequest(); // UpdateNetworkSmDeviceFieldsRequest | 
apiInstance.updateNetworkSmDeviceFields(networkId, updateNetworkSmDeviceFieldsRequest, (error, data, response) => {
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
 **updateNetworkSmDeviceFieldsRequest** | [**UpdateNetworkSmDeviceFieldsRequest**](UpdateNetworkSmDeviceFieldsRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSmDevicesTags

> Object updateNetworkSmDevicesTags(networkId, updateNetworkSmDevicesTagsRequest)

Add, delete, or update the tags of a set of devices

Add, delete, or update the tags of a set of devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSmDevicesTagsRequest = new MerakiDashboardApi.UpdateNetworkSmDevicesTagsRequest(); // UpdateNetworkSmDevicesTagsRequest | 
apiInstance.updateNetworkSmDevicesTags(networkId, updateNetworkSmDevicesTagsRequest, (error, data, response) => {
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
 **updateNetworkSmDevicesTagsRequest** | [**UpdateNetworkSmDevicesTagsRequest**](UpdateNetworkSmDevicesTagsRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wipeNetworkSmDevice

> Object wipeNetworkSmDevice(networkId, opts)

Wipe a device

Wipe a device

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SMApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'wipeNetworkSmDeviceRequest': new MerakiDashboardApi.WipeNetworkSmDeviceRequest() // WipeNetworkSmDeviceRequest | 
};
apiInstance.wipeNetworkSmDevice(networkId, opts, (error, data, response) => {
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
 **wipeNetworkSmDeviceRequest** | [**WipeNetworkSmDeviceRequest**](WipeNetworkSmDeviceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

