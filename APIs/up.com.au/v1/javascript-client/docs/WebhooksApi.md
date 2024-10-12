# UpApi.WebhooksApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooksGet**](WebhooksApi.md#webhooksGet) | **GET** /webhooks | List webhooks
[**webhooksIdDelete**](WebhooksApi.md#webhooksIdDelete) | **DELETE** /webhooks/{id} | Delete webhook
[**webhooksIdGet**](WebhooksApi.md#webhooksIdGet) | **GET** /webhooks/{id} | Retrieve webhook
[**webhooksPost**](WebhooksApi.md#webhooksPost) | **POST** /webhooks | Create webhook
[**webhooksWebhookIdLogsGet**](WebhooksApi.md#webhooksWebhookIdLogsGet) | **GET** /webhooks/{webhookId}/logs | List webhook logs
[**webhooksWebhookIdPingPost**](WebhooksApi.md#webhooksWebhookIdPingPost) | **POST** /webhooks/{webhookId}/ping | Ping webhook



## webhooksGet

> ListWebhooksResponse webhooksGet(opts)

List webhooks

Retrieve a list of configured webhooks. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered oldest first to newest last. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.WebhooksApi();
let opts = {
  'pageSize': 30 // Number | The number of records to return in each page. 
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
 **pageSize** | **Number**| The number of records to return in each page.  | [optional] 

### Return type

[**ListWebhooksResponse**](ListWebhooksResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksIdDelete

> webhooksIdDelete(id)

Delete webhook

Delete a specific webhook by providing its unique identifier. Once deleted, webhook events will no longer be sent to the configured URL. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.WebhooksApi();
let id = "a940825b-80b6-4798-b378-c6284259b4c5"; // String | The unique identifier for the webhook. 
apiInstance.webhooksIdDelete(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the webhook.  | 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webhooksIdGet

> GetWebhookResponse webhooksIdGet(id)

Retrieve webhook

Retrieve a specific webhook by providing its unique identifier. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.WebhooksApi();
let id = "c8283a72-24b0-4fd8-9b13-fccccab371e5"; // String | The unique identifier for the webhook. 
apiInstance.webhooksIdGet(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the webhook.  | 

### Return type

[**GetWebhookResponse**](GetWebhookResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksPost

> CreateWebhookResponse webhooksPost(opts)

Create webhook

Create a new webhook with a given URL. The URL will receive webhook events as JSON-encoded &#x60;POST&#x60; requests. The URL must respond with a HTTP &#x60;200&#x60; status on success.  There is currently a limit of 10 webhooks at any given time. Once this limit is reached, existing webhooks will need to be deleted before new webhooks can be created.  Event delivery is retried with exponential backoff if the URL is unreachable or it does not respond with a &#x60;200&#x60; status. The response includes a &#x60;secretKey&#x60; attribute, which is used to sign requests sent to the webhook URL. It will not be returned from any other endpoints within the Up API. If the &#x60;secretKey&#x60; is lost, simply create a new webhook with the same URL, capture its &#x60;secretKey&#x60; and then delete the original webhook. See [Handling webhook events](#callback_post_webhookURL) for details on how to process webhook events.  It is probably a good idea to test the webhook by [sending it a &#x60;PING&#x60; event](#post_webhooks_webhookId_ping) after creating it. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.WebhooksApi();
let opts = {
  'createWebhookRequest': new UpApi.CreateWebhookRequest() // CreateWebhookRequest | 
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
 **createWebhookRequest** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | [optional] 

### Return type

[**CreateWebhookResponse**](CreateWebhookResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webhooksWebhookIdLogsGet

> ListWebhookDeliveryLogsResponse webhooksWebhookIdLogsGet(webhookId, opts)

List webhook logs

Retrieve a list of delivery logs for a webhook by providing its unique identifier. This is useful for analysis and debugging purposes. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered newest first to oldest last. Logs may be automatically purged after a period of time. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.WebhooksApi();
let webhookId = "7104f5df-4993-495f-9d29-2b4d062c03a9"; // String | The unique identifier for the webhook. 
let opts = {
  'pageSize': 30 // Number | The number of records to return in each page. 
};
apiInstance.webhooksWebhookIdLogsGet(webhookId, opts, (error, data, response) => {
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
 **webhookId** | **String**| The unique identifier for the webhook.  | 
 **pageSize** | **Number**| The number of records to return in each page.  | [optional] 

### Return type

[**ListWebhookDeliveryLogsResponse**](ListWebhookDeliveryLogsResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksWebhookIdPingPost

> WebhookEventCallback webhooksWebhookIdPingPost(webhookId)

Ping webhook

Send a &#x60;PING&#x60; event to a webhook by providing its unique identifier. This is useful for testing and debugging purposes. The event is delivered asynchronously and its data is returned in the response to this request. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.WebhooksApi();
let webhookId = "830e127d-fb89-4400-92bb-f3f48289dcba"; // String | The unique identifier for the webhook. 
apiInstance.webhooksWebhookIdPingPost(webhookId, (error, data, response) => {
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
 **webhookId** | **String**| The unique identifier for the webhook.  | 

### Return type

[**WebhookEventCallback**](WebhookEventCallback.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

