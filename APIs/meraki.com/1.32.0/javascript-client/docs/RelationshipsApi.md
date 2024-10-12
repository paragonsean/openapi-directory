# MerakiDashboardApi.RelationshipsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceSensorRelationships_1**](RelationshipsApi.md#getDeviceSensorRelationships_1) | **GET** /devices/{serial}/sensor/relationships | List the sensor roles for a given sensor or camera device.
[**getNetworkSensorRelationships_1**](RelationshipsApi.md#getNetworkSensorRelationships_1) | **GET** /networks/{networkId}/sensor/relationships | List the sensor roles for devices in a given network
[**updateDeviceSensorRelationships_1**](RelationshipsApi.md#updateDeviceSensorRelationships_1) | **PUT** /devices/{serial}/sensor/relationships | Assign one or more sensor roles to a given sensor or camera device.



## getDeviceSensorRelationships_1

> [GetDeviceSensorRelationships200ResponseInner] getDeviceSensorRelationships_1(serial)

List the sensor roles for a given sensor or camera device.

List the sensor roles for a given sensor or camera device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RelationshipsApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceSensorRelationships_1(serial, (error, data, response) => {
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

[**[GetDeviceSensorRelationships200ResponseInner]**](GetDeviceSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSensorRelationships_1

> [GetNetworkSensorRelationships200ResponseInner] getNetworkSensorRelationships_1(networkId)

List the sensor roles for devices in a given network

List the sensor roles for devices in a given network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RelationshipsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSensorRelationships_1(networkId, (error, data, response) => {
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

[**[GetNetworkSensorRelationships200ResponseInner]**](GetNetworkSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceSensorRelationships_1

> GetDeviceSensorRelationships200ResponseInner updateDeviceSensorRelationships_1(serial, opts)

Assign one or more sensor roles to a given sensor or camera device.

Assign one or more sensor roles to a given sensor or camera device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.RelationshipsApi();
let serial = "serial_example"; // String | 
let opts = {
  'updateDeviceSensorRelationshipsRequest': new MerakiDashboardApi.UpdateDeviceSensorRelationshipsRequest() // UpdateDeviceSensorRelationshipsRequest | 
};
apiInstance.updateDeviceSensorRelationships_1(serial, opts, (error, data, response) => {
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
 **updateDeviceSensorRelationshipsRequest** | [**UpdateDeviceSensorRelationshipsRequest**](UpdateDeviceSensorRelationshipsRequest.md)|  | [optional] 

### Return type

[**GetDeviceSensorRelationships200ResponseInner**](GetDeviceSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

