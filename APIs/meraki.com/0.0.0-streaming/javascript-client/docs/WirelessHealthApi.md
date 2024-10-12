# MerakiDashboardApi.WirelessHealthApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkClientConnectionStats**](WirelessHealthApi.md#getNetworkClientConnectionStats) | **GET** /networks/{networkId}/clients/{clientId}/connectionStats | Aggregated connectivity info for a given client on this network
[**getNetworkClientLatencyStats**](WirelessHealthApi.md#getNetworkClientLatencyStats) | **GET** /networks/{networkId}/clients/{clientId}/latencyStats | Aggregated latency info for a given client on this network
[**getNetworkClientsConnectionStats**](WirelessHealthApi.md#getNetworkClientsConnectionStats) | **GET** /networks/{networkId}/clients/connectionStats | Aggregated connectivity info for this network, grouped by clients
[**getNetworkClientsLatencyStats**](WirelessHealthApi.md#getNetworkClientsLatencyStats) | **GET** /networks/{networkId}/clients/latencyStats | Aggregated latency info for this network, grouped by clients
[**getNetworkConnectionStats**](WirelessHealthApi.md#getNetworkConnectionStats) | **GET** /networks/{networkId}/connectionStats | Aggregated connectivity info for this network
[**getNetworkDeviceConnectionStats**](WirelessHealthApi.md#getNetworkDeviceConnectionStats) | **GET** /networks/{networkId}/devices/{serial}/connectionStats | Aggregated connectivity info for a given AP on this network
[**getNetworkDeviceLatencyStats**](WirelessHealthApi.md#getNetworkDeviceLatencyStats) | **GET** /networks/{networkId}/devices/{serial}/latencyStats | Aggregated latency info for a given AP on this network
[**getNetworkDevicesConnectionStats**](WirelessHealthApi.md#getNetworkDevicesConnectionStats) | **GET** /networks/{networkId}/devices/connectionStats | Aggregated connectivity info for this network, grouped by node
[**getNetworkDevicesLatencyStats**](WirelessHealthApi.md#getNetworkDevicesLatencyStats) | **GET** /networks/{networkId}/devices/latencyStats | Aggregated latency info for this network, grouped by node
[**getNetworkFailedConnections**](WirelessHealthApi.md#getNetworkFailedConnections) | **GET** /networks/{networkId}/failedConnections | List of all failed client connection events on this network in a given time range
[**getNetworkLatencyStats**](WirelessHealthApi.md#getNetworkLatencyStats) | **GET** /networks/{networkId}/latencyStats | Aggregated latency info for this network



## getNetworkClientConnectionStats

> Object getNetworkClientConnectionStats(networkId, clientId, opts)

Aggregated connectivity info for a given client on this network

Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkClientConnectionStats(networkId, clientId, opts, (error, data, response) => {
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
 **clientId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkClientLatencyStats

> Object getNetworkClientLatencyStats(networkId, clientId, opts)

Aggregated latency info for a given client on this network

Aggregated latency info for a given client on this network. Clients are identified by their MAC.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let clientId = "clientId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkClientLatencyStats(networkId, clientId, opts, (error, data, response) => {
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
 **clientId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkClientsConnectionStats

> [Object] getNetworkClientsConnectionStats(networkId, opts)

Aggregated connectivity info for this network, grouped by clients

Aggregated connectivity info for this network, grouped by clients

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkClientsConnectionStats(networkId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkClientsLatencyStats

> [Object] getNetworkClientsLatencyStats(networkId, opts)

Aggregated latency info for this network, grouped by clients

Aggregated latency info for this network, grouped by clients

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkClientsLatencyStats(networkId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkConnectionStats

> Object getNetworkConnectionStats(networkId, opts)

Aggregated connectivity info for this network

Aggregated connectivity info for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkConnectionStats(networkId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkDeviceConnectionStats

> Object getNetworkDeviceConnectionStats(networkId, serial, opts)

Aggregated connectivity info for a given AP on this network

Aggregated connectivity info for a given AP on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let serial = "serial_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkDeviceConnectionStats(networkId, serial, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkDeviceLatencyStats

> Object getNetworkDeviceLatencyStats(networkId, serial, opts)

Aggregated latency info for a given AP on this network

Aggregated latency info for a given AP on this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let serial = "serial_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkDeviceLatencyStats(networkId, serial, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkDevicesConnectionStats

> [Object] getNetworkDevicesConnectionStats(networkId, opts)

Aggregated connectivity info for this network, grouped by node

Aggregated connectivity info for this network, grouped by node

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example" // String | Filter results by AP Tag
};
apiInstance.getNetworkDevicesConnectionStats(networkId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkDevicesLatencyStats

> [Object] getNetworkDevicesLatencyStats(networkId, opts)

Aggregated latency info for this network, grouped by node

Aggregated latency info for this network, grouped by node

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkDevicesLatencyStats(networkId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFailedConnections

> [Object] getNetworkFailedConnections(networkId, opts)

List of all failed client connection events on this network in a given time range

List of all failed client connection events on this network in a given time range

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'serial': "serial_example", // String | Filter by AP
  'clientId': "clientId_example" // String | Filter by client MAC
};
apiInstance.getNetworkFailedConnections(networkId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **serial** | **String**| Filter by AP | [optional] 
 **clientId** | **String**| Filter by client MAC | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkLatencyStats

> Object getNetworkLatencyStats(networkId, opts)

Aggregated latency info for this network

Aggregated latency info for this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.WirelessHealthApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
  'band': "band_example", // String | Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
  'ssid': 56, // Number | Filter results by SSID
  'vlan': 56, // Number | Filter results by VLAN
  'apTag': "apTag_example", // String | Filter results by AP Tag
  'fields': "fields_example" // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
};
apiInstance.getNetworkLatencyStats(networkId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] 
 **band** | **String**| Filter results by band (either &#39;2.4&#39; or &#39;5&#39;). Note that data prior to February 2020 will not have band information. | [optional] 
 **ssid** | **Number**| Filter results by SSID | [optional] 
 **vlan** | **Number**| Filter results by VLAN | [optional] 
 **apTag** | **String**| Filter results by AP Tag | [optional] 
 **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

