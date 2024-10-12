# AutomationActionsV4.CallbacksApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postAutomationV4ActionsCallbacksCallbackIdCompleteComplete**](CallbacksApi.md#postAutomationV4ActionsCallbacksCallbackIdCompleteComplete) | **POST** /automation/v4/actions/callbacks/{callbackId}/complete | Completes a single callback
[**postAutomationV4ActionsCallbacksCompleteCompleteBatch**](CallbacksApi.md#postAutomationV4ActionsCallbacksCompleteCompleteBatch) | **POST** /automation/v4/actions/callbacks/complete | Completes a batch of callbacks



## postAutomationV4ActionsCallbacksCallbackIdCompleteComplete

> postAutomationV4ActionsCallbacksCallbackIdCompleteComplete(callbackId, callbackCompletionRequest)

Completes a single callback

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.CallbacksApi();
let callbackId = "callbackId_example"; // String | 
let callbackCompletionRequest = new AutomationActionsV4.CallbackCompletionRequest(); // CallbackCompletionRequest | 
apiInstance.postAutomationV4ActionsCallbacksCallbackIdCompleteComplete(callbackId, callbackCompletionRequest, (error, data, response) => {
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
 **callbackId** | **String**|  | 
 **callbackCompletionRequest** | [**CallbackCompletionRequest**](CallbackCompletionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## postAutomationV4ActionsCallbacksCompleteCompleteBatch

> postAutomationV4ActionsCallbacksCompleteCompleteBatch(batchInputCallbackCompletionBatchRequest)

Completes a batch of callbacks

### Example

```javascript
import AutomationActionsV4 from 'automation_actions_v4';
let defaultClient = AutomationActionsV4.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new AutomationActionsV4.CallbacksApi();
let batchInputCallbackCompletionBatchRequest = new AutomationActionsV4.BatchInputCallbackCompletionBatchRequest(); // BatchInputCallbackCompletionBatchRequest | 
apiInstance.postAutomationV4ActionsCallbacksCompleteCompleteBatch(batchInputCallbackCompletionBatchRequest, (error, data, response) => {
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
 **batchInputCallbackCompletionBatchRequest** | [**BatchInputCallbackCompletionBatchRequest**](BatchInputCallbackCompletionBatchRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

