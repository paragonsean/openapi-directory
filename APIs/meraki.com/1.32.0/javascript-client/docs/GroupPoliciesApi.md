# MerakiDashboardApi.GroupPoliciesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkGroupPolicy_1**](GroupPoliciesApi.md#createNetworkGroupPolicy_1) | **POST** /networks/{networkId}/groupPolicies | Create a group policy
[**deleteNetworkGroupPolicy_1**](GroupPoliciesApi.md#deleteNetworkGroupPolicy_1) | **DELETE** /networks/{networkId}/groupPolicies/{groupPolicyId} | Delete a group policy
[**getNetworkGroupPolicies_1**](GroupPoliciesApi.md#getNetworkGroupPolicies_1) | **GET** /networks/{networkId}/groupPolicies | List the group policies in a network
[**getNetworkGroupPolicy_1**](GroupPoliciesApi.md#getNetworkGroupPolicy_1) | **GET** /networks/{networkId}/groupPolicies/{groupPolicyId} | Display a group policy
[**updateNetworkGroupPolicy_1**](GroupPoliciesApi.md#updateNetworkGroupPolicy_1) | **PUT** /networks/{networkId}/groupPolicies/{groupPolicyId} | Update a group policy



## createNetworkGroupPolicy_1

> Object createNetworkGroupPolicy_1(networkId, createNetworkGroupPolicyRequest)

Create a group policy

Create a group policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupPoliciesApi();
let networkId = "networkId_example"; // String | 
let createNetworkGroupPolicyRequest = new MerakiDashboardApi.CreateNetworkGroupPolicyRequest(); // CreateNetworkGroupPolicyRequest | 
apiInstance.createNetworkGroupPolicy_1(networkId, createNetworkGroupPolicyRequest, (error, data, response) => {
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
 **createNetworkGroupPolicyRequest** | [**CreateNetworkGroupPolicyRequest**](CreateNetworkGroupPolicyRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkGroupPolicy_1

> deleteNetworkGroupPolicy_1(networkId, groupPolicyId)

Delete a group policy

Delete a group policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupPoliciesApi();
let networkId = "networkId_example"; // String | 
let groupPolicyId = "groupPolicyId_example"; // String | 
apiInstance.deleteNetworkGroupPolicy_1(networkId, groupPolicyId, (error, data, response) => {
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
 **groupPolicyId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkGroupPolicies_1

> [Object] getNetworkGroupPolicies_1(networkId)

List the group policies in a network

List the group policies in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupPoliciesApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkGroupPolicies_1(networkId, (error, data, response) => {
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


## getNetworkGroupPolicy_1

> Object getNetworkGroupPolicy_1(networkId, groupPolicyId)

Display a group policy

Display a group policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupPoliciesApi();
let networkId = "networkId_example"; // String | 
let groupPolicyId = "groupPolicyId_example"; // String | 
apiInstance.getNetworkGroupPolicy_1(networkId, groupPolicyId, (error, data, response) => {
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
 **groupPolicyId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkGroupPolicy_1

> Object updateNetworkGroupPolicy_1(networkId, groupPolicyId, opts)

Update a group policy

Update a group policy

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupPoliciesApi();
let networkId = "networkId_example"; // String | 
let groupPolicyId = "groupPolicyId_example"; // String | 
let opts = {
  'updateNetworkGroupPolicyRequest': new MerakiDashboardApi.UpdateNetworkGroupPolicyRequest() // UpdateNetworkGroupPolicyRequest | 
};
apiInstance.updateNetworkGroupPolicy_1(networkId, groupPolicyId, opts, (error, data, response) => {
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
 **groupPolicyId** | **String**|  | 
 **updateNetworkGroupPolicyRequest** | [**UpdateNetworkGroupPolicyRequest**](UpdateNetworkGroupPolicyRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

