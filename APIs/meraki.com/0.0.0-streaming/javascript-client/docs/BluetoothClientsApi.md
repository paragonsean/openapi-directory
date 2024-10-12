# MerakiDashboardApi.BluetoothClientsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkBluetoothClient**](BluetoothClientsApi.md#getNetworkBluetoothClient) | **GET** /networks/{networkId}/bluetoothClients/{bluetoothClientId} | Return a Bluetooth client
[**getNetworkBluetoothClients**](BluetoothClientsApi.md#getNetworkBluetoothClients) | **GET** /networks/{networkId}/bluetoothClients | List the Bluetooth clients seen by APs in this network



## getNetworkBluetoothClient

> Object getNetworkBluetoothClient(networkId, bluetoothClientId, opts)

Return a Bluetooth client

Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BluetoothClientsApi();
let networkId = "networkId_example"; // String | 
let bluetoothClientId = "bluetoothClientId_example"; // String | 
let opts = {
  'includeConnectivityHistory': true, // Boolean | Include the connectivity history for this client
  'connectivityHistoryTimespan': 56 // Number | The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.
};
apiInstance.getNetworkBluetoothClient(networkId, bluetoothClientId, opts, (error, data, response) => {
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
 **bluetoothClientId** | **String**|  | 
 **includeConnectivityHistory** | **Boolean**| Include the connectivity history for this client | [optional] 
 **connectivityHistoryTimespan** | **Number**| The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkBluetoothClients

> [Object] getNetworkBluetoothClients(networkId, opts)

List the Bluetooth clients seen by APs in this network

List the Bluetooth clients seen by APs in this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BluetoothClientsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day.
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'includeConnectivityHistory': true // Boolean | Include the connectivity history for this client
};
apiInstance.getNetworkBluetoothClients(networkId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 7 days from today. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day. | [optional] 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **includeConnectivityHistory** | **Boolean**| Include the connectivity history for this client | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

