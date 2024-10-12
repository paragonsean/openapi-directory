# Signl4Api.WebhooksApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWebhookById**](WebhooksApi.md#getWebhookById) | **GET** /webhooks/{webhookId} | Get Webhook by Id
[**webhooksGet**](WebhooksApi.md#webhooksGet) | **GET** /webhooks | Get Webhooks
[**webhooksPost**](WebhooksApi.md#webhooksPost) | **POST** /webhooks | Create Webhook
[**webhooksWebhookIdDelete**](WebhooksApi.md#webhooksWebhookIdDelete) | **DELETE** /webhooks/{webhookId} | Delete Webhook by Id
[**webhooksWebhookIdDisablePost**](WebhooksApi.md#webhooksWebhookIdDisablePost) | **POST** /webhooks/{webhookId}/disable | Ability to enable a webHook.
[**webhooksWebhookIdEnablePost**](WebhooksApi.md#webhooksWebhookIdEnablePost) | **POST** /webhooks/{webhookId}/enable | Ability to disable a webHook.
[**webhooksWebhookIdPut**](WebhooksApi.md#webhooksWebhookIdPut) | **PUT** /webhooks/{webhookId} | Update Webhook by Id



## getWebhookById

> String getWebhookById(webhookId)

Get Webhook by Id

Returns information of the webhook specified by the passed id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.WebhooksApi();
let webhookId = "webhookId_example"; // String | Id of the outbound webhook to be retrieved.
apiInstance.getWebhookById(webhookId, (error, data, response) => {
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
 **webhookId** | **String**| Id of the outbound webhook to be retrieved. | 

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## webhooksGet

> [WebhookInfo] webhooksGet(opts)

Get Webhooks

Returns a collection of defined outbound webhooks in the system.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.WebhooksApi();
let opts = {
  'teamId': "teamId_example" // String | 
};
apiInstance.webhooksGet(opts, (error, data, response) => {
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
 **teamId** | **String**|  | [optional] 

### Return type

[**[WebhookInfo]**](WebhookInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## webhooksPost

> String webhooksPost(opts)

Create Webhook

Creates a new outbound webhook that will be notified when certain events occur.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.WebhooksApi();
let opts = {
  'webhookBaseInfo': new Signl4Api.WebhookBaseInfo() // WebhookBaseInfo | Json object that contains the external URL of the webhook.
};
apiInstance.webhooksPost(opts, (error, data, response) => {
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
 **webhookBaseInfo** | [**WebhookBaseInfo**](WebhookBaseInfo.md)| Json object that contains the external URL of the webhook. | [optional] 

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## webhooksWebhookIdDelete

> webhooksWebhookIdDelete(webhookId)

Delete Webhook by Id

Deletes the specified webhook so that it will no longer be notified.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.WebhooksApi();
let webhookId = "webhookId_example"; // String | Id of the outbound webhook that will be deleted.
apiInstance.webhooksWebhookIdDelete(webhookId, (error, data, response) => {
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
 **webhookId** | **String**| Id of the outbound webhook that will be deleted. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## webhooksWebhookIdDisablePost

> WebhookInfo webhooksWebhookIdDisablePost(webhookId)

Ability to enable a webHook.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.WebhooksApi();
let webhookId = "webhookId_example"; // String | Webhook ID for webhook which should be disabled.
apiInstance.webhooksWebhookIdDisablePost(webhookId, (error, data, response) => {
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
 **webhookId** | **String**| Webhook ID for webhook which should be disabled. | 

### Return type

[**WebhookInfo**](WebhookInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## webhooksWebhookIdEnablePost

> WebhookInfo webhooksWebhookIdEnablePost(webhookId)

Ability to disable a webHook.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.WebhooksApi();
let webhookId = "webhookId_example"; // String | Webhook ID for webhook which should be enabled.
apiInstance.webhooksWebhookIdEnablePost(webhookId, (error, data, response) => {
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
 **webhookId** | **String**| Webhook ID for webhook which should be enabled. | 

### Return type

[**WebhookInfo**](WebhookInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## webhooksWebhookIdPut

> WebhookInfo webhooksWebhookIdPut(webhookId, opts)

Update Webhook by Id

Updates the specified webhook.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.WebhooksApi();
let webhookId = "webhookId_example"; // String | Id of the outbound webhook to be updated.
let opts = {
  'webhookBaseInfo': new Signl4Api.WebhookBaseInfo() // WebhookBaseInfo | Json object containing the updated URL of the webhook.
};
apiInstance.webhooksWebhookIdPut(webhookId, opts, (error, data, response) => {
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
 **webhookId** | **String**| Id of the outbound webhook to be updated. | 
 **webhookBaseInfo** | [**WebhookBaseInfo**](WebhookBaseInfo.md)| Json object containing the updated URL of the webhook. | [optional] 

### Return type

[**WebhookInfo**](WebhookInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain

