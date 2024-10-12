# MerakiDashboardApi.VLANsApi

All URIs are relative to *https://api.meraki.com/api/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkVlan**](VLANsApi.md#createNetworkVlan) | **POST** /networks/{networkId}/vlans | Add a VLAN
[**deleteNetworkVlan**](VLANsApi.md#deleteNetworkVlan) | **DELETE** /networks/{networkId}/vlans/{vlanId} | Delete a VLAN from a network
[**getNetworkVlan**](VLANsApi.md#getNetworkVlan) | **GET** /networks/{networkId}/vlans/{vlanId} | Return a VLAN
[**getNetworkVlans**](VLANsApi.md#getNetworkVlans) | **GET** /networks/{networkId}/vlans | List the VLANs for an MX network
[**getNetworkVlansEnabledState**](VLANsApi.md#getNetworkVlansEnabledState) | **GET** /networks/{networkId}/vlansEnabledState | Returns the enabled status of VLANs for the network
[**updateNetworkVlan**](VLANsApi.md#updateNetworkVlan) | **PUT** /networks/{networkId}/vlans/{vlanId} | Update a VLAN
[**updateNetworkVlansEnabledState**](VLANsApi.md#updateNetworkVlansEnabledState) | **PUT** /networks/{networkId}/vlansEnabledState | Enable/Disable VLANs for the given network



## createNetworkVlan

> Object createNetworkVlan(networkId, createNetworkVlanRequest)

Add a VLAN

Add a VLAN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.VLANsApi();
let networkId = "networkId_example"; // String | 
let createNetworkVlanRequest = new MerakiDashboardApi.CreateNetworkVlanRequest(); // CreateNetworkVlanRequest | 
apiInstance.createNetworkVlan(networkId, createNetworkVlanRequest, (error, data, response) => {
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
 **createNetworkVlanRequest** | [**CreateNetworkVlanRequest**](CreateNetworkVlanRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkVlan

> deleteNetworkVlan(networkId, vlanId)

Delete a VLAN from a network

Delete a VLAN from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.VLANsApi();
let networkId = "networkId_example"; // String | 
let vlanId = "vlanId_example"; // String | 
apiInstance.deleteNetworkVlan(networkId, vlanId, (error, data, response) => {
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
 **vlanId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkVlan

> Object getNetworkVlan(networkId, vlanId)

Return a VLAN

Return a VLAN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.VLANsApi();
let networkId = "networkId_example"; // String | 
let vlanId = "vlanId_example"; // String | 
apiInstance.getNetworkVlan(networkId, vlanId, (error, data, response) => {
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
 **vlanId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkVlans

> [Object] getNetworkVlans(networkId)

List the VLANs for an MX network

List the VLANs for an MX network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.VLANsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkVlans(networkId, (error, data, response) => {
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


## getNetworkVlansEnabledState

> Object getNetworkVlansEnabledState(networkId)

Returns the enabled status of VLANs for the network

Returns the enabled status of VLANs for the network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.VLANsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkVlansEnabledState(networkId, (error, data, response) => {
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


## updateNetworkVlan

> Object updateNetworkVlan(networkId, vlanId, opts)

Update a VLAN

Update a VLAN

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.VLANsApi();
let networkId = "networkId_example"; // String | 
let vlanId = "vlanId_example"; // String | 
let opts = {
  'updateNetworkVlanRequest': new MerakiDashboardApi.UpdateNetworkVlanRequest() // UpdateNetworkVlanRequest | 
};
apiInstance.updateNetworkVlan(networkId, vlanId, opts, (error, data, response) => {
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
 **vlanId** | **String**|  | 
 **updateNetworkVlanRequest** | [**UpdateNetworkVlanRequest**](UpdateNetworkVlanRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkVlansEnabledState

> Object updateNetworkVlansEnabledState(networkId, updateNetworkVlansEnabledStateRequest)

Enable/Disable VLANs for the given network

Enable/Disable VLANs for the given network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.VLANsApi();
let networkId = "networkId_example"; // String | 
let updateNetworkVlansEnabledStateRequest = new MerakiDashboardApi.UpdateNetworkVlansEnabledStateRequest(); // UpdateNetworkVlansEnabledStateRequest | 
apiInstance.updateNetworkVlansEnabledState(networkId, updateNetworkVlansEnabledStateRequest, (error, data, response) => {
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
 **updateNetworkVlansEnabledStateRequest** | [**UpdateNetworkVlansEnabledStateRequest**](UpdateNetworkVlansEnabledStateRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

