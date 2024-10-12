# MerakiDashboardApi.StagedApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkFirmwareUpgradesStagedEvent_2**](StagedApi.md#createNetworkFirmwareUpgradesStagedEvent_2) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events | Create a Staged Upgrade Event for a network
[**createNetworkFirmwareUpgradesStagedGroup_2**](StagedApi.md#createNetworkFirmwareUpgradesStagedGroup_2) | **POST** /networks/{networkId}/firmwareUpgrades/staged/groups | Create a Staged Upgrade Group for a network
[**deferNetworkFirmwareUpgradesStagedEvents_2**](StagedApi.md#deferNetworkFirmwareUpgradesStagedEvents_2) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/defer | Postpone by 1 week all pending staged upgrade stages for a network
[**deleteNetworkFirmwareUpgradesStagedGroup_2**](StagedApi.md#deleteNetworkFirmwareUpgradesStagedGroup_2) | **DELETE** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Delete a Staged Upgrade Group
[**getNetworkFirmwareUpgradesStagedEvents_2**](StagedApi.md#getNetworkFirmwareUpgradesStagedEvents_2) | **GET** /networks/{networkId}/firmwareUpgrades/staged/events | Get the Staged Upgrade Event from a network
[**getNetworkFirmwareUpgradesStagedGroup_2**](StagedApi.md#getNetworkFirmwareUpgradesStagedGroup_2) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Get a Staged Upgrade Group from a network
[**getNetworkFirmwareUpgradesStagedGroups_2**](StagedApi.md#getNetworkFirmwareUpgradesStagedGroups_2) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups | List of Staged Upgrade Groups in a network
[**getNetworkFirmwareUpgradesStagedStages_2**](StagedApi.md#getNetworkFirmwareUpgradesStagedStages_2) | **GET** /networks/{networkId}/firmwareUpgrades/staged/stages | Order of Staged Upgrade Groups in a network
[**rollbacksNetworkFirmwareUpgradesStagedEvents_2**](StagedApi.md#rollbacksNetworkFirmwareUpgradesStagedEvents_2) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/rollbacks | Rollback a Staged Upgrade Event for a network
[**updateNetworkFirmwareUpgradesStagedEvents_2**](StagedApi.md#updateNetworkFirmwareUpgradesStagedEvents_2) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/events | Update the Staged Upgrade Event for a network
[**updateNetworkFirmwareUpgradesStagedGroup_2**](StagedApi.md#updateNetworkFirmwareUpgradesStagedGroup_2) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Update a Staged Upgrade Group for a network
[**updateNetworkFirmwareUpgradesStagedStages_2**](StagedApi.md#updateNetworkFirmwareUpgradesStagedStages_2) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/stages | Assign Staged Upgrade Group order in the sequence.



## createNetworkFirmwareUpgradesStagedEvent_2

> GetNetworkFirmwareUpgradesStagedEvents200Response createNetworkFirmwareUpgradesStagedEvent_2(networkId, createNetworkFirmwareUpgradesStagedEventRequest)

Create a Staged Upgrade Event for a network

Create a Staged Upgrade Event for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesStagedEventRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedEventRequest(); // CreateNetworkFirmwareUpgradesStagedEventRequest | 
apiInstance.createNetworkFirmwareUpgradesStagedEvent_2(networkId, createNetworkFirmwareUpgradesStagedEventRequest, (error, data, response) => {
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
 **createNetworkFirmwareUpgradesStagedEventRequest** | [**CreateNetworkFirmwareUpgradesStagedEventRequest**](CreateNetworkFirmwareUpgradesStagedEventRequest.md)|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkFirmwareUpgradesStagedGroup_2

> Object createNetworkFirmwareUpgradesStagedGroup_2(networkId, createNetworkFirmwareUpgradesStagedGroupRequest)

Create a Staged Upgrade Group for a network

Create a Staged Upgrade Group for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesStagedGroupRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
apiInstance.createNetworkFirmwareUpgradesStagedGroup_2(networkId, createNetworkFirmwareUpgradesStagedGroupRequest, (error, data, response) => {
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
 **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deferNetworkFirmwareUpgradesStagedEvents_2

> GetNetworkFirmwareUpgradesStagedEvents200Response deferNetworkFirmwareUpgradesStagedEvents_2(networkId)

Postpone by 1 week all pending staged upgrade stages for a network

Postpone by 1 week all pending staged upgrade stages for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
apiInstance.deferNetworkFirmwareUpgradesStagedEvents_2(networkId, (error, data, response) => {
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

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteNetworkFirmwareUpgradesStagedGroup_2

> deleteNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId)

Delete a Staged Upgrade Group

Delete a Staged Upgrade Group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
apiInstance.deleteNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkFirmwareUpgradesStagedEvents_2

> GetNetworkFirmwareUpgradesStagedEvents200Response getNetworkFirmwareUpgradesStagedEvents_2(networkId)

Get the Staged Upgrade Event from a network

Get the Staged Upgrade Event from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedEvents_2(networkId, (error, data, response) => {
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

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgradesStagedGroup_2

> GetNetworkFirmwareUpgradesStagedGroups200ResponseInner getNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId)

Get a Staged Upgrade Group from a network

Get a Staged Upgrade Group from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedGroups200ResponseInner**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgradesStagedGroups_2

> [GetNetworkFirmwareUpgradesStagedGroups200ResponseInner] getNetworkFirmwareUpgradesStagedGroups_2(networkId)

List of Staged Upgrade Groups in a network

List of Staged Upgrade Groups in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedGroups_2(networkId, (error, data, response) => {
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

[**[GetNetworkFirmwareUpgradesStagedGroups200ResponseInner]**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgradesStagedStages_2

> [GetNetworkFirmwareUpgradesStagedStages200ResponseInner] getNetworkFirmwareUpgradesStagedStages_2(networkId)

Order of Staged Upgrade Groups in a network

Order of Staged Upgrade Groups in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedStages_2(networkId, (error, data, response) => {
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

[**[GetNetworkFirmwareUpgradesStagedStages200ResponseInner]**](GetNetworkFirmwareUpgradesStagedStages200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rollbacksNetworkFirmwareUpgradesStagedEvents_2

> GetNetworkFirmwareUpgradesStagedEvents200Response rollbacksNetworkFirmwareUpgradesStagedEvents_2(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest)

Rollback a Staged Upgrade Event for a network

Rollback a Staged Upgrade Event for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
let rollbacksNetworkFirmwareUpgradesStagedEventsRequest = new MerakiDashboardApi.RollbacksNetworkFirmwareUpgradesStagedEventsRequest(); // RollbacksNetworkFirmwareUpgradesStagedEventsRequest | 
apiInstance.rollbacksNetworkFirmwareUpgradesStagedEvents_2(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest, (error, data, response) => {
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
 **rollbacksNetworkFirmwareUpgradesStagedEventsRequest** | [**RollbacksNetworkFirmwareUpgradesStagedEventsRequest**](RollbacksNetworkFirmwareUpgradesStagedEventsRequest.md)|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkFirmwareUpgradesStagedEvents_2

> GetNetworkFirmwareUpgradesStagedEvents200Response updateNetworkFirmwareUpgradesStagedEvents_2(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest)

Update the Staged Upgrade Event for a network

Update the Staged Upgrade Event for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
let updateNetworkFirmwareUpgradesStagedEventsRequest = new MerakiDashboardApi.UpdateNetworkFirmwareUpgradesStagedEventsRequest(); // UpdateNetworkFirmwareUpgradesStagedEventsRequest | 
apiInstance.updateNetworkFirmwareUpgradesStagedEvents_2(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest, (error, data, response) => {
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
 **updateNetworkFirmwareUpgradesStagedEventsRequest** | [**UpdateNetworkFirmwareUpgradesStagedEventsRequest**](UpdateNetworkFirmwareUpgradesStagedEventsRequest.md)|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkFirmwareUpgradesStagedGroup_2

> Object updateNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest)

Update a Staged Upgrade Group for a network

Update a Staged Upgrade Group for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
let createNetworkFirmwareUpgradesStagedGroupRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
apiInstance.updateNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest, (error, data, response) => {
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
 **groupId** | **String**|  | 
 **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateNetworkFirmwareUpgradesStagedStages_2

> [GetNetworkFirmwareUpgradesStagedStages200ResponseInner] updateNetworkFirmwareUpgradesStagedStages_2(networkId, opts)

Assign Staged Upgrade Group order in the sequence.

Assign Staged Upgrade Group order in the sequence.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.StagedApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkFirmwareUpgradesStagedStagesRequest': new MerakiDashboardApi.UpdateNetworkFirmwareUpgradesStagedStagesRequest() // UpdateNetworkFirmwareUpgradesStagedStagesRequest | 
};
apiInstance.updateNetworkFirmwareUpgradesStagedStages_2(networkId, opts, (error, data, response) => {
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
 **updateNetworkFirmwareUpgradesStagedStagesRequest** | [**UpdateNetworkFirmwareUpgradesStagedStagesRequest**](UpdateNetworkFirmwareUpgradesStagedStagesRequest.md)|  | [optional] 

### Return type

[**[GetNetworkFirmwareUpgradesStagedStages200ResponseInner]**](GetNetworkFirmwareUpgradesStagedStages200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

