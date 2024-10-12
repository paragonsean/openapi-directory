# MerakiDashboardApi.TargetGroupsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSmTargetGroup_1**](TargetGroupsApi.md#createNetworkSmTargetGroup_1) | **POST** /networks/{networkId}/sm/targetGroups | Add a target group
[**deleteNetworkSmTargetGroup_1**](TargetGroupsApi.md#deleteNetworkSmTargetGroup_1) | **DELETE** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Delete a target group from a network
[**getNetworkSmTargetGroup_1**](TargetGroupsApi.md#getNetworkSmTargetGroup_1) | **GET** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Return a target group
[**getNetworkSmTargetGroups_1**](TargetGroupsApi.md#getNetworkSmTargetGroups_1) | **GET** /networks/{networkId}/sm/targetGroups | List the target groups in this network
[**updateNetworkSmTargetGroup_1**](TargetGroupsApi.md#updateNetworkSmTargetGroup_1) | **PUT** /networks/{networkId}/sm/targetGroups/{targetGroupId} | Update a target group



## createNetworkSmTargetGroup_1

> Object createNetworkSmTargetGroup_1(networkId, opts)

Add a target group

Add a target group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TargetGroupsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'createNetworkSmTargetGroupRequest': new MerakiDashboardApi.CreateNetworkSmTargetGroupRequest() // CreateNetworkSmTargetGroupRequest | 
};
apiInstance.createNetworkSmTargetGroup_1(networkId, opts, (error, data, response) => {
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
 **createNetworkSmTargetGroupRequest** | [**CreateNetworkSmTargetGroupRequest**](CreateNetworkSmTargetGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkSmTargetGroup_1

> deleteNetworkSmTargetGroup_1(networkId, targetGroupId)

Delete a target group from a network

Delete a target group from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TargetGroupsApi();
let networkId = "networkId_example"; // String | 
let targetGroupId = "targetGroupId_example"; // String | 
apiInstance.deleteNetworkSmTargetGroup_1(networkId, targetGroupId, (error, data, response) => {
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
 **targetGroupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkSmTargetGroup_1

> Object getNetworkSmTargetGroup_1(networkId, targetGroupId, opts)

Return a target group

Return a target group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TargetGroupsApi();
let networkId = "networkId_example"; // String | 
let targetGroupId = "targetGroupId_example"; // String | 
let opts = {
  'withDetails': true // Boolean | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
};
apiInstance.getNetworkSmTargetGroup_1(networkId, targetGroupId, opts, (error, data, response) => {
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
 **targetGroupId** | **String**|  | 
 **withDetails** | **Boolean**| Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSmTargetGroups_1

> [Object] getNetworkSmTargetGroups_1(networkId, opts)

List the target groups in this network

List the target groups in this network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TargetGroupsApi();
let networkId = "networkId_example"; // String | 
let opts = {
  'withDetails': true // Boolean | Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
};
apiInstance.getNetworkSmTargetGroups_1(networkId, opts, (error, data, response) => {
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
 **withDetails** | **Boolean**| Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSmTargetGroup_1

> Object updateNetworkSmTargetGroup_1(networkId, targetGroupId, opts)

Update a target group

Update a target group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.TargetGroupsApi();
let networkId = "networkId_example"; // String | 
let targetGroupId = "targetGroupId_example"; // String | 
let opts = {
  'createNetworkSmTargetGroupRequest': new MerakiDashboardApi.CreateNetworkSmTargetGroupRequest() // CreateNetworkSmTargetGroupRequest | 
};
apiInstance.updateNetworkSmTargetGroup_1(networkId, targetGroupId, opts, (error, data, response) => {
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
 **targetGroupId** | **String**|  | 
 **createNetworkSmTargetGroupRequest** | [**CreateNetworkSmTargetGroupRequest**](CreateNetworkSmTargetGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

