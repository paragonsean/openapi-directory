# MerakiDashboardApi.RendezvousPointsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSwitchRoutingMulticastRendezvousPoint_3**](RendezvousPointsApi.md#createNetworkSwitchRoutingMulticastRendezvousPoint_3) | **POST** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | Create a multicast rendezvous point
[**deleteNetworkSwitchRoutingMulticastRendezvousPoint_3**](RendezvousPointsApi.md#deleteNetworkSwitchRoutingMulticastRendezvousPoint_3) | **DELETE** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Delete a multicast rendezvous point
[**getNetworkSwitchRoutingMulticastRendezvousPoint_3**](RendezvousPointsApi.md#getNetworkSwitchRoutingMulticastRendezvousPoint_3) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Return a multicast rendezvous point
[**getNetworkSwitchRoutingMulticastRendezvousPoints_3**](RendezvousPointsApi.md#getNetworkSwitchRoutingMulticastRendezvousPoints_3) | **GET** /networks/{networkId}/switch/routing/multicast/rendezvousPoints | List multicast rendezvous points
[**updateNetworkSwitchRoutingMulticastRendezvousPoint_3**](RendezvousPointsApi.md#updateNetworkSwitchRoutingMulticastRendezvousPoint_3) | **PUT** /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId} | Update a multicast rendezvous point



## createNetworkSwitchRoutingMulticastRendezvousPoint_3

> Object createNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest)

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

let apiInstance = new MerakiDashboardApi.RendezvousPointsApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchRoutingMulticastRendezvousPointRequest = new MerakiDashboardApi.CreateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // CreateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
apiInstance.createNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, createNetworkSwitchRoutingMulticastRendezvousPointRequest, (error, data, response) => {
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


## deleteNetworkSwitchRoutingMulticastRendezvousPoint_3

> deleteNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId)

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

let apiInstance = new MerakiDashboardApi.RendezvousPointsApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
apiInstance.deleteNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId, (error, data, response) => {
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


## getNetworkSwitchRoutingMulticastRendezvousPoint_3

> Object getNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId)

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

let apiInstance = new MerakiDashboardApi.RendezvousPointsApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId, (error, data, response) => {
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


## getNetworkSwitchRoutingMulticastRendezvousPoints_3

> [[Object]] getNetworkSwitchRoutingMulticastRendezvousPoints_3(networkId)

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

let apiInstance = new MerakiDashboardApi.RendezvousPointsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchRoutingMulticastRendezvousPoints_3(networkId, (error, data, response) => {
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


## updateNetworkSwitchRoutingMulticastRendezvousPoint_3

> Object updateNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest)

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

let apiInstance = new MerakiDashboardApi.RendezvousPointsApi();
let networkId = "networkId_example"; // String | 
let rendezvousPointId = "rendezvousPointId_example"; // String | 
let updateNetworkSwitchRoutingMulticastRendezvousPointRequest = new MerakiDashboardApi.UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest(); // UpdateNetworkSwitchRoutingMulticastRendezvousPointRequest | 
apiInstance.updateNetworkSwitchRoutingMulticastRendezvousPoint_3(networkId, rendezvousPointId, updateNetworkSwitchRoutingMulticastRendezvousPointRequest, (error, data, response) => {
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

