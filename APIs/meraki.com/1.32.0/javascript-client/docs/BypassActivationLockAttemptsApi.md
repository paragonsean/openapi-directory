# MerakiDashboardApi.BypassActivationLockAttemptsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkSmBypassActivationLockAttempt_1**](BypassActivationLockAttemptsApi.md#createNetworkSmBypassActivationLockAttempt_1) | **POST** /networks/{networkId}/sm/bypassActivationLockAttempts | Bypass activation lock attempt
[**getNetworkSmBypassActivationLockAttempt_1**](BypassActivationLockAttemptsApi.md#getNetworkSmBypassActivationLockAttempt_1) | **GET** /networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId} | Bypass activation lock attempt status



## createNetworkSmBypassActivationLockAttempt_1

> Object createNetworkSmBypassActivationLockAttempt_1(networkId, createNetworkSmBypassActivationLockAttemptRequest)

Bypass activation lock attempt

Bypass activation lock attempt

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BypassActivationLockAttemptsApi();
let networkId = "networkId_example"; // String | 
let createNetworkSmBypassActivationLockAttemptRequest = new MerakiDashboardApi.CreateNetworkSmBypassActivationLockAttemptRequest(); // CreateNetworkSmBypassActivationLockAttemptRequest | 
apiInstance.createNetworkSmBypassActivationLockAttempt_1(networkId, createNetworkSmBypassActivationLockAttemptRequest, (error, data, response) => {
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
 **createNetworkSmBypassActivationLockAttemptRequest** | [**CreateNetworkSmBypassActivationLockAttemptRequest**](CreateNetworkSmBypassActivationLockAttemptRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getNetworkSmBypassActivationLockAttempt_1

> Object getNetworkSmBypassActivationLockAttempt_1(networkId, attemptId)

Bypass activation lock attempt status

Bypass activation lock attempt status

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.BypassActivationLockAttemptsApi();
let networkId = "networkId_example"; // String | 
let attemptId = "attemptId_example"; // String | 
apiInstance.getNetworkSmBypassActivationLockAttempt_1(networkId, attemptId, (error, data, response) => {
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
 **attemptId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

