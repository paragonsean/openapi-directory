# MerakiDashboardApi.AlternateManagementInterfaceApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSwitchAlternateManagementInterface_1**](AlternateManagementInterfaceApi.md#getNetworkSwitchAlternateManagementInterface_1) | **GET** /networks/{networkId}/switch/alternateManagementInterface | Return the switch alternate management interface for the network
[**getNetworkWirelessAlternateManagementInterface_1**](AlternateManagementInterfaceApi.md#getNetworkWirelessAlternateManagementInterface_1) | **GET** /networks/{networkId}/wireless/alternateManagementInterface | Return alternate management interface and devices with IP assigned
[**updateNetworkSwitchAlternateManagementInterface_1**](AlternateManagementInterfaceApi.md#updateNetworkSwitchAlternateManagementInterface_1) | **PUT** /networks/{networkId}/switch/alternateManagementInterface | Update the switch alternate management interface for the network
[**updateNetworkWirelessAlternateManagementInterface_1**](AlternateManagementInterfaceApi.md#updateNetworkWirelessAlternateManagementInterface_1) | **PUT** /networks/{networkId}/wireless/alternateManagementInterface | Update alternate management interface and device static IP



## getNetworkSwitchAlternateManagementInterface_1

> Object getNetworkSwitchAlternateManagementInterface_1(networkId)

Return the switch alternate management interface for the network

Return the switch alternate management interface for the network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AlternateManagementInterfaceApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchAlternateManagementInterface_1(networkId, (error, data, response) => {
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


## getNetworkWirelessAlternateManagementInterface_1

> Object getNetworkWirelessAlternateManagementInterface_1(networkId)

Return alternate management interface and devices with IP assigned

Return alternate management interface and devices with IP assigned

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AlternateManagementInterfaceApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkWirelessAlternateManagementInterface_1(networkId, (error, data, response) => {
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


## updateNetworkSwitchAlternateManagementInterface_1

> Object updateNetworkSwitchAlternateManagementInterface_1(networkId, opts)

Update the switch alternate management interface for the network

Update the switch alternate management interface for the network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AlternateManagementInterfaceApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchAlternateManagementInterfaceRequest': new MerakiDashboardApi.UpdateNetworkSwitchAlternateManagementInterfaceRequest() // UpdateNetworkSwitchAlternateManagementInterfaceRequest | 
};
apiInstance.updateNetworkSwitchAlternateManagementInterface_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkSwitchAlternateManagementInterfaceRequest** | [**UpdateNetworkSwitchAlternateManagementInterfaceRequest**](UpdateNetworkSwitchAlternateManagementInterfaceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkWirelessAlternateManagementInterface_1

> Object updateNetworkWirelessAlternateManagementInterface_1(networkId, opts)

Update alternate management interface and device static IP

Update alternate management interface and device static IP

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AlternateManagementInterfaceApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkWirelessAlternateManagementInterfaceRequest': new MerakiDashboardApi.UpdateNetworkWirelessAlternateManagementInterfaceRequest() // UpdateNetworkWirelessAlternateManagementInterfaceRequest | 
};
apiInstance.updateNetworkWirelessAlternateManagementInterface_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkWirelessAlternateManagementInterfaceRequest** | [**UpdateNetworkWirelessAlternateManagementInterfaceRequest**](UpdateNetworkWirelessAlternateManagementInterfaceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

