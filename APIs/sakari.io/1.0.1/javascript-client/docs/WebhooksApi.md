# Sakari.WebhooksApi

All URIs are relative to *https://api.sakari.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooksFetchAll**](WebhooksApi.md#webhooksFetchAll) | **GET** /v1/accounts/{accountId}/webhooks | Fetch active webhooks
[**webhooksSubscribe**](WebhooksApi.md#webhooksSubscribe) | **POST** /v1/accounts/{accountId}/webhooks | Subscribe to message events
[**webhooksUnsubscribe**](WebhooksApi.md#webhooksUnsubscribe) | **DELETE** /v1/accounts/{accountId}/webhooks/{url} | Unsubscribe to message events



## webhooksFetchAll

> WebhooksResponse webhooksFetchAll(accountId)

Fetch active webhooks

When messages are acknowledge by carriers, a notification is sent to the specified URL

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.WebhooksApi();
let accountId = "accountId_example"; // String | Account to apply operations to
apiInstance.webhooksFetchAll(accountId, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksSubscribe

> WebhookResponse webhooksSubscribe(accountId, webhooksSubscribeRequest)

Subscribe to message events

When messages are acknowledge by carriers, a notification is sent to the specified URL

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.WebhooksApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let webhooksSubscribeRequest = new Sakari.WebhooksSubscribeRequest(); // WebhooksSubscribeRequest | 
apiInstance.webhooksSubscribe(accountId, webhooksSubscribeRequest, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **webhooksSubscribeRequest** | [**WebhooksSubscribeRequest**](WebhooksSubscribeRequest.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webhooksUnsubscribe

> webhooksUnsubscribe(accountId, url)

Unsubscribe to message events

Delete subscription for receiving notifications

### Example

```javascript
import Sakari from 'sakari';
let defaultClient = Sakari.ApiClient.instance;
// Configure OAuth2 access token for authorization: sakari_auth
let sakari_auth = defaultClient.authentications['sakari_auth'];
sakari_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Sakari.WebhooksApi();
let accountId = "accountId_example"; // String | Account to apply operations to
let url = "url_example"; // String | Account to apply operations to
apiInstance.webhooksUnsubscribe(accountId, url, (error, data, response) => {
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
 **accountId** | **String**| Account to apply operations to | 
 **url** | **String**| Account to apply operations to | 

### Return type

null (empty response body)

### Authorization

[sakari_auth](../README.md#sakari_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

