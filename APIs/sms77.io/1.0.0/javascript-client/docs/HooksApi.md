# SevenIoApi.HooksApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hooksGet**](HooksApi.md#hooksGet) | **GET** /hooks | 
[**hooksPOST**](HooksApi.md#hooksPOST) | **POST** /hooks | 



## hooksGet

> HooksGet200Response hooksGet(action)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.HooksApi();
let action = "action_example"; // String | Determines the action to execute.
apiInstance.hooksGet(action, (error, data, response) => {
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
 **action** | **String**| Determines the action to execute. | 

### Return type

[**HooksGet200Response**](HooksGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hooksPOST

> HooksPOST200Response hooksPOST(action, opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.HooksApi();
let action = "action_example"; // String | Determines the action to execute.
let opts = {
  'id': 56, // Number | The Webhook ID you wish to unsubscribe.
  'targetUrl': "targetUrl_example", // String | Target URL of your Webhook.
  'eventType': "eventType_example", // String | Type of event for which you would like to receive a webhook.
  'requestMethod': "'POST'" // String | Request method in which you want to receive the webhook.
};
apiInstance.hooksPOST(action, opts, (error, data, response) => {
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
 **action** | **String**| Determines the action to execute. | 
 **id** | **Number**| The Webhook ID you wish to unsubscribe. | [optional] 
 **targetUrl** | **String**| Target URL of your Webhook. | [optional] 
 **eventType** | **String**| Type of event for which you would like to receive a webhook. | [optional] 
 **requestMethod** | **String**| Request method in which you want to receive the webhook. | [optional] [default to &#39;POST&#39;]

### Return type

[**HooksPOST200Response**](HooksPOST200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

