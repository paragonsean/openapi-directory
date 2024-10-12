# MerakiDashboardApi.WirelessProfilesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkCameraWirelessProfile_1**](WirelessProfilesApi.md#createNetworkCameraWirelessProfile_1) | **POST** /networks/{networkId}/camera/wirelessProfiles | Creates a new camera wireless profile for this network.
[**deleteNetworkCameraWirelessProfile_1**](WirelessProfilesApi.md#deleteNetworkCameraWirelessProfile_1) | **DELETE** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Delete an existing camera wireless profile for this network.
[**getDeviceCameraWirelessProfiles_1**](WirelessProfilesApi.md#getDeviceCameraWirelessProfiles_1) | **GET** /devices/{serial}/camera/wirelessProfiles | Returns wireless profile assigned to the given camera
[**getNetworkCameraWirelessProfile_1**](WirelessProfilesApi.md#getNetworkCameraWirelessProfile_1) | **GET** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Retrieve a single camera wireless profile.
[**getNetworkCameraWirelessProfiles_1**](WirelessProfilesApi.md#getNetworkCameraWirelessProfiles_1) | **GET** /networks/{networkId}/camera/wirelessProfiles | List the camera wireless profiles for this network.
[**updateDeviceCameraWirelessProfiles_1**](WirelessProfilesApi.md#updateDeviceCameraWirelessProfiles_1) | **PUT** /devices/{serial}/camera/wirelessProfiles | Assign wireless profiles to the given camera
[**updateNetworkCameraWirelessProfile_1**](WirelessProfilesApi.md#updateNetworkCameraWirelessProfile_1) | **PUT** /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId} | Update an existing camera wireless profile in this network.



## createNetworkCameraWirelessProfile_1

> Object createNetworkCameraWirelessProfile_1(networkId, createNetworkCameraWirelessProfileRequest)

Creates a new camera wireless profile for this network.

Creates a new camera wireless profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessProfilesApi();
let networkId = "networkId_example"; // String | 
let createNetworkCameraWirelessProfileRequest = new MerakiDashboardApi.CreateNetworkCameraWirelessProfileRequest(); // CreateNetworkCameraWirelessProfileRequest | 
apiInstance.createNetworkCameraWirelessProfile_1(networkId, createNetworkCameraWirelessProfileRequest, (error, data, response) => {
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
 **createNetworkCameraWirelessProfileRequest** | [**CreateNetworkCameraWirelessProfileRequest**](CreateNetworkCameraWirelessProfileRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkCameraWirelessProfile_1

> deleteNetworkCameraWirelessProfile_1(networkId, wirelessProfileId)

Delete an existing camera wireless profile for this network.

Delete an existing camera wireless profile for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessProfilesApi();
let networkId = "networkId_example"; // String | 
let wirelessProfileId = "wirelessProfileId_example"; // String | 
apiInstance.deleteNetworkCameraWirelessProfile_1(networkId, wirelessProfileId, (error, data, response) => {
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
 **wirelessProfileId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDeviceCameraWirelessProfiles_1

> Object getDeviceCameraWirelessProfiles_1(serial)

Returns wireless profile assigned to the given camera

Returns wireless profile assigned to the given camera

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessProfilesApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceCameraWirelessProfiles_1(serial, (error, data, response) => {
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


## getNetworkCameraWirelessProfile_1

> Object getNetworkCameraWirelessProfile_1(networkId, wirelessProfileId)

Retrieve a single camera wireless profile.

Retrieve a single camera wireless profile.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessProfilesApi();
let networkId = "networkId_example"; // String | 
let wirelessProfileId = "wirelessProfileId_example"; // String | 
apiInstance.getNetworkCameraWirelessProfile_1(networkId, wirelessProfileId, (error, data, response) => {
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
 **wirelessProfileId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkCameraWirelessProfiles_1

> [Object] getNetworkCameraWirelessProfiles_1(networkId)

List the camera wireless profiles for this network.

List the camera wireless profiles for this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessProfilesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkCameraWirelessProfiles_1(networkId, (error, data, response) => {
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


## updateDeviceCameraWirelessProfiles_1

> Object updateDeviceCameraWirelessProfiles_1(serial, updateDeviceCameraWirelessProfilesRequest)

Assign wireless profiles to the given camera

Assign wireless profiles to the given camera. Incremental updates are not supported, all profile assignment need to be supplied at once.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessProfilesApi();
let serial = "serial_example"; // String | 
let updateDeviceCameraWirelessProfilesRequest = new MerakiDashboardApi.UpdateDeviceCameraWirelessProfilesRequest(); // UpdateDeviceCameraWirelessProfilesRequest | 
apiInstance.updateDeviceCameraWirelessProfiles_1(serial, updateDeviceCameraWirelessProfilesRequest, (error, data, response) => {
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
 **updateDeviceCameraWirelessProfilesRequest** | [**UpdateDeviceCameraWirelessProfilesRequest**](UpdateDeviceCameraWirelessProfilesRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkCameraWirelessProfile_1

> Object updateNetworkCameraWirelessProfile_1(networkId, wirelessProfileId, opts)

Update an existing camera wireless profile in this network.

Update an existing camera wireless profile in this network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessProfilesApi();
let networkId = "networkId_example"; // String | 
let wirelessProfileId = "wirelessProfileId_example"; // String | 
let opts = {
  'updateNetworkCameraWirelessProfileRequest': new MerakiDashboardApi.UpdateNetworkCameraWirelessProfileRequest() // UpdateNetworkCameraWirelessProfileRequest | 
};
apiInstance.updateNetworkCameraWirelessProfile_1(networkId, wirelessProfileId, opts, (error, data, response) => {
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
 **wirelessProfileId** | **String**|  | 
 **updateNetworkCameraWirelessProfileRequest** | [**UpdateNetworkCameraWirelessProfileRequest**](UpdateNetworkCameraWirelessProfileRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

