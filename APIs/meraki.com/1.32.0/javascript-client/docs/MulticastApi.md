# MerakiDashboardApi.MulticastApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSwitchRoutingMulticastRendezvousPoint_2**](MulticastApi.md#createNetworkSwitchRoutingMulticastRendezvousPoint_2) | **POST** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | Create a multicast rendezvous point
[**deleteNetworkSwitchRoutingMulticastRendezvousPoint_2**](MulticastApi.md#deleteNetworkSwitchRoutingMulticastRendezvousPoint_2) | **DELETE** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Delete a multicast rendezvous point
[**getNetworkSwitchRoutingMulticastRendezvousPoint_2**](MulticastApi.md#getNetworkSwitchRoutingMulticastRendezvousPoint_2) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Return a multicast rendezvous point
[**getNetworkSwitchRoutingMulticastRendezvousPoints_2**](MulticastApi.md#getNetworkSwitchRoutingMulticastRendezvousPoints_2) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | List multicast rendezvous points
[**getNetworkSwitchRoutingMulticast_2**](MulticastApi.md#getNetworkSwitchRoutingMulticast_2) | **GET** /networks/{networkId}/switch/routing/multicast | Return multicast settings for a network
[**updateNetworkSwitchRoutingMulticastRendezvousPoint_2**](MulticastApi.md#updateNetworkSwitchRoutingMulticastRendezvousPoint_2) | **PUT** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Update a multicast rendezvous point
[**updateNetworkSwitchRoutingMulticast_2**](MulticastApi.md#updateNetworkSwitchRoutingMulticast_2) | **PUT** /networks/{networkId}/switch/routing/multicast | Update multicast settings for a network



## createNetworkSwitchRoutingMulticastRendezvousPoint_2

> Object createNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest)

Create a multicast rendezvous point

Create a multicast rendezvous point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MulticastApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchRoutingMulticastRendezvousPointRequest = new MerakiDashboardApi.CreateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // CreateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
apiInstance.createNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest, (error, data, response) => {
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
 **createNetworkSwitchRoutingMulticastRendezvousPointRequest** | [**CreateNetworkSwitchRoutingMulticastRendezvousPointRequest**](CreateNetworkSwitchRoutingMulticastRendezvousPointRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkSwitchRoutingMulticastRendezvousPoint_2

> deleteNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId)

Delete a multicast rendezvous point

Delete a multicast rendezvous point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MulticastApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
apiInstance.deleteNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId, (error, data, response) => {
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
 **rendezvousPointId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkSwitchRoutingMulticastRendezvousPoint_2

> Object getNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId)

Return a multicast rendezvous point

Return a multicast rendezvous point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MulticastApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId, (error, data, response) => {
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
 **rendezvousPointId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchRoutingMulticastRendezvousPoints_2

> [[Object]] getNetworkSwitchRoutingMulticastRendezvousPoints_2(networkId)

List multicast rendezvous points

List multicast rendezvous points

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MulticastApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoints_2(networkId, (error, data, response) => {
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

**[[Object]]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchRoutingMulticast_2

> Object getNetworkSwitchRoutingMulticast_2(networkId)

Return multicast settings for a network

Return multicast settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MulticastApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchRoutingMulticast_2(networkId, (error, data, response) => {
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


## updateNetworkSwitchRoutingMulticastRendezvousPoint_2

> Object updateNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest)

Update a multicast rendezvous point

Update a multicast rendezvous point

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MulticastApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
let updateNetworkSwitchRoutingMulticastRendezvousPointRequest = new MerakiDashboardApi.UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
apiInstance.updateNetworkSwitchRoutingMulticastRendezvousPoint_2(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest, (error, data, response) => {
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
 **rendezvousPointId** | **String**|  | 
 **updateNetworkSwitchRoutingMulticastRendezvousPointRequest** | [**UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest**](UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkSwitchRoutingMulticast_2

> Object updateNetworkSwitchRoutingMulticast_2(networkId, opts)

Update multicast settings for a network

Update multicast settings for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.MulticastApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkSwitchRoutingMulticastRequest': new MerakiDashboardApi.UpdateNetworkSwitchRoutingMulticastRequest() // UpdateNetworkSwitchRoutingMulticastRequest | 
};
apiInstance.updateNetworkSwitchRoutingMulticast_2(networkId, opts, (error, data, response) => {
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
 **updateNetworkSwitchRoutingMulticastRequest** | [**UpdateNetworkSwitchRoutingMulticastRequest**](UpdateNetworkSwitchRoutingMulticastRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

