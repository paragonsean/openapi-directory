# MerakiDashboardApi.FirmwareUpgradesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkFirmwareUpgradesRollback_1**](FirmwareUpgradesApi.md#createNetworkFirmwareUpgradesRollback_1) | **POST** /networks/{networkId}/firmwareUpgrades/rollbacks | Rollback a Firmware Upgrade For A Network
[**createNetworkFirmwareUpgradesStagedEvent_1**](FirmwareUpgradesApi.md#createNetworkFirmwareUpgradesStagedEvent_1) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events | Create a Staged Upgrade Event for a network
[**createNetworkFirmwareUpgradesStagedGroup_1**](FirmwareUpgradesApi.md#createNetworkFirmwareUpgradesStagedGroup_1) | **POST** /networks/{networkId}/firmwareUpgrades/staged/groups | Create a Staged Upgrade Group for a network
[**deferNetworkFirmwareUpgradesStagedEvents_1**](FirmwareUpgradesApi.md#deferNetworkFirmwareUpgradesStagedEvents_1) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/defer | Postpone by 1 week all pending staged upgrade stages for a network
[**deleteNetworkFirmwareUpgradesStagedGroup_1**](FirmwareUpgradesApi.md#deleteNetworkFirmwareUpgradesStagedGroup_1) | **DELETE** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Delete a Staged Upgrade Group
[**getNetworkFirmwareUpgradesStagedEvents_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgradesStagedEvents_1) | **GET** /networks/{networkId}/firmwareUpgrades/staged/events | Get the Staged Upgrade Event from a network
[**getNetworkFirmwareUpgradesStagedGroup_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgradesStagedGroup_1) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Get a Staged Upgrade Group from a network
[**getNetworkFirmwareUpgradesStagedGroups_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgradesStagedGroups_1) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups | List of Staged Upgrade Groups in a network
[**getNetworkFirmwareUpgradesStagedStages_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgradesStagedStages_1) | **GET** /networks/{networkId}/firmwareUpgrades/staged/stages | Order of Staged Upgrade Groups in a network
[**getNetworkFirmwareUpgrades_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgrades_1) | **GET** /networks/{networkId}/firmwareUpgrades | Get firmware upgrade information for a network
[**rollbacksNetworkFirmwareUpgradesStagedEvents_1**](FirmwareUpgradesApi.md#rollbacksNetworkFirmwareUpgradesStagedEvents_1) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/rollbacks | Rollback a Staged Upgrade Event for a network
[**updateNetworkFirmwareUpgradesStagedEvents_1**](FirmwareUpgradesApi.md#updateNetworkFirmwareUpgradesStagedEvents_1) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/events | Update the Staged Upgrade Event for a network
[**updateNetworkFirmwareUpgradesStagedGroup_1**](FirmwareUpgradesApi.md#updateNetworkFirmwareUpgradesStagedGroup_1) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Update a Staged Upgrade Group for a network
[**updateNetworkFirmwareUpgradesStagedStages_1**](FirmwareUpgradesApi.md#updateNetworkFirmwareUpgradesStagedStages_1) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/stages | Assign Staged Upgrade Group order in the sequence.
[**updateNetworkFirmwareUpgrades_1**](FirmwareUpgradesApi.md#updateNetworkFirmwareUpgrades_1) | **PUT** /networks/{networkId}/firmwareUpgrades | Update firmware upgrade information for a network



## createNetworkFirmwareUpgradesRollback_1

> CreateNetworkFirmwareUpgradesRollback200Response createNetworkFirmwareUpgradesRollback_1(networkId, createNetworkFirmwareUpgradesRollbackRequest)

Rollback a Firmware Upgrade For A Network

Rollback a Firmware Upgrade For A Network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesRollbackRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesRollbackRequest(); // CreateNetworkFirmwareUpgradesRollbackRequest | 
apiInstance.createNetworkFirmwareUpgradesRollback_1(networkId, createNetworkFirmwareUpgradesRollbackRequest, (error, data, response) => {
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
 **createNetworkFirmwareUpgradesRollbackRequest** | [**CreateNetworkFirmwareUpgradesRollbackRequest**](CreateNetworkFirmwareUpgradesRollbackRequest.md)|  | 

### Return type

[**CreateNetworkFirmwareUpgradesRollback200Response**](CreateNetworkFirmwareUpgradesRollback200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createNetworkFirmwareUpgradesStagedEvent_1

> GetNetworkFirmwareUpgradesStagedEvents200Response createNetworkFirmwareUpgradesStagedEvent_1(networkId, createNetworkFirmwareUpgradesStagedEventRequest)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesStagedEventRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedEventRequest(); // CreateNetworkFirmwareUpgradesStagedEventRequest | 
apiInstance.createNetworkFirmwareUpgradesStagedEvent_1(networkId, createNetworkFirmwareUpgradesStagedEventRequest, (error, data, response) => {
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


## createNetworkFirmwareUpgradesStagedGroup_1

> Object createNetworkFirmwareUpgradesStagedGroup_1(networkId, createNetworkFirmwareUpgradesStagedGroupRequest)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesStagedGroupRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
apiInstance.createNetworkFirmwareUpgradesStagedGroup_1(networkId, createNetworkFirmwareUpgradesStagedGroupRequest, (error, data, response) => {
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


## deferNetworkFirmwareUpgradesStagedEvents_1

> GetNetworkFirmwareUpgradesStagedEvents200Response deferNetworkFirmwareUpgradesStagedEvents_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
apiInstance.deferNetworkFirmwareUpgradesStagedEvents_1(networkId, (error, data, response) => {
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


## deleteNetworkFirmwareUpgradesStagedGroup_1

> deleteNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
apiInstance.deleteNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId, (error, data, response) => {
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


## getNetworkFirmwareUpgradesStagedEvents_1

> GetNetworkFirmwareUpgradesStagedEvents200Response getNetworkFirmwareUpgradesStagedEvents_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedEvents_1(networkId, (error, data, response) => {
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


## getNetworkFirmwareUpgradesStagedGroup_1

> GetNetworkFirmwareUpgradesStagedGroups200ResponseInner getNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId, (error, data, response) => {
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


## getNetworkFirmwareUpgradesStagedGroups_1

> [GetNetworkFirmwareUpgradesStagedGroups200ResponseInner] getNetworkFirmwareUpgradesStagedGroups_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedGroups_1(networkId, (error, data, response) => {
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


## getNetworkFirmwareUpgradesStagedStages_1

> [GetNetworkFirmwareUpgradesStagedStages200ResponseInner] getNetworkFirmwareUpgradesStagedStages_1(networkId)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedStages_1(networkId, (error, data, response) => {
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


## getNetworkFirmwareUpgrades_1

> GetNetworkFirmwareUpgrades200Response getNetworkFirmwareUpgrades_1(networkId)

Get firmware upgrade information for a network

Get firmware upgrade information for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgrades_1(networkId, (error, data, response) => {
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

[**GetNetworkFirmwareUpgrades200Response**](GetNetworkFirmwareUpgrades200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rollbacksNetworkFirmwareUpgradesStagedEvents_1

> GetNetworkFirmwareUpgradesStagedEvents200Response rollbacksNetworkFirmwareUpgradesStagedEvents_1(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let rollbacksNetworkFirmwareUpgradesStagedEventsRequest = new MerakiDashboardApi.RollbacksNetworkFirmwareUpgradesStagedEventsRequest(); // RollbacksNetworkFirmwareUpgradesStagedEventsRequest | 
apiInstance.rollbacksNetworkFirmwareUpgradesStagedEvents_1(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest, (error, data, response) => {
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


## updateNetworkFirmwareUpgradesStagedEvents_1

> GetNetworkFirmwareUpgradesStagedEvents200Response updateNetworkFirmwareUpgradesStagedEvents_1(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let updateNetworkFirmwareUpgradesStagedEventsRequest = new MerakiDashboardApi.UpdateNetworkFirmwareUpgradesStagedEventsRequest(); // UpdateNetworkFirmwareUpgradesStagedEventsRequest | 
apiInstance.updateNetworkFirmwareUpgradesStagedEvents_1(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest, (error, data, response) => {
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


## updateNetworkFirmwareUpgradesStagedGroup_1

> Object updateNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
let createNetworkFirmwareUpgradesStagedGroupRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
apiInstance.updateNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest, (error, data, response) => {
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


## updateNetworkFirmwareUpgradesStagedStages_1

> [GetNetworkFirmwareUpgradesStagedStages200ResponseInner] updateNetworkFirmwareUpgradesStagedStages_1(networkId, opts)

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

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkFirmwareUpgradesStagedStagesRequest': new MerakiDashboardApi.UpdateNetworkFirmwareUpgradesStagedStagesRequest() // UpdateNetworkFirmwareUpgradesStagedStagesRequest | 
};
apiInstance.updateNetworkFirmwareUpgradesStagedStages_1(networkId, opts, (error, data, response) => {
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


## updateNetworkFirmwareUpgrades_1

> GetNetworkFirmwareUpgrades200Response updateNetworkFirmwareUpgrades_1(networkId, opts)

Update firmware upgrade information for a network

Update firmware upgrade information for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirmwareUpgradesApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'updateNetworkFirmwareUpgradesRequest': new MerakiDashboardApi.UpdateNetworkFirmwareUpgradesRequest() // UpdateNetworkFirmwareUpgradesRequest | 
};
apiInstance.updateNetworkFirmwareUpgrades_1(networkId, opts, (error, data, response) => {
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
 **updateNetworkFirmwareUpgradesRequest** | [**UpdateNetworkFirmwareUpgradesRequest**](UpdateNetworkFirmwareUpgradesRequest.md)|  | [optional] 

### Return type

[**GetNetworkFirmwareUpgrades200Response**](GetNetworkFirmwareUpgrades200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

