# WebhooksWebhooks.SettingsApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteWebhooksV3AppIdSettingsClear**](SettingsApi.md#deleteWebhooksV3AppIdSettingsClear) | **DELETE** /webhooks/v3/{appId}/settings | 
[**getWebhooksV3AppIdSettingsGetAll**](SettingsApi.md#getWebhooksV3AppIdSettingsGetAll) | **GET** /webhooks/v3/{appId}/settings | 
[**putWebhooksV3AppIdSettingsConfigure**](SettingsApi.md#putWebhooksV3AppIdSettingsConfigure) | **PUT** /webhooks/v3/{appId}/settings | 



## deleteWebhooksV3AppIdSettingsClear

> deleteWebhooksV3AppIdSettingsClear(appId)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SettingsApi();
let appId = 56; // Number | 
apiInstance.deleteWebhooksV3AppIdSettingsClear(appId, (error, data, response) => {
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
 **appId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getWebhooksV3AppIdSettingsGetAll

> SettingsResponse getWebhooksV3AppIdSettingsGetAll(appId)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SettingsApi();
let appId = 56; // Number | 
apiInstance.getWebhooksV3AppIdSettingsGetAll(appId, (error, data, response) => {
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
 **appId** | **Number**|  | 

### Return type

[**SettingsResponse**](SettingsResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## putWebhooksV3AppIdSettingsConfigure

> SettingsResponse putWebhooksV3AppIdSettingsConfigure(appId, settingsChangeRequest)



### Example

```javascript
import WebhooksWebhooks from 'webhooks_webhooks';
let defaultClient = WebhooksWebhooks.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new WebhooksWebhooks.SettingsApi();
let appId = 56; // Number | 
let settingsChangeRequest = new WebhooksWebhooks.SettingsChangeRequest(); // SettingsChangeRequest | 
apiInstance.putWebhooksV3AppIdSettingsConfigure(appId, settingsChangeRequest, (error, data, response) => {
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
 **appId** | **Number**|  | 
 **settingsChangeRequest** | [**SettingsChangeRequest**](SettingsChangeRequest.md)|  | 

### Return type

[**SettingsResponse**](SettingsResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

