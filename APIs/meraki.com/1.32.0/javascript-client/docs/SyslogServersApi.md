# MerakiDashboardApi.SyslogServersApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNetworkSyslogServers_1**](SyslogServersApi.md#getNetworkSyslogServers_1) | **GET** /networks/{networkId}/syslogServers | List the syslog servers for a network
[**updateNetworkSyslogServers_1**](SyslogServersApi.md#updateNetworkSyslogServers_1) | **PUT** /networks/{networkId}/syslogServers | Update the syslog servers for a network



## getNetworkSyslogServers_1

> GetNetworkSyslogServers200Response getNetworkSyslogServers_1(networkId)

List the syslog servers for a network

List the syslog servers for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SyslogServersApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSyslogServers_1(networkId, (error, data, response) => {
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

[**GetNetworkSyslogServers200Response**](GetNetworkSyslogServers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSyslogServers_1

> GetNetworkSyslogServers200Response updateNetworkSyslogServers_1(networkId, updateNetworkSyslogServersRequest)

Update the syslog servers for a network

Update the syslog servers for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.SyslogServersApi();
let networkId = "networkId_example"; // String | 
let updateNetworkSyslogServersRequest = new MerakiDashboardApi.UpdateNetworkSyslogServersRequest(); // UpdateNetworkSyslogServersRequest | 
apiInstance.updateNetworkSyslogServers_1(networkId, updateNetworkSyslogServersRequest, (error, data, response) => {
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
 **updateNetworkSyslogServersRequest** | [**UpdateNetworkSyslogServersRequest**](UpdateNetworkSyslogServersRequest.md)|  | 

### Return type

[**GetNetworkSyslogServers200Response**](GetNetworkSyslogServers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

