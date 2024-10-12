# MerakiDashboardApi.AccessPoliciesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSwitchAccessPolicy_1**](AccessPoliciesApi.md#createNetworkSwitchAccessPolicy_1) | **POST** /networks/{networkId}/switch/accessPolicies | Create an access policy for a switch network
[**deleteNetworkSwitchAccessPolicy_1**](AccessPoliciesApi.md#deleteNetworkSwitchAccessPolicy_1) | **DELETE** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Delete an access policy for a switch network
[**getNetworkSwitchAccessPolicies_1**](AccessPoliciesApi.md#getNetworkSwitchAccessPolicies_1) | **GET** /networks/{networkId}/switch/accessPolicies | List the access policies for a switch network
[**getNetworkSwitchAccessPolicy_1**](AccessPoliciesApi.md#getNetworkSwitchAccessPolicy_1) | **GET** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Return a specific access policy for a switch network
[**updateNetworkSwitchAccessPolicy_1**](AccessPoliciesApi.md#updateNetworkSwitchAccessPolicy_1) | **PUT** /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber} | Update an access policy for a switch network



## createNetworkSwitchAccessPolicy_1

> GetNetworkSwitchAccessPolicies200ResponseInner createNetworkSwitchAccessPolicy_1(networkId, createNetworkSwitchAccessPolicyRequest)

Create an access policy for a switch network

Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AccessPoliciesApi();
let networkId = "networkId_example"; // String | 
let createNetworkSwitchAccessPolicyRequest = new MerakiDashboardApi.CreateNetworkSwitchAccessPolicyRequest(); // CreateNetworkSwitchAccessPolicyRequest | 
apiInstance.createNetworkSwitchAccessPolicy_1(networkId, createNetworkSwitchAccessPolicyRequest, (error, data, response) => {
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
 **createNetworkSwitchAccessPolicyRequest** | [**CreateNetworkSwitchAccessPolicyRequest**](CreateNetworkSwitchAccessPolicyRequest.md)|  | 

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkSwitchAccessPolicy_1

> deleteNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber)

Delete an access policy for a switch network

Delete an access policy for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AccessPoliciesApi();
let networkId = "networkId_example"; // String | 
let accessPolicyNumber = "accessPolicyNumber_example"; // String | 
apiInstance.deleteNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber, (error, data, response) => {
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
 **accessPolicyNumber** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkSwitchAccessPolicies_1

> [GetNetworkSwitchAccessPolicies200ResponseInner] getNetworkSwitchAccessPolicies_1(networkId)

List the access policies for a switch network

List the access policies for a switch network. Only returns access policies with &#39;my RADIUS server&#39; as authentication method

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AccessPoliciesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkSwitchAccessPolicies_1(networkId, (error, data, response) => {
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

[**[GetNetworkSwitchAccessPolicies200ResponseInner]**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkSwitchAccessPolicy_1

> GetNetworkSwitchAccessPolicies200ResponseInner getNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber)

Return a specific access policy for a switch network

Return a specific access policy for a switch network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AccessPoliciesApi();
let networkId = "networkId_example"; // String | 
let accessPolicyNumber = "accessPolicyNumber_example"; // String | 
apiInstance.getNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber, (error, data, response) => {
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
 **accessPolicyNumber** | **String**|  | 

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkSwitchAccessPolicy_1

> GetNetworkSwitchAccessPolicies200ResponseInner updateNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber, opts)

Update an access policy for a switch network

Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AccessPoliciesApi();
let networkId = "networkId_example"; // String | 
let accessPolicyNumber = "accessPolicyNumber_example"; // String | 
let opts = {
  'updateNetworkSwitchAccessPolicyRequest': new MerakiDashboardApi.UpdateNetworkSwitchAccessPolicyRequest() // UpdateNetworkSwitchAccessPolicyRequest | 
};
apiInstance.updateNetworkSwitchAccessPolicy_1(networkId, accessPolicyNumber, opts, (error, data, response) => {
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
 **accessPolicyNumber** | **String**|  | 
 **updateNetworkSwitchAccessPolicyRequest** | [**UpdateNetworkSwitchAccessPolicyRequest**](UpdateNetworkSwitchAccessPolicyRequest.md)|  | [optional] 

### Return type

[**GetNetworkSwitchAccessPolicies200ResponseInner**](GetNetworkSwitchAccessPolicies200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

